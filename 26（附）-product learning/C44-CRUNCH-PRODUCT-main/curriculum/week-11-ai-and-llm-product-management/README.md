# Week 11 — AI & LLM Product Management

> **Goal:** by Sunday you can take a vague "we need an AI feature" request, decide honestly whether an LLM is even the right tool for it, scope the feature with a human-in-the-loop design and a deterministic fallback, build a real eval set with a rubric and track its pass rate over time in SQL, and write a guardrail plan for hallucination, safety, and cost — all before a single line of model-calling code gets written.

Welcome back to **C44 · Crunch Product**. Every week so far has assumed the system you're building behaves the same way twice: give it the same input, get the same output, write a deterministic acceptance criterion, done. This week that assumption breaks. An LLM-backed feature can give you a great answer, a mediocre answer, and a confidently wrong answer to the exact same input on three different calls — and your job as the PM doesn't change, but *how* you do that job changes completely. "Looks right in the demo" is not a spec. "The model is smart" is not a guardrail. "We'll figure out cost later" is how a single sprint's shipping decision turns into a five-figure monthly bill nobody signed off on.

We keep working with **Loopline**, the fictional task-management app from Week 1. Sales has been losing renewal conversations to a competitor that ships an "AI-powered" task assistant, and the VP of Product has an ask that lands on your desk in exactly this shape: *"Can we get some AI in the product by next sprint?"* That sentence has no scope, no success metric, and no acceptance criteria — it's a green light with nothing else attached, and shipping straight into it is how teams end up with a feature that sounds impressive in a launch email and falls apart the first time a real user types something the demo never tried. This week you turn that sentence into **Loopline Copilot**: a feature where a user types a one-line goal — *"migrate the billing system to Stripe by end of Q2"* — and the model drafts a checklist of subtasks the user reviews and edits before anything is created. Small, bounded, reviewable. By Saturday you'll have specced it end to end: scope, human-in-the-loop design, an eval set with SQL-tracked quality over time, and a guardrail plan for what happens when the model is wrong, expensive, or attacked.

**Data tooling rule for this week (and this course):** every eval case, every eval result, every dollar of model spend is a **row**, not a cell in a spreadsheet. You'll build three real tables this week — `eval_cases`, `eval_runs` / `eval_results`, and `ai_usage_log` — and query them in **SQL** (PostgreSQL 16 primary, SQLite fallback) and, where noted, **Python + pandas**. The reason is sharper here than in any earlier week: an AI feature's quality and cost both *drift* — a model update, a prompt tweak, or a traffic spike can silently change either one, and the only way to catch that is a queryable history, not a snapshot someone eyeballs once. A spreadsheet of "eval scores" a teammate updates by hand is exactly the kind of system of record that quietly rots. Spreadsheets are a presentation surface, taught on their own in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/); this course's system of record is always SQL.

## Learning objectives

By the end of this week, you will be able to:

- **Decide** whether a feature is genuinely a good fit for an LLM versus a rules engine, classic ML, or "don't build it" — using a concrete checklist instead of vibes, and reasoning explicitly about the cost/latency/quality triangle and a build-vs-buy call.
- **Scope** an AI feature end to end: the bounded task the model performs, the human-in-the-loop review point, and the deterministic fallback for when the model fails, refuses, or is unavailable.
- **Write** an eval set for a probabilistic feature — a golden set of input cases spanning happy path, edge cases, and adversarial attempts, each with a rubric a grader (human or model) can score consistently.
- **Store and query** eval results in SQL to track a feature's quality over time, across prompt versions and model versions, and detect a regression before it reaches production.
- **Design** guardrails for the three ways a shipped AI feature actually breaks: it hallucinates, it costs more than budgeted, and it gets misused — with concrete, testable controls for each, not just "we'll monitor it."
- **Write** a product spec whose acceptance criteria admit that the output is not deterministic, and say precisely what "good enough" means anyway.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | Past the outcome set: neither the product-management nor the human-computer interaction course C44 stands in for carries an outcome on scoping and evaluating a probabilistic feature. This week is additional to both. |
| Industry | Decide whether a model belongs in the feature at all, then make its quality measurable — a golden set, a pass rate tracked across prompt and model versions, a cost cap, and a deterministic fallback for when it fails. |
| Beyond the bar | Eval results live in a queryable table, so a quality regression between two versions is something you detect rather than argue about — `exercises/exercise-02-build-an-eval-set.md` |

## Prerequisites

- Weeks 1–10 — this week assumes you can write a PRD (Week 4), read a metrics query (Week 6), and reason about cost/revenue tradeoffs (Week 10) without re-explanation. It also assumes you remember Loopline's shape: workspaces, tasks, the free/pro split from Week 10.
- Comfortable with `SELECT`, `WHERE`, `GROUP BY`, `JOIN`, and basic aggregates in SQL. If any of that feels shaky, skim [C33 Crunch SQL Weeks 1–3](../../../C33-CRUNCH-SQL/curriculum/) first.
- PostgreSQL 16+ **or** SQLite 3.35+, plus Python 3.10+ with `pandas`, installed. Install steps are in [`resources.md`](./resources.md).
- **No prior AI/ML background required.** This week is deliberately *not* about how to train or fine-tune a model, and it is not a prompt-engineering tutorial. It's about the product judgment that sits around a model call you don't need to build yourself — the same judgment gap that separates teams that ship a durable AI feature from teams that ship a demo.
- **No spreadsheets as a data store.** Every dataset this week is structured, queryable data with real relationships between rows — eval cases to eval results, usage events to cost. It goes in SQL and/or Python, exactly like every week before this one.

## Set up the seed data (do this first)

Three seed tables carry this week: Loopline Copilot's **eval set** (`eval_cases`), its **eval run history** (`eval_runs` / `eval_results`), and its **usage/cost log** (`ai_usage_log`). Create the database once.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_ai.db
```

**PostgreSQL:**

```bash
createdb loopline_ai
psql loopline_ai
```

The `CREATE TABLE` / `INSERT` statements live inside the lecture that first uses each table — `eval_cases`, `eval_runs`, and `eval_results` in [Lecture 2](./lecture-notes/02-evals-for-ai-features.md), `ai_usage_log` in [Lecture 3](./lecture-notes/03-guardrails-cost-and-safety.md) — so you set each one up right before you need it. The mini-project queries this exact Loopline Copilot data. A couple of exercises have you build a **second, smaller instance of the same table shapes** for a different feature, so you get the rep of designing an eval set and reading usage data yourself, not just querying one someone else built — those are called out explicitly where they happen.

**Python setup**, for the pandas cross-checks in Lecture 3, Exercise 3, and the mini-project:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas sqlalchemy psycopg2-binary   # psycopg2-binary only needed if you're on Postgres
```

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | When to use an LLM; cost/latency/quality triangle | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Scope an AI feature and its fallback | 0h | 1.5h | 0h | 0.5h | 1h | 0h | 3h |
| Wednesday | Evals: golden sets, grading, SQL tracking | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Guardrails: hallucination, HITL, cost, safety | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Challenges: LLM vs. rules, cost-cap under a spike | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (spec the feature end to end) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-when-to-use-an-llm.md](./lecture-notes/01-when-to-use-an-llm.md) | Probabilistic vs. deterministic features, a 5-question fit checklist, build-vs-buy, the cost/latency/quality triangle | 2h |
| 2 | [lecture-notes/02-evals-for-ai-features.md](./lecture-notes/02-evals-for-ai-features.md) | Building a golden eval set, grading approaches, offline vs. online evaluation, tracking eval results in SQL over time | 2h |
| 3 | [lecture-notes/03-guardrails-cost-and-safety.md](./lecture-notes/03-guardrails-cost-and-safety.md) | Human-in-the-loop patterns, hallucination guardrails, cost controls with SQL-tracked spend, safety and abuse guardrails | 2h |
| 4 | [exercises/exercise-01-scope-an-ai-feature.md](./exercises/exercise-01-scope-an-ai-feature.md) | Run Loopline Copilot through the fit checklist and scope it with a fallback | 1.5h |
| 5 | [exercises/exercise-02-build-an-eval-set.md](./exercises/exercise-02-build-an-eval-set.md) | Write and grade a golden eval set against seeded model outputs; query pass rate by category | 1.5h |
| 6 | [exercises/exercise-03-design-guardrails.md](./exercises/exercise-03-design-guardrails.md) | Design and SQL-test a cost cap and a safety guardrail against the seeded usage log | 1.5h |
| 7 | [challenges/challenge-01-decide-llm-vs-rules.md](./challenges/challenge-01-decide-llm-vs-rules.md) | Decide LLM vs. rules vs. "don't build it" for five real feature requests | 1.5h |
| 8 | [challenges/challenge-02-cost-cap-an-ai-feature.md](./challenges/challenge-02-cost-cap-an-ai-feature.md) | Design a cost cap that survives a viral traffic spike without breaking the UX | 1.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | Spec Loopline Copilot end to end: scope, HITL design, SQL-tracked eval set, guardrail plan | 2.5h |
| 10 | [homework.md](./homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](./quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official/primary-source reading on LLM evals, safety, and cost | — |

## By the end of this week you can…

- Run any "let's add AI" request through a checklist and give a defensible LLM/rules/no-build verdict, not a hunch.
- Scope an AI feature with a named human-in-the-loop review point and a deterministic fallback for when the model can't be trusted.
- Write a golden eval set with real rubrics, grade outputs against it, and store the results as queryable rows, not a one-time screenshot.
- Query eval history in SQL to catch a quality regression between two prompt or model versions before a user does.
- Design and test — in SQL, against real usage data — a cost cap and a safety guardrail that hold up under a traffic spike or an adversarial input.
- Write acceptance criteria for a feature whose output is genuinely not deterministic, and defend what "good enough" means with evidence.

## Up next

[Week 12 — Capstone: zero to one](../week-12-capstone-zero-to-one/) — every skill from Weeks 1–11, including this week's AI judgment, comes together to take a product from a blank page to a launched v1.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
