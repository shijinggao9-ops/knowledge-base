# Week 8 — UX & Design Collaboration

> **Goal:** by Sunday you can take any flow in your product, map it step by step, put your finger on exactly where users get stuck, run a usability test that proves it, critique a screen without saying "I don't like it," reason honestly about accessibility trade-offs, and write a redesign spec a designer and an engineer can both act on without a meeting.

Welcome back to **C44 · Crunch Product**. Every week so far has aimed you at *what* to build — users, JTBD, problem framing, specs, prioritization, metrics, experiments. This week aims you at *how it feels to use the thing once it's built*. A feature can be correctly prioritized, perfectly spec'd, and statistically validated by an A/B test (Week 7) and still be a product nobody enjoys using, because the flow to get there was five taps too many, the error message was cryptic, or a screen reader user couldn't complete it at all. That gap — between "the feature is live" and "the feature is usable" — is UX, and a PM who can't operate in that gap is not fully equipped for the job.

We keep working with **Loopline**, the fictional team task-management app from Week 1. This week Loopline has two flows in trouble: its **"Upgrade to Team plan" checkout** (users abandon it constantly) and its **guest invite acceptance flow** (support tickets are piling up). You'll map them, test them, critique screens from them, and write the redesign spec that fixes them — the exact sequence a PM runs before asking a designer to open Figma.

This week is deliberately light on new SQL syntax. What SQL you do write is in service of one rule this course holds hard: **when usability-test results, flow data, or accessibility findings need to be stored, tallied, or queried, they go in a SQL table — never a spreadsheet.** A spreadsheet is fine for a one-off sketch on a whiteboard; the moment you have five sessions × three tasks × pass/fail/time, that's structured data, and structured data belongs in a table you can `SELECT` from, not a grid of merged cells. You'll see exactly why in Lecture 2.

## Learning objectives

By the end of this week, you will be able to:

- **Map** a user flow — screens, steps, decision points, and exit ramps — and read Nielsen's ten usability heuristics well enough to spot friction *before* a real user hits it.
- **Design and run** a task-based usability test with a think-aloud protocol, on as few as five participants, and turn what you observed into a prioritized, severity-ranked list of fixes.
- **Give design critique** that's grounded in the user's goal and the evidence, not personal taste — using a structured framework a designer can actually act on.
- **Reason** about accessibility as a spectrum of trade-offs (cost, risk, reach) rather than a binary pass/fail, and defend a ship-now-vs-fix-first decision with numbers.
- **Write** a flow spec — the redesign document that captures the current flow, the friction found, the proposed new flow, and the metrics that will tell you if it worked.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `CS 3750` — evaluate an interface against usability heuristics, run a task-based usability study with users, critique a design from evidence, and iterate it into a specified redesign. |
| Industry | Take a support queue full of complaints and return three things: evidence, a severity-ranked fix list, and a redesign spec a designer and an engineer can both execute without another meeting. |
| Beyond the bar | Usability results are logged as one row per observation in SQL, so "which task failed most, and how badly" is a query anyone can re-run rather than a memory of the sessions — `exercises/exercise-02-run-a-usability-test.md` |

## Prerequisites

- Weeks 1–5 of this course (PM foundations, user research, problem framing, PRDs, prioritization). If you've also done Week 6 (SQL analytics) and Week 7 (experimentation), you'll recognize the metrics vocabulary here immediately — but this week stands on its own if you haven't.
- **No** design tool required. Every flow and screen this week is given to you as a labeled text/ASCII wireframe — you don't need to know Figma to do this week's work (though if you have it, feel free to sketch along).
- PostgreSQL 16+ **or** SQLite 3.35+, for logging and querying usability-test results in Exercise 2, Challenge 1, and the mini-project. SQLite is the fastest path if you haven't set anything up yet. See [`resources.md`](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/resources.md).
- Five people you can ask to spend 10–15 minutes each clicking through a flow while you watch — coworkers, classmates, friends, family. You do not need "real users"; you need fresh eyes who have never seen the flow.

## Set up the usability-log table

Exercise 2, Challenge 1, and the mini-project all store test results in the same shape of table. Create it once now so it's ready when you need it.

**SQLite:**

```bash
sqlite3 loopline_ux.db
```

**PostgreSQL:**

```bash
createdb loopline_ux
psql loopline_ux
```

Then run this (works unchanged on both engines):

```sql
CREATE TABLE usability_sessions (
    session_id     INTEGER PRIMARY KEY,
    participant    TEXT    NOT NULL,   -- pseudonym, never a real name
    flow_name      TEXT    NOT NULL,   -- e.g. 'team_plan_checkout'
    task_number    INTEGER NOT NULL,
    task_label     TEXT    NOT NULL,
    success        BOOLEAN NOT NULL,   -- did they complete the task unassisted?
    time_seconds   INTEGER,            -- NULL if they never finished
    error_count    INTEGER NOT NULL DEFAULT 0,
    severity_hint  INTEGER,            -- 0-4 heuristic severity of the worst issue hit, if any
    notable_quote  TEXT
);
```

This is the table every query in this week's lectures and exercises assumes exists. Keep it around all week — you'll `INSERT` into it repeatedly, not recreate it.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Flows, friction, Nielsen's heuristics | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Tuesday | Designing a usability test | 2h | 0h | 0h | 0.5h | 1h | 0h | 3.5h |
| Wednesday | Running the test + logging to SQL | 0h | 2h | 0h | 0.5h | 1h | 0h | 3.5h |
| Thursday | Critique frameworks, accessibility basics | 2h | 1h | 1h | 0.5h | 1h | 0.5h | 6h |
| Friday | Trade-off negotiation; challenges | 0h | 0h | 1.5h | 0.5h | 1h | 1h | 4h |
| Saturday | Mini-project (test + redesign spec) | 0h | 0h | 0h | 0h | 0h | 3h | 3h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **4h** | **4.5h** | **2.5h** | **3.5h** | **5h** | **4.5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-flows-friction-and-heuristics.md](01-flows-friction-and-heuristics.md) | Mapping a user flow; Nielsen's 10 heuristics; finding friction before users hit it | 2h |
| 2 | [lecture-notes/02-running-usability-tests.md](02-running-usability-tests.md) | Task-based testing, think-aloud protocol, the 5-user rule, logging results to SQL | 2h |
| 3 | [lecture-notes/03-critique-and-tradeoffs.md](03-critique-and-tradeoffs.md) | Productive critique frameworks, accessibility (WCAG/POUR), negotiating trade-offs | 2h |
| 4 | [exercises/exercise-01-map-a-flow-and-friction.md](exercise-01-map-a-flow-and-friction.md) | Map Loopline's checkout flow and score its friction against the heuristics | 1.5h |
| 5 | [exercises/exercise-02-run-a-usability-test.md](exercise-02-run-a-usability-test.md) | Write tasks, run 5 think-aloud sessions, log results in SQL, summarize | 2h |
| 6 | [exercises/exercise-03-critique-a-screen.md](exercise-03-critique-a-screen.md) | Critique a Loopline screen against the heuristics + an accessibility pass | 1h |
| 7 | [challenges/challenge-01-redesign-a-broken-flow.md](challenge-01-redesign-a-broken-flow.md) | Redesign Loopline's broken Team-plan checkout end to end | 1.5h |
| 8 | [challenges/challenge-02-balance-accessibility-and-speed.md](challenge-02-balance-accessibility-and-speed.md) | Triage 6 ship-or-fix accessibility scenarios against a deadline | 1h |
| 9 | [mini-project/README.md](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/mini-project/README.md) | Critique, test, and write a redesign spec for Loopline's guest invite flow | 3h |
| 10 | [homework.md](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/resources.md) | Official heuristics, WCAG docs, free testing and accessibility tools | — |

## By the end of this week you can…

- Turn any flow into a numbered step-by-step map with decision points and exit ramps called out.
- Recite and apply Nielsen's 10 heuristics from memory, with a severity rating for each violation you find.
- Plan and run a 5-user think-aloud usability test, log the results in a queryable SQL table, and pull a prioritized fix list out of it.
- Give critique in a structured framework that a designer can act on the same day, instead of vague taste-based feedback.
- Explain WCAG's POUR principles and make (and defend, with numbers) a real ship-now-vs-fix-first accessibility call.
- Write a flow spec that a designer and an engineer can both build from without a meeting.

## Up next

[Week 9 — Go-to-market & launch](../week-09-go-to-market-and-launch/) — once the flow is fixed and tested, the next skill is getting it in front of the world.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
