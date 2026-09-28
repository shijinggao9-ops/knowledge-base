# Week 5 — Prioritization & Roadmapping

> **Goal:** by Sunday you can take a messy, politically-loaded backlog of 14 real feature requests, score it with RICE and Kano, re-sequence it with cost of delay, and defend a one-quarter now/next/later roadmap to a room that includes a Sales VP who wants their deal-blocking feature shipped yesterday.

Welcome back to **C44 · Crunch Product**. Weeks 1–4 built the judgment and the artifacts: who the user is, what job they hire your product for, how to size a problem, and how to write a PRD precise enough to build from. This week answers the question every one of those PRDs eventually collides with: **you have more validated, well-specified ideas than engineering time to build them — so what ships first, and why?** Prioritization is where product management stops being a writing exercise and starts being a resource-allocation one, with real stakeholders who each think *their* item is obviously next.

We keep working the same running example from Weeks 1–4: **Loopline**, the fictional team task-management app. Stuck Task Alerts (Week 4's PRD) shipped. Now it's quarterly planning, and your backlog has 14 credible, stakeholder-requested items — a Sales VP with three enterprise deals stuck on "guest access," a Support lead begging for a digest mode because managers are muting your new alerts, a community forum with 1,800 upvotes on dark mode, and an exec who wants AI-generated task summaries before the next board meeting. Every one of them sounds urgent in the room. Your job this week is to build a defensible, data-backed answer for what ships this quarter, next quarter, and later — and to know the difference between a feature that's *popular* and one that's *valuable*.

## Learning objectives

By the end of this week, you will be able to:

- **Score** a backlog with **RICE** (Reach × Impact × Confidence ÷ Effort) and a custom **weighted scoring model**, computed in SQL — not a spreadsheet — and explain what each input actually measures.
- **Classify** features with the **Kano model** (Basic/Must-be, Performance/One-dimensional, Attractive/Delighter, Indifferent, Reverse) from survey data, and read a Better/Worse satisfaction coefficient.
- **Apply cost of delay** and **WSJF** (Weighted Shortest Job First) to re-rank a backlog by urgency and business value, not just size — and explain why RICE and WSJF can disagree, sometimes sharply, about the same item.
- **Sequence** work under real dependencies, where the highest-scoring item can't ship before a lower-scoring prerequisite.
- **Build** a **now/next/later roadmap** tied to outcomes and a stated capacity constraint, and **communicate uncertainty** honestly instead of promising dates you can't keep.
- **Defend** a prioritization decision to conflicting stakeholders — and separately, **detect** when a RICE score has been gamed to make a pet feature look more urgent than it is.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGT 4570` — prioritize a feature portfolio under resource constraints and construct a roadmap tied to outcomes, dependencies and a stated capacity. |
| Industry | Hold the roadmap review: rank a contested backlog, sequence it against real dependencies and a fixed amount of engineering time, and defend three calls to stakeholders who each arrived with their own numbers. |
| Beyond the bar | You audit somebody else's scoring and prove it was inflated — the half of prioritisation no framework teaches, because the framework is what gets gamed — `challenges/challenge-02-expose-a-gamed-rice-score.md` |

## Prerequisites

- Weeks 1–4 — this week assumes you can read a JTBD statement, a validated problem brief, and a PRD without re-explanation. We reuse the Loopline PRD from Week 4 as backlog item context.
- PostgreSQL 16+ **or** SQLite 3.35+, plus **Python 3.10+ with pandas**, installed. If you only install one database engine, SQLite is zero-setup and everything here runs unchanged on either. Install steps are in [`resources.md`](./resources.md).
- **No spreadsheets as a data store.** A backlog with RICE/WSJF scores, survey tallies, and a roadmap is exactly the kind of structured, queryable data this course models in **SQL and/or Python (pandas)** — never Excel/Sheets as the system of record. The classic "prioritization spreadsheet" you've probably seen at a real company is, underneath, a table with rows and columns and a formula column; we build the same thing properly, in a database, where it can be queried, joined, and audited. Spreadsheets are a presentation surface only, and are taught separately in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/).

## Set up the seed backlog (do this first)

Every lecture, exercise, challenge, and the mini-project this week works against the same two seed tables: Loopline's Q3 backlog, and a Kano survey. Create them once.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_backlog.db
```

**PostgreSQL:**

```bash
createdb loopline_backlog
psql loopline_backlog
```

Then paste this into the shell (unchanged on both engines):

```sql
CREATE TABLE backlog_items (
    item_id                  INTEGER PRIMARY KEY,
    item_key                 TEXT    NOT NULL UNIQUE,
    title                    TEXT    NOT NULL,
    requested_by             TEXT    NOT NULL,   -- who's asking: stakeholder or source
    reach                    NUMERIC NOT NULL,   -- teams/quarter this touches
    impact                   NUMERIC NOT NULL,   -- RICE scale: 3=massive .. 0.25=minimal
    confidence               NUMERIC NOT NULL,   -- 1.0 / 0.8 / 0.5 / 0.2
    effort_weeks             NUMERIC NOT NULL,   -- person-weeks (RICE denominator)
    user_business_value      NUMERIC NOT NULL,   -- WSJF component, 1-10 relative scale
    time_criticality         NUMERIC NOT NULL,   -- WSJF component, 1-10 relative scale
    risk_reduction_opp_enable NUMERIC NOT NULL,  -- WSJF component ("RR-OE"), 1-10 relative scale
    job_size_points          NUMERIC NOT NULL    -- WSJF denominator, story points (Fibonacci-ish)
);

INSERT INTO backlog_items
(item_id, item_key, title, requested_by, reach, impact, confidence, effort_weeks,
 user_business_value, time_criticality, risk_reduction_opp_enable, job_size_points) VALUES
(1,  'stuck_alert_digest_mode',     'Digest Mode for Stuck Alerts',            'Support (alert fatigue tickets)',        140,  1,    0.8, 3,  5, 3, 2, 3),
(2,  'configurable_stuck_threshold','Configurable Stuck Threshold per Team',   'Sales (2 renewal escalations)',           40,  2,    0.8, 5,  8, 8, 3, 5),
(3,  'mobile_push_notifications',   'Mobile Push Notifications',               'Design Research (Week 2 interviews)',    600,  2,    0.5, 8,  6, 3, 5, 8),
(4,  'bulk_task_reassignment',      'Bulk Task Reassignment',                  'Support (offboarding workflow)',          90,  1,    0.8, 2,  4, 2, 1, 2),
(5,  'dark_mode',                   'Dark Mode',                               'Community forum (1,800 upvotes)',       1800,  0.25, 1.0, 3,  2, 1, 1, 3),
(6,  'recurring_tasks',             'Recurring Tasks',                         'User research (top verbatim request)',   950,  2,    0.8, 8,  8, 5, 3, 8),
(7,  'time_tracking_integration',   'Time Tracking Integration',               'Sales (competitive parity)',              60,  1,    0.5, 8,  5, 3, 2, 8),
(8,  'custom_fields',               'Custom Fields on Tasks',                  'Sales (enterprise prospects)',            25,  2,    0.5, 8,  6, 5, 3, 8),
(9,  'public_api_webhooks',         'Public API & Webhooks',                   'Eng partnerships team',                   15,  3,    0.8, 13, 5, 3, 8, 13),
(10, 'guest_external_access',       'Guest & External Collaborator Access',    'Sales (3 signed deals blocked)',           20,  3,    1.0, 5,  9, 9, 2, 5),
(11, 'task_templates',              'Task Templates',                         'Customer Success (onboarding time)',      500,  1,    0.8, 3,  4, 2, 2, 3),
(12, 'advanced_search_filters',     'Advanced Search & Filters',               'Power users (NPS verbatims)',             300,  1,    0.5, 5,  4, 2, 2, 5),
(13, 'audit_log_compliance',        'Audit Log for Compliance',                'Sales (SOC 2 questionnaire)',              18,  2,    0.8, 5,  7, 6, 5, 5),
(14, 'ai_task_summaries',           'AI-Generated Task Summaries',             'Exec (board-meeting ask)',                950,  1,    0.2, 13, 5, 4, 3, 13);

CREATE TABLE backlog_dependencies (
    item_key             TEXT NOT NULL,   -- this item...
    depends_on_item_key  TEXT NOT NULL,   -- ...cannot ship before this one
    reason                TEXT NOT NULL
);

INSERT INTO backlog_dependencies VALUES
('guest_external_access', 'audit_log_compliance', 'Security review for the 3 blocked deals requires an audit trail of guest actions before external access can be enabled.'),
('ai_task_summaries',     'public_api_webhooks',  'Summary generation needs a stable event/webhook feed to consume task activity; building it against the old internal-only pipeline would be thrown away.');

CREATE TABLE kano_survey_responses (
    response_id          INTEGER PRIMARY KEY,
    item_key             TEXT    NOT NULL,
    respondent_id         INTEGER NOT NULL,
    functional_answer    INTEGER NOT NULL,  -- "If Loopline HAD this, how would you feel?"    1=like it 2=expect it(must-be) 3=neutral 4=can tolerate 5=dislike it
    dysfunctional_answer INTEGER NOT NULL   -- "If Loopline did NOT have this, how would you feel?" same 1-5 scale
);

-- 20 respondents x 3 features = 60 rows. Simplified to clean, unambiguous pairs so the
-- counting is teachable by hand before you automate it in SQL — real survey exports are
-- messier (Exercise 2 addresses that). item_keys match backlog_items.item_key.
INSERT INTO kano_survey_responses (response_id, item_key, respondent_id, functional_answer, dysfunctional_answer) VALUES
-- recurring_tasks: users expect this now (table stakes vs. competitors)
(1,'recurring_tasks',1,2,5),(2,'recurring_tasks',2,2,5),(3,'recurring_tasks',3,2,5),(4,'recurring_tasks',4,2,5),
(5,'recurring_tasks',5,2,5),(6,'recurring_tasks',6,2,5),(7,'recurring_tasks',7,2,5),(8,'recurring_tasks',8,2,5),
(9,'recurring_tasks',9,2,5),(10,'recurring_tasks',10,1,5),(11,'recurring_tasks',11,1,5),(12,'recurring_tasks',12,1,5),
(13,'recurring_tasks',13,1,5),(14,'recurring_tasks',14,1,5),(15,'recurring_tasks',15,2,2),(16,'recurring_tasks',16,2,2),
(17,'recurring_tasks',17,3,3),(18,'recurring_tasks',18,3,3),(19,'recurring_tasks',19,4,4),(20,'recurring_tasks',20,4,4),
-- dark_mode: loud on the forum, mostly indifferent underneath
(21,'dark_mode',1,3,3),(22,'dark_mode',2,3,3),(23,'dark_mode',3,3,3),(24,'dark_mode',4,3,3),(25,'dark_mode',5,3,3),
(26,'dark_mode',6,3,3),(27,'dark_mode',7,4,4),(28,'dark_mode',8,4,4),(29,'dark_mode',9,4,4),(30,'dark_mode',10,4,4),
(31,'dark_mode',11,4,4),(32,'dark_mode',12,4,4),(33,'dark_mode',13,1,2),(34,'dark_mode',14,1,2),(35,'dark_mode',15,1,2),
(36,'dark_mode',16,1,2),(37,'dark_mode',17,1,2),(38,'dark_mode',18,1,2),(39,'dark_mode',19,1,1),(40,'dark_mode',20,1,1),
-- ai_task_summaries: exciting to most, actively distrusted by a vocal minority
(41,'ai_task_summaries',1,1,3),(42,'ai_task_summaries',2,1,3),(43,'ai_task_summaries',3,1,3),(44,'ai_task_summaries',4,1,3),
(45,'ai_task_summaries',5,1,3),(46,'ai_task_summaries',6,1,3),(47,'ai_task_summaries',7,1,3),(48,'ai_task_summaries',8,1,3),
(49,'ai_task_summaries',9,1,3),(50,'ai_task_summaries',10,1,3),(51,'ai_task_summaries',11,3,3),(52,'ai_task_summaries',12,3,3),
(53,'ai_task_summaries',13,3,3),(54,'ai_task_summaries',14,3,3),(55,'ai_task_summaries',15,3,3),(56,'ai_task_summaries',16,3,3),
(57,'ai_task_summaries',17,5,3),(58,'ai_task_summaries',18,5,3),(59,'ai_task_summaries',19,5,3),(60,'ai_task_summaries',20,5,3);
```

Sanity checks — these should print `14`, `2`, and `60`:

```sql
SELECT COUNT(*) FROM backlog_items;
SELECT COUNT(*) FROM backlog_dependencies;
SELECT COUNT(*) FROM kano_survey_responses;
```

Notice what's already baked into this backlog on purpose: the forum's most-upvoted request (`dark_mode`, 1,800 votes) has the *weakest* RICE impact score and, once you run Kano in Lecture 1, turns out to be mostly **Indifferent**. The item tied to three signed enterprise deals (`guest_external_access`) has one of the *smallest* reach numbers in the table. That gap — between what's loud and what's valuable — is the entire subject of this week.

**Python setup**, for Lecture 3 and Exercise 3 (roadmap assembly and one-pagers):

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas sqlalchemy psycopg2-binary   # psycopg2-binary only needed if you're on Postgres
```

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | RICE, weighted scoring, and Kano | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Kano tallying in SQL; scoring practice | 0h | 1.5h | 0h | 0.5h | 1h | 0h | 3h |
| Wednesday | Cost of delay, WSJF, and sequencing | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Outcome-based roadmaps; now/next/later | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Challenges: stakeholder conflict, gamed RICE | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (prioritize + build the roadmap) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-prioritization-frameworks.md](./lecture-notes/01-prioritization-frameworks.md) | RICE and weighted scoring in SQL; the full Kano model, the evaluation matrix, and Better/Worse coefficients | 2h |
| 2 | [lecture-notes/02-cost-of-delay-and-sequencing.md](./lecture-notes/02-cost-of-delay-and-sequencing.md) | Cost of delay, WSJF, why RICE and WSJF disagree, dependency-respecting sequencing | 2h |
| 3 | [lecture-notes/03-outcome-based-roadmaps.md](./lecture-notes/03-outcome-based-roadmaps.md) | Now/next/later roadmaps in pandas, tying items to outcomes and metrics, communicating uncertainty | 2h |
| 4 | [exercises/exercise-01-score-a-backlog-with-rice.md](./exercises/exercise-01-score-a-backlog-with-rice.md) | Compute and rank RICE scores in SQL; build a weighted scoring alternative | 1.5h |
| 5 | [exercises/exercise-02-kano-classify-features.md](./exercises/exercise-02-kano-classify-features.md) | Classify a fourth feature's raw survey data by hand and in SQL | 1.5h |
| 6 | [exercises/exercise-03-build-a-now-next-later.md](./exercises/exercise-03-build-a-now-next-later.md) | Assemble a capacity-constrained now/next/later roadmap in pandas | 1.5h |
| 7 | [challenges/challenge-01-resolve-stakeholder-conflict.md](./challenges/challenge-01-resolve-stakeholder-conflict.md) | Sales VP vs. Engineering lead, both citing "data" — mediate it in writing | 1.5h |
| 8 | [challenges/challenge-02-expose-a-gamed-rice-score.md](./challenges/challenge-02-expose-a-gamed-rice-score.md) | Audit a RICE score that was quietly inflated, and correct the ranking | 1.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | Prioritize the full 14-item backlog with RICE + Kano, then build and defend a one-quarter roadmap | 2.5h |
| 10 | [homework.md](./homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](./quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official/primary-source reading on RICE, Kano, WSJF, and roadmapping | — |

## By the end of this week you can…

- Compute a RICE score in SQL, explain each of its four inputs, and name at least two concrete ways a stakeholder can game it.
- Run a Kano survey's raw answers through the evaluation matrix and come out with a defensible category and a Better/Worse coefficient — not just a gut feeling.
- Explain, with this week's own data, why a feature can win RICE and lose WSJF (or vice versa) — and know which framework to reach for when.
- Sequence a backlog under real dependencies, not just by score.
- Build a now/next/later roadmap that's tied to stated outcomes, respects a stated capacity constraint, and communicates uncertainty instead of hiding it.
- Sit across from a Sales VP and an Engineering lead who each think they're right, and mediate the conflict with a written, numbers-backed decision.

## Up next

[Week 6 — Product analytics in SQL](../week-06-product-analytics-in-sql/) — once you've decided what to build, the next skill is proving, with data, whether it actually worked.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
