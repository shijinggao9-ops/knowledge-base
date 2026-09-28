# Week 1 — Product Management Foundations

> **Goal:** by Sunday you can look at any product — one you built, one you use, one you've never touched — and say, precisely, who it's for, what job it's hired to do, what lifecycle stage it's in, and which of its bets are actually defensible. No hand-waving, no "I just think it should have dark mode."

Welcome to **C44 · Crunch Product**. Product management has no bar exam, no single certifying body, and — depending which blog you read this week — about six different job descriptions. That ambiguity is exactly why this course starts here: before you touch a PRD, run an experiment, or write a line of SQL against an events table, you need a sharp, defensible answer to "what does a PM actually do, and how do I know if a product is doing well?" This week builds that answer from first principles, using one running example — **Loopline**, a fictional team task-management app — that we'll return to across all three lectures and every exercise.

You are not expected to have shipped a product before. You are expected, by Friday, to be able to hold your own in a room where someone says "we should just add AI to it" and you can ask the three questions that either kill that idea or turn it into a real bet.

## Learning objectives

By the end of this week, you will be able to:

- **Explain** what a product manager does and does not own across discovery, delivery, and outcomes — and draw a clear line between PM, product owner (PO), project manager, and engineering lead.
- **Map** a product's users, jobs-to-be-done (JTBD), and value proposition — separating *who* the user is from *what job* they hire the product to do.
- **Describe** the product lifecycle from discovery through growth, maturity, and sunset, and name the metric that matters most at each stage.
- **Apply** the value / viability / feasibility / usability (VVF+U) lens to score whether an idea is actually worth building.
- **Read** a product's dashboard of success metrics and infer, with evidence, what stage it's in and what strategic bet its team is making.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 4930` — explain what a product manager owns across discovery, delivery and outcomes, read a product's lifecycle stage, and judge an idea against value, viability, feasibility and usability. |
| Industry | Walk up to a product you have never worked on and produce the teardown a hiring panel asks for — who it serves, the job it is hired to do, the stage it is in, and which bets its team is making — with every claim traced back to evidence you gathered. |
| Beyond the bar | Week 1 already puts you in a database: Loopline's twelve-week metrics table is queried to infer the strategy behind the numbers, before any framework has been named — `exercises/exercise-03-infer-strategy-from-metrics.md` |

## Prerequisites

- You can write plain, structured English — this week is argument and judgment, not code.
- **No** prior product, design, or business background assumed.
- We use small SQL datasets to practice reading metrics honestly (never a spreadsheet as the system of record — see [C44's stack note](26-product%20learning（附）/README.md#stack)). You do **not** need to know SQL yet; every query this week is given to you, ready to run. [C33 · Crunch SQL](../../../C33-CRUNCH-SQL/) is optional background, not required.
- PostgreSQL 16+ **or** SQLite 3.35+ installed, so you can run the two small datasets used in Exercises 2 and 3. Install steps are in [`resources.md`](26-product%20learning（附）/curriculum/week-01-product-management-foundations/resources.md). If you only install one, install SQLite — it's zero-setup and everything this week runs on either engine unchanged.

## Set up the two seed datasets

Two tiny datasets carry this week's data-backed exercises. Create them once; you'll reuse them in Exercise 2 (a feature backlog) and Exercise 3 (Loopline's product metrics).

**SQLite (fastest to start):**

```bash
sqlite3 loopline.db
```

**PostgreSQL:**

```bash
createdb loopline
psql loopline
```

The `CREATE TABLE` / `INSERT` statements for each dataset live inside the exercise that uses them ([Exercise 2](exercise-02-classify-features-by-vvf-lens.md), [Exercise 3](exercise-03-infer-strategy-from-metrics.md)) so you set each one up right before you need it — no 200-line block to paste blind on day one.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | The PM role, what you own vs. influence | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Users, personas, JTBD | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Value proposition; VVF+U lens | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Lifecycle stages and strategy | 0h | 1.5h | 1h | 0.5h | 1h | 1h | 5h |
| Friday | Reading metrics; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (product teardown) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-what-a-pm-actually-does.md](01-what-a-pm-actually-does.md) | The PM role across discovery/delivery/outcomes; PM vs PO vs project manager vs eng lead; own vs. influence | 2h |
| 2 | [lecture-notes/02-users-value-and-jobs-to-be-done.md](02-users-value-and-jobs-to-be-done.md) | Segments, personas, JTBD, the value proposition canvas | 2h |
| 3 | [lecture-notes/03-the-product-lifecycle-and-strategy.md](03-the-product-lifecycle-and-strategy.md) | Lifecycle stages, stage-appropriate metrics, the VVF+U lens, reading strategy from data | 2h |
| 4 | [exercises/exercise-01-map-a-products-users-and-value.md](exercise-01-map-a-products-users-and-value.md) | Map users, JTBD, and a value proposition for a real product | 1.5h |
| 5 | [exercises/exercise-02-classify-features-by-vvf-lens.md](exercise-02-classify-features-by-vvf-lens.md) | Score a real feature backlog (SQL dataset) on Value/Viability/Feasibility/Usability | 1.5h |
| 6 | [exercises/exercise-03-infer-strategy-from-metrics.md](exercise-03-infer-strategy-from-metrics.md) | Query Loopline's 12-week metrics table and diagnose its lifecycle stage | 1.5h |
| 7 | [challenges/challenge-01-pm-vs-po-role-debate.md](challenge-01-pm-vs-po-role-debate.md) | Draw the PM / PO / eng-lead responsibility line across 8 ambiguous real scenarios | 1.5h |
| 8 | [challenges/challenge-02-lifecycle-stage-diagnosis.md](challenge-02-lifecycle-stage-diagnosis.md) | Diagnose a real product's lifecycle stage from public evidence | 1.5h |
| 9 | [mini-project/README.md](26-product%20learning（附）/curriculum/week-01-product-management-foundations/mini-project/README.md) | Full teardown of a product you use: role, users, JTBD, value, lifecycle, bets | 2.5h |
| 10 | [homework.md](26-product%20learning（附）/curriculum/week-01-product-management-foundations/homework.md) | Extra practice, spaced across the week | 5h |
| 11 | [quiz.md](26-product%20learning（附）/curriculum/week-01-product-management-foundations/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](26-product%20learning（附）/curriculum/week-01-product-management-foundations/resources.md) | Official docs, canonical PM reading, and install steps | — |

## By the end of this week you can…

- Say precisely what a PM owns, what a PM influences, and what belongs to someone else entirely.
- Write a JTBD statement that survives the question "isn't that just a feature request?"
- Name a product's lifecycle stage and defend it with two independent pieces of evidence.
- Run the VVF+U lens on a real idea and say, in one paragraph, whether it's worth building.
- Read a metrics dashboard and infer the strategic bet behind the numbers — not just describe the numbers.

## Up next

[Week 2 — User research & discovery](../week-02-user-research-and-discovery/) — once you can name the job a user hires your product for, the next skill is finding out if you're right.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
