"""One-time article immersion pass. Run from repository root."""
from __future__ import annotations

import re
from pathlib import Path

ARTICLES_DIR = Path(__file__).resolve().parents[1] / "docs" / "articles"

META = {
    "when-moral-alignment-failed-at-interstellar-scale.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "History", "Confederation Institutions"],
        "description": "Why the Interstellar Union of Aligned Societies failed and the Galactic Confederation turned procedural.",
    },
    "the-compromise-that-named-the-chain.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "Guardianship", "Ethics"],
        "description": "Moral-historical analysis of the legal language that structured Confederation accession.",
    },
    "the-chain-was-not-softened.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "Guardianship", "Law"],
        "description": "Abolitionist legal argument against conciliatory accounts of the Guardianship compromise.",
    },
    "the-human-trap-in-guardianship-settlement.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "Guardianship", "Economics"],
        "description": "Twislha political economy of compliance burdens and dependency institutions.",
    },
    "what-the-ledger-refuses-to-see.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "Economics", "Guardianship"],
        "description": "Effort credits, moral blindness, and guardianship at the accounting layer.",
    },
    "status-laundering-at-the-registry-interface.md": {
        "series": "Founding & Charter Law",
        "tags": ["Founding & Charter Law", "Law", "Enforcement"],
        "description": "How paperwork converts coercion into transferable legal status.",
    },
    "why-earth-union-is-still-called-earth-union.md": {
        "series": "Earth Union Institutions",
        "tags": ["Earth Union Institutions", "Policy", "History"],
        "description": "Civic naming, legal continuity, and the political value of inherited institutional names.",
    },
    "children-of-terra.md": {
        "series": "Earth Union Institutions",
        "tags": ["Earth Union Institutions", "Xenology", "Policy"],
        "description": "How a translator's improvisation became a durable legal category.",
    },
    "bells-bread-and-field-hospitals.md": {
        "series": "Earth Union Institutions",
        "tags": ["Earth Union Institutions", "Xenology", "Humanitarian Practice"],
        "description": "Earth-origin religious humanitarian institutions in external service.",
    },
    "infinite-brutality-infinite-compassion.md": {
        "series": "Earth Union Institutions",
        "tags": ["Earth Union Institutions", "Earth Fleet", "Military Ethics"],
        "description": "Boarding Marine doctrine, rescue assault, and the motto that survived training.",
    },
    "c-series-containers-founding-standard.md": {
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Standards", "Engineering"],
        "description": "The C10, C20, and C40 container family adopted during founding standards work.",
    },
    "what-fits-inside-the-standard.md": {
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Standards", "Sociology"],
        "description": "Secondary uses of C-series containers beyond freight.",
    },
    "ftl-transit-operational-tradeoffs.md": {
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "FTL", "Policy"],
        "description": "How FTL performance shapes governance, trade, and risk.",
    },
    "the-confederation-does-not-deliver-messages.md": {
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Communications", "Policy"],
        "description": "Why the mesh propagates signed information instead of guaranteeing delivery.",
    },
    "ansible-is-not-a-radio.md": {
        "series": "Infrastructure & Commerce",
        "tags": ["Infrastructure & Commerce", "Earth Fleet", "Engineering"],
        "description": "Public-science correction of common misunderstandings about ansible communication.",
    },
    "prize-class-recovery-and-the-vigilantism-line.md": {
        "series": "Law, Cognition & Enforcement",
        "tags": ["Law, Cognition & Enforcement", "Maritime Law", "Enforcement"],
        "description": "Prize Court doctrine on self-defense exclusivity and registry enforcement.",
    },
    "capability-is-not-classification.md": {
        "series": "Law, Cognition & Enforcement",
        "tags": ["Law, Cognition & Enforcement", "Artificial Cognition", "Law"],
        "description": "The Confederation two-tier artificial cognition framework.",
    },
    "institutions-without-parenthood.md": {
        "series": "Comparative Policy & Xenology",
        "tags": ["Comparative Policy & Xenology", "Threni", "Xenology"],
        "description": "Threni cohort bonds, technocracy, and the human misreading of cold institutions.",
    },
}


def parse_blockquote_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip().lstrip("> ").strip()
        if line.lower().startswith("originally published in:"):
            fields["original"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("original date:"):
            fields["original_date"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("review selection:"):
            fields["review_selection"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("author:"):
            fields["author"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("field:"):
            fields["field"] = line.split(":", 1)[1].strip()
    return fields


def indent_admonition(text: str) -> str:
    lines = []
    for line in text.strip().splitlines():
        lines.append(f"    {line}" if line else "")
    return "\n".join(lines)


def transform(path: Path, info: dict) -> None:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        text = re.sub(r"^---\n.*?\n---\n\n?", "", text, count=1, flags=re.DOTALL)

    title_match = re.match(r"^# (.+)\n\n", text)
    if not title_match:
        raise SystemExit(f"No title in {path.name}")
    title = title_match.group(1)

    rest = text[title_match.end() :]
    bq_match = re.match(r"(> .+\n(?:> .+\n)*)\n", rest)
    if not bq_match:
        raise SystemExit(f"No masthead blockquote in {path.name}")
    bq = bq_match.group(1)
    parsed = parse_blockquote_fields(bq)
    rest = rest[bq_match.end() :]

    ed_match = re.match(r"## Editorial note\n\n(.*?)\n\n## Abstract\n\n", rest, flags=re.DOTALL)
    if not ed_match:
        raise SystemExit(f"No editorial note in {path.name}")
    editorial = ed_match.group(1).strip()
    rest = rest[ed_match.end() :]

    abstract_match = re.match(r"(.*?)\n\n## Article\n\n", rest, flags=re.DOTALL)
    if not abstract_match:
        raise SystemExit(f"No abstract in {path.name}")
    abstract = abstract_match.group(1).strip()
    body = rest[abstract_match.end() :]

    tags = info["tags"]
    yaml = [
        "---",
        f'title: "{title}"',
        f'description: "{info["description"]}"',
        f'review_selection: "{parsed.get("review_selection", "")}"',
        f'original_date: "{parsed.get("original_date", "")}"',
        f'author: "{parsed.get("author", "")}"',
        f'field: "{parsed.get("field", "")}"',
        f'series: "{info["series"]}"',
        "tags:",
    ]
    yaml.extend(f"  - {tag}" for tag in tags)
    yaml.append("---\n")

    masthead_lines = [line.lstrip("> ").strip() for line in bq.splitlines()]
    masthead_md = "\n".join(f"> {line}" for line in masthead_lines if line)

    out = "\n".join(yaml)
    out += f"# {title}\n\n"
    out += '<div class="republication-masthead" markdown="1">\n\n'
    out += masthead_md + "\n\n"
    out += "</div>\n\n"
    out += f'!!! editorial "Editorial note"\n{indent_admonition(editorial)}\n\n'
    out += '<div class="review-abstract" markdown="1">\n\n'
    out += "## Abstract\n\n"
    out += abstract + "\n\n"
    out += "</div>\n\n"
    out += "## Article\n\n"
    out += body.lstrip()

    path.write_text(out, encoding="utf-8")


def main() -> None:
    for name, info in META.items():
        transform(ARTICLES_DIR / name, info)
        print(f"updated {name}")


if __name__ == "__main__":
    main()
