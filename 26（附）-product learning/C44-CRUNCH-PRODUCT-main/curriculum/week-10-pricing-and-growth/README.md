# Week 10 — Pricing & Growth

> **Goal:** by Sunday you can look at a flat, one-size-fits-all price, explain precisely why it's leaving money on the table *and* losing deals at the same time, redesign it into tiers that map to real willingness-to-pay, find the one growth loop worth investing in out of several plausible candidates, and — in SQL and pandas, never a spreadsheet — model what a price change and a growth loop actually do to revenue over the next 12 months.

Welcome back to **C44 · Crunch Product**. For nine weeks you've built the judgment to decide *what* to build (Weeks 1–5), *proven* it with data and experiments (Weeks 6–7), made it *usable* (Week 8), and *launched* it (Week 9). This week asks a different question, one most PM curricula skip past: once the thing is built and shipped, **how does it make money, and how does it grow?** Pricing is not a finance-team afterthought bolted on after the roadmap is decided — it's a product decision as consequential as anything you've spec'd so far, because the price *is* part of the product experience, and the packaging around it *is* part of the roadmap. Growth is the same story: a product doesn't grow because a growth team wants it to, it grows because some mechanism — a loop — keeps feeding itself, and your job is to find that mechanism, not just hope for it.

We keep working with **Loopline**, the fictional team task-management app from Week 1. Loopline has one problem hiding in plain sight: it has charged every customer the exact same **$12 per seat per month** since launch — a two-person startup and a 200-seat enterprise account pay the identical rate for the identical product. That flat price is quietly costing Loopline in both directions: small teams call it expensive for what they get, and enterprise buyers who need the SSO and audit-log features Loopline shipped since Week 5's roadmap (remember `guest_external_access` and `audit_log_compliance`?) are getting those compliance features **for free**, bundled into a price that was set before those features existed. Meanwhile, Loopline's guest-invite feature — the same one from that Week 5 dependency — has quietly become a real growth channel, and nobody has measured whether it's worth investing in versus paid search. This week you fix both.

## Learning objectives

By the end of this week, you will be able to:

- **Compare** subscription, usage-based, freemium, and seat-based pricing models, and choose the right one for a given product and buyer.
- **Design** a tiered packaging structure — Good/Better/Best — that gates features by value metric, uses anchoring deliberately, and is grounded in willingness-to-pay evidence rather than a guess.
- **Distinguish** a growth loop from a funnel, name the four common loop types, and read a loop diagram for its trigger, action, and reward.
- **Compute** a loop's k-factor and cycle time from raw event data, and use both numbers to judge whether a loop is worth investing in.
- **Model**, in SQL and pandas, the revenue impact of a pricing change — including a realistic, risk-adjusted view of migration churn, not just the naive "everyone pays the new price" number.
- **Connect** a pricing decision and a growth-loop decision to a single North Star metric, and defend a packaging-and-growth recommendation that a CFO and a Growth lead would both sign off on.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGT 4570` — analyze pricing models and packaging, evaluate the growth model, and connect both to the business's primary metric. |
| Industry | Bring leadership one plan that survives two readings at once — the revenue model and the growth model — and say what the repricing costs in churn, not only what it earns. |
| Beyond the bar | The tier migration is modelled with risk-adjusted churn in SQL, instead of the naive "everyone pays the new price" number that makes every repricing look good — `exercises/exercise-03-model-a-pricing-change.md` |

## Prerequisites

- Weeks 1–9 — this week assumes you can read a PRD, a metrics dashboard, and an experiment result without re-explanation, and that you remember Loopline's Week 5 backlog (`guest_external_access`, `audit_log_compliance`) and Week 6's analytics muscle.
- PostgreSQL 16+ **or** SQLite 3.35+, plus **Python 3.10+ with pandas**, installed. If you only install one database engine, SQLite is zero-setup and everything here runs unchanged on either. Install steps are in [`resources.md`](./resources.md).
- **No spreadsheets as a data store.** Every dataset this week — Loopline's subscription book, its guest-invite events, its growth-channel comparison — is structured, queryable data with real relationships between rows. It goes in **SQL and/or Python (pandas)**, exactly like every week before this one. A "pricing model" that lives in a spreadsheet is a set of formulas nobody can audit, join, or re-run at scale; the same model as a table with a schema is something you can `SELECT`, version, and hand to a finance analyst who can trust it. Spreadsheets are a presentation surface only, and are taught on their own in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/).

## Set up the seed data (do this first)

Three seed tables carry this week: Loopline's current subscription book, its guest-invite growth-loop events, and a comparison of its growth channels. Create the database once.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_growth.db
```

**PostgreSQL:**

```bash
createdb loopline_growth
psql loopline_growth
```

The `CREATE TABLE` / `INSERT` statements live inside the lecture or exercise that first uses each table — `subscriptions` in [Lecture 3](./lecture-notes/03-modeling-pricing-and-growth.md), `referral_events` and `growth_channels` in [Lecture 2](./lecture-notes/02-growth-loops-and-funnels.md) — so you set each one up right before you need it.

**Python setup**, for the modeling work in Lecture 3, Exercise 3, and the mini-project:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas sqlalchemy psycopg2-binary   # psycopg2-binary only needed if you're on Postgres
```

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Pricing models, packaging, anchoring | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Willingness-to-pay; design your own tiers | 0h | 1.5h | 0h | 0.5h | 1h | 0h | 3h |
| Wednesday | Growth loops vs. funnels; loop math | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Modeling pricing + growth in SQL/pandas | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Challenges: reprice without churning, find the leverage loop | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (model + recommend) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-pricing-models-and-packaging.md](./lecture-notes/01-pricing-models-and-packaging.md) | Subscription, usage, freemium, seat-based pricing; Good/Better/Best packaging; anchoring; willingness-to-pay research; Loopline's flat-price problem | 2h |
| 2 | [lecture-notes/02-growth-loops-and-funnels.md](./lecture-notes/02-growth-loops-and-funnels.md) | Loops vs. funnels; the four loop types; loop math (k-factor, cycle time); instrumenting Loopline's guest-invite loop | 2h |
| 3 | [lecture-notes/03-modeling-pricing-and-growth.md](./lecture-notes/03-modeling-pricing-and-growth.md) | MRR/ARPU/NRR in SQL; modeling a tier migration with risk-adjusted churn; loop compounding in pandas; tying it to the North Star | 2h |
| 4 | [exercises/exercise-01-design-a-pricing-tier.md](./exercises/exercise-01-design-a-pricing-tier.md) | Design your own three-tier pricing table for Loopline | 1.5h |
| 5 | [exercises/exercise-02-map-a-growth-loop.md](./exercises/exercise-02-map-a-growth-loop.md) | Query the guest-invite loop's raw events; compute k-factor and cycle time; diagram the loop | 1.5h |
| 6 | [exercises/exercise-03-model-a-pricing-change.md](./exercises/exercise-03-model-a-pricing-change.md) | Migrate Loopline's subscription book to a new tier structure in SQL, with risk-adjusted revenue | 1.5h |
| 7 | [challenges/challenge-01-reprice-without-churning.md](./challenges/challenge-01-reprice-without-churning.md) | Design a rollout plan that captures the upside of Exercise 3's repricing without the churn | 1.5h |
| 8 | [challenges/challenge-02-find-the-highest-leverage-loop.md](./challenges/challenge-02-find-the-highest-leverage-loop.md) | Compare three real growth channels and defend which one deserves the next dollar of investment | 1.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | Model a pricing change and a growth loop against the seed data, and recommend a packaging + growth plan tied to the North Star | 2.5h |
| 10 | [homework.md](./homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](./quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official/primary-source reading on pricing, loops, and revenue modeling | — |

## By the end of this week you can…

- Name the right pricing model for a given product and defend it against the three alternatives.
- Design tiers that gate on a real value metric, use anchoring on purpose, and can point to willingness-to-pay evidence behind every price point.
- Tell a loop from a funnel on sight, and compute a loop's k-factor and cycle time from raw event data.
- Query a subscription book in SQL to get real MRR, ARPU, and churn — and model a price change with a risk-adjusted, not naive, revenue projection.
- Compare growth channels on equal footing and say which one deserves the next dollar, with numbers, not intuition.
- Tie a pricing and a growth decision back to a single North Star metric and defend the combined plan to a room with a CFO and a Growth lead in it.

## Up next

[Week 11 — AI & LLM product management](../week-11-ai-and-llm-product-management/) — once you can price and grow a product, the next skill is scoping, evaluating, and shipping the AI features that are now table stakes in almost every product category.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
