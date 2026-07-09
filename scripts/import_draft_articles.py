#!/usr/bin/env python3
"""Convert draft article files in docs/articles/tbd*.md into republication shape."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "docs" / "articles"

RELATED_TITLES: dict[str, str] = {
    "from-nations-to-habitats.md": "From Nations To Habitats",
    "the-state-that-kept-saying-yes.md": "The State That Kept Saying Yes",
    "the-pressure-vessel-called-earth.md": "The Pressure Vessel Called Earth",
    "earth-did-not-steal-your-property.md": "Earth Did Not Steal Your Property",
    "why-earth-union-is-still-called-earth-union.md": "Why Earth Union Is Still Called Earth Union",
    "children-of-terra.md": "Children of Terra",
    "bells-bread-and-field-hospitals.md": "Bells, Bread, and Field Hospitals",
    "infinite-brutality-infinite-compassion.md": "Infinite Brutality, Infinite Compassion",
    "the-ships-that-do-not-fight.md": "The Ships That Do Not Fight",
    "galactic-confederation-at-founding.md": "The Galactic Confederation at Founding",
    "when-moral-alignment-failed-at-interstellar-scale.md": "When Moral Alignment Failed at Interstellar Scale",
    "earth-stole-my-property.md": "Earth Stole My Property",
    "the-door-was-not-hidden.md": "The Door Was Not Hidden",
    "the-human-trap-in-guardianship-settlement.md": "The Human Trap in the Guardianship Settlement",
    "the-chain-was-not-softened.md": "The Chain Was Not Softened",
}

EU_BATCH = {
    "tbd.md": {
        "slug": "from-nations-to-habitats",
        "title": "From Nations To Habitats",
        "description": "Institutional history of Earth Union from dependent habitats through Greth contact, Compact accession, IUAS, and Confederation membership.",
        "selection_date": "2496.199",
        "original_publication_date": "2495.441",
        "author": "Professor Amira Sato-Klein, Department of Earth Political Development, University of Geneva-Hellas",
        "field": "History and Policy",
        "type": "Republication",
        "series": ["Historical Summaries", "Earth Union Studies"],
        "dossiers": ["Earth Union Primer", "Compact and Confederation Origins"],
        "tags": ["earth-union", "history", "policy"],
        "venue": "*Introductory Compendium For Students Of Earth Union*, 19th revised edition",
        "republication_note": (
            "This chapter assumes no prior familiarity with pre-Union Earth politics. Students from non-Earth polities should remember that many of the old names were administrative, cultural, national, linguistic, military, and emotional categories at the same time. This is one reason early Earth history is so irritating to teach."
        ),
        "abstract": (
            "This survey traces Earth Union from dependent habitats and nation-state sovereignty through Greth contact, the Compact of Five, habitat-based reform, accession politics, the IUAS experiment, and membership in the Galactic Confederation. The argument is institutional rather than heroic: Earth grew by answering practical questions with procedure, then arming the procedure when the galaxy objected."
        ),
        "related": [
            "why-earth-union-is-still-called-earth-union.md",
            "galactic-confederation-at-founding.md",
            "when-moral-alignment-failed-at-interstellar-scale.md",
            "children-of-terra.md",
        ],
    },
    "tbd1.md": {
        "slug": "the-state-that-kept-saying-yes",
        "title": "The State That Kept Saying Yes",
        "description": "Welfare-state militarism, citizenship machinery, and how Earth Union's institutions opened doors a fugitive slave was not meant to reach.",
        "selection_date": "2496.202",
        "original_publication_date": "2496.178",
        "author": "Taran Vel, PhD, President Emeritus of Earth Union, Professor of Civic Systems, University of Luna, Senior Chief Petty Officer, Retired, Slave Emeritus",
        "field": "Civic Systems and External Power",
        "type": "Field Memoir",
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "tags": ["earth-union", "history", "policy", "guardianship"],
        "venue": "*Journal of Civic Systems and External Power*, Vol. 88",
        "republication_note": (
            "President Emeritus Vel insists on the full title line reproduced above, including the final title, which has no constitutional status, no academic standing, and no recognized military meaning. During his presidency, his office required the same styling for state visits. Several host governments objected. None objected twice."
        ),
        "related": [
            "from-nations-to-habitats.md",
            "infinite-brutality-infinite-compassion.md",
            "earth-did-not-steal-your-property.md",
            "bells-bread-and-field-hospitals.md",
        ],
    },
    "tbd2.md": {
        "slug": "the-pressure-vessel-called-earth",
        "title": "The Pressure Vessel Called Earth",
        "description": "A Kharrek scholar on Earth Union's moral sincerity, civic safety, and the interventionist patience of a polity that arms its good intentions.",
        "selection_date": "2496.223",
        "original_publication_date": "2496.144",
        "author": "Professor Sarekh Venn-Tor, Department of Comparative Statecraft, Tesh-Vorr Civic War College",
        "field": "Strategic Ethics and Comparative Statecraft",
        "type": "Republication",
        "series": ["Earth Union Studies"],
        "dossiers": ["Earth Union Primer"],
        "tags": ["earth-union", "comparative-policy", "policy"],
        "venue": "*Strategic Ethics Review*, Vol. 66",
        "republication_note": (
            "Professor Sarekh Venn-Tor is a Kharrek scholar of statecraft and military ethics whose work often concerns the political consequences of moral certainty. This essay drew immediate criticism from Earth Union readers, many of whom insisted that the author had misunderstood Earth policy while proving several of his points in the same correspondence. It also drew criticism from Kharrek traditionalists, who disliked his description of Luptaxi patronage as morally exposed. The Review considers this a productive distribution of anger."
        ),
        "related": [
            "the-state-that-kept-saying-yes.md",
            "from-nations-to-habitats.md",
            "infinite-brutality-infinite-compassion.md",
            "children-of-terra.md",
        ],
    },
    "tbd3.md": {
        "slug": "earth-did-not-steal-your-property",
        "title": "Earth Did Not Steal Your Property",
        "description": "An abolitionist legal reply to the Guardianship property complaint — the child hidden in the word Guardian.",
        "selection_date": "2496.224",
        "original_publication_date": "2495.378",
        "author": "Dr. Elian Voss, Senior Fellow in Abolitionist Legal History, University of Mars",
        "field": "Abolitionist Legal History",
        "type": "Institutional Response",
        "series": ["Guardianship Debates", "Earth Union Studies"],
        "dossiers": ["Guardianship Settlement", "Earth Union Primer"],
        "tags": ["guardianship", "earth-union", "law"],
        "venue": "*Civic Abolition Review*, Vol. 41",
        "republication_note": (
            "Dr. Voss wrote this response after renewed circulation of the complaint usually summarized as Earth stole my property. The Review has republished it because the complaint is useful, though not in the way its author intended. It demonstrates why the word Guardianship remains one of the ugliest legal inventions to survive the founding congress: it permits slaveholders to describe ownership as care, then act surprised when others decline the performance."
        ),
        "related": [
            "earth-stole-my-property.md",
            "the-door-was-not-hidden.md",
            "the-human-trap-in-guardianship-settlement.md",
            "the-chain-was-not-softened.md",
        ],
    },
}


def _yaml_list(key: str, items: list[str]) -> str:
    lines = [f"{key}:"] + [f'  - "{item}"' for item in items]
    return "\n".join(lines)


def _drop_until_h1(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[index:])
    return text


def _extract_abstract(body: str) -> tuple[str, str]:
    match = re.search(r"^## Abstract\s*\n(.*?)(?=^## )", body, re.MULTILINE | re.DOTALL)
    if not match:
        return "", body
    abstract = match.group(1).strip()
    rest = body[: match.start()] + body[match.end() :]
    return abstract, rest.lstrip()


def _strip_preamble(body: str) -> str:
    lines = body.splitlines()
    if not lines or not lines[0].startswith("# "):
        return body

    start = 1
    while start < len(lines):
        line = lines[start].strip()
        if not line:
            start += 1
            continue
        if line.startswith("## Abstract"):
            break
        if re.match(r"^## \d+\.", line):
            break
        start += 1
    return "\n".join(lines[start:]).lstrip()


def _normalize_body(body: str) -> tuple[str, str]:
    body = _drop_until_h1(body)
    body = _strip_preamble(body)
    abstract, body = _extract_abstract(body)
    body = re.sub(r"^## (\d+\. )", r"### \1", body, flags=re.MULTILINE)
    if not body.lstrip().startswith("## Article"):
        body = "## Article\n\n" + body
    body = re.sub(r"^## Editorial Afterword\s*$", "## Notes", body, flags=re.MULTILINE)
    return abstract, body


def build_article(spec: dict, source_name: str) -> str:
    source = (ARTICLES_DIR / source_name).read_text(encoding="utf-8")
    abstract, body = _normalize_body(source)
    if spec.get("abstract"):
        abstract = spec["abstract"]

    related_lines = "\n".join(
        f"- [{RELATED_TITLES[path]}]({path})" for path in spec["related"]
    )
    if "## Related Review selections" not in body:
        body = body.rstrip() + f"\n\n## Related Review selections\n\n{related_lines}\n"

    series_text = ", ".join(spec["series"])
    dossiers = spec.get("dossiers", [])
    dossier_block = ""
    if dossiers:
        dossier_block = f'  <div><dt>Dossier</dt><dd>{", ".join(dossiers)}</dd></div>\n'

    tags_yaml = _yaml_list("tags", spec["tags"])
    series_yaml = _yaml_list("series", spec["series"])
    dossiers_yaml = _yaml_list("dossiers", dossiers) if dossiers else ""

    fm_parts = [
        "---",
        f'title: "{spec["title"]}"',
        f'description: "{spec["description"]}"',
        f'selection_date: "{spec["selection_date"]}"',
        f'release_cycle: "{spec["selection_date"]}"',
        f'field: "{spec["field"]}"',
        f'type: "{spec["type"]}"',
        series_yaml,
    ]
    if dossiers_yaml:
        fm_parts.append(dossiers_yaml)
    fm_parts.extend(
        [
            f'originating_publication: "{spec["venue"]}"',
            f'original_publication_date: "{spec["original_publication_date"]}"',
            f'author: "{spec["author"]}"',
            'status: "Public archive edition"',
            tags_yaml,
            "---",
        ]
    )

    return (
        "\n".join(fm_parts)
        + f'''
# {spec["title"]}

<div class="republication-masthead" markdown="1">

<dl class="masthead-register">
  <div><dt>Originally published in</dt><dd markdown="1">{spec["venue"]}</dd></div>
  <div><dt>Republished by</dt><dd>Galactic Confederation Review</dd></div>
  <div><dt>Series</dt><dd>{series_text}</dd></div>
{dossier_block}  <div><dt>Original date</dt><dd>{spec["original_publication_date"]}</dd></div>
  <div><dt>Republication date</dt><dd>{spec["selection_date"]}</dd></div>
  <div><dt>Author</dt><dd>{spec["author"]}</dd></div>
  <div><dt>Field</dt><dd>{spec["field"]}</dd></div>
</dl>

</div>

!!! editorial "Republication note"
    {spec["republication_note"]}

<div class="review-abstract" markdown="1">

## Abstract

{abstract}

</div>

{body}'''
    )


def import_batch(specs: dict[str, dict]) -> None:
    for source_name, spec in specs.items():
        target = ARTICLES_DIR / f"{spec['slug']}.md"
        target.write_text(build_article(spec, source_name), encoding="utf-8")
        print(f"Wrote {target.name}")
        source = ARTICLES_DIR / source_name
        if source.exists() and source.name != target.name:
            source.unlink()
            print(f"Removed {source_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch",
        choices=("eu",),
        default="eu",
        help="Draft batch to import (default: eu)",
    )
    args = parser.parse_args()
    if args.batch == "eu":
        import_batch(EU_BATCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
