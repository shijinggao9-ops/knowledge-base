# Exercise 2 — Classify Features by the VVF Lens

**Goal:** Apply the value / viability / feasibility / usability (VVF+U) lens from Lecture 3 to ten real items sitting in Loopline's backlog, using a real SQL table as the system of record — not a spreadsheet, not a sticky-note wall.

**Estimated time:** 60–90 minutes.

## Setup — seed the backlog table

You do **not** need prior SQL experience — every statement below is ready to paste. Open `sqlite3 loopline.db` (or `psql loopline`) and run:

```sql
CREATE TABLE features (
    feature_id             INTEGER PRIMARY KEY,
    feature_name           TEXT    NOT NULL,
    description             TEXT    NOT NULL,
    requested_by            TEXT    NOT NULL,   -- which segment/persona asked for it
    dev_weeks_estimate      NUMERIC NOT NULL,   -- engineering's rough sizing
    projected_arr_impact    NUMERIC,            -- estimated annual recurring revenue impact, USD; NULL = unknown
    technical_risk          TEXT    NOT NULL,   -- 'Low', 'Medium', or 'High'
    customer_votes          INTEGER NOT NULL    -- upvotes on the public feature-request board
);

INSERT INTO features VALUES
(1,'AI stand-up summarizer','Nightly AI-generated summary of task comments for a Monday status view','Mid-size software teams (engineering managers)',5,180000,'Medium',312),
(2,'Native mobile app','Full-featured iOS/Android app beyond the current mobile web view','Agencies (on-the-go client checks)',10,240000,'High',498),
(3,'Slack integration','Two-way sync: task updates post to Slack, replies update the task','Mid-size software teams',3,150000,'Low',276),
(4,'Client-facing shareable view','Read-only, brandable project view agencies can send to their own clients','Agencies',4,210000,'Medium',201),
(5,'Dark mode','System-matching dark color theme across the app','All segments (top-voted request)',2,20000,'Low',540),
(6,'Recurring tasks','Tasks that automatically regenerate on a schedule (daily/weekly/monthly)','Early-stage startup teams',2,60000,'Low',233),
(7,'Time tracking add-on','Per-task timers and a weekly time report, billed as a paid add-on','Agencies',6,300000,'Medium',167),
(8,'SSO / SAML enterprise login','Single sign-on via Okta/Azure AD, required by enterprise security review','Mid-size software teams (IT/security buyers)',4,400000,'Medium',58),
(9,'Public API','REST API so customers can build their own integrations','Mid-size software teams (technical buyers)',7,90000,'High',142),
(10,'Custom task fields','Let teams add their own metadata fields to tasks (priority, custom tags, etc.)','Early-stage startup teams',3,70000,'Low',189);
```

Sanity check — this should print `10`:

```sql
SELECT COUNT(*) FROM features;
```

Add four columns you'll fill in yourself — your VVF+U scores and your call:

```sql
ALTER TABLE features ADD COLUMN value_score      INTEGER;  -- 1-5
ALTER TABLE features ADD COLUMN viability_score  INTEGER;  -- 1-5
ALTER TABLE features ADD COLUMN feasibility_score INTEGER; -- 1-5
ALTER TABLE features ADD COLUMN usability_score  INTEGER;  -- 1-5
ALTER TABLE features ADD COLUMN recommendation   TEXT;     -- 'Build now', 'Validate first', or 'Reject'
```

## Tasks

1. **Read the whole backlog first.** Run `SELECT feature_name, description, requested_by, dev_weeks_estimate, projected_arr_impact, technical_risk, customer_votes FROM features ORDER BY customer_votes DESC;` and skim every row before scoring anything. Note which columns are *evidence you have* (votes, estimates) and which are *judgment calls you're about to make* (the scores).

2. **Score each of the 10 features 1–5 on each of the four VVF+U lenses**, using this rubric:

   | Score | Value | Viability | Feasibility | Usability |
   |---|---|---|---|---|
   | 1 | No evidence anyone wants this | Actively hurts the business (cost, legal, brand) | Effectively unbuildable with current team/time | Users would never find or complete it |
   | 3 | Some signal (moderate votes, one segment) | Roughly cost-neutral, unclear ROI | Buildable but risky or slow | Usable with some onboarding/education |
   | 5 | Strong signal (high votes, maps to a real named job) | Clearly strengthens revenue, cost, or strategic position | Low-risk, fits current skills/timeline | Self-evident, no explanation needed |

   Write each score with the `UPDATE` statement, e.g.:

   ```sql
   UPDATE features
   SET value_score = 4, viability_score = 3, feasibility_score = 4, usability_score = 5
   WHERE feature_id = 1;
   ```

   Do this for all 10 `feature_id`s. **You must be able to defend every score in one sentence** — write that sentence in `rationale.md` as you go (Task 4).

3. **Assign a recommendation** to each row (`'Build now'`, `'Validate first'`, or `'Reject'`) via `UPDATE`, using this decision rule:

   - **Build now:** all four scores are 4 or 5.
   - **Reject:** value score is 1 or 2 (if users don't want it, the other three scores don't matter).
   - **Validate first:** everything else — meaning at least one lens has real, unresolved uncertainty (this is the *most common* honest answer, not a cop-out; re-read the AI-summarizer worked example in Lecture 3 if this feels unsatisfying).

4. **Write `rationale.md`** — for each of the 10 features, one sentence stating your four scores and the single strongest reason behind your weakest score (the score that's actually driving your recommendation).

5. **Query your own scoring.** Run:

   ```sql
   SELECT feature_name, recommendation
   FROM features
   ORDER BY
       CASE recommendation
           WHEN 'Build now' THEN 1
           WHEN 'Validate first' THEN 2
           WHEN 'Reject' THEN 3
       END,
       customer_votes DESC;
   ```

   Save the output into `report.md` under three headers: **Build now**, **Validate first**, **Reject**.

## Expected outcome (self-check)

- At least one feature should land in each of the three recommendation buckets — if everything scored "Build now," you were not being critical enough (real backlogs are never that clean).
- `customer_votes` alone should **not** determine your `value_score`. Feature 5 (Dark mode) has the highest votes in the table but is a weak strategic bet if it doesn't map to a real job from Lecture 2 — score it honestly, not by popularity.
- Feature 8 (SSO) has low votes but the highest `projected_arr_impact` and comes from a segment (IT/security buyers) that doesn't show up elsewhere in the vote count — a common enterprise-software pattern where the loudest requesters and the actual buyers are different people. Notice this in your rationale.

## Done when…

- [ ] All 10 rows have all four scores and a recommendation, verifiable with `SELECT * FROM features;`.
- [ ] `rationale.md` has one defensible sentence per feature, naming the actual driving score.
- [ ] `report.md` groups all 10 features into the three recommendation buckets.
- [ ] You can explain, out loud, why votes and value score are not the same thing.

## Stretch

- Write one more query: which features have `technical_risk = 'High'` **and** `feasibility_score >= 4`? Are you being consistent, or did the risk label and your score quietly disagree?
- Loopline can only staff **12 dev-weeks** this quarter. Write a query that lists, in priority order, which "Build now" features fit inside that budget (`SUM(dev_weeks_estimate)` running total) — and which get bumped to next quarter.

## Submission

Commit `rationale.md` and `report.md` to your portfolio under `c44-week-01/exercise-02/`.
