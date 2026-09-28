# Week 3 — Problem & Opportunity Framing

> **Goal:** by Sunday you can take a vague complaint — "import is broken, people are churning" — and turn it into a falsifiable problem statement, a defensible opportunity size backed by a SQL query against real usage data, and a clear decision about whether to pursue it or kill it. No more "I have a good feeling about this one."

Welcome back to **C44 · Crunch Product**. Week 1 gave you the vocabulary (JTBD, lifecycle, VVF+U). Week 2 gave you the muscle to go find out what's true (interviews, surveys, usability tests). This week is where those two things collide with reality: you have a pile of qualitative signal and a database full of behavioral data, and a stakeholder wants to know two things — *is this actually a problem worth solving*, and *how big is it*. Answering both, in writing, with evidence, is the single highest-leverage skill a PM has. Most roadmap waste traces back to skipping this step.

We continue with **Loopline**, the fictional team task-management app from Weeks 1–2. This week Loopline has a specific, textured problem on its hands: new teams that try to import their existing task backlog from a spreadsheet keep hitting failures — and the teams that fail convert to paid customers at a much lower rate than the teams that succeed. Is that "the" problem, or a symptom of something else? How big is it really, in dollars, not vibes? You'll answer both with a real dataset and real SQL, not a spreadsheet guess.

## Learning objectives

By the end of this week, you will be able to:

- **Write** a crisp, falsifiable problem statement using the who/what/why/impact structure, and translate it into a JTBD (jobs-to-be-done) statement.
- **Distinguish** a problem from a solution in disguise, and a symptom from its root cause, using a structured technique (the Five Whys) rather than a hunch.
- **Size an opportunity two ways** — top-down (market-wide, TAM/SAM/SOM) and bottom-up (built from your own funnel and usage data) — and know when to trust which.
- **Estimate reach and value** — how many users/teams are affected, and what it's worth — by querying real event and account data in SQL, not eyeballing a chart.
- **Build an opportunity-solution tree** that maps a desired outcome to candidate opportunities to candidate solutions, and use it to make — and defend — a kill/greenlight call.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGT 4570` — frame a problem and size the opportunity behind it: separate problem from solution, write a jobs-to-be-done statement, and estimate the opportunity both top-down and bottom-up. |
| Industry | Write the problem brief a leadership team greenlights or kills engineering time on, with every number traced to a query you ran or an assumption you labelled as one. |
| Beyond the bar | The bottom-up size is computed from a real cohort table and reported as a range with its assumptions stated, rather than lifted from a market report — `exercises/exercise-02-bottom-up-sizing-in-sql.md` |

## Prerequisites

- Week 1 (PM foundations, JTBD, VVF+U) and Week 2 (user research & discovery) completed, or the equivalent — this week assumes you can read a JTBD statement and a discovery finding without re-deriving them from scratch.
- PostgreSQL 16+ **or** SQLite 3.35+ installed and working — you used one of these in Week 1's data-backed exercises. Install steps are in [`resources.md`](./resources.md) if you need a refresher.
- No spreadsheet required or wanted. Per [C44's stack note](../../README.md#stack), whenever this course stores, models, or queries data, it uses **SQL and/or Python**, never Excel as a data store — sizing an opportunity is exactly the kind of task people wrongly reach for a spreadsheet to do, and this week shows you the more defensible way.

## Set up this week's seed dataset

One dataset carries the whole week: `signup_cohort`, 30 fictional Loopline teams who signed up for a trial in November 2025, with whether they tried to import an existing backlog, whether it worked, and whether they converted to a paid plan. You'll query it in Lecture 2, Exercise 2, Challenge 2, and the mini-project — set it up once now.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_opportunity.db
```

**PostgreSQL:**

```bash
createdb loopline_opportunity
psql loopline_opportunity
```

Then paste this into the shell (works unchanged on both engines):

```sql
CREATE TABLE signup_cohort (
    team_id                     INTEGER PRIMARY KEY,
    signup_date                 DATE    NOT NULL,
    seats                       INTEGER NOT NULL,
    import_attempted            BOOLEAN NOT NULL,
    import_succeeded            BOOLEAN,             -- NULL if never attempted
    import_row_count            INTEGER,             -- NULL if never attempted
    import_error_type           TEXT,                -- NULL unless it failed
    contacted_support_about_import BOOLEAN NOT NULL,
    converted_to_paid           BOOLEAN NOT NULL,
    mrr                         NUMERIC NOT NULL      -- 0 if not converted
);

INSERT INTO signup_cohort VALUES
(1, '2025-11-01', 2, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(2, '2025-11-02', 3, FALSE, NULL, NULL, NULL, FALSE, TRUE, 20),
(3, '2025-11-03', 2, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(4, '2025-11-04', 4, FALSE, NULL, NULL, NULL, FALSE, TRUE, 25),
(5, '2025-11-05', 3, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(6, '2025-11-06', 2, FALSE, NULL, NULL, NULL, FALSE, TRUE, 20),
(7, '2025-11-07', 5, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(8, '2025-11-08', 3, FALSE, NULL, NULL, NULL, FALSE, TRUE, 30),
(9, '2025-11-09', 2, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(10, '2025-11-10', 4, FALSE, NULL, NULL, NULL, FALSE, TRUE, 25),
(11, '2025-11-11', 3, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(12, '2025-11-12', 2, FALSE, NULL, NULL, NULL, FALSE, TRUE, 20),
(13, '2025-11-13', 6, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(14, '2025-11-14', 3, FALSE, NULL, NULL, NULL, FALSE, TRUE, 35),
(15, '2025-11-15', 2, FALSE, NULL, NULL, NULL, FALSE, FALSE, 0),
(16, '2025-11-16', 4, FALSE, NULL, NULL, NULL, FALSE, TRUE, 25),
(17, '2025-11-17', 5, TRUE, TRUE, 40, NULL, FALSE, TRUE, 60),
(18, '2025-11-18', 6, TRUE, TRUE, 120, NULL, FALSE, TRUE, 75),
(19, '2025-11-19', 4, TRUE, TRUE, 85, NULL, FALSE, TRUE, 50),
(20, '2025-11-20', 8, TRUE, TRUE, 300, NULL, FALSE, FALSE, 0),
(21, '2025-11-21', 5, TRUE, TRUE, 60, NULL, FALSE, TRUE, 90),
(22, '2025-11-22', 7, TRUE, TRUE, 150, NULL, FALSE, TRUE, 65),
(23, '2025-11-23', 6, TRUE, TRUE, 95, NULL, FALSE, FALSE, 0),
(24, '2025-11-24', 9, TRUE, TRUE, 250, NULL, FALSE, TRUE, 80),
(25, '2025-11-25', 3, TRUE, FALSE, 850, 'row_limit_exceeded', TRUE, FALSE, 0),
(26, '2025-11-26', 4, TRUE, FALSE, 210, 'duplicate_emails', TRUE, FALSE, 0),
(27, '2025-11-27', 5, TRUE, FALSE, 60, 'encoding_error', FALSE, TRUE, 45),
(28, '2025-11-28', 6, TRUE, FALSE, 1200, 'row_limit_exceeded', TRUE, FALSE, 0),
(29, '2025-11-29', 4, TRUE, FALSE, 180, 'duplicate_emails', TRUE, FALSE, 0),
(30, '2025-11-30', 5, TRUE, FALSE, 430, 'encoding_error', FALSE, FALSE, 0);
```

Sanity check — this should print `30`:

```sql
SELECT COUNT(*) FROM signup_cohort;
```

Read the story in the data before you touch it analytically: rows 1–16 are teams that never attempted an import (they typed their tasks in by hand). Rows 17–24 attempted an import and it worked. Rows 25–30 attempted an import and it failed, for one of three distinct reasons captured in `import_error_type`. Those three reasons are not the same problem wearing a disguise — Lecture 1 is partly about why that distinction matters.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Problem vs. solution vs. symptom | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Writing problem statements + JTBD | 1.5h | 1.5h | 0h | 0.5h | 1h | 0h | 4.5h |
| Wednesday | Sizing: TAM/SAM/SOM + bottom-up SQL | 2h | 2h | 1h | 0.5h | 1h | 0h | 6.5h |
| Thursday | Opportunity-solution trees | 1.5h | 1.5h | 1h | 0.5h | 1h | 1h | 5.5h |
| Friday | Challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (validated problem brief) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **5h** | **6h** | **3h** | **3.5h** | **5h** | **5h** | **28.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-writing-problem-statements.md](./lecture-notes/01-writing-problem-statements.md) | Problem vs. solution vs. symptom, the Five Whys, the who/what/why/impact structure, JTBD statements | 2h |
| 2 | [lecture-notes/02-sizing-the-opportunity.md](./lecture-notes/02-sizing-the-opportunity.md) | TAM/SAM/SOM, top-down vs. bottom-up sizing, extrapolating a dollar figure from `signup_cohort` in SQL | 2h |
| 3 | [lecture-notes/03-opportunity-solution-trees.md](./lecture-notes/03-opportunity-solution-trees.md) | Outcome → opportunities → solutions; choosing what to pursue and killing the rest, in Mermaid/Markdown | 1.5h |
| 4 | [exercises/exercise-01-problem-vs-solution-sort.md](./exercises/exercise-01-problem-vs-solution-sort.md) | Sort 15 real-sounding statements into problem / solution / symptom | 1h |
| 5 | [exercises/exercise-02-bottom-up-sizing-in-sql.md](./exercises/exercise-02-bottom-up-sizing-in-sql.md) | Query `signup_cohort` to build a bottom-up opportunity size with a stated range | 2h |
| 6 | [exercises/exercise-03-build-an-opportunity-tree.md](./exercises/exercise-03-build-an-opportunity-tree.md) | Build a full opportunity-solution tree for Loopline's activation outcome | 1.5h |
| 7 | [challenges/challenge-01-defend-killing-a-loved-idea.md](./challenges/challenge-01-defend-killing-a-loved-idea.md) | Write the memo that kills a popular, well-liked feature idea | 1.5h |
| 8 | [challenges/challenge-02-reconcile-two-sizing-estimates.md](./challenges/challenge-02-reconcile-two-sizing-estimates.md) | Explain — and resolve — a >100x gap between a top-down and a bottom-up estimate | 1.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | Full validated problem brief: JTBD statement + SQL-backed opportunity size | 2.5h |
| 10 | [homework.md](./homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](./quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official docs, canonical JTBD/OST reading, and install steps | — |

## By the end of this week you can…

- Take a stakeholder's vague complaint and hand back a problem statement specific enough that it can be proven wrong.
- Trace a symptom to its root cause with the Five Whys instead of jumping to the first plausible fix.
- Produce two independent size estimates for an opportunity — one top-down, one bottom-up — from a SQL query, and explain any gap between them.
- Draw an opportunity-solution tree that makes a prioritization decision legible and defensible to someone who disagrees with it.
- Write a one-page kill memo for an idea everyone likes, backed by evidence instead of authority.

## Up next

[Week 4 — PRDs & specs](../week-04-prds-and-specs/) — once you know which opportunity you're pursuing, the next skill is writing the spec precise enough that engineering can build it without guessing.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
