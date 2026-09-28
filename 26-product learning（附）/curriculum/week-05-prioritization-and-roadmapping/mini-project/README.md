# Mini-Project — Prioritize Loopline's Q3 Backlog and Defend the Roadmap

> Take all 14 items in Loopline's real backlog, score them with RICE and Kano, re-sequence them with cost of delay and dependencies, and produce a capacity-constrained now/next/later roadmap you could actually present — and defend — in a real roadmap review. This is the week's capstone: every lecture, exercise, and challenge fed into this one deliverable.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

A stakeholder doesn't hand you a spreadsheet of pre-computed priorities — they hand you competing requests, a fixed amount of engineering time, and an expectation that you'll be able to explain, calmly and with numbers, why their thing is or isn't Now. That's the actual job. This project is the full pipeline, start to finish, on Loopline's real backlog from the [week README](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/README.md).

---

## Deliverable

A directory in your portfolio `c44-week-05/mini-project/` containing:

1. **`scoring.sql`** — every SQL query that computes RICE, WSJF, and Kano classifications for the full backlog.
2. **`roadmap.py`** — the pandas script that assembles the final now/next/later roadmap, respecting capacity and dependencies.
3. **`roadmap.md`** — the actual roadmap document you'd present: the now/next/later table, an outcome + metric for every Now and Next item, and honest uncertainty language for Later (per Lecture 3 §5).
4. **`defense.md`** — a written defense of three specific decisions a skeptical stakeholder is guaranteed to push back on (see below).
5. **`notes.md`** — a short reflection (see the end).

Everything runs against the seed tables from the [week README](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/README.md). Works on PostgreSQL or SQLite; note which you used.

---

## Part A — Score the backlog (SQL)

In `scoring.sql`:

1. Compute **RICE** for all 14 items, ranked.
2. Compute **cost of delay and WSJF** for all 14 items, ranked.
3. Run the **Kano classification** for the four surveyed features (`recurring_tasks`, `dark_mode`, `ai_task_summaries` from the seed, plus `guest_external_access` from Exercise 2 — insert that data if you haven't already), with tallies and Better/Worse coefficients for each.
4. Produce one combined query or view that shows, for every item: `item_key`, `title`, `rice_score`, `rice_rank`, `wsjf_score`, `wsjf_rank`, and `rank_shift` (the difference between the two ranks). Use a window function (`RANK() OVER (...)`).

## Part B — Sequence and build the roadmap (Python)

In `roadmap.py`:

1. Load the scored backlog and the dependency table.
2. Implement the capacity-constrained, dependency-respecting sequencer from Lecture 3 / Exercise 3: **Now capacity = 20 job-size points, Next capacity = 20 job-size points**, everything else falls to Later.
3. Assert (a real `assert`, not a comment) that every dependency in `backlog_dependencies` is satisfied by your final ordering — i.e., no item's prerequisite is scheduled after it, whether they land in the same bucket or different ones.
4. Export the final roadmap table to `roadmap.csv`.

## Part C — Write the roadmap document

In `roadmap.md`, produce the actual artifact:

- A **Now** section: every item, its outcome, its metric (Lecture 3 §4 style), and its job-size points, summing to ≤20.
- A **Next** section: same shape, directional language (Lecture 3 §5 — no dates, named dependencies/risks where relevant).
- A **Later** section: every remaining item with a one-sentence reason it's there — cite the specific RICE, WSJF, or Kano finding that justifies deprioritizing it. `dark_mode` must explicitly reference its Kano result, not just "low score."
- A one-paragraph **"how we got here"** intro explaining, in plain English a non-PM stakeholder could follow, that the roadmap combines value-per-effort (RICE), urgency (cost of delay), what kind of value it is (Kano), and what the team can actually build (capacity) — not any single number alone.

## Part D — Defend three decisions

In `defense.md`, write a short, specific defense (3–5 sentences each) for:

1. **Why `dark_mode` — the single most-upvoted request in Loopline's history — is not in Now or Next.** Use the actual Kano tally, not just "it scored low."
2. **Why `audit_log_compliance` is in Now even though a stakeholder might ask "why are we building an internal compliance feature before [some more exciting Later item]?"** Use the dependency and the WSJF numbers.
3. **One decision you are genuinely least confident about**, and why. Every real roadmap has at least one call that's closer than the others — name yours, and say what evidence would change your mind.

---

## Rules

- **Every score must trace to a query in `scoring.sql`.** No hand-typed numbers in `roadmap.md` that don't come from a query you ran and can show.
- **Respect the capacity constraint.** Now ≤ 20 job-size points. If your sequencer would put a partial item over the line, it stays out — don't round the capacity up to fit one more thing.
- **Respect both dependencies.** `guest_external_access` cannot precede `audit_log_compliance`; `ai_task_summaries` cannot precede `public_api_webhooks`.
- **No spreadsheets.** Scoring lives in SQL, sequencing lives in Python/pandas, per this course's data-tooling rule.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness of scoring | 25% | RICE, WSJF, and Kano numbers all verifiably match what the seed data produces |
| Roadmap validity | 20% | Capacity respected exactly; both dependencies provably satisfied (the `assert` passes) |
| Outcome/metric quality | 15% | Every Now/Next item has a falsifiable outcome and a metric traceable to a real table/query, not "we'll see how it goes" |
| Honest uncertainty | 15% | Now/Next/Later language matches Lecture 3 §5's certainty rules; nothing in Later gets a disguised date |
| Defense quality | 20% | `defense.md`'s three answers use real numbers, take the counterargument seriously, and the "least confident" answer is genuinely candid, not a humble-brag |
| Process discipline | 5% | Everything traces to a runnable query/script; no hand-typed unverifiable numbers |

---

## Reflection (`notes.md`, ~200 words)

1. Where did RICE and WSJF disagree most sharply on *your* analysis, and which one did you end up trusting for that item?
2. Which Kano result most surprised you, and did it change anything about your roadmap versus what pure RICE/WSJF would have produced?
3. If Loopline's engineering capacity were cut to 13 points next quarter instead of 20, which specific item would you cut from Now first, and why that one and not another?
4. What's the one number in your whole analysis you're least sure is honestly estimated — your own version of Challenge 2's gamed score? What would you need to trust it more?

---

## Why this matters

This mini-project is the shape of real quarterly planning: a pile of legitimate, competing asks; a fixed amount of engineering time; and a room full of people who will ask "why not mine?" Do the scoring in SQL, the sequencing in Python, and the defense in writing, and you have a roadmap that survives contact with a skeptical VP — not because it gives everyone what they want, but because every "no" in it is backed by a number someone can check.

When done: push, then take the [quiz](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/quiz.md).
