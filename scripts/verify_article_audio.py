#!/usr/bin/env python3
"""Verify accessibility audio editions for Review articles."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from lib.speech_text import load_article_speech_text  # noqa: E402

ARTICLES_DIR = ROOT / "docs" / "articles"
AUDIO_DIR = ROOT / "docs" / "assets" / "audio"
MANIFEST_PATH = AUDIO_DIR / "manifest.json"
SITE_ARTICLES_DIR = ROOT / "site" / "articles"


def published_article_slugs() -> list[str]:
  import yaml

  nav = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))["nav"]

  def walk(items):
    for item in items:
      if isinstance(item, dict):
        for value in item.values():
          if isinstance(value, str) and value.startswith("articles/") and value.endswith(".md"):
            slug = Path(value).stem
            if slug != "index":
              yield slug
          elif isinstance(value, list):
            yield from walk(value)
      elif isinstance(item, str) and item.startswith("articles/"):
        slug = Path(item).stem
        if slug != "index":
          yield slug

  return sorted(set(walk(nav)))


def all_article_slugs() -> list[str]:
  return sorted(
    path.stem
    for path in ARTICLES_DIR.glob("*.md")
    if path.name != "index.md"
  )


def verify_mp3(path: Path) -> tuple[float | None, str | None]:
  try:
    from mutagen.mp3 import MP3
  except ImportError:
    if path.stat().st_size < 100_000:
      return None, "file too small"
    return None, None

  try:
    audio = MP3(path)
    duration = audio.info.length
    if duration < 30:
      return duration, "duration under 30 seconds"
    return duration, None
  except Exception as exc:
    return None, str(exc)


def verify_site_players(slugs: list[str]) -> list[str]:
  missing: list[str] = []
  for slug in slugs:
    page = SITE_ARTICLES_DIR / slug / "index.html"
    if not page.exists():
      missing.append(f"{slug}: built page missing")
      continue
    if "review-audio" not in page.read_text(encoding="utf-8"):
      missing.append(f"{slug}: audio player not in built HTML")
  return missing


def main() -> int:
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "--scope",
    choices=("published", "all"),
    default="published",
    help="Verify published nav articles (default) or every article markdown file",
  )
  parser.add_argument(
    "--check-site",
    action="store_true",
    help="Also verify built site pages include audio players (requires mkdocs build)",
  )
  args = parser.parse_args()

  slugs = published_article_slugs() if args.scope == "published" else all_article_slugs()
  manifest = (
    json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if MANIFEST_PATH.exists()
    else {"articles": {}}
  )
  manifest_articles = manifest.get("articles", {})

  issues: list[str] = []
  durations: list[tuple[str, float, int]] = []

  for slug in slugs:
    mp3 = AUDIO_DIR / f"{slug}.mp3"
    article = ARTICLES_DIR / f"{slug}.md"

    if not article.exists():
      issues.append(f"{slug}: article markdown missing")
      continue
    if not mp3.exists():
      issues.append(f"{slug}: missing MP3")
      continue

    speech = load_article_speech_text(article)
    if not speech.strip():
      issues.append(f"{slug}: empty speech text")
      continue

    duration, mp3_issue = verify_mp3(mp3)
    if mp3_issue:
      issues.append(f"{slug}: {mp3_issue}")
    elif duration:
      durations.append((slug, duration, len(speech)))

    if slug not in manifest_articles:
      issues.append(f"{slug}: missing manifest entry")

  if durations:
    rates = [chars / duration for _, duration, chars in durations]
    median = sorted(rates)[len(rates) // 2]
    for slug, duration, chars in durations:
      rate = chars / duration
      if rate < median * 0.5 or rate > median * 1.8:
        issues.append(f"{slug}: narration rate outlier ({rate:.1f} chars/s; median {median:.1f})")

  if args.check_site:
    issues.extend(verify_site_players(slugs))

  print(f"Checked {len(slugs)} article(s) in scope '{args.scope}'.")
  if durations:
    total_hours = sum(duration for _, duration, _ in durations) / 3600
    print(f"Total audio duration: {total_hours:.2f} hours")

  if issues:
    print("Issues found:")
    for issue in issues:
      print(f"  - {issue}")
    return 1

  print("All checks passed.")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
