# Mini-Project — Loopline's Q3 Pricing & Growth Plan

> You are the PM presenting to Loopline's leadership team next week. Model a pricing change and a growth loop against this week's seed data in SQL and Python, and deliver one recommendation that covers packaging, rollout, and where the next growth dollar goes — all tied back to Weekly Active Teams, Loopline's North Star.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it deliberately makes you hold two models — a revenue model and a growth model — in your head at the same time and reconcile them into one plan, because that's the actual job. A pricing change that maximizes MRR while quietly killing the guest-invite loop's supply of new inviters is a bad plan even if the MRR number looks great in isolation. A growth investment that ignores what the pricing change is about to do to which segments churns fastest is equally blind. You'll use the exact tables and queries from this week's lectures and exercises — this project is where they come together into one deliverable.

---

## Deliverable

A directory in your portfolio `c44-week-10/mini-project/` containing:

1. `revenue-model.sql` — your queries (baseline, tier migration, risk-adjustment) with their output, building directly on Exercise 3.
2. `growth-model.py` — a pandas script projecting the guest-invite loop's growth over 6 months, building on Lecture 3, Section 5, plus a same-units comparison against at least one other `growth_channels` row (building on Challenge 2).
3. `recommendation.md` — the actual plan (structure below).

## `recommendation.md` structure

### Part 1 — Packaging (Lecture 1 + Exercise 1)

- State your final three-tier structure — either your Exercise 1 design, the canonical Starter/Team/Business tiers from Lecture 3, or a revised hybrid. Whichever you choose, say explicitly why, in one sentence.
- Name the value metric each tier gates on.

### Part 2 — Revenue model (Lecture 3 + Exercise 3)

- Report your baseline MRR, naive projected MRR, and risk-adjusted projected MRR from `revenue-model.sql`.
- State, in one paragraph, which segment carries the most risk in your model and why.

### Part 3 — Rollout plan (Challenge 1)

- In one paragraph, state your rollout mechanism (grandfathering, phasing, caps, or a combination) and the risk-adjusted revenue you'd expect in month 1 versus a full immediate migration.
- This does not need to repeat Challenge 1's full detail if you did that challenge — a tight summary referencing it is fine. If you did not do Challenge 1, this section needs the real reasoning, not a placeholder.

### Part 4 — Growth model (Lecture 2 + Lecture 3 §5)

- Report your `growth-model.py` output: the guest-invite loop's projected active-user growth over 6 months, and your comparison against at least one other channel from `growth_channels`.
- State, in one paragraph, what — if anything — you'd change about how Loopline invests in this loop (more engineering time on the invite flow, more marketing push to surface the invite feature, or leave it alone and focus effort elsewhere).

### Part 5 — One combined recommendation, tied to the North Star

- In one paragraph: does your pricing plan help or hurt the growth loop, and does your growth plan help or hurt revenue? Name at least one specific interaction between the two (for example: does raising the Business tier price risk losing Enterprise accounts who are also, coincidentally, the accounts sending the most guest invites?).
- Close with a single sentence stating your recommendation's expected effect on **Weekly Active Teams** over the next two quarters — not MRR, not signups. If you can't state a WAT effect, you haven't actually connected the two models yet — go back and find the connection.

---

## Milestones

- **Milestone 1 (45 min):** Finalize `revenue-model.sql` — baseline, tier assignment, naive and risk-adjusted projections.
- **Milestone 2 (45 min):** Build `growth-model.py` — the 6-month loop projection plus the channel comparison.
- **Milestone 3 (45 min):** Draft Parts 1–3 of `recommendation.md`.
- **Milestone 4 (45 min):** Draft Parts 4–5, and do one full read-through checking that Part 5 actually connects the two models instead of just summarizing each separately.

---

## Rules

- **Every number in `recommendation.md` must trace back to a query or script output** in `revenue-model.sql` or `growth-model.py` — no numbers invented fresh in the write-up.
- **State your assumptions explicitly** wherever you extend beyond this week's seed data (an assumed customer lifetime for LTV, an assumed rollout speed, etc.) — this mirrors every exercise and challenge this week.
- **Part 5 must name a specific interaction** between the pricing plan and the growth plan — a generic "both are important" sentence does not satisfy this requirement.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Packaging (Part 1) | 10% | Clear tiers with a named value-metric gate per tier |
| Revenue model (Part 2) | 20% | Baseline, naive, and risk-adjusted MRR all reported with real query output; risk driver correctly identified |
| Rollout plan (Part 3) | 15% | A real mechanism with a stated month-1 expectation, not just "grandfather everyone" with no numbers |
| Growth model (Part 4) | 20% | A real 6-month projection from `growth-model.py`, plus a grounded same-units channel comparison |
| Combined recommendation (Part 5) | 25% | Names a specific pricing↔growth interaction; ends on a stated Weekly Active Teams effect |
| Numbers trace to code (Rules) | 10% | Every cited number is reproducible from the committed `.sql`/`.py` files |

---

## Why this matters

This is the shape of a real quarterly planning cycle at almost any B2B SaaS company: Finance wants the revenue number, Growth wants the investment case, and somebody — usually the PM — has to sit at the intersection and make sure the two plans don't quietly undermine each other. The discipline of tracing every claim back to a query you can rerun, instead of a number that sounded right in the room, is the single habit from this week most likely to still matter ten years into a product career.

When done: push, then take the [quiz](26-product%20learning（附）/curriculum/week-10-pricing-and-growth/quiz.md) and start [Week 11 — AI & LLM product management](../../week-11-ai-and-llm-product-management/).
