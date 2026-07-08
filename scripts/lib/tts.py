"""Text-to-speech backends for Review article narration."""

from __future__ import annotations

import asyncio
import io
import os
import wave
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable

import edge_tts
import requests


class TTSBackend(ABC):
    name: str

    @abstractmethod
    def synthesize_chunks(self, chunks: Iterable[str], output_path: Path) -> None:
        raise NotImplementedError


class EdgeTTSBackend(TTSBackend):
    name = "edge-tts"

    def __init__(self, voice: str = "en-GB-SoniaNeural", rate: str = "-5%") -> None:
        self.voice = voice
        self.rate = rate

    async def _synthesize_chunk(self, text: str) -> bytes:
        communicate = edge_tts.Communicate(text, self.voice, rate=self.rate)
        buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buffer.write(chunk["data"])
        return buffer.getvalue()

    def synthesize_chunks(self, chunks: Iterable[str], output_path: Path) -> None:
        mp3_parts = asyncio.run(self._synthesize_all(chunks))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(b"".join(mp3_parts))

    async def _synthesize_all(self, chunks: Iterable[str]) -> list[bytes]:
        parts: list[bytes] = []
        for index, chunk in enumerate(chunks, start=1):
            print(f"  edge-tts chunk {index}: {len(chunk)} chars")
            parts.append(await self._synthesize_chunk(chunk))
        return parts


class LLMVoXBackend(TTSBackend):
    """Use a running LLMVoX streaming server `/tts` endpoint."""

    name = "llmvox"

    def __init__(
        self,
        base_url: str | None = None,
        sample_rate: int = 24000,
        timeout_seconds: int = 600,
    ) -> None:
        self.base_url = (base_url or os.environ.get("LLMVOX_URL", "http://127.0.0.1:9000")).rstrip("/")
        self.sample_rate = sample_rate
        self.timeout_seconds = timeout_seconds

    def synthesize_chunks(self, chunks: Iterable[str], output_path: Path) -> None:
        frames: list[bytes] = []
        endpoint = f"{self.base_url}/tts"

        for index, chunk in enumerate(chunks, start=1):
            print(f"  llmvox chunk {index}: {len(chunk)} chars")
            with requests.post(
                endpoint,
                json={"text": chunk},
                stream=True,
                timeout=self.timeout_seconds,
            ) as response:
                response.raise_for_status()
                for data in response.iter_content(chunk_size=None):
                    if data:
                        frames.append(data)

        if not frames:
            raise RuntimeError("LLMVoX returned no audio data")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        self._write_wav(output_path, b"".join(frames))

    def _write_wav(self, output_path: Path, pcm_bytes: bytes) -> None:
        try:
            import numpy as np
        except ImportError as exc:
            raise RuntimeError("LLMVoX WAV export requires numpy") from exc

        audio = np.frombuffer(pcm_bytes, dtype=np.float32)
        audio = np.clip(audio, -1.0, 1.0)
        pcm16 = (audio * 32767).astype(np.int16)

        with wave.open(str(output_path), "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(pcm16.tobytes())


def get_backend(name: str) -> TTSBackend:
    normalized = name.strip().lower()
    if normalized in {"edge", "edge-tts", "edgetts"}:
        voice = os.environ.get("REVIEW_TTS_VOICE", "en-GB-SoniaNeural")
        rate = os.environ.get("REVIEW_TTS_RATE", "-5%")
        return EdgeTTSBackend(voice=voice, rate=rate)
    if normalized in {"llmvox", "llm-vox"}:
        return LLMVoXBackend()
    raise ValueError(f"Unknown TTS backend: {name}")
