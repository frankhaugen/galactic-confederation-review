"""Convert republication masthead blockquotes to definition-list register layout."""
import re
from pathlib import Path

ARTICLES = Path(__file__).resolve().parents[1] / "docs" / "articles"
MASTHEAD_RE = re.compile(
    r'<div class="republication-masthead" markdown="1">\s*\n'
    r'((?:> .+\n)+)'
    r'\s*</div>',
    re.MULTILINE,
)
LINE_RE = re.compile(r'^> (.+?): (.+)$')


def convert_blockquote(block: str) -> str:
    rows: list[tuple[str, str]] = []
    for line in block.strip().splitlines():
        match = LINE_RE.match(line.strip())
        if not match:
            continue
        label, value = match.group(1), match.group(2)
        rows.append((label, value))

    if not rows:
        return block

    parts = ['<dl class="masthead-register">']
    for label, value in rows:
        needs_md = "*" in value or "[" in value
        md_attr = ' markdown="1"' if needs_md else ""
        parts.append(f"  <div><dt>{label}</dt><dd{md_attr}>{value}</dd></div>")
    parts.append("</dl>")
    return "\n".join(parts)


def main() -> None:
    for path in sorted(ARTICLES.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "republication-masthead" not in text:
            continue

        def repl(match: re.Match[str]) -> str:
            inner = convert_blockquote(match.group(1))
            return (
                '<div class="republication-masthead" markdown="1">\n\n'
                f"{inner}\n\n"
                "</div>"
            )

        updated, count = MASTHEAD_RE.subn(repl, text)
        if count:
            path.write_text(updated, encoding="utf-8")
            print("updated", path.name)


if __name__ == "__main__":
    main()
