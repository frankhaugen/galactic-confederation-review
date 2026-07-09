# AI Skills

These are reusable, vendor-independent task patterns for AI assistants working
in this repository. `README.md` is the canonical publication model.

## Skill: Orient in the repository

Use when starting unfamiliar work.

1. Read `README.md`, `AI_INSTRUCTIONS.md`, `mkdocs.yml`, and `AGENTS.md`.
2. Check `git status --short --branch`.
3. List source files with `rg --files docs .github`.
4. Inspect recent changes with `git diff --stat`.
5. Note any existing uncommitted changes before editing.
6. Distinguish legacy issue-based navigation from the target
   selection/series/dossier model before planning edits.

## Skill: Add or revise a selection

Use when creating or materially changing a republished selection.

1. Follow the publication model in `README.md` and `AI_INSTRUCTIONS.md`.
2. Decide release date, series, dossier fit, field, and selection type before
   drafting.
3. For new selections, use the YAML front matter and header format in
   `README.md`. For legacy selections, preserve existing masthead markup unless
   migration is requested.
4. Keep the article voice scholarly and in-universe. Preserve the fictional
   author's voice; do not normalize all authors to the Review's tone.
5. Add or update the selection in `mkdocs.yml`.
6. Add or update the archive register in `docs/articles/index.md`.
7. Add or update all relevant `docs/series/*.md` pages.
8. Add or update any relevant `docs/dossiers/*.md` pages.
9. Add or update the author profile in `docs/authors.md` when needed, including
   LLM voice metadata for new authors.
10. Add related selections only when the relationship is meaningful.
11. If the article slug changes, rename any existing
    `docs/assets/audio/<slug>.mp3` to match.
12. Do not create a new issue, series, or dossier without the thresholds in
    `README.md` unless the user explicitly requests it.
13. Run `mkdocs build --strict`.
14. When narration should ship with the selection, follow **Skill: Publish
    article audio editions**.

## Skill: Import a draft selection (`tbd*.md`)

Use when a user-authored draft in `docs/articles/tbd*.md` is ready for
republication.

1. Read the draft and identify final title, author, originating venue, series
   fit, dossier fit, release date, and related selections.
2. Choose the final filename slug (`kebab-case.md`). Delete or avoid leaving
   `tbd*.md` in the tree after import.
3. Convert the draft to the standard new-selection shape from `README.md` and
   `AI_INSTRUCTIONS.md`: YAML front matter, in-universe header, republication
   note, and article body. Legacy masthead markup is acceptable only when
   matching an existing migrated cluster.
4. Assign `selection_date`, `field`, `type`, `series`, `dossiers`, `tags`, and
   other metadata from `README.md`.
5. Register the piece in `mkdocs.yml`, `docs/articles/index.md`, relevant series
   pages, and relevant dossier pages.
6. Update `docs/authors.md` and meaningful cross-links from related selections.
7. Rename any pre-generated audio from the draft slug to the final slug, or
   regenerate narration.
8. Run `python scripts/verify_article_audio.py --scope published --check-site`
   when audio is part of the release.
9. Run `mkdocs build --strict`.

`scripts/import_draft_articles.py` converts `tbd*.md` drafts when batch metadata
is already defined. Run with `--batch <name>` when available; prefer hand
conversion when the draft shape diverges from the helper's assumptions or when
the target model uses series/dossier metadata the script does not yet set.

## Skill: Add or update a series page

Use when creating or revising a reader track under `docs/series/`.

1. Read `README.md` **Series pages** for the template.
2. Include: short description, intended audience, what the series does not
   cover, recommended starting selections, all selections in release order, and
   optional pedagogical order when different from release order.
3. Keep the page navigational. Do not turn it into an essay unless explicitly
   requested.
4. Register new series pages in `mkdocs.yml`.
5. Run `mkdocs build --strict`.

## Skill: Add or update a dossier page

Use when creating or revising a curated reading packet under `docs/dossiers/`.

1. Read `README.md` **Dossier pages** for the template.
2. Include: editorial introduction, why the selections belong together, suggested
   reading order, release dates, notes on absent works, and dissenting or
   response pieces when available.
3. Do not create a dossier for fewer than three plausibly related selections
   unless the user explicitly requests it.
4. Dossiers may be updated as new selections appear. They are not locked issues.
5. Register new dossier pages in `mkdocs.yml`.
6. Run `mkdocs build --strict`.

## Skill: Update the archive register

Use when adding, renaming, or re-dating selections in `docs/articles/index.md`.

1. List selections by release date, not primarily by issue.
2. If grouping is useful, group by year first, then release date.
3. Include release date, title, series, and field in the table.
4. Do not make the register issue-centric unless maintaining a legacy view the
   user explicitly wants preserved.
5. Run `mkdocs build --strict`.

## Skill: Publish article audio editions

Use when adding or refreshing narrated accessibility editions.

1. Install audio dependencies: `pip install -r requirements-audio.txt`.
2. Generate narration: `python scripts/generate_article_audio.py` for all
   articles, or `--article <slug>` for one.
3. Regenerate a single article when needed:
   `python scripts/generate_article_audio.py --article <slug> --force`.
4. Optional backends: `edge-tts` (default, no GPU) or `llmvox` with `LLMVOX_URL`
   pointing at a running LLMVoX `/tts` server.
5. Verify: `python scripts/verify_article_audio.py --check-site`.
6. Commit MP3s and `docs/assets/audio/manifest.json` with the article source
   when publishing.
7. Do not hand-edit article Markdown for the player; `hooks/audio_player.py`
   injects it when a matching MP3 exists under `docs/assets/audio/`.

## Skill: Add a companion or excerpt selection

Use when a new selection builds on an existing article, standards document,
historical event, or technical concept already present in the archive.

1. Read the related existing selection first and identify what perspective is
   missing: technical rule, legal consequence, social practice, field report,
   dissent, or later historical reassessment.
2. Choose an originating venue and author status that fit the requested voice.
3. Make the new selection additive. Avoid repeating the same explanation except
   where a short recap is needed for context.
4. If the piece is a thesis excerpt, student essay, or partial republication,
   state that clearly in the republication note or notes.
5. For alien or non-Earth authors, ground the voice in institution, discipline,
   method, and social position rather than exotic phrasing.
6. Include concrete examples, especially mundane cases alongside unusual ones.
7. Link back to the primary related selection and update the archive register,
   series pages, dossier pages, `docs/authors.md`, and `mkdocs.yml`.
8. Run `mkdocs build --strict` after article, navigation, or index changes.

## Skill: Edit house pages

Use when changing `index.md`, `about.md`, `editorial-policy.md`, or
`authors.md`.

1. Preserve the Review's institutional distance.
2. Avoid making the Review omniscient or promotional.
3. Keep claims consistent with the archive model: republication, selection,
   provenance, and non-endorsement.
4. On the home page, emphasize recent releases and active series. Do not center
   a "current issue" unless there is an explicit editorial event.
5. For `authors.md`, keep reader-visible bios separate from LLM voice metadata.
6. Verify links and navigation with `mkdocs build --strict`.

## Skill: Update navigation

Use when adding, removing, renaming, or reordering pages.

1. Edit `mkdocs.yml`.
2. Prefer the target navigation shape from `README.md`: home, latest selections,
   series, dossiers, archive register, authors, tags, editorial policy, about.
3. Legacy issue navigation may remain until migrated. Do not remove it unless
   asked.
4. Ensure every referenced page exists under `docs/`.
5. Ensure renamed pages have matching links in `docs/index.md`, series pages,
   dossier pages, and related selections.
6. Run `mkdocs build --strict`.

## Skill: Review editorial voice

Use when asked to check style, tone, or consistency.

Look for:

- accidental out-of-universe narration
- promotional or casual phrasing
- claims that imply endorsement rather than republication
- modern idioms that break the archive voice
- wiki-page or lore-dump titles
- republication notes that explain the setting to outsiders
- inconsistent terms for member polities, journals, institutions, or dates
- all authors sounding like the Review instead of their institutions
- editorial notes that summarize too much instead of framing selection relevance
- absent-work references left unexplained

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
