# Exercise 2 — Design an Unbiased Survey

**Goal:** Write a survey that measures something real, not something your own wording talked people into. Then back it with a SQL schema so the responses are queryable data, not a pile of text.

**Estimated time:** 60 minutes.

## Setup

You already ran the seed (see the [week README](../README.md)). Confirm you're connected:

```sql
SELECT COUNT(*) FROM survey_responses;   -- must print 20
```

Create a file `survey.md` for the questions and `schema.sql` for the table definition.

## The brief

Shiftly's interviews (this week's `interview_quotes` seed data) surfaced a recurring theme: **manager approval is a bottleneck**, for both shift workers waiting on it and managers stuck being the human router. Your job: design a **follow-up survey** to check how widespread and severe this is, across more people than the 15 interviewed. This is evaluative-leaning — you already know the theme from interviews; the survey's job is to quantify it, not discover something new.

## Part 1 — Write the survey (10 items)

Write exactly 10 survey items. Your survey must include, at minimum:

1. **Two segmentation items** at the top (e.g., role, workplace type) — factual, easy, builds momentum per Lecture 3.
2. **Three behavior/frequency items** about actual past experience with shift swapping (not hypotheticals).
3. **Two difficulty/severity items** using a labeled 5-point scale, with both endpoints explicitly named.
4. **One item specifically about manager approval** — the theme you're checking — written so it doesn't presuppose the bottleneck exists.
5. **One open-text item** at the end for anything you didn't ask about.
6. **One item you deliberately skip-logic to only one segment** (mirror the seed's `would_pay`, which only managers see) — state in `survey.md` which segment sees it and why.

For each item, write a one-line note: what specifically it's measuring, and why it's phrased that way.

## Part 2 — Audit your own draft

Before finalizing, run every item against this checklist. Fix anything that fails:

- [ ] No item contains a loaded adjective ("frustrating," "outdated," "convenient") baked into the question.
- [ ] No item is double-barreled (asks two things joined by "and"/"or").
- [ ] No item uses absolute wording ("always," "never") where a frequency scale would be more honest.
- [ ] No item asks about hypothetical future behavior ("would you use…") where a past-behavior question could be asked instead.
- [ ] Every scale item has both endpoints labeled, and scale direction (1 = best or 1 = worst) is consistent across the whole survey.
- [ ] Segmentation items come first; the open-text item comes last.

## Part 3 — Schema it in SQL

Write a `CREATE TABLE survey_v2_responses` statement in `schema.sql` that could store real responses to your 10 items. Requirements:

- One column per closed-ended item, with a type that matches the data (`TEXT` for categorical, `INTEGER` for a Likert 1–5, `BOOLEAN` for yes/no).
- The skip-logic item's column must allow `NULL`, and a comment explaining that `NULL` means "not asked," not a negative answer — exactly like `would_pay` in the seed schema.
- A `submitted_at DATE NOT NULL` column.
- Then write **one** `SELECT` query against your new (empty) table's shape that a stakeholder would plausibly ask for — e.g., average difficulty by segment. It won't return rows yet (no data), but it must be syntactically valid — run it to confirm.

## Done when…

- [ ] `survey.md` has exactly 10 items meeting the Part 1 requirements, each with a one-line rationale.
- [ ] Every checklist item in Part 2 is checked off, with a note on what you changed if a first draft failed one.
- [ ] `schema.sql` has a valid `CREATE TABLE` statement plus one valid `SELECT` query.
- [ ] You can explain, in one sentence, why the skip-logic column must allow `NULL` rather than defaulting to `FALSE`.

## Stretch

- Add a second `CASE`-based query that buckets your difficulty scale into three labeled bands (as in Lecture 3), against your new table's shape.
- Write the one interview quote (real or invented, in the style of the seed `interview_quotes`) that would make you most confident your survey item about manager approval is measuring the right thing.

## Submission

Commit `survey.md` and `schema.sql` to your portfolio under `c44-week-02/exercise-02/`.
