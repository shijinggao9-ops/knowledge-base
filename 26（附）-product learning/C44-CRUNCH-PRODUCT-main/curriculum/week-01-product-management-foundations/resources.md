# Week 1 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

This week's data work is small — two seed tables, ready-made queries — but set up the real tooling now since it only gets heavier from here.

- **SQLite 3.35+** — the zero-setup engine; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **PostgreSQL 16+** — the course's primary engine from Week 6 onward:
  <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **A plain Markdown editor** — anything works (VS Code, Obsidian, even a plain text editor). This week's deliverables are all Markdown files in your portfolio.
- **Python 3.10+ with pandas** (optional this week, used in the Exercise 3 stretch goal): `pip install pandas` — <https://pandas.pydata.org/docs/getting_started/install.html>

## Required reading (this week's core)

- **Marty Cagan, "The Product Manager Role" (SVPG):** <https://www.svpg.com/the-product-manager-role/>
  *Why: the clearest short statement of what the role structurally is, from one of the field's most cited voices — read before Lecture 1.*
- **Clayton Christensen et al., "Know Your Customers' Jobs to Be Done" (HBR):** <https://hbr.org/2016/09/know-your-customers-jobs-to-be-done>
  *Why: the original milkshake study and the founding JTBD framing — read before Lecture 2.*
- **Strategyzer, "Value Proposition Canvas":** <https://www.strategyzer.com/library/the-value-proposition-canvas>
  *Why: the pains/gains → relievers/creators structure used throughout this week, explained by its originators.*
- **IDEO, "Desirability, Feasibility, Viability":** <https://www.ideou.com/blogs/inspiration/how-to-balance-desirability-feasibility-and-viability-to-drive-innovation>
  *Why: the design-thinking root of the VVF lens this course extends with usability — read before Lecture 3.*

## Reference (keep in tabs)

- **Atlassian, "Product Manager vs. Product Owner":** <https://www.atlassian.com/agile/product-management/product-manager-vs-owner>
  *Why: a second, practitioner-facing take on the PM/PO line for Challenge 1.*
- **Scrum.org, "The Product Owner":** <https://www.scrum.org/resources/what-is-a-product-owner>
  *Why: the formal Scrum definition, useful as a baseline before you argue where a real company deviates from it.*
- **Reforge, "North Star Metrics":** <https://www.reforge.com/blog/north-star-metrics>
  *Why: how stage-appropriate metrics roll up into one guiding number — a preview of later weeks.*
- **Strategyn, "What is Jobs-to-be-Done?":** <https://strategyn.com/jobs-to-be-done/>
  *Why: Tony Ulwick's "Outcome-Driven Innovation" variant of JTBD — a useful second lens on the same idea.*

## Practice beyond this week's exercises

- **web.archive.org (Wayback Machine)** — <https://web.archive.org/>
  *Why: essential for Challenge 2 and the mini-project's pricing/changelog history digging.*
- **Product Hunt** — <https://www.producthunt.com/>
  *Why: browsing recent launches is a fast way to practice spotting a stated (or missing) value proposition in the wild.*
- **A real company's public job postings page** (pick any product-led company you use)
  *Why: reading current openings is one of the fastest ways to infer what stage a company believes it's in — directly useful for Challenge 2.*

## Deeper background (optional this week)

- **Clayton Christensen, "The Innovator's Dilemma"** (book) — the broader theory JTBD sits inside.
  *Why: explains why even well-run companies miss disruptive shifts — relevant again in Week 11's AI product work.*
- **Marty Cagan, "Inspired: How to Create Tech Products Customers Love"** (book) — a widely cited practitioner reference for the whole discovery→delivery→outcomes loop from Lecture 1.
  *Why: the closest thing this field has to a canonical text; worth owning, not just this week.*

## Glossary

| Term | Definition |
|------|------------|
| **PM (Product Manager)** | Owns problem definition, prioritization rationale, roadmap narrative, and cross-functional trade-off alignment. |
| **PO (Product Owner)** | Backlog- and sprint-priority-focused role from Scrum; often a narrower slice of full-scope PM. |
| **Segment** | A group of users sharing observable traits (company size, role, geography). |
| **Persona** | A semi-fictional composite of a segment, grounded in real evidence — not invention. |
| **JTBD (Jobs-to-be-Done)** | The durable functional/emotional/social outcome a user "hires" a product to accomplish. |
| **Value proposition** | The explicit map from named pains/gains to specific, checkable product behaviors that address them. |
| **Lifecycle stage** | Where a product sits along discovery → validation → growth → maturity → decline, each with its own primary metric. |
| **VVF+U lens** | Value / Viability / Feasibility / Usability — four independent tests an idea must pass before it's worth building. |
| **North Star metric** | The single metric a team treats as the best proxy for whether the product is delivering durable value. |
| **Strategic bet** | A claim + reason to believe it + specific bet + falsification condition — a strategy stated so it can be proven wrong. |
| **Activation rate** | Share of new signups who complete the steps that make them likely to get real value (often "first key action"). |
| **WAU/MAU ratio** | Weekly active ÷ monthly active users — a common proxy for how "sticky" engagement is, not just how large. |
| **NRR (net revenue retention)** | Revenue from an existing cohort of customers over time, including expansion and churn — a maturity-stage metric. |

---

*Broken link? Open an issue or PR.*
