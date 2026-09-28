# Week 5 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

- **PostgreSQL 16+** or **SQLite 3.35+** — you likely already have one from earlier weeks. If not: PostgreSQL <https://www.postgresql.org/download/> (macOS: [Postgres.app](https://postgresapp.com/)); SQLite ships on macOS/most Linux already — check with `sqlite3 --version`.
- **Python 3.10+** with `pandas` and `sqlalchemy`:
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  pip install pandas sqlalchemy psycopg2-binary
  ```
- **A GUI (optional)** — [DBeaver](https://dbeaver.io/) (free, both engines) if you want to browse the backlog tables visually. Not required — the terminal is enough this week.

## Required reading (this week's core)

- **Intercom, "RICE: Simple prioritization for product managers"** — the original public writeup of the framework, by the team that popularized it:
  <https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/>
  *Why: the canonical explanation of Reach/Impact/Confidence/Effort, straight from its creators.*
- **Kano Model overview (with the evaluation matrix and Better/Worse coefficients laid out clearly):**
  <https://www.productplan.com/glossary/kano-model/>
  *Why: a clean reference for the matrix and the math — bookmark it for Exercise 2 and the mini-project.*
- **Scaled Agile Framework, "WSJF" (official, canonical reference):**
  <https://scaledagileframework.com/wsjf/>
  *Why: the primary source for cost of delay's three components and the WSJF formula, from the framework that formalized it.*
- **ProductPlan, "Now-Next-Later Roadmap":**
  <https://www.productplan.com/glossary/now-next-later-roadmap/>
  *Why: the reference for this week's roadmap format and why it beats date-based roadmaps for communicating uncertainty.*

## Reference (keep in tabs)

- **Don Reinertsen's Cost of Delay, explained (Black Swan Farming primer by Joshua Arnold):**
  <https://blackswanfarming.com/cost-of-delay/>
  *Why: the deepest accessible treatment of *why* cost of delay matters, beyond just the WSJF formula.*
- **Janna Bastow, "Introducing the Now-Next-Later Roadmap" (the format's creator):**
  <https://www.mindtheproduct.com/now-next-later-roadmaps-janna-bastow-mind-the-product/>
  *Why: hear the reasoning straight from the person who popularized the format at ProdPad.*
- **Atlassian, "Prioritization framework" (RICE, WSJF, MoSCoW, Value vs. Effort, compared side by side):**
  <https://www.atlassian.com/agile/product-management/prioritization-framework>
  *Why: a useful map of the wider landscape of frameworks this course doesn't cover in depth (MoSCoW, Value vs. Effort).*
- **SVPG (Marty Cagan), "Roadmaps":**
  <https://www.svpg.com/roadmaps/>
  *Why: the philosophical case for outcome-based roadmaps over feature-and-date roadmaps, from a widely cited voice in the field.*
- **pandas documentation, "Group by: split-apply-combine":**
  <https://pandas.pydata.org/docs/user_guide/groupby.html>
  *Why: useful when you extend Exercise 3's capacity-bucketing logic beyond a simple loop.*
- **PostgreSQL — Window Functions:**
  <https://www.postgresql.org/docs/current/tutorial-window.html>
  *Why: `RANK() OVER (...)`, used in Exercise 1's stretch goal and the mini-project's rank-shift query.*

## Practice beyond the seed backlog

- **ProductPlan's free prioritization templates and glossary** (browse the broader glossary for MoSCoW, Value vs. Effort, and other frameworks this week only touches on):
  <https://www.productplan.com/glossary/>
  *Why: good for comparing this week's two frameworks against alternatives you'll encounter on the job.*
- **Reforge / Lenny's Newsletter public archive — search "prioritization framework" or "roadmap"** for widely-cited, free public essays on real-company prioritization fights:
  <https://www.lennysnewsletter.com/>
  *Why: real, named examples of the Sales-vs-Engineering conflict Challenge 1 asks you to mediate.*

## Deeper background (optional this week)

- **Noriaki Kano's original 1984 paper context (summary, since the original is in Japanese and not freely available in English translation):**
  <https://en.wikipedia.org/wiki/Kano_model>
  *Why: understand where the "attractive quality vs. must-be quality" distinction actually came from — quality engineering in manufacturing, decades before software PMs adopted it.*
- **Don Reinertsen, *The Principles of Product Development Flow*** — the book WSJF and cost-of-delay thinking trace back to (summary/excerpts freely available via the SAFe link above):
  *Why: the deeper "why" behind treating delay as a real, quantifiable cost, not just an inconvenience.*

## Glossary

| Term | Definition |
|------|------------|
| **RICE** | Reach × Impact × Confidence ÷ Effort — a value-per-effort prioritization score. |
| **Reach** | How many people/teams a backlog item affects in a given period. |
| **Impact** | How much the item moves the needle per person reached (RICE's 3/2/1/0.5/0.25 scale). |
| **Confidence** | How certain you are the Reach and Impact estimates are accurate — *not* how much a stakeholder wants it. |
| **Effort** | Total work required, usually in person-weeks or -months. |
| **Weighted scoring** | A generalized version of RICE: pick your own criteria, weight them, and sum. |
| **Kano model** | A framework classifying feature value into Must-be, One-dimensional, Attractive, Indifferent, and Reverse. |
| **Must-be / Basic** | A feature whose absence causes dissatisfaction but whose presence isn't noticed as delight — table stakes. |
| **One-dimensional / Performance** | Satisfaction scales roughly linearly with how well the feature is built. |
| **Attractive / Delighter** | A feature that delights when present but causes no complaint when absent. |
| **Indifferent** | Users genuinely don't care whether it's built. |
| **Reverse** | Some users are actively less satisfied when the feature exists. |
| **Better / Worse coefficient** | Kano's quantified satisfaction-upside / dissatisfaction-downside scores, from −1 to 1. |
| **Cost of delay (CoD)** | The quantified cost, per unit of time, of not shipping something now. |
| **WSJF** | Weighted Shortest Job First — Cost of Delay ÷ Job Size; SAFe's urgency-aware prioritization score. |
| **User-Business Value (UBV)** | WSJF's component for direct value to users or revenue. |
| **Time Criticality (TC)** | WSJF's component for whether value decays if you wait. |
| **Risk Reduction / Opportunity Enablement (RR-OE)** | WSJF's component for value from reducing risk or unlocking future work. |
| **Now / Next / Later** | A roadmap format expressing decreasing certainty instead of specific dates. |
| **Capacity constraint** | The stated amount of work (e.g., job-size points) a team can actually do in a period — makes tradeoffs explicit. |
| **Dependency** | A hard requirement that one backlog item must ship before another, regardless of relative score. |

---

*Broken link? Open an issue or PR.*
