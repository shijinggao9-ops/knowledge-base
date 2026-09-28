# Week 12 — Homework

Five problems, ~5 hours total, spread across the week. Unlike Weeks 1–11's homework, this set isn't reinforcement of a single lecture — it's extra reps on the *whole loop*, applied faster and lighter than the mini-project, plus two SQL-specific extensions of the AI Task Summaries dataset. Commit each.

---

## Problem 1 — A second capstone cycle, compressed (90 min)

Pick a **second** product idea — different from your main capstone, right-sized the same way (Lecture 1, Section 4). In `second-idea/quick-cycle.md`, write a **compressed** version of the full arc, one paragraph per act:

1. Problem statement + one piece of real evidence (not three — one, but a real one).
2. MVP scope in 2–3 user stories, plus one explicit non-goal.
3. Your top 3 backlog items, RICE-scored only (skip WSJF this time), and which one is "Now."
4. What your North Star metric would be, and why, in 2–3 sentences (no dashboard needed — just the reasoning).
5. Your next-quarter bet, in Lecture 3 Section 4's three-part format.

**Why this matters:** a PM who can only run the five-act loop once, slowly, with heavy scaffolding, hasn't fully internalized it. Running it a second time, faster, on a different idea, is the real test of whether the pattern transferred — and it's genuinely useful practice for a live interview, where you may be asked to sketch a product idea from scratch in twenty minutes.

---

## Problem 2 — Extend the AI Task Summaries dataset (75 min)

In `extend-mvp-events.sql`:

1. Write `INSERT` statements adding **6 more users** (users 19–24) to `mvp_users`, exposed on `2025-02-14` like the rest, split evenly between `free` and `pro`.
2. Write plausible `mvp_launch_events` rows for them — invent a believable engagement pattern for each (at least one power user, at least one who never tries the feature), following the existing data's style.
3. Re-run Lecture 2's Section 2.3 (WASU trend) and Section 2.4 (retention by plan) queries against the now-24-user dataset. Report the new numbers in a comment.
4. In 2–3 sentences: did adding 6 more users change the *story* (strong trial, weak retention, pro-skewed) or just the raw counts? Why does that distinction matter when you're deciding whether a finding is robust versus a small-sample artifact?

---

## Problem 3 — A third North Star candidate (45 min)

Lecture 2, Section 1 compared three North Star candidates for AI Task Summaries and picked WASU. In `alternative-north-star.md`, propose a **fourth** candidate this week didn't cover — for example, "average summaries generated per active user per week" (an intensity metric) or "percentage of generated summaries that were never dismissed" (a quality/trust metric). Write the SQL to compute it against the existing `mvp_launch_events` table, report the result, and argue in 3–4 sentences whether it would have changed the recommendation in Lecture 3's worked example if it had been the chosen North Star instead of WASU.

---

## Problem 4 — Defend a bad number that ISN'T diagnosable (60 min)

Lecture 3's worked example reframed a weak retention number as diagnosable and fixable. In `undiagnosable-defense.md`, write a short scenario (3–4 sentences) where the honest answer is the opposite: a metric is bad, and after real investigation, you genuinely cannot find a diagnosable, fixable cause — the evidence points to the underlying value proposition being weak, full stop. Then write the launch narrative's Section 3–5 (did it work, what we learned, the bet) for that scenario. What does an honest "the bet didn't work, and we don't have a good fix" next-quarter bet look like? (Hint: it is not "we'll keep trying the same thing" — Week 5's sequencing and Week 9's kill-switch discipline both apply to knowing when to stop, not just when to continue.)

---

## Problem 5 — Audit a real product's public story (60 min)

Pick a real, existing product you use or know well. Using only publicly available information (its own marketing/changelog, public reviews, its own stated positioning — no insider knowledge required), write a short `real-product-audit.md`:

1. What problem does its marketing claim to solve, and for whom?
2. What's one piece of public evidence (a review, a case study, a stated user count) that the problem is real?
3. What do you think its rough North Star metric is, based on what it optimizes its own product experience around (this is inference, not fact — say so)?
4. Using Lecture 1 Section 3's coherence audit, does the public story hang together, or can you spot a likely orphaned artifact (a feature that seems to serve a different goal than the stated mission, a metric the product seems to chase that doesn't obviously serve the stated user problem)?

**Why this matters:** the coherence-audit skill this week teaches isn't just for grading your own capstone — it's a real, transferable way to evaluate any product's story, including ones you'll be asked to assess or compete against on the job.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 90 min |
| 2 | 75 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 60 min |
| **Total** | **~5.5 h** |

After homework, take the [quiz](./quiz.md) and finish the [mini-project](./mini-project/README.md) if you haven't already.
