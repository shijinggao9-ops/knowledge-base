# Week 2 — User Research & Discovery

> **Goal:** by Sunday you can pick the right research method for a given question, run a user interview that doesn't lead the witness, design a survey that yields data instead of flattery, and turn a pile of raw notes into a validated-findings brief — with every note, code, and response stored and queried in SQL, not scattered across a spreadsheet.

Welcome back to **C44 · Crunch Product**. Week 1 gave you the PM's job description. This week gives you the PM's most important raw material: **what users actually do, need, and struggle with** — as opposed to what your team *assumes* they do, need, and struggle with. Nearly every failed feature in this industry failed the same way: someone skipped this week.

We work the whole week against one running scenario: **Shiftly**, a scheduling app used by hourly shift workers (restaurant, retail, warehouse, and healthcare staff) and the managers who schedule them. Shiftly's team has a hunch — shift swapping is painful and a "swap marketplace" feature might fix it — but a hunch is not research. You are the PM who has to find out if the hunch is right, and you'll do it the way a real team does: interviews, a survey, and synthesis, with every artifact landing in a real database you can query.

You'll set up one small SQL database below (three tables: recruited participants, coded interview quotes, and survey responses) and use it across the lectures, exercises, and the mini-project. This is deliberate: research that only lives in someone's head, a stack of sticky notes, or an ungoverned spreadsheet is research nobody can re-query in six months. SQL is your lab notebook.

## Learning objectives

By the end of this week, you will be able to:

- **Choose** the right research method for a given question — generative or evaluative — and explain the cost of picking wrong.
- **Recruit and screen** the right participants for a study, including hard-to-reach segments, without introducing sampling bias.
- **Run** a non-leading user interview using Mom Test principles, and take notes that survive synthesis weeks later.
- **Design** a survey that avoids leading, loaded, and double-barreled questions and produces data you can actually analyze.
- **Store and query** interview quotes and survey responses in SQL — never a spreadsheet as your system of record for research data.
- **Synthesize** raw research into a small number of validated needs and insights a team can act on, and separate real signal from surface-level feature requests.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `CS 147` — conduct needfinding with real users: choose the method for the question, run interviews that do not lead the participant, design an unbiased instrument, and synthesize raw data into validated needs. |
| Industry | Recruit and screen five participants, run the sessions, and hand the team a one-page validated-findings brief that says plainly what the research established and what it did not. |
| Beyond the bar | Research data is stored the way a team has to store it — every quote coded into SQL rows and re-queried at synthesis, instead of living on sticky notes nobody can query in six months — `exercises/exercise-03-affinity-map-a-transcript.md` |

## Prerequisites

- Week 1 of this course (the PM role, product lifecycle, value/viability/feasibility).
- Comfort with basic `SELECT`, `WHERE`, `GROUP BY`, and `INSERT` in SQL. If those aren't automatic yet, skim [C33 Crunch SQL Week 1](../../../C33-CRUNCH-SQL/curriculum/week-01-relational-model-and-select/) first — it's not required, but this week assumes you can read and write simple queries. Every query used here is explained inline regardless.
- PostgreSQL 16+ **or** SQLite 3.35+ installed (see [`resources.md`](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/resources.md) if you need either).
- No prior research experience assumed. That's what this week is for.

## Set up the seed database (do this first)

Everything this week runs against one small research database for **Shiftly**. Create it once.

**PostgreSQL:**

```bash
createdb shiftly_research
psql shiftly_research
```

**SQLite:**

```bash
sqlite3 shiftly_research.db
```

Then paste this into the shell (works unchanged on both engines):

```sql
-- Who we recruited and interviewed
CREATE TABLE participants (
    participant_id  INTEGER PRIMARY KEY,
    segment         TEXT    NOT NULL,   -- 'manager' or 'shift_worker'
    workplace_type  TEXT    NOT NULL,   -- 'restaurant', 'retail', 'warehouse', 'healthcare'
    tenure_months   INTEGER NOT NULL,
    recruited_via   TEXT    NOT NULL,   -- 'in_app_banner', 'manager_referral', 'staffing_agency', 'panel'
    interviewed_on  DATE    NOT NULL
);

INSERT INTO participants VALUES
(1,'manager','restaurant',38,'manager_referral','2026-06-01'),
(2,'shift_worker','restaurant',4,'in_app_banner','2026-06-01'),
(3,'shift_worker','restaurant',14,'in_app_banner','2026-06-02'),
(4,'manager','retail',52,'staffing_agency','2026-06-02'),
(5,'shift_worker','retail',2,'in_app_banner','2026-06-02'),
(6,'shift_worker','retail',9,'panel','2026-06-03'),
(7,'shift_worker','warehouse',21,'manager_referral','2026-06-03'),
(8,'manager','warehouse',61,'manager_referral','2026-06-03'),
(9,'shift_worker','warehouse',6,'in_app_banner','2026-06-04'),
(10,'shift_worker','healthcare',3,'panel','2026-06-04'),
(11,'manager','healthcare',44,'staffing_agency','2026-06-04'),
(12,'shift_worker','healthcare',12,'in_app_banner','2026-06-05'),
(13,'shift_worker','restaurant',7,'panel','2026-06-05'),
(14,'shift_worker','retail',18,'manager_referral','2026-06-05'),
(15,'manager','restaurant',29,'manager_referral','2026-06-05');

-- Coded quotes pulled from those interviews (theme assigned during synthesis)
CREATE TABLE interview_quotes (
    quote_id        INTEGER PRIMARY KEY,
    participant_id  INTEGER NOT NULL REFERENCES participants(participant_id),
    quote_text      TEXT    NOT NULL,
    theme           TEXT             -- NULL until an analyst codes it
);

INSERT INTO interview_quotes VALUES
(1,2,'When somebody can''t make their shift, I just post it in our group chat and hope someone bites.','manual_texting'),
(2,2,'Last month a coworker said she''d cover my Saturday, then never showed up, so I got written up instead of her.','no_shows_trust'),
(3,3,'I don''t actually know who else is even scheduled that day unless I ask around.','no_visibility'),
(4,3,'Even after two people agree to swap, I still have to text my manager and wait for her to say yes.','manager_bottleneck'),
(5,5,'Most of my swap requests come in the night before, so there''s no time to plan.','last_minute_stress'),
(6,6,'It feels like the same three people always get their swaps approved fast and the rest of us wait.','fairness_concerns'),
(7,6,'If it''s not in writing somewhere, my manager just says she never agreed to it.','record_keeping'),
(8,7,'We have a whole side text thread that''s basically the real schedule.','manual_texting'),
(9,7,'I once swapped with a guy who then left the company before we squared it away, and I got blamed for the no-show.','no_shows_trust'),
(10,9,'I can''t tell from the app whether someone''s free — I just have to ask everyone one by one.','no_visibility'),
(11,10,'Nobody at my hospital unit swaps without the charge nurse literally signing off in person.','manager_bottleneck'),
(12,12,'Twice I picked up a shift I thought was approved and it turned out my manager never saw the message.','record_keeping'),
(13,13,'The people who are friends with the manager get their swaps waved through, the rest of us wait days.','fairness_concerns'),
(14,14,'By the time my manager approves a swap the shift is already happening.','last_minute_stress'),
(15,1,'I get texts about swaps at 11pm, on my day off, on vacation — there''s no boundary.','manager_bottleneck'),
(16,1,'Half my week is just being the human router for who''s covering what.','manager_bottleneck'),
(17,4,'I don''t have a record of who actually agreed to what, so when there''s a no-show I can''t prove anything.','record_keeping'),
(18,8,'People swap in a group chat I''m not even in, and I find out when nobody shows up.','no_visibility'),
(19,11,'I trust my senior staff to swap directly, but I still have to be the one who checks the license and certification match.','manager_bottleneck'),
(20,15,'If I could see everyone''s availability in one place, I''d stop being the bottleneck for every swap.','no_visibility');

-- Survey responses (a follow-up quantitative check on what interviews suggested)
CREATE TABLE survey_responses (
    response_id      INTEGER PRIMARY KEY,
    segment          TEXT    NOT NULL,   -- 'manager' or 'shift_worker'
    workplace_type   TEXT    NOT NULL,
    swap_frequency   TEXT    NOT NULL,   -- 'never','rarely','monthly','weekly','several_times_a_week'
    swap_difficulty  INTEGER NOT NULL,   -- 1 (very easy) .. 5 (very hard)
    used_group_chat  BOOLEAN NOT NULL,   -- workaround usage
    would_pay        BOOLEAN,            -- only asked of managers; NULL = question skipped, not "no"
    submitted_at     DATE    NOT NULL
);

INSERT INTO survey_responses VALUES
(1,'shift_worker','restaurant','weekly',4,TRUE,NULL,'2026-06-08'),
(2,'shift_worker','restaurant','monthly',3,TRUE,NULL,'2026-06-08'),
(3,'manager','restaurant','rarely',2,FALSE,TRUE,'2026-06-08'),
(4,'shift_worker','retail','several_times_a_week',5,TRUE,NULL,'2026-06-09'),
(5,'shift_worker','retail','weekly',4,TRUE,NULL,'2026-06-09'),
(6,'manager','retail','never',1,FALSE,TRUE,'2026-06-09'),
(7,'shift_worker','warehouse','monthly',3,TRUE,NULL,'2026-06-09'),
(8,'shift_worker','warehouse','weekly',4,TRUE,NULL,'2026-06-10'),
(9,'manager','warehouse','rarely',2,FALSE,FALSE,'2026-06-10'),
(10,'shift_worker','healthcare','rarely',5,FALSE,NULL,'2026-06-10'),
(11,'shift_worker','healthcare','monthly',4,TRUE,NULL,'2026-06-10'),
(12,'manager','healthcare','never',2,FALSE,TRUE,'2026-06-11'),
(13,'shift_worker','restaurant','several_times_a_week',5,TRUE,NULL,'2026-06-11'),
(14,'shift_worker','retail','weekly',3,TRUE,NULL,'2026-06-11'),
(15,'shift_worker','warehouse','rarely',2,FALSE,NULL,'2026-06-11'),
(16,'shift_worker','healthcare','weekly',5,TRUE,NULL,'2026-06-12'),
(17,'manager','restaurant','never',1,FALSE,TRUE,'2026-06-12'),
(18,'shift_worker','retail','monthly',3,TRUE,NULL,'2026-06-12'),
(19,'shift_worker','warehouse','several_times_a_week',5,TRUE,NULL,'2026-06-12'),
(20,'manager','healthcare','rarely',2,FALSE,FALSE,'2026-06-13');
```

Sanity check — this should print `15`, `20`, `20`:

```sql
SELECT COUNT(*) FROM participants;
SELECT COUNT(*) FROM interview_quotes;
SELECT COUNT(*) FROM survey_responses;
```

Notice two things on purpose: `interview_quotes.theme` is filled in here (this is *already-coded* data you'll query in Lecture 3), but Exercise 3 hands you a **fresh, uncoded** transcript you must code yourself. And `survey_responses.would_pay` is `NULL` for every `shift_worker` row — that question was only shown to managers. A `NULL` here means "not applicable," not "no." Keep that distinction; it matters the moment you start aggregating.

## Weekly schedule

Adds up to approximately **28 hours** (full-time pace). Treat it as a target, not a contract.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Setup; generative vs evaluative research | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | The Mom Test, interview scripts | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Notes that survive synthesis; rewrite drills | 0h | 1.5h | 1h | 0.5h | 1h | 0h | 4h |
| Thursday | Survey design + SQL for research data | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Synthesis & affinity mapping; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (5 interviews + brief) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **5.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-generative-vs-evaluative-research.md](01-generative-vs-evaluative-research.md) | Generative vs evaluative, matching method to question, the cost of researching the wrong thing | 2h |
| 2 | [lecture-notes/02-interviews-that-avoid-leading.md](02-interviews-that-avoid-leading.md) | The Mom Test, open questions, behavior over opinion, note-taking that survives synthesis | 2h |
| 3 | [lecture-notes/03-surveys-and-synthesis.md](03-surveys-and-synthesis.md) | Unbiased survey items, storing responses in SQL, affinity-mapping transcripts into themes | 2h |
| 4 | [exercises/exercise-01-rewrite-leading-questions.md](exercise-01-rewrite-leading-questions.md) | Rewrite 10 leading interview questions into Mom-Test-clean ones | 1h |
| 5 | [exercises/exercise-02-design-an-unbiased-survey.md](exercise-02-design-an-unbiased-survey.md) | Design and schema-back a bias-audited survey for Shiftly | 1h |
| 6 | [exercises/exercise-03-affinity-map-a-transcript.md](exercise-03-affinity-map-a-transcript.md) | Code a raw interview transcript into SQL rows and themes | 1.5h |
| 7 | [challenges/challenge-01-recruit-a-hard-to-reach-segment.md](challenge-01-recruit-a-hard-to-reach-segment.md) | Plan recruiting for night-shift warehouse workers | 1h |
| 8 | [challenges/challenge-02-separate-signal-from-noise.md](challenge-02-separate-signal-from-noise.md) | Sort 20 raw feedback items into real needs vs. solutioned requests | 1h |
| 9 | [mini-project/README.md](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/mini-project/README.md) | Run 5 interviews, code them in SQL, ship a validated-findings brief | 2.5h |
| 10 | [homework.md](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/resources.md) | Official docs, the Mom Test, and the few links worth your time | — |

## By the end of this week you can…

- Look at a product question and say, in one sentence, whether it needs generative or evaluative research — and why.
- Run a 30-minute interview that gets you real behavior, not polite opinions.
- Write a survey a statistician wouldn't wince at, and load its responses straight into a queryable table.
- Take a stack of raw quotes and produce three to five validated findings a team can actually act on.

## Up next

[Week 3 — Problem & opportunity framing](../week-03-problem-and-opportunity-framing/) — once you know what users actually struggle with, you turn it into a sized, defensible problem statement.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
