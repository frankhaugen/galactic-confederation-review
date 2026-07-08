#!/usr/bin/env python3
"""Generate accessibility audio editions for Review articles."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from lib.speech_text import chunk_text, load_article_speech_text  # noqa: E402
from lib.tts import get_backend  # noqa: E402

ARTICLES_DIR = ROOT / "docs" / "articles"
AUDIO_DIR = ROOT / "docs" / "assets" / "audio"
MANIFEST_PATH = AUDIO_DIR / "manifest.json"


def article_paths(selected: list[str] | None = None) -> list[Path]:
    paths = sorted(
        path
        for path in ARTICLES_DIR.glob("*.md")
        if path.name != "index.md"
    )
    if not selected:
        return paths
    wanted = {name.removesuffix(".md") for name in selected}
    return [path for path in paths if path.stem in wanted]


def output_path_for(article_path: Path, backend_name: str) -> Path:
    suffix = ".wav" if backend_name.startswith("llmvox") else ".mp3"
    return AUDIO_DIR / f"{article_path.stem}{suffix}"


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"articles": {}}


def save_manifest(manifest: dict) -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def generate_article(
    article_path: Path,
    backend_name: str,
    *,
    force: bool = False,
    max_chars: int = 3500,
) -> dict:
    output_path = output_path_for(article_path, backend_name)
    if output_path.exists() and not force:
        return {
            "slug": article_path.stem,
            "status": "skipped",
            "output": str(output_path.relative_to(ROOT)).replace("\\", "/"),
        }

    speech_text = load_article_speech_text(article_path)
    if not speech_text:
        return {"slug": article_path.stem, "status": "empty"}

    chunks = chunk_text(speech_text, max_chars=max_chars)
    backend = get_backend(backend_name)
    print(f"Generating {article_path.name} via {backend.name} ({len(chunks)} chunks)")
    backend.synthesize_chunks(chunks, output_path)

    return {
        "slug": article_path.stem,
        "status": "generated",
        "backend": backend.name,
        "chunks": len(chunks),
        "chars": len(speech_text),
        "output": str(output_path.relative_to(ROOT)).replace("\\", "/"),
        "generated_at": datetime.now(UTC).isoformat(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--backend",
        default="edge-tts",
        help="TTS backend: edge-tts (default) or llmvox",
    )
    parser.add_argument(
        "--article",
        action="append",
        dest="articles",
        help="Article slug or filename (repeatable). Default: all articles.",
    )
    parser.add_argument("--force", action="store_true", help="Regenerate even if output exists")
    parser.add_argument("--max-chars", type=int, default=3500, help="Chunk size for TTS requests")
    args = parser.parse_args()

    manifest = load_manifest()
    manifest.setdefault("articles", {})
    manifest["backend"] = args.backend
    manifest["updated_at"] = datetime.now(UTC).isoformat()

    results = []
    for article_path in article_paths(args.articles):
        result = generate_article(
            article_path,
            args.backend,
            force=args.force,
            max_chars=args.max_chars,
        )
        results.append(result)
        if result.get("output"):
            manifest["articles"][result["slug"]] = result

    save_manifest(manifest)

    generated = sum(1 for item in results if item["status"] == "generated")
    skipped = sum(1 for item in results if item["status"] == "skipped")
    print(f"Done. generated={generated} skipped={skipped} total={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
