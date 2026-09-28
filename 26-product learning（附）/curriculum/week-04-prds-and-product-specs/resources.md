# Week 4 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

- **PostgreSQL 16+** — the course's primary engine for the events schema in Lecture 3 and Exercise 3:
  <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **SQLite 3.35+** — the zero-setup fallback; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **A Markdown editor** — any plain-text editor works. If you want live preview, [Obsidian](https://obsidian.md/) or VS Code's built-in Markdown preview are both free.

## Required reading (this week's core)

- **Atlassian, "How to write a great PRD":** <https://www.atlassian.com/agile/product-management/requirements>
  *Why: a clean, practical walkthrough of PRD sections that lines up closely with Lecture 1's skeleton.*
- **Bill Wake, "INVEST in Good Stories, and SMART Tasks":** <https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/>
  *Why: the original source for the INVEST mnemonic taught in Lecture 2 — read it straight from the source.*
- **Dan North, "Introducing BDD":** <https://dannorth.net/introducing-bdd/>
  *Why: where Given/When/Then acceptance criteria come from, explained by the person who coined it.*
- **Segment, "Tracking Plan" guide:** <https://segment.com/docs/getting-started/04-full-install/>
  *Why: the industry-standard practice of specifying event names and properties before instrumentation — directly informs Lecture 3.*

## Reference (keep in tabs)

- **Mike Cohn / Mountain Goat Software, "User Stories":** <https://www.mountaingoatsoftware.com/agile/user-stories>
  *Why: deep, free archive on story writing and slicing from one of the most-cited voices in agile practice.*
- **Atlassian, "Acceptance Criteria: A Guide":** <https://www.atlassian.com/work-management/project-management/acceptance-criteria>
  *Why: more worked examples of strong vs. weak acceptance criteria.*
- **PostgreSQL — JSON functions:** <https://www.postgresql.org/docs/current/functions-json.html>
  *Why: the reference for querying the `properties` JSON column used in this week's `events` table (Postgres uses `->`/`->>`/`jsonb` operators).*
- **SQLite — JSON1 extension:** <https://www.sqlite.org/json1.html>
  *Why: the equivalent reference for `json_extract()` on SQLite, used in this week's example queries.*
- **Google SRE Book — table of contents (free):** <https://sre.google/sre-book/table-of-contents/>
  *Why: chapters on error handling and graceful degradation deepen the "error state" category from Lecture 3's edge-case checklist.*

## Practice beyond this week's exercises

- **Reforge / product-management public essays** — search for "PRD template," "spec writing," or "acceptance criteria" from practicing PMs at Stripe, Linear, Figma, and similar — many publish their internal methodology publicly.
  *Why: seeing real, shipped specs (even redacted ones) grounds the technique in what actually gets used, not just theory.*
- **GitHub, public RFC repositories** (search "RFC template" on GitHub) — many open-source projects run a lightweight RFC process with a similar goals/non-goals/open-questions shape.
  *Why: RFCs are a close cousin of PRDs; reading a few sharpens your eye for what "buildable" looks like in the wild.*

## Deeper background (optional this week)

- **Clayton Christensen, "Competing Against Luck" (book, not free, but widely summarized)** — connects back to Week 1's JTBD framing and shows how a durable job (not a feature list) should anchor a PRD's context section.
- **Marty Cagan, "Inspired" (book, not free, but SVPG publishes many of its ideas as free essays)** — <https://www.svpg.com/articles/> for the free essay archive.
  *Why: the canonical modern-PM text on product discovery feeding directly into spec writing.*

## Glossary

| Term | Definition |
|------|------------|
| **PRD** | Product requirements document — the spec that tells a team what to build, why, and how success is measured. |
| **Non-goal** | Something adjacent to the feature, explicitly excluded from this iteration, with a stated reason. |
| **User story** | A short "As a / I want / so that" statement of a capability from the user's point of view. |
| **INVEST** | Independent, Negotiable, Valuable, Estimable, Small, Testable — the six-letter test for a well-formed story. |
| **Acceptance criteria** | Precise, checkable Given/When/Then statements defining exactly what "done" means for a story. |
| **Definition of done (DoD)** | A checklist that applies across every story in a feature (instrumentation, rollout, no open P0/P1s), distinct from per-story acceptance criteria. |
| **Edge case** | A boundary, error, empty, permission, or timing scenario outside the happy path that still needs a deliberate, stated behavior. |
| **Instrumentation** | The specific events, properties, and schema a feature must log so its behavior and impact are SQL-queryable after launch. |
| **Guardrail metric** | A metric that reveals harm even when the primary success metric looks good. |
| **Open question** | An unresolved decision in a PRD, given an explicit owner and a point by which it must be resolved. |

---

*Broken link? Open an issue or PR.*
