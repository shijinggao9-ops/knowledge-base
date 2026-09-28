# Challenge 2 — Reconcile a 10x Gap Between Two Sizings

**Time:** ~90 minutes. **Difficulty:** Hard. **No single right answer.**

## The scenario

You present both sizing estimates for the import-friction opportunity to Loopline's leadership team:

- **Top-down (Lecture 2):** ~$240,000/year — built from a chain of market assumptions (2,000,000 spreadsheet-using teams worldwide → 5% plausibly switch this year → 0.4% reachable by Loopline → $50/mo blended ARPU).
- **Bottom-up (Exercise 2):** ~$18,900–$29,400/year — built from the actual `signup_cohort` conversion gap (75% vs. 16.7%), extrapolated at an assumed 300 signups/month.

The top-down number is roughly **10x** the bottom-up number's midpoint. The CFO, reasonably, asks: *"Which one is right? Because a $240K opportunity and a $24K opportunity are very different roadmap decisions — one funds a team of three for the quarter, the other barely funds a contractor for a month."*

You cannot answer "they're both sort of right" and stop there — that's not an answer, it's a dodge. Your job is to actually investigate the gap and come back with a specific, defensible reconciliation.

## Your task

Write `reconciliation.md` that does all of the following:

### Part 1 — Audit both estimates' assumptions (30 min)

For **each** of the assumptions listed below, rate it **Solid** (backed by real data or a conservative, well-justified guess), **Soft** (a plausible guess doing a lot of work in the calculation), or **Unfounded** (essentially invented, no real basis), and say why in one sentence.

**Top-down assumptions:**
1. 2,000,000 spreadsheet-using teams worldwide
2. 5% of those would plausibly switch to a tool like Loopline within 12 months
3. Loopline could reach/convert 0.4% of that switching population this year
4. $50/month blended ARPU

**Bottom-up assumptions:**
5. 300 signups/month company-wide
6. The `signup_cohort` sample (30 teams, one month, November 2025) is representative of a typical month
7. The 58.3-point conversion gap (75% vs. 16.7%) would fully close if the import bug were fixed — i.e., it's fully causal, not partly explained by team-size confounding (Exercise 2, Task 5)
8. $45–$70 avg MRR range for newly-converted teams is representative of *future* converted teams, not just this month's sample

### Part 2 — Find the assumption doing the most work (20 min)

Pick the single assumption from your Part 1 audit (from either list) that you believe is most responsible for the 10x gap, and prove it: recompute the affected estimate with a more conservative version of that one assumption, holding everything else constant, and show how much the gap closes (or doesn't).

### Part 3 — Write the actual answer to the CFO (30 min)

In 300–450 words, answer the CFO's question directly. Your answer must:

- State a number (or narrow range) you'd actually put in front of leadership as **this quarter's decision-relevant estimate**, and say which method it's closer to and why.
- Explain, in plain language a non-PM would understand, why the two methods disagree by roughly 10x — without hand-waving "market sizing is imprecise."
- Name the **one thing** you'd go do next to narrow the range fastest (e.g., "get the real monthly signup number from growth," "run the seat-bucket confound check on a bigger sample," "re-derive the 0.4% reachability assumption with input from marketing") — a single next action, not a wish list.
- State honestly whether $18,900–$29,400/year (the more conservative, bottom-up-grounded number) is, on its own, large enough to justify the engineering time this quarter — your genuine judgment call, defended in one or two sentences.

## Constraints

- You may not simply average the two numbers ($130,000ish) and present that as the answer — that's mathematically meaningless when the two numbers measure different things, and the CFO will see through it immediately.
- You must engage with **at least 3 of the 8 assumptions** by name in your final answer, not just in the audit table.
- Keep Part 3 to the stated word count — a CFO update that's too long doesn't get read.

## Hints

<details>
<summary>On which assumption usually does the most work</summary>

In sizing chains built from multiple multiplied percentages, the assumption applied *last*, or the one with the widest plausible range, usually swings the final number the most. Check the "reach/capture" style assumption (#3 here) against the others — small percentage assumptions multiplied against large base numbers are usually the least-grounded link in a top-down chain, precisely because nobody has direct evidence for them yet.

</details>

<details>
<summary>On the confound assumption (#7)</summary>

Exercise 2's Task 5 gave you real evidence on this — the succeeded-vs-failed gap did **not** fully disappear when you controlled for seat-size buckets, but the per-bucket sample sizes were small (3–5 rows each). That's genuinely in-between: neither "fully causal, trust the number" nor "fully confounded, ignore the number." A strong answer treats it that way rather than picking whichever conclusion is more convenient for the argument.

</details>

## How success is judged

| Signal | Weak reconciliation | Strong reconciliation |
|--------|----------------------|-------------------------|
| Assumption audit | Vague or skipped | All 8 rated with specific one-sentence justification |
| Root cause of the gap | "Market sizing is imprecise" (true but useless) | Names the specific assumption(s) doing the most work, with a recomputed number proving it |
| CFO answer | Averages the two numbers, or picks one with no justification | States a decision-relevant number, explains the gap in plain language, names one concrete next action |
| Honesty | Overstates confidence either direction | States plainly what's still uncertain and what evidence would resolve it |

## Submission

Commit `reconciliation.md` to your portfolio under `c44-week-03/challenge-02/`.
