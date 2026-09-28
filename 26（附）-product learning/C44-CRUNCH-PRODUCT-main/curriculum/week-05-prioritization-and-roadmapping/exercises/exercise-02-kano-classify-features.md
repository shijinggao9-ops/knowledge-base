# Exercise 2 — Kano-Classify a Feature Set

**Goal:** Apply the Kano evaluation matrix to raw, un-simplified survey data for a feature the lecture never walked through — `guest_external_access` — first by hand, then in SQL, and learn why *who you survey* can flip the answer.

**Estimated time:** 90 minutes.

## Setup

The lecture's seed only contains survey data for `recurring_tasks`, `dark_mode`, and `ai_task_summaries`. For this exercise, load one more feature's responses — 20 respondents for `guest_external_access` — into the same table:

```sql
INSERT INTO kano_survey_responses (response_id, item_key, respondent_id, functional_answer, dysfunctional_answer) VALUES
(61,'guest_external_access',1,2,5),(62,'guest_external_access',2,2,5),(63,'guest_external_access',3,2,5),
(64,'guest_external_access',4,2,5),(65,'guest_external_access',5,2,5),(66,'guest_external_access',6,2,5),
(67,'guest_external_access',7,2,5),(68,'guest_external_access',8,2,5),
(69,'guest_external_access',9,2,3),(70,'guest_external_access',10,3,2),(71,'guest_external_access',11,3,4),
(72,'guest_external_access',12,4,3),(73,'guest_external_access',13,2,4),(74,'guest_external_access',14,4,2),
(75,'guest_external_access',15,3,3),(76,'guest_external_access',16,4,4),
(77,'guest_external_access',17,1,3),(78,'guest_external_access',18,1,4),
(79,'guest_external_access',19,1,5),
(80,'guest_external_access',20,5,5);
```

```sql
SELECT COUNT(*) FROM kano_survey_responses WHERE item_key = 'guest_external_access';   -- must print 20
```

Notice this data is **not** cleaned up the way the lecture's demo was — you'll see near-ties between categories, and you have to apply the tie-break rule for real, not just read about it.

## Tasks

### Task 1 — Classify by hand, one respondent at a time

Before writing any SQL, take **respondents 1, 9, 17, and 20** and classify each one by hand using the evaluation matrix from Lecture 1. Write out, for each: their (functional, dysfunctional) pair, and the resulting category letter. Show your work — which row and column of the matrix you landed on.

### Task 2 — Classify all 20 in SQL

Write the `CASE`-based classification query from Lecture 1, adapted to filter on `item_key = 'guest_external_access'`, and tally the category counts with `GROUP BY`.

*(Expected distribution: you should find Must-be and Indifferent very close in count — close enough that the tie-break rule matters. Do not round or fudge a count to avoid the tie; report what the query actually returns.)*

### Task 3 — Apply the tie-break rule, and justify it

Using the course convention from Lecture 1 (**M > O > A > I** on ties), state the final Kano category for `guest_external_access`. Then write 3–4 sentences: does the tie-break rule's outcome match your intuition about this feature, given what you know about it from the week README (three signed enterprise deals depend on it)? Why or why not?

### Task 4 — Compute Better and Worse

Using the formulas from Lecture 1, compute the Better and Worse coefficients for `guest_external_access` from your Task 2 tally. Show the arithmetic, not just the final numbers.

### Task 5 — The segmentation question

Look again at the 20 responses. Respondents 1–8 all gave the exact same pair — a clear must-be signal. Respondents 9–16 are much more mixed/indifferent. Write a short paragraph (150–250 words) answering: **if you knew respondents 1–8 were all enterprise-tier team admins and respondents 9–16 were all individual contributors on free-tier teams, how would that change how you present this Kano result to the roadmap conversation?** Is "run one Kano survey on your whole user base" always the right design, or does it depend on the feature?

## Expected results (spot checks)

- Task 1, respondent 1: (2, 5) → row "2 (must-be)", column "5 (dislike)" → **M**.
- Task 1, respondent 20: (5, 5) → **Q**.
- Task 2 → total categories should sum to 20 across all letters.

## Done when…

- [ ] Task 1 shows hand-worked reasoning for all 4 respondents, not just the final letter.
- [ ] Task 2's SQL runs and its tally sums to 20.
- [ ] Task 3 explicitly applies the tie-break rule (don't skip it even if your tally isn't a true tie — state whether it was needed).
- [ ] Task 4 shows the Better/Worse arithmetic with real numbers from your own tally.
- [ ] Task 5 is a real paragraph with a stated position, not just "it depends."

## Stretch

- Rerun Task 2's tally as **two separate queries** — one filtered to respondents 1–8, one to respondents 9–16 — and compute Better/Worse for each subgroup separately. How different are the two segments' results?
- In one sentence, propose a rule for when a PM should segment a Kano survey by user tier/role before trusting the aggregate result.

## Submission

Commit `exercise-02.md` (your written answers) and `exercise-02.sql` (your queries) to your portfolio under `c44-week-05/exercise-02/`.
