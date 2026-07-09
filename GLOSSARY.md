# Glossary

In-universe and editorial terms for contributors, agents, and maintainers of the
Galactic Confederation Review. When writing house copy, navigation, republication
notes, series pages, or dossier introductions, prefer these terms over
present-day equivalents.

## Communications and access

| Prefer | Avoid (in house copy) | Notes |
| ------ | --------------------- | ----- |
| **the mesh**, **public mesh**, **public mesh edition** | online, internet, website, web | The Confederation's distributed civic and scholarly access layer. The Review's archive is a **public mesh republication periodical**, not a website in the modern sense. |
| **mesh circulation**, **mesh release** | online publication, going live | A selection entering public mesh availability. |
| **archive register** | database, content index | The ordered list of released selections. |
| **pulse traffic**, **bulk traffic** | real-time chat, email | Ansible and postal metaphors; see Communications selections. |

Authors inside republished articles may use period-appropriate or polemical terms
(including "internet" as a category error they are arguing against). House voice
should not.

## Publication model

| Term | Meaning |
| ---- | ------- |
| **selection** | One republished work: article, lecture, extract, technical note, memoir fragment, institutional response, or similar. |
| **selection date** / **release date** | Confederation ordinal date (`YEAR.CYCLE_DAY`) when the Review released the work to the public mesh archive. |
| **series** | Optional continuing reader track across releases (Species Profiles, Earth Union Studies, etc.). |
| **dossier** | Optional curated reading packet assembled after enough related selections exist. |
| **republication note** | Short Review framing: why the work was selected, abridgement, controversy, absent works. |
| **editorial content** | Rare original work produced by Review staff (Language Desk, etc.). An indulgence; not ordinary republication. |

## Optional structure

Not every selection belongs to a series or dossier.

- **Standalone selection** — released on its own merits; may later be added to a series or dossier.
- **Series only** — tracked across time without dossier membership.
- **Dossier only** — unusual; dossiers normally draw from existing releases.

When adding metadata, omit empty `series:` or `dossiers:` lists rather than forcing a fit.

## Institutions and voice

| Term | Meaning |
| ---- | ------- |
| **member polity** | A political unit in the Galactic Confederation. |
| **originating publication** | Journal, institute, office, or archive where the work first appeared. |
| **public archive edition** | Distribution class for this mesh-facing republication layer. |
| **absent work** | A cited source not selected for republication; normal, not an error. |

## Author metadata (contributors)

Published **contributing authors** appear on `docs/authors.md` with
institution-style bios and a list of their selections in this archive.

**Editorial staff** (Language Desk, etc.) appear on `docs/editorial-content.md`,
not on the authors page.

Each author entry may include an HTML comment block (`<!-- author-metadata: ... -->`)
in the Markdown source for LLM authoring guidance. That block is not shown to mesh
readers in the built site.

## Dates

Confederation standard ordinal notation:

```text
YEAR.CYCLE_DAY
```

Example: `2496.221` — the 221st day of cycle year 2496.

Selection dates are archive release dates, not necessarily original publication dates.
