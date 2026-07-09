# Galactic Confederation Review

Selected scholarship from across the Galactic Confederation.

This repository contains the Markdown source for an in-universe academic republication archive connected to *The Calypso Cycle*.

The Review is funded by the Galactic Confederation but editorially independent. It republishes notable works from member polity journals, universities, institutes, veterans' organizations, policy offices, technical societies, and independent scholars.

## Publication model

The Galactic Confederation Review is not a journal issue system in the old fixed-volume sense.

It is an online republication periodical. Selections are released when they clear editorial review, rights confirmation, translation review, and archive formatting. Some releases stand alone. Some belong to long-running series. Some are later gathered into dossiers when a subject has enough gravity to deserve a reader-facing collection.

The default unit is the **selection**.

A selection is one republished article, lecture, archival extract, technical explanation, public argument, memoir fragment, field note, or institutional response.

The archive is ordered by **release sequence**, not by topic blocks.

Readers may browse by:

* latest selections
* series tracks
* dossiers
* field tags
* author
* originating polity or institution
* archive date

## Terms

### Selection

A single republished work.

Every article in `docs/articles/` is a selection.

Selections are the primary archival object. A selection can belong to zero, one, or several reader-facing structures.

### Release date

The date the Review released the selection into the public archive.

Use Confederation standard ordinal notation:

```text
YEAR.CYCLE_DAY
```

Examples:

```text
2496.045
2496.088
2496.187
2496.203
2496.221
```

Dates should not look artificially neat. The Review publishes as works become ready. Avoid tidy spacing unless the sequence is deliberately ceremonial or bureaucratic.

Good:

```text
2496.045
2496.088
2496.187
2496.201
2496.203
2496.204
2496.217
2496.221
```

Bad:

```text
2496.100
2496.110
2496.120
2496.130
```

### Series

A series is a continuing reader track.

A series lets readers follow a type of article across time, even when the main release stream jumps between law, species profiles, history, engineering, and memoir.

Examples:

* Species Profiles
* Historical Summaries
* Earth Union Studies
* Comparative Law
* Guardianship Debates
* Standards and Infrastructure
* Communications and Transit
* Fleet and Rescue Doctrine
* Civic Systems and Welfare Militarism
* Commercial Practice
* Personhood and Cognitive Law

A series does not need to publish in order without interruption. It may receive new entries whenever a suitable work is ready.

### Dossier

A dossier is a curated collection around a subject.

Dossiers replace the older "issue" concept for most purposes. They are not fixed-period releases. They are reading packets assembled after enough selections exist.

Examples:

* Guardianship Settlement Dossier
* Earth Union Primer Dossier
* Compact and Confederation Origins Dossier
* Ansible and Communications Dossier
* Ship Law and Registry Dossier
* Boarding Marine Ethics Dossier

A dossier may contain selections released across several dates and several series.

### Issue

Avoid creating new "issues" unless the user explicitly asks for a classic issue.

Existing issue pages may remain as legacy collections, but new work should prefer:

```text
selection -> series -> optional dossier
```

Do not force every article into an issue.

## Site shape

The publication should feel like a living online archive, not a quarterly magazine.

Recommended reader navigation:

```text
Review Home
Latest Selections
Series
  Species Profiles
  Historical Summaries
  Earth Union Studies
  Comparative Law
  Guardianship Debates
  Standards and Infrastructure
  Communications and Transit
  Fleet and Rescue Doctrine
Dossiers
  Earth Union Primer
  Guardianship Settlement
  Compact and Confederation Origins
  Ship Law and Registry
Archive Register
Authors
Tags
Editorial Policy
About the Review
```

The home page should emphasize recent releases and active series.

It should not present one "current issue" as the organizing center unless there is an explicit editorial event.

## File structure

Preferred structure:

```text
docs/
  index.md
  about.md
  editorial-policy.md

  articles/
    index.md
    <slug>.md

  series/
    index.md
    species-profiles.md
    historical-summaries.md
    earth-union-studies.md
    comparative-law.md
    guardianship-debates.md
    standards-and-infrastructure.md
    communications-and-transit.md
    fleet-and-rescue-doctrine.md

  dossiers/
    index.md
    earth-union-primer.md
    guardianship-settlement.md
    compact-and-confederation-origins.md
    ship-law-and-registry.md

  authors.md
  tags.md
  assets/
    audio/
    stylesheets/
```

Existing `docs/issues/` pages may remain as legacy redirects or legacy dossiers, but new organizational pages should go under `docs/dossiers/`.

Do not delete or rename existing files unless explicitly instructed.

## Article metadata

Every article should include YAML front matter.

Required:

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
  - habitats
---
```

Use `selection_date` for the in-universe release date visible to readers.

Use `release_cycle` only if site tooling needs a second field. If not needed, keep it the same as `selection_date`.

Optional:

```yaml
originating_institution: "University of Luna"
originating_polity: "Earth Union"
translator: "Review Translation Office"
editorial_note: "Short note if needed"
series_position: 3
audio: true
```

`series_position` is optional. Use it only when the series has a deliberate pedagogical order.

## Article header format

Each article should open with a consistent in-universe header.

Use this shape:

```markdown
# Article Title

## Optional Subtitle

By Author Name  
Institution or role

Original publication: Journal or archive name, date if known  
Republication date: 2496.221  
Series: Historical Summaries  
Dossier: Earth Union Primer

Republication note: Short note from the Review explaining why the work was selected, whether it is abridged, and any relevant conflict, controversy, or context.
```

The republication note should sound like an editorial archive, not a fandom wiki.

Good:

```markdown
Republication note: Selected for the Earth Union primer track because it gives non-Union students a compact account of the 2189 habitat reform and the later Compact accession. The Review has preserved the author's dry footnote style because removing it would create more harm than clarity.
```

Bad:

```markdown
This article explains all the lore you need to understand Earth Union.
```

## Series pages

A series page is a reading track.

It should include:

* short description
* intended audience
* what the series does not cover
* recommended starting selections
* all selections in release order
* optional "pedagogical order" if different from release order

Template:

```markdown
# Species Profiles

The Species Profiles series republishes introductory and mid-level works on Confederation member species, with emphasis on civic biology, social structure, legal implications, and common translation errors.

This series is for readers who want species context without reading the law and treaty material first.

## Start here

1. [The Species Without Mothers](../articles/the-species-without-mothers.md)
2. [Institutions Without Parenthood](../articles/institutions-without-parenthood.md)

## Release order

| Release | Selection | Field |
| ------- | --------- | ----- |
| 2496.207 | [The Species Without Mothers](../articles/the-species-without-mothers.md) | Xenology and Civic Biology |
| 2496.220 | [Institutions Without Parenthood](../articles/institutions-without-parenthood.md) | Xenology and Policy |
```

Series pages should not become essays unless explicitly requested. They are navigation pages.

## Dossier pages

A dossier is a curated packet.

It should include:

* editorial introduction
* why the selections belong together
* suggested reading order
* release dates
* notes on absent works
* dissenting or response pieces when available

Template:

```markdown
# Earth Union Primer Dossier

This dossier gathers selections useful for students trying to understand Earth Union as polity, culture, legal actor, and strategic force.

It is not a complete history. It is a guided entry point.

## Suggested reading order

| Order | Release | Selection | Why here |
| ----- | ------- | --------- | -------- |
| 1 | 2496.199 | [From Nations To Habitats](../articles/from-nations-to-habitats.md) | Basic institutional history |
| 2 | 2496.201 | [Why Earth Union Is Still Called Earth Union](../articles/why-earth-union-is-still-called-earth-union.md) | Naming and legitimacy |
| 3 | 2496.202 | [The State That Kept Saying Yes](../articles/the-state-that-kept-saying-yes.md) | Welfare-state militarism from inside |
```

Dossiers may be updated as new selections appear.

Do not treat dossiers as locked publication issues.

## Archive register

The archive register should list all selections by release date.

Recommended table:

```markdown
# Archive Register

| Release | Title | Series | Field |
| ------- | ----- | ------ | ----- |
| 2496.045 | [Bells, Bread, and Field Hospitals](bells-bread-and-field-hospitals.md) | Earth Union Studies | Xenology and Policy |
| 2496.088 | [The Ships That Do Not Fight](the-ships-that-do-not-fight.md) | Fleet and Rescue Doctrine | Administrative Practice |
| 2496.187 | [Children of Terra](children-of-terra.md) | Earth Union Studies | Policy and Xenology |
```

The register should not group primarily by issue.

If grouping is useful, group by year first, then release date.

## Dates and sequencing rules

Dates are archive release dates, not necessarily original publication dates.

Use irregular but plausible release dates.

A release date can be earlier than another article in the same series.

A dossier can contain articles from different years.

A response article may be released before the Review republishes the original if the original is not selected for public archive release. This is allowed and in-universe plausible.

When adding a new article:

1. Choose a release date that fits existing nearby releases.
2. Avoid round-number clustering.
3. Add the article to `docs/articles/`.
4. Add the article to `docs/articles/index.md`.
5. Add it to all relevant `docs/series/*.md` pages.
6. Add it to any relevant `docs/dossiers/*.md` page.
7. Add audio only if the article is ready for narration.
8. Update `mkdocs.yml` navigation if the series or dossier page is new.

## Selection types

Use one of these broad types:

* Republication
* Abridged Republication
* Annotated Republication
* Lecture Transcript
* Field Memoir
* Technical Note
* Institutional Response
* Editorial Note
* Archival Extract
* Public Argument
* Review Essay

The Review republishes many kinds of material. Do not make everything sound like a peer-reviewed paper.

## Fields

Use human-readable fields. Do not over-normalize.

Good examples:

* History and Policy
* Xenology and Civic Biology
* Commercial and Maritime Law
* Communications Policy
* Engineering
* Military Ethics
* Comparative Public Law
* Political Economy
* Administrative Practice
* Cognitive Law and Policy
* Infrastructure Sociology
* Transport Liability and Civil Movement Law

Do not invent a new field if an existing one clearly fits.

Do invent a new field if forcing the article into an old field makes it less clear.

## Tone and identity

The Review is an in-universe publication.

It is not a wiki.

It is not an encyclopedia.

It is not a lore dump.

It is a selective republication archive with editorial personality.

The Review should feel like:

* academically literate
* dryly funny when appropriate
* institutionally cautious
* willing to publish controversy
* transparent about selection limits
* aware that republication is not endorsement
* aware that many referenced works are absent
* broad enough for students, professionals, and interested citizens

The Review should not feel like:

* omniscient narrator
* fan explanation
* RPG sourcebook
* author notes
* plot summary
* real-world blog commentary
* clean moral scoreboard

## In-universe editorial stance

The Review is funded by the Galactic Confederation but editorially independent.

Selection for republication does not imply endorsement by:

* the Review
* the Galactic Confederation
* the originating polity
* the author's institution
* the author's species, government, ship, order, guild, or creditors

The Review selects works because they travel well across polity boundaries.

A work may be selected because it is:

* useful
* provocative
* controversial
* clarifying
* historically important
* technically elegant
* widely misunderstood
* frequently cited
* dangerous in an instructive way
* funny by accident

## Absent works

The Review is selective.

Many cited works are not present in the archive.

This is not an error.

Use notes like:

```markdown
The original response series cited by Voss has not been selected for public archive release.

The annexes referenced in this article remain under institutional circulation restrictions.

Several replies are summarized in later selections but are not reproduced here.
```

This explains why a reader can see arguments referring to works that are not available on the site.

## Article style

Articles should preserve the voice of the fictional author.

Do not make all authors sound like the Review.

A Kharrek military academic should not sound like an Earth Union abolitionist.

An Earth Fleet veteran should not sound like a technical standards committee.

A public law scholar should not sound like a field engineer.

The Review's voice belongs mainly in:

* republication notes
* series pages
* dossier introductions
* archive metadata
* editorial policy

## Agentic contribution rules

When an agent adds content, it should preserve the publication mold.

Before adding an article, decide:

1. What is the selection?
2. What is its release date?
3. What series does it belong to?
4. Does it belong to an existing dossier?
5. Does it need a new dossier, or is that premature?
6. Does it need a new series, or does an existing series fit?
7. Is the article standalone enough to publish without all referenced works?
8. Does the article header make its origin clear?
9. Does the title sound like a republished article, not a wiki page?
10. Does the site navigation still help a reader?

Do not create a new issue for a single article.

Do not create a new series for a single article unless it is clearly intended to continue.

Do not create a new dossier until at least three selections plausibly belong in it, unless the user explicitly requests it.

Do not rewrite existing article prose unless asked.

Do not normalize all dates.

Do not move existing files unless asked.

Do not remove legacy issue pages unless asked.

Do not convert article pages into encyclopedic reference entries.

## Suggested starting series

The current and likely near-future site can use these series.

### Species Profiles

Introductory and mid-level works on member species, civic biology, kinship, social structure, legal implications, and translation errors.

Example selections:

* The Species Without Mothers
* Institutions Without Parenthood

### Historical Summaries

Student-facing institutional history, chronology, founding narratives, and long-arc polity explanations.

Example selections:

* From Nations To Habitats
* The Galactic Confederation at Founding
* When Moral Alignment Failed at Interstellar Scale

### Earth Union Studies

Works about Earth Union as polity, culture, legal actor, welfare state, Fleet power, and uncomfortable neighbor.

Example selections:

* Why Earth Union Is Still Called Earth Union
* The State That Kept Saying Yes
* Bells, Bread, and Field Hospitals

### Comparative Law

Law across systems, especially when similar terms hide incompatible institutions.

Example selections:

* Prize-Class Recovery and the Vigilantism Line
* The Door Was Not Hidden
* Status Laundering at the Registry Interface

### Guardianship Debates

Works about Guardianship, slavery, regulated unfreedom, abolitionist pressure, legal compromise, and economic fraud.

Example selections:

* The Compromise That Named the Chain
* The Chain Was Not Softened
* Earth Stole My Property
* What the Ledger Refuses to See

### Standards and Infrastructure

Works about containers, registries, ship law, insurance, engineering standards, and the procedural machinery of trade.

Example selections:

* C-Series Containers and the Founding Standard
* The Ship Is The Flag
* The Ship That Can Sign Its Own Shadow
* What Fits Inside the Standard

### Communications and Transit

Works about ansibles, message systems, transit constraints, FTL, and the institutional consequences of distance.

Example selections:

* The Ansible Is Not a Radio
* The Confederation Does Not Deliver Messages
* Faster-Than-Light Transit

### Fleet and Rescue Doctrine

Works about Earth Fleet, Nosies, rescue, anti-piracy doctrine, military ethics, boarding, and public-force legitimacy.

Example selections:

* The Ships That Do Not Fight
* Infinite Brutality, Infinite Compassion

## Recommended front page behavior

The front page should show:

1. Publication identity.
2. Latest selections in release order.
3. Active series.
4. Featured dossiers.
5. A short editorial mandate.

It should not say "Current issue" unless the Review is deliberately presenting a temporary themed release.

Suggested front page language:

```markdown
The Galactic Confederation Review republishes selected scholarship, policy argument, technical explanation, and archival controversy from across member polities.

Selections are released as they clear review. Some stand alone. Some belong to continuing series. Some are later gathered into dossiers for readers who want a guided path through a subject.
```

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

## Audio editions

Each article may publish a narrated audio edition.

The site injects an audio player automatically when a matching file exists under:

```text
docs/assets/audio/
```

Generate narration locally:

```bash
pip install -r requirements-audio.txt
python scripts/generate_article_audio.py
```

Regenerate a single article:

```bash
python scripts/generate_article_audio.py --article article-slug --force
```

Verify generated audio:

```bash
python scripts/verify_article_audio.py --check-site
```

## Publishing

GitHub Pages is published by:

```text
.github/workflows/pages.yml
```

In repository settings:

1. Go to Settings.
2. Go to Pages.
3. Set source to GitHub Actions.
4. Push to `main`.

## Core rule

The Galactic Confederation Review is a sequential republication archive with series and dossiers.

It is not a stack of fixed issues.

When in doubt, publish the selection, attach it to the right series, and let dossiers emerge when the archive has earned them.
