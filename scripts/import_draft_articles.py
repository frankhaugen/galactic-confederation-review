#!/usr/bin/env python3
"""One-time helper: convert draft article files into republication shape."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "docs" / "articles"

SPECS = {
    "tbd.md": {
        "slug": "the-lie-of-just-one-passenger",
        "title": 'The Lie Of "Just One Passenger"',
        "description": "Why carrying even one passenger alters vessel class, insurance, crew duty, and port clearance — transport law for small operators.",
        "review_selection": "2496.205",
        "original_date": "2495.112",
        "author": "Professor Iren Tal Osh, Chair of Transport Liability and Civil Movement Law, Veyran Institute of Commercial Systems",
        "field": "Transport Liability and Civil Movement Law",
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Maritime Law", "Transport Law"],
        "venue": "*Port Authority Quarterly*, Issue 214",
        "editorial": (
            "This article is often assigned in certification courses for small operators, usually on the day after students discover that cargo does not scream, sue, require atmosphere compatibility, or have relatives. The Review has restored several passages omitted from later training editions, including Professor Osh's footnote on passenger pets, which remains unfair to pets and accurate about their owners."
        ),
        "related": [
            "the-margin-was-the-freedom.md",
            "the-captain-is-not-always-a-captain.md",
            "the-ship-that-can-sign-its-own-shadow.md",
            "c-series-containers-founding-standard.md",
        ],
    },
    "tbd2.md": {
        "slug": "the-margin-was-the-freedom",
        "title": "The Margin Was The Freedom",
        "description": "Abridged memoir of forty-one years as an owner-master — access, solvency, and the middle space the Confederation registry left open.",
        "review_selection": "2496.206",
        "original_date": "2496.156",
        "author": "Captain Sella Varr, retired owner-master, light commercial transport",
        "field": "Field Memoir and Commercial Practice",
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Maritime Law", "Commercial Practice"],
        "venue": "Port cooperative memoir edition (abridged)",
        "editorial": (
            "Captain Varr's memoir was first printed in a port cooperative edition of eight hundred copies, most of which appear to have been bought by people who already knew her, owed her money, or both. The Review has abridged the central chapters for the Hard Science issue because policy language tends to make independent transport sound cleaner than it is. Captain Varr does not dispute the value of the Confederation registry, freedom of navigation, or owner-master rules. She is grateful for them. She is also very clear about what it means to live for decades inside the narrow space between access and solvency."
        ),
        "abstract": (
            "This abridged memoir records forty-one years of owner-master commercial transport: thin margins, open routes, recognized competence, and the difference between a registered ship with standing and a life spent begging concession holders for permission to move. Captain Varr does not treat independence as romance. She treats it as work that kept tributary commerce alive while larger carriers optimized the main rivers."
        ),
        "related": [
            "the-captain-is-not-always-a-captain.md",
            "the-ship-that-can-sign-its-own-shadow.md",
            "the-ship-is-the-flag.md",
            "the-lie-of-just-one-passenger.md",
        ],
    },
    "tbd3.md": {
        "slug": "the-captain-is-not-always-a-captain",
        "title": "The Captain Is Not Always A Captain",
        "description": "Owner-masters, spacer competence, and the founding congress' proportional qualification regime for small vessels.",
        "review_selection": "2496.222",
        "original_date": "2494.195",
        "author": "Hareth Mol Vesh, Senior Lecturer in Commercial Institutions, Third Kethari School of Trade Law",
        "field": "Commercial and Maritime Law",
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Maritime Law", "Founding & Charter Law"],
        "venue": "*Journal of Interstellar Mercantile Systems*, Vol. 90",
        "editorial": (
            "Professor Mol Vesh has now written three consecutive essays on Confederation vessel law for this archive. At this stage, the Review considers intervention unnecessary. The man is happy, and the footnotes are contained."
        ),
        "related": [
            "the-ship-is-the-flag.md",
            "the-ship-that-can-sign-its-own-shadow.md",
            "the-margin-was-the-freedom.md",
            "galactic-confederation-at-founding.md",
        ],
    },
    "tbd4.md": {
        "slug": "the-ship-is-the-flag",
        "title": "The Ship Is The Flag",
        "description": "Registry, route freedom, and how the Confederation replaced flag jurisdictions with hull standing as commercial legal identity.",
        "review_selection": "2496.209",
        "original_date": "2494.181",
        "author": "Hareth Mol Vesh, Senior Lecturer in Commercial Institutions, Third Kethari School of Trade Law",
        "field": "Commercial and Maritime Law",
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Maritime Law", "Founding & Charter Law"],
        "venue": "*Journal of Interstellar Mercantile Systems*, Vol. 89",
        "editorial": (
            "Professor Mol Vesh wrote this essay after the Review selected *The Ship That Can Sign Its Own Shadow*. We are told, by sources close to the author, that the second essay began as three footnotes, became an appendix, then escaped containment. The Review sympathizes."
        ),
        "related": [
            "the-ship-that-can-sign-its-own-shadow.md",
            "the-captain-is-not-always-a-captain.md",
            "the-margin-was-the-freedom.md",
            "galactic-confederation-at-founding.md",
        ],
    },
}

RELATED_TITLES = {
    "the-lie-of-just-one-passenger.md": 'The Lie Of "Just One Passenger"',
    "the-margin-was-the-freedom.md": "The Margin Was The Freedom",
    "the-captain-is-not-always-a-captain.md": "The Captain Is Not Always A Captain",
    "the-ship-is-the-flag.md": "The Ship Is The Flag",
    "the-ship-that-can-sign-its-own-shadow.md": "The Ship That Can Sign Its Own Shadow",
    "c-series-containers-founding-standard.md": "C-Series Containers and the Founding Standard",
    "galactic-confederation-at-founding.md": "The Galactic Confederation at Founding",
}


def _yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def _extract_abstract(body: str) -> tuple[str, str]:
    match = re.search(r"^## Abstract\s*\n(.*?)(?=^## )", body, re.MULTILINE | re.DOTALL)
    if not match:
        return "", body
    abstract = match.group(1).strip()
    rest = body[: match.start()] + body[match.end() :]
    return abstract, rest.lstrip()


def _strip_preamble(body: str) -> str:
    lines = body.splitlines()
    start = 0
    if lines and lines[0].startswith("# "):
        start = 1
        while start < len(lines) and (
            not lines[start].strip()
            or lines[start].startswith("## ")
            or lines[start].startswith("By ")
            or lines[start].startswith("Original publication:")
            or lines[start].startswith("Republication note:")
            or lines[start] == "GCR Archive Selection"
            or lines[start].startswith("Edited and abridged")
        ):
            if lines[start].startswith("## Abstract"):
                break
            start += 1
    return "\n".join(lines[start:]).lstrip()


def _normalize_body(body: str) -> str:
    body = _strip_preamble(body)
    abstract, body = _extract_abstract(body)
    body = re.sub(r"^## (\d+\. )", r"### \1", body, flags=re.MULTILINE)
    if not body.lstrip().startswith("## Article"):
        body = "## Article\n\n" + body
    body = re.sub(r"^## Editorial Afterword\s*$", "## Notes", body, flags=re.MULTILINE)
    if "## Related Review selections" not in body:
        body = body.rstrip() + "\n"
    return abstract, body


def build_article(spec: dict, source_name: str) -> str:
    source = (ARTICLES_DIR / source_name).read_text(encoding="utf-8")
    abstract, body = _normalize_body(source)
    if spec.get("abstract"):
        abstract = spec["abstract"]

    tags_yaml = _yaml_list(spec["tags"])
    related_lines = "\n".join(
        f"- [{RELATED_TITLES[path]}]({path})" for path in spec["related"]
    )
    if "## Related Review selections" not in body:
        body = body.rstrip() + f"\n\n## Related Review selections\n\n{related_lines}\n"

    frontmatter = f'''---
title: "{spec["title"]}"
description: "{spec["description"]}"
review_selection: "{spec["review_selection"]}"
original_date: "{spec["original_date"]}"
author: "{spec["author"]}"
field: "{spec["field"]}"
series: "{spec["series"]}"
tags:
{tags_yaml}
issue: "2494.338"
issue_theme: "Hard Science"
---
# {spec["title"]}

<div class="republication-masthead" markdown="1">

<dl class="masthead-register">
  <div><dt>Originally published in</dt><dd markdown="1">{spec["venue"]}</dd></div>
  <div><dt>Republished by</dt><dd>Galactic Confederation Review</dd></div>
  <div><dt>Review issue</dt><dd markdown="1">[2494.338 — *Hard Science*](../issues/2494-338-hard-science.md)</dd></div>
  <div><dt>Original date</dt><dd>{spec["original_date"]}</dd></div>
  <div><dt>Review selection</dt><dd>{spec["review_selection"]}</dd></div>
  <div><dt>Author</dt><dd>{spec["author"]}</dd></div>
  <div><dt>Field</dt><dd>{spec["field"]}</dd></div>
</dl>

</div>

!!! editorial "Editorial note"
    {spec["editorial"]}

<div class="review-abstract" markdown="1">

## Abstract

{abstract}

</div>

'''
    return frontmatter + body


def main() -> int:
    for source_name, spec in SPECS.items():
        target = ARTICLES_DIR / f"{spec['slug']}.md"
        target.write_text(build_article(spec, source_name), encoding="utf-8")
        print(f"Wrote {target.name}")
        source = ARTICLES_DIR / source_name
        if source.exists() and source_name != target.name:
            source.unlink()
            print(f"Removed {source_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
