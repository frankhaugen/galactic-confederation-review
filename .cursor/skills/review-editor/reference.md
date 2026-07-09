# Review Editor — reference

## Release date picking

Read `docs/articles/index.md`. Choose a new `selection_date` that:

- is later than the most recent entry unless deliberately backfilling
- avoids round-number clustering (`2496.230`, `2496.240`, …)
- fits the subject (responses may release after the works they answer)

Good next slots after `2496.224`: `2496.227`, `2496.229`, `2496.233`.

## Active series (optional)

| Series | Use for |
| ------ | ------- |
| Species Profiles | Member species, civic biology, kinship, translation |
| Historical Summaries | Institutional history, founding, chronology |
| Earth Union Studies | Earth Union polity, culture, Fleet, welfare state |
| Comparative Law | Cross-system law, incompatible institutions |
| Guardianship Debates | Guardianship, abolition, compromise, ledger |
| Standards and Infrastructure | Containers, registries, ship law, standards |
| Communications and Transit | Ansible, mesh policy, FTL, distance |
| Fleet and Rescue Doctrine | Nosies, rescue, boarding ethics, Fleet |

Omit `series` and `dossiers` in front matter when the piece stands alone.

## Selection types

Republication · Abridged Republication · Annotated Republication · Lecture
Transcript · Field Memoir · Technical Note · Institutional Response · Editorial
Note · Archival Extract · Public Argument · Review Essay

Use **Editorial Note** only for Review staff work on `docs/editorial-content.md`.

## Article skeleton

```markdown
---
title: "Title"
description: "One-line archive summary."
selection_date: "2496.227"
release_cycle: "2496.227"
field: "History and Policy"
type: "Republication"
series:
  - "Historical Summaries"
originating_publication: "*Journal Name*, Vol. N"
original_publication_date: "2495.338"
author: "Name, Title, Institution"
status: "Public archive edition"
tags:
  - tag-one
---
# Title

<div class="republication-masthead" markdown="1">

<dl class="masthead-register">
  <div><dt>Originally published in</dt><dd markdown="1">*Journal Name*</dd></div>
  <div><dt>Republished by</dt><dd>Galactic Confederation Review</dd></div>
  <div><dt>Series</dt><dd>Series Name</dd></div>
  <div><dt>Original date</dt><dd>2495.338</dd></div>
  <div><dt>Republication date</dt><dd>2496.227</dd></div>
  <div><dt>Author</dt><dd>Name, Institution</dd></div>
  <div><dt>Field</dt><dd>History and Policy</dd></div>
</dl>

</div>

!!! editorial "Republication note"
    Why the Review selected this work. Note abridgement, controversy, absent cited works.

<div class="review-abstract" markdown="1">

## Abstract

Two to four sentences. Argument scope, not plot summary.

</div>

## Article

### 1. First section

Body in the **author's** voice.

## Related Review selections

- [Related Title](related-slug.md)
```

## Files to touch after writing

| File | Action |
| ---- | ------ |
| `docs/articles/<slug>.md` | Create selection |
| `docs/articles/index.md` | Add row in correct year section |
| `docs/index.md` | Add to Latest selections (rotate oldest card) |
| `docs/series/<track>.md` | Add row if series member |
| `docs/dossiers/<name>.md` | Add row if dossier member |
| `docs/authors.md` | New author bio + `<!-- author-metadata -->` |
| `docs/editorial-content.md` | Only for Language Desk / staff work |

Do not add every article to `mkdocs.yml` nav; articles are reached via register,
series, and dossiers.

## Publish commands

```bash
python -m mkdocs build --strict
pip install -r requirements-audio.txt
python scripts/generate_article_audio.py --article <slug> --force
python scripts/verify_article_audio.py --scope all --check-site
```

Or one shot after the Markdown is written:

```bash
python scripts/publish_selection.py --slug <slug> --commit --push --message "Release selection: Title."
```
