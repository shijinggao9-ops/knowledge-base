# Week 2 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of written analysis, SQL practice, and a small original exercise. Commit each.

All SQL problems run against the `shiftly_research` seed from the [README](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/README.md) unless a problem says otherwise.

---

## Problem 1 — Diagnose the research plan (45 min)

In `diagnosis.md`, read each mini-scenario and answer: (a) generative or evaluative research, (b) which specific method from Lecture 1's menu you'd use, and (c) one sentence on what would go wrong if the team used the *other* family instead.

1. A team has three competing redesigns of the schedule screen and wants to know which one people complete a task fastest with.
2. A team suspects something about how people plan their week is broken, but has no specific feature idea yet.
3. A team wants to know if a change shipped to 15% of production users actually reduced no-shows.
4. A team wants to understand how warehouse managers currently make scheduling decisions before writing a single line of a spec.
5. A team has a working prototype and wants to find every place people get confused or stuck using it.

---

## Problem 2 — Twenty leading-question rewrites, without the answer key (60 min)

Exercise 1 gave you 10 questions with guidance. This time, write **10 new leading questions of your own** (about any product or service you use) and rewrite each into a Mom-Test-clean version, following the same three-part format (name the failure, rewrite, what it surfaces). Put them in `own-rewrites.md`. Half the exercise is learning to *generate* a leading question so you can recognize the pattern instantly when you didn't write it — most people find their own drafts leak leading questions without noticing until they've done this deliberately once.

---

## Problem 3 — SQL warm-ups on the seed data (75 min)

Write and run each against `shiftly_research`. Put them in `warmups.sql` with a `-- N` comment and the result beneath each.

1. Count of participants by `segment`.
2. Count of participants by `workplace_type`, sorted highest to lowest.
3. All quotes from `manager` participants only (join `interview_quotes` to `participants`).
4. Average `swap_difficulty` for `workplace_type = 'healthcare'` only.
5. The single highest `swap_difficulty` rating and which `workplace_type` it belongs to.
6. Count of survey respondents where `used_group_chat = TRUE`, broken down by `segment`.
7. All distinct `theme` values currently in `interview_quotes` (should be 7, unless you already did Exercise 3).
8. The participant(s) with the most interview quotes recorded (`GROUP BY participant_id`, ordered descending).
9. Every quote where the `theme` is still `NULL` (should be zero unless you're working before Exercise 3).
10. `swap_frequency` values and how many respondents reported each, sorted by count descending.
11. Average `swap_difficulty` split by `swap_frequency` — does more frequent swapping correlate with higher reported difficulty?
12. Every participant who was interviewed in the first three days of the recruiting window (`interviewed_on <= '2026-06-03'`).
13. Count of `survey_responses` rows where `would_pay` is `NULL` versus not `NULL` — confirm it matches "only managers were asked."
14. The `workplace_type` with the highest average `swap_difficulty` across the survey.
15. A `CASE`-based query bucketing `tenure_months` into `'under 1 year'` (< 12) and `'1 year or more'` (>= 12), with a count of participants in each bucket.

---

## Problem 4 — Write a screener from scratch (45 min)

In `screener-practice.md`, write a 5-question screener (following Lecture 2/Challenge 1's pattern) for recruiting participants for a **generative** study on how people choose what to cook for dinner on a weeknight. Include at least one detail-based cross-check question (not a plain yes/no) designed to catch someone who would say anything to qualify for an incentive. Explain in one sentence per question what it's screening for and why a yes/no version of the same question would be weaker.

---

## Problem 5 — Audit a real survey (60 min)

Find a real survey you've been sent recently (a product NPS survey, a course feedback form, a customer satisfaction email — anything with more than 3 questions) or use one from your own memory if you can reconstruct it accurately. In `survey-audit.md`:

1. List at least 5 of its actual questions, as close to verbatim as you can recall or find.
2. Run each one through the Lecture 3 checklist (leading wording, double-barreled, absolute wording, hypothetical framing, scale labeling).
3. For every question that fails at least one check, write the fixed version.
4. One paragraph: what would you guess this organization is trying to learn, and does their survey's *actual* wording serve that goal or work against it?

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 45 min |
| 2 | 60 min |
| 3 | 75 min |
| 4 | 45 min |
| 5 | 60 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/quiz.md) and ship the [mini-project](26-product%20learning（附）/curriculum/week-02-user-research-and-discovery/mini-project/README.md).
