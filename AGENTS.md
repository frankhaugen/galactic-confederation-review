# Agent Guide

This repository is maintained as a vendor-independent AI-collaboration workspace.
Any capable coding or writing assistant should be able to use these instructions,
regardless of model provider, IDE, chat surface, or automation runner.

## Start here

Read these files before making changes:

- `AI_INSTRUCTIONS.md` for project-wide behavior, editorial voice, safety, and workflow.
- `AI_SKILLS.md` for reusable task patterns such as article editing, navigation updates, and site verification.
- `README.md` for local setup and publishing commands.
- `mkdocs.yml` before changing navigation, theme behavior, plugins, or site metadata.

## Repository shape

- Source Markdown lives in `docs/`.
- Article pages live in `docs/articles/`.
- Site styling lives in `docs/assets/stylesheets/extra.css`.
- Article audio editions live in `docs/assets/audio/`.
- Audio generation scripts live in `scripts/`; the MkDocs player hook lives in `hooks/audio_player.py`.
- GitHub Pages publishing lives in `.github/workflows/pages.yml`.
- `site/`, `.venv/`, `.cache/`, and `__pycache__/` are generated or local-only and should not be committed.

## Working rules

- Preserve user-authored changes already present in the worktree.
- Keep edits narrow and consistent with the existing Markdown style.
- Prefer source changes in `docs/` and config changes in `mkdocs.yml`; do not edit generated `site/` output.
- Run `mkdocs build --strict` when changing content, navigation, theme configuration, or publishing behavior.
- If a build cannot be run, state that clearly in the handoff.
- When work is complete, commit the finished changes and push `main` to its upstream unless the user explicitly asks not to publish yet.

## Voice

The Review speaks like an independent scholarly republication archive inside the
setting. It is calm, precise, editorially restrained, and institutionally aware.
It should not sound like marketing copy, fandom summary, game lore exposition, or
a modern software product.

When in doubt, favor:

- archival clarity over drama
- institutional language over casual narration
- concrete political, legal, technical, or historical claims over vague atmosphere
- respectful distance over endorsement

## Audio editions (accessibility)

The Review publishes machine-narrated audio editions for article accessibility. For generation, verification, renaming rules, and commit expectations, follow `AI_SKILLS.md` **Skill: Publish article audio editions**.
