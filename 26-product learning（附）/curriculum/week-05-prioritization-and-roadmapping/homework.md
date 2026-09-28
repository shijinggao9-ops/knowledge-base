# Week 5 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on SQL/Python, a written explanation, and an extend-the-dataset task. Commit each.

All queries run against the `backlog_items`, `backlog_dependencies`, and `kano_survey_responses` seed from the [README](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/README.md) unless a problem says otherwise.

---

## Problem 1 — RICE and WSJF, twenty questions (75 min)

Write and run each as SQL. Put them in `warmups.sql` with a `-- N` comment and the result beneath each.

1. The single highest RICE score, and the item it belongs to.
2. The single highest WSJF score, and the item it belongs to.
3. Every item where `confidence < 0.8` (the estimates you should trust least).
4. Every item requested by someone with `'Sales'` in the `requested_by` text.
5. The average RICE score across the whole backlog.
6. The average WSJF score across the whole backlog.
7. Every item whose `job_size_points` is 8 or more (the largest builds).
8. The item with the single smallest `reach` value.
9. The item with the single largest `reach` value — and its RICE rank (is it #1? why or why not?).
10. Every item where `time_criticality >= 8` (the most urgent, by WSJF's definition).
11. The three items with the lowest `effort_weeks`.
12. Every item whose `risk_reduction_opp_enable` score is higher than its `user_business_value` score (infrastructure-leaning items).
13. Using a window function, the RICE rank and WSJF rank side by side for every item, in one query.
14. From Q13's output, the item with the single largest absolute rank difference between RICE and WSJF.
15. Every item that appears in `backlog_dependencies` as a `depends_on_item_key` (i.e., something else needs it first).
16. The total `job_size_points` across the entire 14-item backlog.
17. What percentage of total `job_size_points` would a 20-point "Now" capacity represent? (One number, one query.)
18. Every item with `impact = 3` (the RICE-scale "massive" tier) — how many are there, and does their WSJF ranking agree they're all urgent?
19. The item with the lowest WSJF score, and one sentence (in a SQL comment) on which cost-of-delay component is dragging it down.
20. A query that returns every item's `title` and a computed `effort_to_reach_ratio` (`effort_weeks / reach`) — which item has the worst ratio, and is that the same item that ranks worst on RICE? Why or why not?

---

## Problem 2 — Explain the disagreement (45 min)

In `disagreement-writeup.md`, answer in prose (no more than 400 words total):

1. Run the RICE and WSJF queries and find the item with the largest rank shift between them (you did this in Problem 1, Q14 — reuse it). Explain in your own words, using the item's actual scores, why the two frameworks disagree about it.
2. Explain the difference between RICE's "Confidence" and WSJF's "Time Criticality" — they sound similar but measure completely different things. Give an example (not from the seed data) of an item that could be high on one and low on the other.
3. In your own words, why does a framework that ignores urgency (RICE) systematically undervalue anything with a deadline or a signed commitment?
4. Name one real-world prioritization decision (from a job, an app you use, or a project) where you now suspect "loudest request" was mistaken for "highest priority." What would a RICE + WSJF pass likely have revealed instead?

---

## Problem 3 — Kano practice on a new feature (60 min)

Pick **one** item from the backlog that has no Kano survey data yet (any of: `stuck_alert_digest_mode`, `configurable_stuck_threshold`, `mobile_push_notifications`, `bulk_task_reassignment`, `time_tracking_integration`, `custom_fields`, `public_api_webhooks`, `task_templates`, `advanced_search_filters`, `audit_log_compliance`).

1. Write your own set of **15 synthetic (functional, dysfunctional) response pairs** for that item — invent them, but make them internally consistent with a plausible story about who'd use this feature and why (a sentence of rationale per cluster of similar responses, not per individual row).
2. Insert them into `kano_survey_responses` (pick unused `response_id`s).
3. Classify them in SQL using Lecture 1's `CASE` query, tally, and compute Better/Worse.
4. Write 2–3 sentences: does the resulting Kano category match what you'd intuitively expect for this feature, given its `requested_by` field and its RICE/WSJF scores? If it doesn't match your intuition, which do you trust more, and why?

**Deliver** `kano-practice.sql` (the inserts and queries) and the 2–3 sentence writeup in the same file as a trailing comment.

---

## Problem 4 — Rebuild the roadmap at a different capacity (45 min)

In `capacity-scenarios.py`:

1. Re-run Exercise 3's sequencer at **three** different Now capacities: 13, 20 (the course default), and 28 job-size points.
2. For each, print the resulting Now bucket's item list and total points used.
3. Answer in a comment block: which single item's inclusion in Now is most sensitive to the capacity number — i.e., it's in Now at 28 points but not at 13? What does that tell you about how "close" that item's priority actually is, versus an item that's in Now at all three capacities?

---

## Problem 5 — Extend the backlog (60 min)

Make the backlog your own and reprioritize it.

1. Write `INSERT` statements to add **3 new backlog items** of your invention — plausible Loopline features with a `requested_by`, and honest (not inflated) RICE and WSJF inputs. Include at least one item with `confidence <= 0.5` (something genuinely unvalidated) and one with `time_criticality >= 8` (something genuinely urgent).
2. Load them (you now have 17 items).
3. Re-run the full RICE and WSJF rankings. Where do your 3 new items land?
4. Add one new row to `backlog_dependencies` connecting one of your new items to an existing one, with a real `reason`.
5. Re-run Exercise 3's sequencer with your 17-item backlog at the default 20-point Now capacity. Did any of your new items make it into Now? Next?

**Deliver** `extend.sql` (the inserts) and `extend-results.md` (the reprioritized rankings and a few sentences on where your new items landed and whether that surprised you).

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 45 min |
| 3 | 60 min |
| 4 | 45 min |
| 5 | 60 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/quiz.md) and ship the [mini-project](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/mini-project/README.md).
