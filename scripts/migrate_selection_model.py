#!/usr/bin/env python3
"""Migrate articles from issue-based metadata to selection/series/dossier model."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "docs" / "articles"

CATALOG: dict[str, dict] = {
    "ansible-is-not-a-radio": {
        "series": ["Communications and Transit"],
        "dossiers": ["Ansible and Communications"],
        "type": "Republication",
    },
    "bells-bread-and-field-hospitals": {
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Republication",
    },
    "c-series-containers-founding-standard": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Technical Note",
    },
    "capability-is-not-classification": {
        "series": ["Comparative Law"],
        "dossiers": [],
        "type": "Republication",
    },
    "children-of-terra": {
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Republication",
    },
    "earth-did-not-steal-your-property": {
        "series": ["Guardianship Debates", "Earth Union Studies"],
        "dossiers": ["Guardianship Settlement", "Earth Union Primer"],
        "type": "Institutional Response",
    },
    "earth-stole-my-property": {
        "series": ["Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Public Argument",
    },
    "ftl-transit-operational-tradeoffs": {
        "series": ["Communications and Transit"],
        "dossiers": ["Ansible and Communications"],
        "type": "Technical Note",
    },
    "from-nations-to-habitats": {
        "series": ["Historical Summaries", "Earth Union Studies"],
        "dossiers": ["Earth Union Primer", "Compact and Confederation Origins"],
        "type": "Republication",
    },
    "galactic-confederation-at-founding": {
        "series": ["Historical Summaries", "Guardianship Debates"],
        "dossiers": ["Guardianship Settlement", "Compact and Confederation Origins"],
        "type": "Republication",
    },
    "infinite-brutality-infinite-compassion": {
        "series": ["Fleet and Rescue Doctrine", "Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Field Memoir",
    },
    "institutions-without-parenthood": {
        "series": ["Species Profiles"],
        "dossiers": [],
        "type": "Republication",
    },
    "prize-class-recovery-and-the-vigilantism-line": {
        "series": ["Comparative Law"],
        "dossiers": [],
        "type": "Republication",
    },
    "routine-predation-in-low-sovereignty-corridors": {
        "series": ["Comparative Law"],
        "dossiers": [],
        "type": "Republication",
    },
    "status-laundering-at-the-registry-interface": {
        "series": ["Comparative Law", "Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Republication",
    },
    "the-captain-is-not-always-a-captain": {
        "series": ["Standards and Infrastructure", "Comparative Law"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Republication",
    },
    "the-chain-was-not-softened": {
        "series": ["Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Republication",
    },
    "the-compromise-that-named-the-chain": {
        "series": ["Guardianship Debates"],
        "dossiers": ["Guardianship Settlement", "Compact and Confederation Origins"],
        "type": "Republication",
    },
    "the-confederation-does-not-deliver-messages": {
        "series": ["Communications and Transit"],
        "dossiers": ["Ansible and Communications"],
        "type": "Republication",
    },
    "the-door-was-not-hidden": {
        "series": ["Comparative Law", "Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Republication",
    },
    "the-human-trap-in-guardianship-settlement": {
        "series": ["Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Republication",
    },
    "the-lie-of-just-one-passenger": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Republication",
    },
    "the-margin-was-the-freedom": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Field Memoir",
    },
    "the-pressure-vessel-called-earth": {
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Republication",
    },
    "the-ship-is-the-flag": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Republication",
    },
    "the-ship-that-can-sign-its-own-shadow": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Republication",
    },
    "the-ships-that-do-not-fight": {
        "series": ["Fleet and Rescue Doctrine"],
        "dossiers": [],
        "type": "Republication",
    },
    "the-species-without-mothers": {
        "series": ["Species Profiles"],
        "dossiers": [],
        "type": "Republication",
    },
    "the-state-that-kept-saying-yes": {
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Field Memoir",
    },
    "the-thinking-software-taboo": {
        "series": ["Comparative Law"],
        "dossiers": [],
        "type": "Republication",
    },
    "what-fits-inside-the-standard": {
        "series": ["Standards and Infrastructure"],
        "dossiers": ["Ship Law and Registry"],
        "type": "Republication",
    },
    "what-the-ledger-refuses-to-see": {
        "series": ["Guardianship Debates"],
        "dossiers": ["Guardianship Settlement"],
        "type": "Republication",
    },
    "when-moral-alignment-failed-at-interstellar-scale": {
        "series": ["Historical Summaries", "Guardianship Debates"],
        "dossiers": ["Compact and Confederation Origins", "Guardianship Settlement"],
        "type": "Republication",
    },
    "why-earth-union-is-still-called-earth-union": {
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "type": "Republication",
    },
}


def _parse_frontmatter(text: str) -> tuple[dict[str, str], list[str], str]:
    if not text.startswith("---"):
        return {}, [], text
    end = text.index("---", 3)
    block = text[3:end].strip()
    body = text[end + 3 :].lstrip()
    fields: dict[str, str] = {}
    tags: list[str] = []
    in_tags = False
    for line in block.splitlines():
        if line.startswith("  - ") and in_tags:
            tags.append(line[4:].strip().strip('"'))
            continue
        in_tags = False
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key == "tags":
            in_tags = True
            continue
        fields[key] = value.strip().strip('"')
    return fields, tags, body


def _extract_venue(body: str) -> str:
    match = re.search(
        r"<dt>Originally published in</dt><dd(?:\s+markdown=\"1\")?>(.*?)</dd>",
        body,
        re.DOTALL,
    )
    if not match:
        return ""
    venue = re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return venue


def _yaml_list(key: str, items: list[str]) -> str:
    if not items:
        return ""
    lines = [f"{key}:"] + [f'  - "{item}"' for item in items]
    return "\n".join(lines)


def _build_frontmatter(old: dict[str, str], tags: list[str], meta: dict) -> str:
    selection_date = old.get("review_selection") or old.get("selection_date", "")
    original_date = old.get("original_date") or old.get("original_publication_date", "")
    title = old.get("title", "")
    description = old.get("description", "")
    author = old.get("author", "")
    field = old.get("field", "")
    tags_block = ""
    if old.get("tags"):
        pass

    lines = [
        "---",
        f'title: "{title}"',
    ]
    if description:
        lines.append(f'description: "{description}"')
    lines.append(f'selection_date: "{selection_date}"')
    lines.append(f'release_cycle: "{selection_date}"')
    lines.append(f'field: "{field}"')
    lines.append(f'type: "{meta["type"]}"')
    series_yaml = _yaml_list("series", meta["series"])
    if series_yaml:
        lines.append(series_yaml)
    dossiers_yaml = _yaml_list("dossiers", meta.get("dossiers", []))
    if dossiers_yaml:
        lines.append(dossiers_yaml)
    venue = old.get("_venue", "")
    if venue:
        lines.append(f'originating_publication: "{venue.replace(chr(34), chr(39))}"')
    if original_date:
        lines.append(f'original_publication_date: "{original_date}"')
    lines.append(f'author: "{author}"')
    lines.append('status: "Public archive edition"')
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f'  - {tag}')
    lines.append("---")
    return "\n".join(lines) + "\n"


def _update_masthead(body: str, meta: dict, selection_date: str) -> str:
    body = re.sub(
        r"\s*<div><dt>Review issue</dt><dd[^>]*>.*?</dd></div>\s*",
        "\n",
        body,
        flags=re.DOTALL,
    )
    body = body.replace(
        "<div><dt>Review selection</dt>",
        "<div><dt>Republication date</dt>",
    )

    series_text = ", ".join(meta["series"])
    dossiers = meta.get("dossiers", [])
    insert_lines = f'  <div><dt>Series</dt><dd>{series_text}</dd></div>\n'
    if dossiers:
        insert_lines += (
            f'  <div><dt>Dossier</dt><dd>{", ".join(dossiers)}</dd></div>\n'
        )

    body = re.sub(
        r"(<div><dt>Republished by</dt><dd>Galactic Confederation Review</dd></div>\n)",
        r"\1" + insert_lines,
        body,
        count=1,
    )

    body = re.sub(
        r'<div><dt>Republication date</dt><dd>\d+\.\d+</dd></div>',
        f"<div><dt>Republication date</dt><dd>{selection_date}</dd></div>",
        body,
        count=1,
    )

    body = body.replace(
        '!!! editorial "Editorial note"',
        '!!! editorial "Republication note"',
    )
    return body


def migrate_article(path: Path) -> None:
    slug = path.stem
    if slug in ("index",) or slug.startswith("tbd"):
        return
    if slug not in CATALOG:
        raise SystemExit(f"No catalog entry for {slug}")

    text = path.read_text(encoding="utf-8")
    old_fm, tags, body = _parse_frontmatter(text)
    venue = _extract_venue(body)
    old_fm["_venue"] = venue
    meta = CATALOG[slug]
    selection_date = old_fm.get("review_selection", "")

    new_fm = _build_frontmatter(old_fm, tags, meta)
    new_body = _update_masthead(body, meta, selection_date)
    path.write_text(new_fm + new_body, encoding="utf-8")
    print(f"Migrated {path.name}")


def main() -> int:
    for path in sorted(ARTICLES.glob("*.md")):
        migrate_article(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
