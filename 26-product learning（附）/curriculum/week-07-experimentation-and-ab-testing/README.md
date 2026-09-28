# Week 7 — Experimentation & A/B Testing

> **Goal:** by Sunday you can take a feature hypothesis, state it as a testable claim with one primary metric, compute the sample size and duration the test actually needs, and — when the results come in — tell the difference between a real effect and noise well enough to write a ship/no-ship recommendation you'd defend to a skeptical VP.

Welcome back to **C44 · Crunch Product**. Weeks 1–6 took you from "what does a PM own" through discovery, framing, specs, prioritization, and reading product data in SQL. Every one of those skills has been about deciding what to build and how to measure it *after* it ships. This week is about the step most teams skip or fake: **proving** a feature actually did what you predicted, instead of eyeballing a dashboard for a week and declaring victory because the line went up.

A/B testing is not a statistics elective — it's the only tool that separates "we shipped this and metrics went up" from "this feature caused metrics to go up." Those are different claims, and conflating them is how roadmaps fill up with features that felt like wins and weren't. This week gives you the whole loop: write a falsifiable hypothesis, size the test *before* you run it, randomize correctly, watch guardrails, analyze honestly, and recognize the five or six classic ways people fool themselves into declaring a fake win.

We keep working the same running example: **Loopline**, the fictional team task-management app. In Week 4 you wrote the PRD for **Stuck Task Alerts** — a Slack ping the moment a task crosses 48 hours untouched, instead of making the manager remember to check a view. It shipped behind a flag. Before Loopline's leadership rolls it out to every team, they want proof it works: does an alert actually get a stuck task moving faster than no alert would? This week you design that test, size it, and analyze real (seeded) results from a 3-week rollout to 40 teams — and you'll find the results are *not* the clean significant win a case study would show you. That's on purpose. Most real experiments look like this one, and knowing what to do with an ambiguous result is the actual skill.

## Learning objectives

By the end of this week, you will be able to:

- **State** a testable hypothesis with a single primary metric, a clear unit of randomization, and a minimum detectable effect (MDE) — before a single user sees a variant, not after.
- **Compute** the sample size and running duration an experiment needs, using the actual math (not a guess), in both a manual formula and Python (`statsmodels`).
- **Assign** and validate randomization — pick the right unit (user, session, team, geography) so treatment and control don't contaminate each other, and check a sample-ratio mismatch before trusting anything else.
- **Analyze** an experiment for statistical significance in Python and SQL — proportions, confidence intervals, and the difference between a p-value and "this matters for the business."
- **Recognize** peeking, p-hacking, multiple comparisons, and novelty effects — the traps that manufacture a fake win — and know when to reach for a holdout, switchback, or before/after design because randomization isn't available at all.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 4930` — design and interpret a controlled experiment to evaluate a product decision, including hypothesis, sample size, significance and threats to validity. |
| Industry | Size the test before it runs, read the result honestly when it lands, and write the ship or no-ship recommendation you would defend to a skeptical VP. |
| Beyond the bar | You are handed a result log that was peeked at and asked to name the trap rather than the number, which is the failure mode that ships fake wins — `exercises/exercise-03-spot-the-p-hacking.md` |

## Prerequisites

- Week 4 (PRDs & specs) — this week assumes you can read a PRD and its event schema without re-explanation; we extend the Stuck Task Alerts feature directly.
- Week 6 (Product analytics in SQL) — comfort querying an events table (`SELECT`, `WHERE`, `GROUP BY`, joins) is assumed. If funnels and cohort queries still feel new, that week is worth a re-read before Lecture 2.
- Basic algebra and comfort with percentages. No prior statistics course required — the sample-size formula, z-test, and t-test are taught from scratch, with the reasoning, not just the button to press.
- **Python 3.10+** with `pip install numpy scipy statsmodels pandas` — Lecture 2 and Exercise 2 run real calculations in Python. If you only get one library working, get `statsmodels`; it has both the power-analysis and proportion-testing functions this week uses.
- PostgreSQL 16+ **or** SQLite 3.35+, for the SQL-side of Lecture 2 and the mini-project. Install steps are in [`resources.md`](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/resources.md).
- **No spreadsheets as a data store.** Every table below — the experiment seed, the daily logs, the analysis — lives in SQL and/or pandas. Spreadsheets are a presentation surface only, taught separately in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/).

## Set up the seed experiment table

Lecture 2, the mini-project, and Challenge 1 all use one dataset: the real (seeded) results of Loopline's **Stuck Task Alerts** experiment, randomized by **team** (not by user — Lecture 1 explains why), run for 3 weeks across 40 teams. Each row is one team's outcome: how many times a task in that team crossed the 48-hour stuck threshold during the test window, and how many of those incidents got a status update within 24 hours of the alert (the primary metric), plus a guardrail metric (overall task completion rate for that team during the window).

**SQLite (fastest to start):**

```bash
sqlite3 loopline_experiment.db
```

**PostgreSQL:**

```bash
createdb loopline_experiment
psql loopline_experiment
```

Then paste this into the shell (unchanged on both engines):

```sql
CREATE TABLE stuck_alert_experiment (
    team_id               INTEGER PRIMARY KEY,
    arm                   TEXT    NOT NULL CHECK (arm IN ('control','treatment')),
    incidents_logged      INTEGER NOT NULL,   -- times a task crossed the 48h stuck threshold
    incidents_unstuck_24h INTEGER NOT NULL,   -- of those, how many got a status update within 24h
    task_completion_rate  NUMERIC NOT NULL    -- guardrail: overall % of the team's tasks completed in-window
);

INSERT INTO stuck_alert_experiment (team_id, arm, incidents_logged, incidents_unstuck_24h, task_completion_rate) VALUES
(1, 'control', 11, 2, 0.706),
(2, 'control', 5, 2, 0.785),
(3, 'control', 5, 2, 0.701),
(4, 'control', 7, 0, 0.753),
(5, 'control', 7, 1, 0.758),
(6, 'control', 7, 2, 0.631),
(7, 'control', 5, 2, 0.631),
(8, 'control', 9, 5, 0.766),
(9, 'control', 4, 4, 0.740),
(10, 'control', 13, 3, 0.722),
(11, 'control', 4, 0, 0.689),
(12, 'control', 12, 0, 0.669),
(13, 'control', 11, 3, 0.666),
(14, 'control', 5, 2, 0.745),
(15, 'control', 11, 1, 0.716),
(16, 'control', 5, 0, 0.701),
(17, 'control', 6, 2, 0.697),
(18, 'control', 6, 3, 0.692),
(19, 'control', 4, 1, 0.766),
(20, 'control', 10, 1, 0.642),
(21, 'treatment', 5, 1, 0.649),
(22, 'treatment', 5, 0, 0.693),
(23, 'treatment', 7, 3, 0.692),
(24, 'treatment', 5, 0, 0.765),
(25, 'treatment', 7, 2, 0.755),
(26, 'treatment', 10, 5, 0.693),
(27, 'treatment', 7, 4, 0.754),
(28, 'treatment', 10, 7, 0.716),
(29, 'treatment', 13, 5, 0.727),
(30, 'treatment', 8, 4, 0.677),
(31, 'treatment', 5, 0, 0.723),
(32, 'treatment', 4, 2, 0.767),
(33, 'treatment', 8, 0, 0.711),
(34, 'treatment', 11, 2, 0.647),
(35, 'treatment', 5, 2, 0.828),
(36, 'treatment', 13, 5, 0.762),
(37, 'treatment', 13, 3, 0.766),
(38, 'treatment', 12, 4, 0.717),
(39, 'treatment', 11, 7, 0.784),
(40, 'treatment', 9, 4, 0.747);
```

Sanity check — this should print `40`:

```sql
SELECT COUNT(*) FROM stuck_alert_experiment;
```

And this should print `20` and `20`:

```sql
SELECT arm, COUNT(*) FROM stuck_alert_experiment GROUP BY arm;
```

Notice the unit here is **team**, not incident — 20 teams got Stuck Task Alerts turned on, 20 didn't, and each team logged a handful of stuck incidents over three weeks. That team-level randomization is deliberate (Lecture 1 explains why alerts can't be randomized per-user), and it's exactly what makes this dataset harder to analyze correctly than a simple "1,000 users, split 50/50" test — which is the whole point of this week.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Designing an experiment: hypothesis, metrics, unit | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Sample size, power, significance | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Traps: peeking, p-hacking, alternatives to A/B | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Practice: size, analyze, spot the p-hacking | 0h | 1.5h | 1h | 0.5h | 1h | 1h | 5h |
| Friday | Challenges: rescue a test, design without randomizing | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (design + analyze the seed experiment) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-designing-an-experiment.md](01-designing-an-experiment.md) | Hypothesis format, primary vs. guardrail metrics, unit of randomization, MDE | 2h |
| 2 | [lecture-notes/02-sample-size-and-significance.md](02-sample-size-and-significance.md) | Power, the sample-size formula, confidence intervals, reading a result in Python and SQL | 2h |
| 3 | [lecture-notes/03-traps-and-alternatives.md](03-traps-and-alternatives.md) | Peeking, multiple comparisons, novelty effects; holdouts, switchbacks, before/after | 2h |
| 4 | [exercises/exercise-01-size-an-experiment.md](exercise-01-size-an-experiment.md) | Compute sample size and duration for a target effect | 1h |
| 5 | [exercises/exercise-02-analyze-ab-results-in-python.md](exercise-02-analyze-ab-results-in-python.md) | Analyze a 14-day A/B dataset in Python: lift, z-test, confidence interval | 1.5h |
| 6 | [exercises/exercise-03-spot-the-p-hacking.md](exercise-03-spot-the-p-hacking.md) | Diagnose a peeking/optional-stopping trap in a real-looking result log | 1h |
| 7 | [challenges/challenge-01-rescue-an-underpowered-test.md](challenge-01-rescue-an-underpowered-test.md) | The Stuck Task Alerts test came back underpowered — what do you actually do? | 1.5h |
| 8 | [challenges/challenge-02-design-a-test-without-randomization.md](challenge-02-design-a-test-without-randomization.md) | Design a rigorous test for a change you cannot randomize | 1.5h |
| 9 | [mini-project/README.md](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/mini-project/README.md) | Full A/B design + analysis of the seed experiment + ship/no-ship recommendation | 2.5h |
| 10 | [homework.md](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/resources.md) | Official docs, install steps, and the few links worth your time | — |

## By the end of this week you can…

- Write a hypothesis with a primary metric, a unit of randomization, and an MDE that a data scientist would sign off on without redlining it.
- Compute how many users (or teams, or sessions) an experiment needs, and tell your team honestly how many days that will take at current traffic.
- Look at an experiment result and say, correctly, whether it's significant, what the confidence interval means, and whether the effect is big enough to matter to the business — three different questions people conflate constantly.
- Spot peeking, p-hacking, and novelty effects in someone else's "we found a winner" claim, and know what a switchback or holdout test looks like when you can't randomize at all.
- Write a ship/no-ship recommendation for an ambiguous result instead of pretending the data gave you a clean answer it didn't.

## Up next

[Week 8 — UX & design collaboration](../week-08-ux-and-design-collaboration/) — once you can prove a feature works, the next skill is shaping it well with design before it ever reaches an experiment.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
