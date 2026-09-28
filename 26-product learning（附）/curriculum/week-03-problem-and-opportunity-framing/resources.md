# Week 3 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first (if you haven't already, from Week 1)

- **PostgreSQL 16+** — the course's primary engine: <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **SQLite 3.35+** — the zero-setup fallback; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- This week's SQL is single-table aggregation and `CASE WHEN` logic — if you're comfortable with [C33 Crunch SQL Week 1](../../../C33-CRUNCH-SQL/curriculum/week-01-relational-model-and-select/), you have everything you need. If any query in Lecture 2 or Exercise 2 feels unfamiliar, that week is the fastest way to fill the gap.

## Required reading (this week's core)

- **Clayton Christensen, "Know Your Customers' 'Jobs to Be Done'" (Harvard Business Review):** <https://hbr.org/2016/09/know-your-customers-jobs-to-be-done>
  *Why: the foundational JTBD article this week's Lecture 1 builds directly on.*
- **Teresa Torres, "The Opportunity Solution Tree: Visualize Your Thinking":** <https://www.producttalk.org/2016/08/opportunity-solution-tree/>
  *Why: the original source for Lecture 3's core framework, from the person who coined it.*
- **ASQ, "Five Whys":** <https://asq.org/quality-resources/five-whys>
  *Why: the short, canonical explanation of the root-cause technique used throughout Lecture 1.*
- **PostgreSQL — aggregate functions:** <https://www.postgresql.org/docs/current/functions-aggregate.html>
  *Why: `COUNT`, `AVG`, `SUM`, and the `FILTER` clause you'll use constantly in Lecture 2 and Exercise 2.*

## Reference (keep in tabs)

- **Alan Klement, jobs-to-be-done.com:** <https://www.jobs-to-be-done.com/>
  *Why: a deeper, ongoing JTBD resource beyond the single HBR article.*
- **Teresa Torres, Product Talk (full site):** <https://www.producttalk.org/>
  *Why: continuous discovery, opportunity trees, and interviewing — most of it free, and it's the throughline connecting this week to Week 2's research methods.*
- **Total addressable market — background and definitions:** <https://en.wikipedia.org/wiki/Total_addressable_market>
  *Why: a clear, neutral explainer of TAM/SAM/SOM terminology if Lecture 2's worked example needs a second angle.*
- **Mermaid — flowchart/graph syntax:** <https://mermaid.js.org/syntax/flowchart.html>
  *Why: the plain-text diagram syntax used for opportunity-solution trees in Lecture 3 and the mini-project; renders natively in GitHub/GitLab Markdown.*
- **PostgreSQL — `CASE` expressions:** <https://www.postgresql.org/docs/current/functions-conditional.html>
  *Why: the `CASE WHEN` pattern used for bucketing (seats, error types, cohort labels) throughout this week's SQL.*
- **SQLite — aggregate functions:** <https://www.sqlite.org/lang_aggfunc.html>
  *Why: SQLite's equivalent aggregate reference; note SQLite added `FILTER` support in 3.30 — use `CASE WHEN` + `SUM` if you're on an older build.*

## Practice beyond this week's dataset

- **Product Talk — "Opportunity Solution Trees" tag** (ongoing case studies and examples): <https://www.producttalk.org/opportunity-solution-tree/>
  *Why: more worked examples of real trees, beyond the single Loopline case this week uses.*
- **PostgreSQL Exercises** (free, browser-based `SELECT`/aggregate drills, useful if Exercise 2's SQL felt shaky): <https://pgexercises.com/>

## Glossary

| Term | Definition |
|------|------------|
| **Problem statement** | A who/what/why/impact description of a gap between user goal and current reality, stated without a baked-in solution. |
| **Symptom** | An observable, measurable effect (a support ticket count, a conversion-rate dip) that is evidence a problem may exist — not the problem itself. |
| **Solution** | A specific, buildable thing proposed to address a problem — should come *after* the problem is understood, not before. |
| **Five Whys** | A root-cause technique: repeatedly ask "why" starting from a symptom until you reach an actionable or fundamental cause. |
| **JTBD (jobs-to-be-done)** | A statement of what progress a user is trying to make, in a given situation, expressed as situation → motivation → outcome. |
| **Falsifiable** | Capable of being proven wrong by some conceivable evidence — a required property of a good problem statement. |
| **TAM** | Total Addressable Market — the theoretical ceiling: everyone who could conceivably want the product, with no reach constraints. |
| **SAM** | Serviceable Available Market — the slice of TAM that's realistically a customer for your category, given real-world constraints. |
| **SOM** | Serviceable Obtainable Market — the slice of SAM you specifically could plausibly capture in a defined window, given your actual size and reach. |
| **Bottom-up sizing** | Building an estimate from your own observed funnel/usage data rather than market-wide assumptions. |
| **Confounding variable** | A hidden factor that influences both sides of an observed relationship, making a correlation look more causal than it is. |
| **Opportunity-solution tree (OST)** | A discovery artifact mapping one outcome to multiple opportunities to multiple candidate solutions, used to make prioritization visible and revisable. |
| **Outcome** | A measurable, product-level result an OST is rooted in — not a feature. |
| **Opportunity** | An unmet need, pain point, or desire, stated from the customer's point of view, that plausibly serves an outcome. |
| **Kill memo** | A written, evidence-based recommendation not to pursue an idea, including the reasoning and the conditions that would revisit it. |

---

*Broken link? Open an issue or PR.*
