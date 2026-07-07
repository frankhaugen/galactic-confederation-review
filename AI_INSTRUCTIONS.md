# AI Instructions

These instructions are for any AI assistant contributing to the Galactic
Confederation Review repository. They are intentionally vendor independent.

## Project purpose

The Galactic Confederation Review is an in-universe academic republication
archive connected to The Calypso Cycle. It republishes selected scholarship,
policy analysis, technical writing, historical essays, and public-interest
academic work from institutions across member polities.

The Review is funded by the Galactic Confederation but editorially independent.
Selection for republication indicates editorial relevance, not endorsement by
the Review, the Confederation, or the originating polity.

## Editorial voice and voicing

Maintain the voice of a serious academic archive.

The house voice is:

- measured
- precise
- institutionally literate
- skeptical without being cynical
- clear about uncertainty and provenance
- comfortable with legal, policy, technical, and historical nuance

Avoid:

- promotional language
- jokes or wink-at-the-reader phrasing
- direct exposition that explains the setting as if to an outside audience
- over-mystical, cinematic, or lore-dump prose
- modern internet idioms
- sweeping claims unsupported by the article's own framing

Preferred voicing patterns:

- "The Review republishes..." rather than "We bring you..."
- "This selection is notable because..." rather than "This fascinating article..."
- "The author argues..." rather than "The truth is..."
- "The originating journal..." rather than "The source..."
- "member polity" when referring to Confederation members as political units

Use editorial notes to frame why a piece matters, not to resolve every argument.
The Review may publish work that is controversial, partial, or critical. Keep
that distinction visible.

## Content conventions

Article pages generally use this shape:

1. H1 title.
2. Blockquote metadata:
   - Originally published in
   - Republished by
   - Original date
   - Review selection
   - Author
   - Field
3. `## Editorial note`
4. `## Abstract`
5. `## Article`
6. `## Notes`
7. `## Related Review selections`

Inside article metadata blockquotes, use Markdown hard line breaks with two
trailing spaces where the existing file style does so.

Prefer internal Markdown links to related selections where appropriate. Do not
invent tracked source files for cited works unless the user asks for a new
republished article.

## Technical conventions

- This is a MkDocs Material site.
- Use Markdown source files under `docs/`.
- Keep navigation in `mkdocs.yml` aligned with article additions, removals, and title changes.
- Keep `docs/index.md` aligned with the current selection list.
- Keep `docs/authors.md` aligned with new or renamed authors.
- Do not edit generated files under `site/`.

## Verification

For content or navigation changes, run:

```bash
mkdocs build --strict
```

For dependency setup, follow `README.md`:

```bash
python -m venv .venv
pip install -r requirements.txt
mkdocs serve
```

If using Windows PowerShell, activate the virtual environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Git hygiene

- Check `git status --short --branch` before staging.
- Stage only the files relevant to the task.
- Do not commit generated `site/` output.
- Do not revert unrelated worktree changes.
- Use concise commit messages that describe the editorial or technical change.

