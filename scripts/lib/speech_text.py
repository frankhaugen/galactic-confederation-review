"""Convert Review article Markdown into narration-ready plain text."""

from __future__ import annotations

import re
from pathlib import Path


_FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
_HTML_TAG_RE = re.compile(r"<[^>]+>")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
_ADMONITION_RE = re.compile(
    r"^!!!\s+(\w+)(?:\s+\"([^\"]+)\")?\s*\n((?:    .+\n?)*)",
    re.MULTILINE,
)
_HTML_BLOCK_RE = re.compile(
    r"<div[^>]*markdown=\"[^\"]*\"[^>]*>\s*\n?(.*?)\n?</div>",
    re.DOTALL | re.IGNORECASE,
)
_TABLE_SEP_RE = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$")


def _strip_admonitions(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        title = match.group(2) or match.group(1).replace("_", " ").title()
        body = re.sub(r"^    ", "", match.group(3), flags=re.MULTILINE).strip()
        return f"{title}. {body}\n\n"

    return _ADMONITION_RE.sub(replace, text)


def _strip_html_blocks(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        inner = match.group(1).strip()
        inner = _HTML_TAG_RE.sub("", inner)
        return f"{inner}\n\n"

    text = _HTML_BLOCK_RE.sub(replace, text)
    return _HTML_TAG_RE.sub("", text)


def _normalize_headings(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        heading = match.group(1).strip()
        heading = _LINK_RE.sub(r"\1", heading)
        heading = _ITALIC_RE.sub(r"\1", heading)
        return f"\n{heading}.\n"

    return _HEADING_RE.sub(replace, text)


def _normalize_tables(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            lines.append(line)
            continue
        if _TABLE_SEP_RE.match(line.strip()):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        lines.append(". ".join(cell for cell in cells if cell))
    return "\n".join(lines)


def _collapse_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def markdown_to_speech_text(markdown: str) -> str:
    text = _FRONTMATTER_RE.sub("", markdown, count=1)
    text = _strip_admonitions(text)
    text = _strip_html_blocks(text)
    text = _CODE_FENCE_RE.sub("", text)
    text = _INLINE_CODE_RE.sub(r"\1", text)
    text = _IMAGE_RE.sub(r"\1", text)
    text = _LINK_RE.sub(r"\1", text)
    text = _BOLD_RE.sub(r"\1", text)
    text = _ITALIC_RE.sub(r"\1", text)
    text = _normalize_tables(text)
    text = _normalize_headings(text)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
    return _collapse_whitespace(text)


def load_article_speech_text(path: Path) -> str:
    return markdown_to_speech_text(path.read_text(encoding="utf-8"))


def chunk_text(text: str, max_chars: int = 3500) -> list[str]:
    """Split narration text on paragraph boundaries for TTS APIs."""
    if len(text) <= max_chars:
        return [text]

    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
            continue

        if current:
            chunks.append(current)
            current = ""

        if len(paragraph) <= max_chars:
            current = paragraph
            continue

        sentences = re.split(r"(?<=[.!?])\s+", paragraph)
        sentence_buf = ""
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            candidate = f"{sentence_buf} {sentence}".strip()
            if len(candidate) <= max_chars:
                sentence_buf = candidate
                continue
            if sentence_buf:
                chunks.append(sentence_buf)
            sentence_buf = sentence
        if sentence_buf:
            current = sentence_buf

    if current:
        chunks.append(current)

    return chunks
