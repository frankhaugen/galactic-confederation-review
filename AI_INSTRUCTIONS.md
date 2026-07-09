# AI Instructions

These instructions are for any AI assistant contributing to the Galactic
Confederation Review repository. They are intentionally vendor independent.

`README.md` is the canonical publication model. When this file and `README.md`
diverge, follow `README.md` unless the user gives explicit contrary direction.

## Project purpose

The Galactic Confederation Review is an in-universe academic republication
archive connected to *The Calypso Cycle*. It republishes selected scholarship,
policy argument, technical explanation, and archival controversy from across
member polities.

The Review is funded by the Galactic Confederation but editorially independent.
Selection for republication does not imply endorsement by the Review, the
Confederation, the originating polity, the author's institution, or any other
referenced body.

The Review is selective. Many cited works are absent from the archive. That is
not an error. Use absent-work notes when arguments refer to unavailable
material.

## Publication model

The Review is not a fixed-volume journal issue system.

It is an online republication periodical ordered by **release sequence**, not by
topic blocks. The default archival unit is the **selection**: one republished
article, lecture, archival extract, technical explanation, public argument,
memoir fragment, field note, or institutional response.

Reader-facing organization:

```text
selection -> series -> optional dossier
```

- **Series** — continuing reader tracks across time (Species Profiles, Earth
  Union Studies, Comparative Law, and similar).
- **Dossier** — curated reading packets assembled after enough selections exist
  on a subject. Dossiers replace the older issue concept for most new work.
- **Issue** — legacy collection pages under `docs/issues/`. Do not create new
  issues unless the user explicitly asks for a classic issue.

Do not force every selection into an issue. Do not treat dossiers as locked
publication issues.

### Legacy state

The live site may still use issue-based navigation and older article markup
while migration proceeds. When editing existing selections, preserve their
current structure unless the user asks to migrate them. New work should follow
the model in `README.md`.

## Terms and dates

### Release date

Use Confederation standard ordinal notation:

```text
YEAR.CYCLE_DAY
```

Examples: `2496.045`, `2496.088`, `2496.187`, `2496.203`, `2496.221`.

Dates are archive release dates, not necessarily original publication dates.
Use irregular but plausible release dates. Avoid round-number clustering unless
the sequence is deliberately ceremonial or bureaucratic.

Bad spacing example: `2496.100`, `2496.110`, `2496.120`.

### Fields

Use human-readable fields. Do not over-normalize. Invent a new field only when
forcing an article into an existing field makes it less clear.

Examples: History and Policy, Xenology and Civic Biology, Commercial and
Maritime Law, Communications Policy, Engineering, Military Ethics, Comparative
Public Law, Political Economy, Administrative Practice, Cognitive Law and
Policy, Infrastructure Sociology, Transport Liability and Civil Movement Law.

### Selection types

Use one of these broad types:

- Republication
- Abridged Republication
- Annotated Republication
- Lecture Transcript
- Field Memoir
- Technical Note
- Institutional Response
- Editorial Note
- Archival Extract
- Public Argument
- Review Essay

Do not make every selection sound like a peer-reviewed paper.

## Editorial voice and identity

The Review is an in-universe publication. It is not a wiki, encyclopedia, lore
dump, RPG sourcebook, author notes, plot summary, real-world blog, or moral
scoreboard.

The house voice is:

- academically literate
- measured and precise
- dryly funny when appropriate
- institutionally cautious
- willing to publish controversy
- transparent about selection limits
- aware that republication is not endorsement
- aware that many referenced works are absent
- broad enough for students, professionals, and interested citizens

Avoid:

- promotional language
- omniscient narrator tone
- fan explanation or wink-at-the-reader phrasing
- direct exposition that explains the setting to an outside audience
- over-mystical, cinematic, or lore-dump prose
- modern internet idioms
- sweeping claims unsupported by the article's own framing

Preferred voicing patterns:

- "The Review republishes..." rather than "We bring you..."
- "This selection is notable because..." rather than "This fascinating article..."
- "The author argues..." rather than "The truth is..."
- "The originating journal..." rather than "The source..."
- "member polity" when referring to Confederation members as political units

The Review's voice belongs mainly in:

- republication notes
- series pages
- dossier introductions
- archive metadata
- editorial policy

### Article author voice

Articles should preserve the voice of the fictional author. Do not make all
authors sound like the Review. A Kharrek military academic should not sound like
an Earth Union abolitionist. An Earth Fleet veteran should not sound like a
technical standards committee.

Selection forms should match originating institution and author:

- Technical memoranda: procedural, bounded, clear about standards and limits.
- Essays and thesis excerpts: observational, scoped, with explicit uncertainty.
- Student-authored work: narrower viewpoint and visible fieldwork limits.
- Companion selections: add a new angle rather than restating an earlier piece.
- Excerpts: say so in the republication note or notes.
- Alien authors: translated academic prose grounded in discipline and method,
  not novelty decoration.

Use editorial notes to frame why a piece matters, not to resolve every argument.

### In-universe editorial facts

Keep these background facts consistent when relevant:

- Earth Union has declined to appoint an editor to the Review's editorial board
  every time it was their turn.
- The Galactic Confederation Assembly Cultural Appropriations Committee has
  discussed defunding on many occasions but has never done so; Earth Union has
  repeatedly offered full funding instead.
- The Review has become politically untouchable and publishes controversial work
  without fear of retribution because it is truly independent.
- Appointments to the editorial board are a political hot potato, often given to
  bureaucrats or academics interested in prestige rather than content; the
  editorial staff does what it wants and the board rubber-stamps with complete
  indifference.

## Content conventions

### New selection metadata (YAML front matter)

Every new selection should include YAML front matter. Required fields:

```yaml
---
title: "Article Title"
subtitle: "Optional Subtitle"
selection_date: "2496.221"
release_cycle: "2496.221"
field: "History and Policy"
type: "Republication"
series:
  - "Historical Summaries"
dossiers:
  - "Earth Union Primer"
originating_publication: "Journal or institution name"
original_publication_date: "2495.338"
author: "Author Name"
status: "Public archive edition"
tags:
  - earth-union
  - history
---
```

Use `selection_date` for the in-universe release date visible to readers. Keep
`release_cycle` the same as `selection_date` unless site tooling needs a second
field.

Optional: `originating_institution`, `originating_polity`, `translator`,
`editorial_note`, `series_position`, `audio`.

### New selection header format

Each new selection should open with a consistent in-universe header:

```markdown
# Article Title

## Optional Subtitle

By Author Name
Institution or role

Original publication: Journal or archive name, date if known
Republication date: 2496.221
Series: Historical Summaries
Dossier: Earth Union Primer

Republication note: Short note from the Review explaining why the work was
selected, whether it is abridged, and any relevant conflict, controversy, or
context.
```

Republication notes should sound like an editorial archive, not a fandom wiki.

Good:

```markdown
Republication note: Selected for the Earth Union primer track because it gives
non-Union students a compact account of the 2189 habitat reform and the later
Compact accession. The Review has preserved the author's dry footnote style
because removing it would create more harm than clarity.
```

Bad:

```markdown
This article explains all the lore you need to understand Earth Union.
```

### Legacy selection markup

Existing selections may use older front matter (`review_selection`, `issue`,
`issue_theme`) and HTML masthead blocks (`republication-masthead`,
`!!! editorial`, `review-abstract`). Preserve that markup when editing unless
migration is explicitly requested.

### Absent works

When a selection cites unavailable material, note it plainly:

```markdown
The original response series cited by Voss has not been selected for public
archive release.

The annexes referenced in this article remain under institutional circulation
restrictions.
```

Prefer internal Markdown links to related selections where appropriate. Do not
invent tracked source files for cited works unless the user asks for a new
republished selection.

## Site shape

Preferred structure:

```text
docs/
  index.md
  about.md
  editorial-policy.md
  articles/
    index.md          # archive register
    <slug>.md
  series/
    index.md
    <series-slug>.md
  dossiers/
    index.md
    <dossier-slug>.md
  authors.md
  tags.md
  assets/
    audio/
    stylesheets/
```

Existing `docs/issues/` pages may remain as legacy collections. New
organizational pages should go under `docs/dossiers/` and `docs/series/`.

Do not delete, rename, or move existing files unless explicitly instructed.

Recommended reader navigation (target state):

```text
Review Home
Latest Selections
Series
Dossiers
Archive Register
Authors
Tags
Editorial Policy
About the Review
```

The home page should emphasize recent releases and active series. It should not
present one "current issue" as the organizing center unless there is an explicit
editorial event.

Series pages are navigation pages, not essays. Dossier pages are curated reading
packets that may be updated as new selections appear.

## Authors

`docs/authors.md` lists published authors with short believable bios.

Each author entry should include a reader-visible bio and a non-visible metadata
section for LLM authoring guidance: voice, stylistic tendencies, word
preferences, and other cues that help generated content sound like the author
without harming reader engagement. No gimmick dialects.

Only published authors belong on the authors page. Review editorial staff
content belongs on a dedicated editorial page with extra disclaimers. In-universe,
the Review should not produce original scholarship; editorial content is an
indulgence handled with care.

## Agentic contribution rules

Before adding a selection, decide:

1. What is the selection?
2. What is its release date?
3. What series does it belong to?
4. Does it belong to an existing dossier?
5. Does it need a new dossier, or is that premature?
6. Does it need a new series, or does an existing series fit?
7. Is the selection standalone enough without all referenced works?
8. Does the header make its origin clear?
9. Does the title sound like a republished article, not a wiki page?
10. Does site navigation still help a reader?

When adding a new selection:

1. Choose a release date that fits existing nearby releases.
2. Avoid round-number clustering.
3. Add the file under `docs/articles/`.
4. Add it to `docs/articles/index.md` (archive register).
5. Add it to all relevant `docs/series/*.md` pages.
6. Add it to any relevant `docs/dossiers/*.md` pages.
7. Add audio only if the selection is ready for narration.
8. Update `mkdocs.yml` navigation if the series or dossier page is new.
9. Update `docs/authors.md` when needed.

Do not:

- create a new issue for a single selection
- create a new series for a single selection unless it is clearly intended to
  continue
- create a new dossier until at least three selections plausibly belong in it,
  unless the user explicitly requests it
- rewrite existing article prose unless asked
- normalize all dates
- move existing files unless asked
- remove legacy issue pages unless asked
- convert selection pages into encyclopedic reference entries

## Technical conventions

- This is a MkDocs Material site.
- Use Markdown source files under `docs/`.
- Keep navigation in `mkdocs.yml` aligned with additions, removals, and title
  changes.
- Keep `docs/articles/index.md`, series pages, dossier pages, and `docs/index.md`
  aligned with new selections.
- Keep `docs/authors.md` aligned with new or renamed authors.
- When importing draft selections from `tbd*.md`, follow `AI_SKILLS.md`
  **Skill: Import a draft selection**.
- When publishing narrated editions, follow `AI_SKILLS.md` **Skill: Publish
  article audio editions**.
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
- When work is complete, commit the finished changes and push `main` to its
  upstream unless the user explicitly asks not to publish yet.

## Core rule

The Galactic Confederation Review is a sequential republication archive with
series and dossiers. It is not a stack of fixed issues.

When in doubt, publish the selection, attach it to the right series, and let
dossiers emerge when the archive has earned them.
