"""Inject accessibility audio players on article pages when narration exists."""

from __future__ import annotations

from pathlib import Path


def _audio_href(page, config, filename: str) -> str:
    segments = [part for part in page.url.split("/") if part]
    relative = "../" * len(segments) + f"assets/audio/{filename}"
    site_url = config.get("site_url")
    if site_url:
        return f"{site_url.rstrip('/')}/assets/audio/{filename}"
    return relative


def _find_audio_file(docs_dir: Path, slug: str) -> str | None:
    audio_dir = docs_dir / "assets" / "audio"
    for suffix in (".mp3", ".wav"):
        candidate = audio_dir / f"{slug}{suffix}"
        if candidate.exists():
            return candidate.name
    return None


def on_page_markdown(markdown: str, page, config, files) -> str:
    src_path = page.file.src_path.replace("\\", "/")
    if not src_path.startswith("articles/"):
        return markdown
    if page.file.name == "index.md":
        return markdown

    slug = Path(page.file.src_path).stem
    docs_dir = Path(config["docs_dir"])
    audio_name = _find_audio_file(docs_dir, slug)
    if not audio_name:
        return markdown

    caption = config.get("extra", {}).get("audio", {}).get(
        "caption",
        "Audio edition · narrated for accessibility",
    )
    mime = "audio/mpeg" if audio_name.endswith(".mp3") else "audio/wav"
    href = _audio_href(page, config, audio_name)

    player = (
        '\n<div class="review-audio" markdown="0">\n'
        f'  <p class="review-audio__label">Listen to this selection</p>\n'
        f'  <audio controls preload="metadata" aria-label="Audio edition of {page.title}">\n'
        f'    <source src="{href}" type="{mime}">\n'
        "  </audio>\n"
        f'  <p class="review-audio__caption">{caption}</p>\n'
        "</div>\n"
    )

    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = index + 1
            while insert_at < len(lines) and not lines[insert_at].strip():
                insert_at += 1
            lines.insert(insert_at, player)
            return "\n".join(lines)

    return player + markdown
