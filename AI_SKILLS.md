# AI Skills

These are reusable, vendor-independent task patterns for AI assistants working
in this repository.

## Skill: Orient in the repository

Use when starting unfamiliar work.

1. Read `README.md`, `mkdocs.yml`, and `AGENTS.md`.
2. Check `git status --short --branch`.
3. List source files with `rg --files docs .github`.
4. Inspect recent changes with `git diff --stat`.
5. Note any existing uncommitted changes before editing.

## Skill: Add or revise an article

Use when creating or materially changing a republished selection.

1. Match the article structure described in `AI_INSTRUCTIONS.md`.
2. Keep the article voice scholarly and in-universe.
3. Add or update the article entry in `mkdocs.yml`.
4. Add or update the selection link in `docs/index.md`.
5. Add or update the author profile in `docs/authors.md` when needed.
6. Add related Review selections only when the relationship is meaningful.
7. Run `mkdocs build --strict`.

## Skill: Add a companion or excerpt article

Use when a new selection builds on an existing article, standards document,
historical event, or technical concept already present in the archive.

1. Read the related existing article first and identify what perspective is
   missing: technical rule, legal consequence, social practice, field report,
   dissent, or later historical reassessment.
2. Choose an originating venue and author status that fit the requested voice:
   standards office, university journal, undergraduate paper, professional
   society bulletin, policy office, field report, or local archive.
3. Make the new article additive. Avoid repeating the same explanation except
   where a short recap is needed for context.
4. If the piece is a thesis excerpt, student essay, or partial republication,
   state that clearly in the editorial note or notes and keep the scope
   appropriately narrower than a mature monograph.
5. For alien or non-Earth authors, ground the voice in institution, discipline,
   method, and social position rather than exotic phrasing.
6. Include concrete examples that demonstrate the article's claim, especially
   mundane cases alongside unusual ones. The Review voice works best when
   strange material is treated with administrative seriousness.
7. Link back to the primary related selection in `## Related Review selections`
   and update `docs/index.md`, `docs/authors.md`, and `mkdocs.yml`.
8. Run `mkdocs build --strict` after article, navigation, or index changes.

## Skill: Edit house pages

Use when changing `index.md`, `about.md`, `editorial-policy.md`, or
`authors.md`.

1. Preserve the Review's institutional distance.
2. Avoid making the Review omniscient or promotional.
3. Keep claims consistent with the archive model: republication, selection,
   provenance, and non-endorsement.
4. Verify links and navigation with `mkdocs build --strict`.

## Skill: Update navigation

Use when adding, removing, renaming, or reordering pages.

1. Edit `mkdocs.yml`.
2. Ensure every referenced page exists under `docs/`.
3. Ensure renamed pages have matching links in `docs/index.md` and related
   selections.
4. Run `mkdocs build --strict`.

## Skill: Review editorial voice

Use when asked to check style, tone, or consistency.

Look for:

- accidental out-of-universe narration
- promotional or casual phrasing
- claims that imply endorsement rather than republication
- modern idioms that break the archive voice
- inconsistent terms for member polities, journals, institutions, or dates
- editorial notes that summarize too much instead of framing selection relevance

Suggest small, line-level fixes before proposing structural rewrites.

## Skill: Prepare a publishable change

Use before committing and pushing.

1. Check `git status --short --branch`.
2. Review the diff for only intended files.
3. Run `mkdocs build --strict` when source, config, or workflow files changed.
4. Stage only intended files.
5. Commit with a short descriptive message.
6. Push `main` to its upstream remote when work is complete, unless the user
   explicitly asks not to publish yet.
