# Week 12 — Capstone — Zero to One

> **Goal:** by Sunday you take a product idea — yours, invented this week, from a genuinely blank page — through the entire arc this course taught: discovery, a validated problem, a PRD, a prioritized roadmap, a SQL-instrumented metrics dashboard, an experiment plan, and a launch narrative you could defend live in front of a CFO, a Growth lead, and your own VP of Product. Nothing here is a new framework. Everything here is the eleven frameworks you already have, used together, on one idea, end to end.

Welcome to the last week of **C44 · Crunch Product**. Eleven weeks ago you didn't know what a JTBD was. Since then you've interviewed a fictional persona set for **Loopline**, framed a validated problem, written a PRD, prioritized a backlog with RICE and WSJF, learned to read a raw `events` table for North Star and retention, designed and read an A/B test, collaborated with design on a real screen, wrote a launch plan and an instrumented rollout, and modeled a pricing change and a growth loop in SQL and pandas — never once in a spreadsheet. Every one of those was a real, gradable skill. This week asks a harder question than any single lecture did: **can you run the whole loop yourself, on an idea nobody handed you, without a professor's scaffolding under every step?**

That's what a capstone is for. It is not a twelfth topic. It's the moment the eleven separate skills either cohere into one thing you can do, or turn out to have been eleven disconnected homework assignments. This week, working example is **Loopline's AI Task Summaries feature** — the same backlog item you saw scored on RICE in Week 5, quizzed on in that week's Q15, and referenced as "coming in Week 11" back in Week 10's closing note. We use its actual two-week launch data to show you, concretely, what "assembling the product story" and "measuring a launched MVP" look like end to end — a broad, promising trial with a real retention problem hiding underneath it, exactly the kind of ambiguous, half-good result you will spend your whole PM career learning to read correctly. Then you do the same thing yourself, on a product of your own choosing, for the capstone.

## Learning objectives

By the end of this week, you will be able to:

- **Run** discovery and frame a validated problem from scratch, for a product idea with zero prior research behind it.
- **Write** a PRD and a prioritized (RICE + WSJF, Now/Next/Later) roadmap for that idea's MVP, using only the frameworks from Weeks 4–5.
- **Instrument** a product — real or hypothetical — with an event schema, and analyze it in SQL: North Star, activation, and a simple retention read, with zero spreadsheets anywhere in the pipeline.
- **Design** an experiment for one specific bet in the roadmap, and reason correctly about sample size, guardrails, and what result would actually change the decision.
- **Present** a coherent product story — from blank page to launched, measured v1 — that a skeptical stakeholder panel would sign off on, including the trade-offs you'd defend under real pushback.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 4930` — carry a product from concept through specification, measurement and launch, and present and defend the result to a stakeholder panel. |
| Industry | Assemble a whole product story into one document a hiring manager or an internal panel can read alone, and hold it up while people pull on the weakest parts of it. |
| Beyond the bar | The defence is rehearsed against five planted, adversarial stakeholder questions rather than delivered into a friendly presentation slot — `challenges/challenge-02-capstone-launch-and-defense.md` |

## Prerequisites

- **Weeks 1–11, all of them.** This week does not re-teach discovery, PRDs, RICE/WSJF, SQL funnels/retention, experimentation, UX collaboration, launch planning, pricing/growth, or AI-feature scoping — it assumes you can do each on demand and asks you to chain them. If any single week feels shaky, this is the week that will expose it; go back and re-read that week's lectures before Monday, not after you're stuck on Wednesday.
- PostgreSQL 16+ **or** SQLite 3.35+, plus **Python 3.10+ with pandas**, installed and working — you've used both continuously since Week 6. Install steps are in [`resources.md`](./resources.md) if you need a refresher.
- **No spreadsheets as a data store, still.** The capstone's metrics dashboard — your own instrumented event data — goes in SQL and/or Python (pandas), exactly like every prior week. Spreadsheets remain a presentation surface only, taught on their own in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/); if you're tempted to sketch your funnel numbers in a grid "just to think," open `psql` instead.
- A portfolio you've been committing to since Week 1 (`c44-week-01/` through `c44-week-11/`). This week's work is `c44-week-12/`, and it is the single most citable artifact in that portfolio — build it like someone will actually read it, because in an interview, they will.

## Set up the seed data (do this first)

Lecture 2 and Exercise 3's Part A both run against one small, fully worked dataset: 18 Loopline users exposed to the **AI Task Summaries** feature on its Feb 14 launch day, tracked for 14 days. It is deliberately small enough to eyeball — you can literally count the rows this week, instead of trusting a query blind, which is exactly the muscle you want warmed up before you build your own instrumentation from scratch in Exercise 3's Part B.

**PostgreSQL:**

```bash
createdb loopline_capstone
psql loopline_capstone
```

**SQLite:**

```bash
sqlite3 loopline_capstone.db
```

Then run the schema and seed:

```sql
CREATE TABLE mvp_users (
    user_id     INTEGER PRIMARY KEY,
    plan        TEXT    NOT NULL,   -- 'free' or 'pro'
    exposed_at  DATE    NOT NULL    -- everyone in this cohort was exposed the same day, on purpose
);

INSERT INTO mvp_users (user_id, plan, exposed_at) VALUES
(1,'pro','2025-02-14'), (2,'pro','2025-02-14'), (3,'free','2025-02-14'), (4,'pro','2025-02-14'),
(5,'free','2025-02-14'), (6,'pro','2025-02-14'), (7,'free','2025-02-14'), (8,'pro','2025-02-14'),
(9,'free','2025-02-14'), (10,'pro','2025-02-14'), (11,'free','2025-02-14'), (12,'pro','2025-02-14'),
(13,'free','2025-02-14'), (14,'pro','2025-02-14'), (15,'free','2025-02-14'), (16,'pro','2025-02-14'),
(17,'free','2025-02-14'), (18,'pro','2025-02-14');

-- PostgreSQL: use SERIAL. SQLite: use INTEGER PRIMARY KEY AUTOINCREMENT.
CREATE TABLE mvp_launch_events (
    event_id     SERIAL PRIMARY KEY,     -- SQLite: INTEGER PRIMARY KEY AUTOINCREMENT
    user_id      INTEGER   NOT NULL,
    event_name   TEXT      NOT NULL,     -- 'summary_generated' or 'login'
    event_date   DATE      NOT NULL
);

INSERT INTO mvp_launch_events (user_id, event_name, event_date) VALUES
-- U1 pro, power user: 9 days of use across the full 2 weeks
(1,'summary_generated','2025-02-14'), (1,'summary_generated','2025-02-15'), (1,'summary_generated','2025-02-16'),
(1,'summary_generated','2025-02-18'), (1,'summary_generated','2025-02-20'), (1,'summary_generated','2025-02-22'),
(1,'summary_generated','2025-02-24'), (1,'summary_generated','2025-02-26'), (1,'summary_generated','2025-02-27'),
-- U2 pro, power user
(2,'summary_generated','2025-02-14'), (2,'summary_generated','2025-02-15'), (2,'summary_generated','2025-02-17'),
(2,'summary_generated','2025-02-19'), (2,'summary_generated','2025-02-21'), (2,'summary_generated','2025-02-23'),
(2,'summary_generated','2025-02-25'), (2,'summary_generated','2025-02-27'),
-- U3 free, power user
(3,'summary_generated','2025-02-14'), (3,'summary_generated','2025-02-16'), (3,'summary_generated','2025-02-18'),
(3,'summary_generated','2025-02-20'), (3,'summary_generated','2025-02-23'), (3,'summary_generated','2025-02-26'),
-- U4 pro, regular user
(4,'summary_generated','2025-02-14'), (4,'summary_generated','2025-02-17'), (4,'summary_generated','2025-02-21'),
(4,'summary_generated','2025-02-25'),
-- U5 free, regular user
(5,'summary_generated','2025-02-14'), (5,'summary_generated','2025-02-18'), (5,'summary_generated','2025-02-23'),
-- U6 pro, regular user
(6,'summary_generated','2025-02-14'), (6,'summary_generated','2025-02-19'), (6,'summary_generated','2025-02-24'),
-- U7 free, tried twice, never on day 0
(7,'summary_generated','2025-02-15'), (7,'summary_generated','2025-02-20'),
-- U8 pro, regular user
(8,'summary_generated','2025-02-14'), (8,'summary_generated','2025-02-21'),
-- U9 free, tried once on day 0, never again
(9,'summary_generated','2025-02-14'),
-- U10 pro, tried once, not on day 0
(10,'summary_generated','2025-02-16'),
-- U11 free, tried once on day 0, never again
(11,'summary_generated','2025-02-14'),
-- U12 pro, tried once, not on day 0
(12,'summary_generated','2025-02-19'),
-- U13 free, one-and-done on day 0
(13,'summary_generated','2025-02-14'),
-- U14 pro, one-and-done on day 0
(14,'summary_generated','2025-02-14'),
-- U15 free, one-and-done, day 1
(15,'summary_generated','2025-02-15'),
-- U16 pro, one-and-done, day 3
(16,'summary_generated','2025-02-17'),
-- U17 free, exposed and active in the app, never tried the feature
(17,'login','2025-02-14'), (17,'login','2025-02-16'), (17,'login','2025-02-19'),
-- U18 pro, exposed, logged in twice, then churned from the app entirely
(18,'login','2025-02-14'), (18,'login','2025-02-15');
```

Sanity checks — these should print `18` and `50`:

```sql
SELECT COUNT(*) FROM mvp_users;
SELECT COUNT(*) FROM mvp_launch_events;
```

**The story this data tells, in one sentence you'll re-derive yourself in Lecture 2:** 11 of 18 exposed users tried AI Task Summaries the very first day, 16 of 18 tried it at some point across two weeks — a strong top-of-funnel — but only 7 were still generating summaries in week two, and pro-plan users retained the feature at twice the rate of free-plan users. That gap between "everyone tried it" and "few kept using it" is this week's central lesson, and it's the exact shape of ambiguity your own capstone launch will almost certainly produce.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). This week the hours skew harder toward the mini-project than any prior week — that's intentional; the capstone *is* the deliverable.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Assembling the product story; pick your capstone idea | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Tuesday | Discovery brief + PRD/roadmap for your idea | 0h | 2h | 0h | 0.5h | 1h | 0h | 3.5h |
| Wednesday | Measuring a launched MVP; build your event schema | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Metrics dashboard in SQL; experiment plan | 0h | 1.5h | 1.5h | 0.5h | 1h | 1h | 5.5h |
| Friday | Presenting to stakeholders; launch defense challenge | 2h | 0h | 1.5h | 0.5h | 1h | 1.5h | 6.5h |
| Saturday | Mini-project (assemble the full capstone) | 0h | 0h | 0h | 0h | 0h | 3h | 3h |
| Sunday | Quiz + final review + polish the portfolio | 0h | 0h | 0h | 1h | 0h | 1h | 2h |
| **Total** | | **4h** | **6.5h** | **4h** | **3.5h** | **5h** | **6.5h** | **~32h** |

## How to navigate this week

Work top to bottom. The exercises build your capstone piece by piece — by the time you reach the mini-project, you're assembling files you've already written, not starting fresh.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-assembling-the-product-story.md](./lecture-notes/01-assembling-the-product-story.md) | The five-act product narrative; auditing a story for coherence; Loopline's arc as a worked example; choosing your capstone idea | 1.5h |
| 2 | [lecture-notes/02-measuring-a-launched-mvp.md](./lecture-notes/02-measuring-a-launched-mvp.md) | North Star selection for a brand-new product; event schema design; the AI Task Summaries dataset in SQL — activation, WASU trend, and a pre/post read | 1.5h |
| 3 | [lecture-notes/03-presenting-to-stakeholders.md](./lecture-notes/03-presenting-to-stakeholders.md) | The launch-readout structure; defending trade-offs under pushback; reframing a bad number; the next-quarter bet | 1h |
| 4 | [exercises/exercise-01-capstone-discovery-brief.md](./exercises/exercise-01-capstone-discovery-brief.md) | Write the discovery brief for your own capstone idea: problem, evidence, JTBD, opportunity size, risk | 1.5h |
| 5 | [exercises/exercise-02-capstone-prd-and-roadmap.md](./exercises/exercise-02-capstone-prd-and-roadmap.md) | Write the PRD and a RICE/WSJF-prioritized Now/Next/Later roadmap for your MVP | 2h |
| 6 | [exercises/exercise-03-capstone-metrics-dashboard.md](./exercises/exercise-03-capstone-metrics-dashboard.md) | Warm up on the AI Task Summaries dataset, then design and populate your own event schema and dashboard queries | 3h |
| 7 | [challenges/challenge-01-capstone-experiment-plan.md](./challenges/challenge-01-capstone-experiment-plan.md) | Design a real experiment for one bet in your roadmap, with sample size and a pre-registered decision rule | 1.5h |
| 8 | [challenges/challenge-02-capstone-launch-and-defense.md](./challenges/challenge-02-capstone-launch-and-defense.md) | Write your launch narrative and defend it against five planted, adversarial stakeholder questions | 2.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | **CAPSTONE** — assemble Exercises 1–3 and Challenges 1–2 into one end-to-end product story, plus a launch decision | 6.5h |
| 10 | [homework.md](./homework.md) | Extra practice: a second, faster capstone cycle on a different idea, plus dashboard extensions | 5h |
| 11 | [quiz.md](./quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official docs, canonical PM reading, and a full course glossary | — |

## By the end of this week you can…

- Take a product idea from a blank page to a validated problem, using real discovery technique, not a guess dressed up as research.
- Write a PRD and a defensible, capacity-constrained roadmap for that idea's MVP.
- Instrument any product with an event schema and read its own dashboard in SQL — North Star, activation, and a retention signal — without a spreadsheet anywhere in the pipeline.
- Design an experiment for a specific bet, with a sample size that isn't a guess and a decision rule written down *before* you see the data.
- Present an idea's full journey — discover, spec, prioritize, measure, launch — as one coherent story, and defend its hardest trade-off live.

## Up next

Nothing in this course — **C44 · Crunch Product** ends here. The judgment you built over twelve weeks — discovery, specs, prioritization, SQL-instrumented metrics, experimentation, launch, pricing and growth, and now a full zero-to-one cycle you ran yourself — carries directly into [C25 Crunch Founders](../../../C25-CRUNCH-FOUNDERS/) if you're building your own company, [C42 Crunch Lead](../../../C42-CRUNCH-LEAD/) if you're moving into managing other PMs or a cross-functional team, and [C43 Crunch Strategy](../../../C43-CRUNCH-STRATEGY/) if you want the company-level layer above product. Ship the capstone, add it to your portfolio, and put it at the top — it is the single most convincing artifact in this course.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
