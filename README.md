# Galactic Confederation Review

Selected scholarship from across the Galactic Confederation.

This repository contains the Markdown source for an in-universe academic republication archive connected to *The Calypso Cycle*.

The Review is funded by the Galactic Confederation but editorially independent. It republishes notable works from member polity journals, universities, institutes, veterans' organizations, policy offices, technical societies, and independent scholars.

## Local development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000
```

## Build

```bash
mkdocs build --strict
```

## Publishing

GitHub Pages is published by `.github/workflows/pages.yml`.

In repository settings:

1. Go to Settings.
2. Go to Pages.
3. Set source to GitHub Actions.
4. Push to `main`.
