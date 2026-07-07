"""Add issue front matter and masthead lines to articles."""
import re
from pathlib import Path

ISSUES = {
    # Guardianship
    "the-compromise-that-named-the-chain.md": ("2495.019", "Guardianship"),
    "the-chain-was-not-softened.md": ("2495.019", "Guardianship"),
    "the-human-trap-in-guardianship-settlement.md": ("2495.019", "Guardianship"),
    "when-moral-alignment-failed-at-interstellar-scale.md": ("2495.019", "Guardianship"),
    "what-the-ledger-refuses-to-see.md": ("2495.019", "Guardianship"),
    "status-laundering-at-the-registry-interface.md": ("2495.019", "Guardianship"),
    # Communications
    "ansible-is-not-a-radio.md": ("2495.301", "Communications"),
    "the-confederation-does-not-deliver-messages.md": ("2495.301", "Communications"),
    # Hard Science
    "ftl-transit-operational-tradeoffs.md": ("2494.338", "Hard Science"),
    "c-series-containers-founding-standard.md": ("2494.338", "Hard Science"),
    "what-fits-inside-the-standard.md": ("2494.338", "Hard Science"),
    "capability-is-not-classification.md": ("2494.338", "Hard Science"),
    # Earth Union
    "bells-bread-and-field-hospitals.md": ("2496.045", "Earth Union"),
    "children-of-terra.md": ("2496.045", "Earth Union"),
    "why-earth-union-is-still-called-earth-union.md": ("2496.045", "Earth Union"),
    "infinite-brutality-infinite-compassion.md": ("2496.045", "Earth Union"),
    # Comparative Law
    "prize-class-recovery-and-the-vigilantism-line.md": ("2496.216", "Comparative Law"),
    "institutions-without-parenthood.md": ("2496.216", "Comparative Law"),
}

SLUGS = {
    "2495.019": "2495-019-guardianship",
    "2495.301": "2495-301-communications",
    "2494.338": "2494-338-hard-science",
    "2496.045": "2496-045-earth-union",
    "2496.216": "2496-216-comparative-law",
}


def main() -> None:
    articles = Path(__file__).resolve().parents[1] / "docs" / "articles"
    for fname, (issue, theme) in ISSUES.items():
        path = articles / fname
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            raise ValueError(f"Invalid front matter in {fname}")
        fm, body = parts[1], parts[2]
        fm = re.sub(r"\nissue:.*\n", "\n", fm)
        fm = re.sub(r"\nissue_theme:.*\n", "\n", fm)
        fm = fm.rstrip() + f'\nissue: "{issue}"\nissue_theme: "{theme}"\n'
        slug = SLUGS[issue]
        issue_line = f"> Review issue: [{issue} — *{theme}*](../issues/{slug}.md)"
        body = re.sub(r"> Review issue:.*\n", "", body)
        body = re.sub(
            r"(> Republished by: Galactic Confederation Review\n)",
            r"\1" + issue_line + "\n",
            body,
            count=1,
        )
        path.write_text("---" + fm + "---" + body, encoding="utf-8")
        print("updated", fname)


if __name__ == "__main__":
    main()
