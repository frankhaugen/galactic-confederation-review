"""Add issue front matter and masthead lines to articles."""
import re
from pathlib import Path

ISSUES = {
    "ftl-transit-operational-tradeoffs.md": ("2494.338", "Distance and Governance"),
    "the-compromise-that-named-the-chain.md": ("2495.019", "The Chain in the Charter"),
    "the-chain-was-not-softened.md": ("2495.019", "The Chain in the Charter"),
    "ansible-is-not-a-radio.md": ("2495.301", "Signals Without Command"),
    "bells-bread-and-field-hospitals.md": ("2496.045", "Mercy at the Frontier"),
    "children-of-terra.md": ("2496.187", "Language Desk: Children of Terra"),
    "the-human-trap-in-guardianship-settlement.md": ("2496.198", "Accounts of Dependency"),
    "why-earth-union-is-still-called-earth-union.md": ("2496.201", "Language Desk: The Name on the Door"),
    "c-series-containers-founding-standard.md": ("2496.212", "The Founding Standard"),
    "what-fits-inside-the-standard.md": ("2496.212", "The Founding Standard"),
    "when-moral-alignment-failed-at-interstellar-scale.md": ("2496.214", "Legibility"),
    "the-confederation-does-not-deliver-messages.md": ("2496.214", "Legibility"),
    "what-the-ledger-refuses-to-see.md": ("2496.214", "Legibility"),
    "status-laundering-at-the-registry-interface.md": ("2496.214", "Legibility"),
    "prize-class-recovery-and-the-vigilantism-line.md": ("2496.216", "Persons, Force, and Classification"),
    "capability-is-not-classification.md": ("2496.216", "Persons, Force, and Classification"),
    "institutions-without-parenthood.md": ("2496.216", "Persons, Force, and Classification"),
    "infinite-brutality-infinite-compassion.md": ("2496.216", "Persons, Force, and Classification"),
}

SLUGS = {
    "2494.338": "2494-338-distance-and-governance",
    "2495.019": "2495-019-the-chain-in-the-charter",
    "2495.301": "2495-301-signals-without-command",
    "2496.045": "2496-045-mercy-at-the-frontier",
    "2496.187": "2496-187-language-desk-children-of-terra",
    "2496.198": "2496-198-accounts-of-dependency",
    "2496.201": "2496-201-language-desk-the-name-on-the-door",
    "2496.212": "2496-212-the-founding-standard",
    "2496.214": "2496-214-legibility",
    "2496.216": "2496-216-persons-force-and-classification",
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
        if issue_line not in body:
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
