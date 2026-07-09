#!/usr/bin/env python3
"""Post-write publish pipeline for a single Review selection."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "docs" / "articles"
REGISTER_PATH = ROOT / "docs" / "articles" / "index.md"
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
PYTHON = VENV_PYTHON if VENV_PYTHON.exists() else Path(sys.executable)


def run(cmd: list[str], *, label: str) -> None:
    print(f"\n==> {label}")
    print("   ", " ".join(cmd))
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(f"{label} failed (exit {result.returncode})")


def latest_release_date() -> str | None:
    if not REGISTER_PATH.exists():
        return None
    text = REGISTER_PATH.read_text(encoding="utf-8")
    dates = re.findall(r"\b(24\d{2}\.\d{3})\b", text)
    return max(dates) if dates else None


def verify_article(slug: str) -> Path:
    path = ARTICLES_DIR / f"{slug}.md"
    if not path.exists():
        raise SystemExit(f"Article not found: {path}")
    text = path.read_text(encoding="utf-8")
    required = ("selection_date:", "title:", "## Article")
    missing = [token for token in required if token not in text]
    if missing:
        raise SystemExit(f"{path.name} missing required content: {', '.join(missing)}")
    return path


def git_add_publish_files() -> None:
    paths = [
        "docs/articles",
        "docs/index.md",
        "docs/authors.md",
        "docs/editorial-content.md",
        "docs/series",
        "docs/dossiers",
        "docs/assets/audio",
    ]
    for rel in paths:
        if (ROOT / rel).exists():
            run(["git", "add", rel], label=f"git add {rel}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Article filename without .md")
    parser.add_argument("--skip-audio", action="store_true")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--commit", action="store_true", help="Stage and commit publish files")
    parser.add_argument("--push", action="store_true", help="Push main after commit")
    parser.add_argument(
        "--message",
        help="Commit subject line (required with --commit)",
    )
    args = parser.parse_args()

    article = verify_article(args.slug)
    latest = latest_release_date()
    if latest:
        print(f"Latest register release: {latest}")

    if not args.skip_build:
        run([str(PYTHON), "-m", "mkdocs", "build", "--strict"], label="mkdocs build --strict")

    if not args.skip_audio:
        run(
            [str(PYTHON), "-m", "pip", "install", "-r", "requirements-audio.txt", "-q"],
            label="install audio dependencies",
        )
        run(
            [
                str(PYTHON),
                "scripts/generate_article_audio.py",
                "--article",
                args.slug,
                "--force",
            ],
            label="generate article audio",
        )
        if not args.skip_build:
            run([str(PYTHON), "-m", "mkdocs", "build", "--strict"], label="mkdocs rebuild after audio")
        run(
            [
                str(PYTHON),
                "scripts/verify_article_audio.py",
                "--scope",
                "all",
                "--check-site",
            ],
            label="verify article audio",
        )

    if args.commit:
        if not args.message:
            raise SystemExit("--commit requires --message")
        git_add_publish_files()
        run(["git", "commit", "-m", args.message], label="git commit")
        if args.push:
            run(["git", "push", "origin", "main"], label="git push origin main")

    print(f"\nPublished selection ready: {article.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
