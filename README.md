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

## Audio editions (accessibility)

Each article can publish a narrated audio edition. The site injects an audio
player automatically when a matching file exists under `docs/assets/audio/`.

Generate narration locally:

```bash
pip install -r requirements-audio.txt
python scripts/generate_article_audio.py
```

By default the generator uses **edge-tts** (no GPU required). To use a running
[LLMVoX](https://github.com/mbzuai-oryx/LLMVoX) server instead:

```bash
set LLMVOX_URL=http://127.0.0.1:9000
python scripts/generate_article_audio.py --backend llmvox
```

Optional voice tuning for edge-tts:

```bash
set REVIEW_TTS_VOICE=en-GB-SoniaNeural
set REVIEW_TTS_RATE=-5%
```

Regenerate a single article:

```bash
python scripts/generate_article_audio.py --article galactic-confederation-at-founding --force
```

Verify generated audio:

```bash
python scripts/verify_article_audio.py --check-site
```

## Publishing

GitHub Pages is published by `.github/workflows/pages.yml`.

In repository settings:

1. Go to Settings.
2. Go to Pages.
3. Set source to GitHub Actions.
4. Push to `main`.
