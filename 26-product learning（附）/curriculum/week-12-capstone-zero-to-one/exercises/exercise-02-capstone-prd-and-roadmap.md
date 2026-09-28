# Exercise 2 — Write the Capstone PRD and Roadmap

**Goal:** Spec your MVP in a PRD that cites Exercise 1's discovery brief directly, then build a RICE/WSJF-scored, capacity-constrained Now/Next/Later roadmap for it — the Act 2 and Act 3 artifacts your Exercise 3 dashboard and Challenge 1 experiment will both depend on.

**Estimated time:** 120 minutes.

## Setup

Have `discovery-brief.md` from Exercise 1 open — you'll cite it by name in two places below. Create `c44-week-12/exercise-02/prd.md` and `c44-week-12/exercise-02/roadmap.md`.

## Part A — The PRD (60 min)

Using Week 4's PRD format, write `prd.md` with these sections:

1. **Problem** — one paragraph, explicitly citing the specific finding from your discovery brief (quote or closely paraphrase the problem statement and JTBD — a reader should not need to open the discovery brief separately to know what problem this PRD solves).
2. **Goals** — 2–3 sentences on what success looks like for the business/product, not just the user.
3. **Non-goals** — at least 3 specific things you are explicitly NOT building in v1, and one sentence each on why (this is the section most student PRDs shortchange; do not shortchange it — Lecture 1 named an unscoped item sneaking into "Now" as one of the most common coherence failures, and a weak non-goals section is exactly how that happens).
4. **User stories** — 3–5, in "As a [user], I want to [action], so that [outcome]" format, covering only in-scope functionality.
5. **Success metric** — exactly ONE primary metric, stated precisely enough that you could write the SQL query for it today (not "engagement" — "percentage of new users who complete their first [core action] within 24 hours of signup"). This is the metric Exercise 3's dashboard must measure — write it carefully.
6. **Open questions** — 2–3 real unresolved questions, honestly stated (not rhetorical "questions" that are actually already-decided statements in disguise).

## Part B — The prioritized backlog and roadmap (60 min)

1. **List 6–8 backlog items** for your product: the MVP items from your PRD's user stories, plus 3–4 plausible **v2/v3 items** you are NOT building now but can imagine wanting later (this gives your RICE/WSJF table enough spread to be meaningful — a 3-item backlog can't demonstrate real prioritization tension).
2. **Score every item on RICE** (Reach × Impact × Confidence ÷ Effort) using Week 5's scales. Show your reasoning for at least 2 items' Confidence scores specifically — Confidence is the input students most often inflate without justification, and Week 5's Q15 lesson (sponsorship enthusiasm is not evidence for Confidence) applies here too.
3. **Score every item on WSJF** (Cost of Delay ÷ Job Size, with Cost of Delay = User-Business Value + Time Criticality + Risk Reduction/Opportunity Enablement). At least one item's WSJF rank should meaningfully diverge from its RICE rank — if none do, revisit your Time Criticality scores; a capstone backlog with zero real urgency variance usually means Time Criticality was scored lazily as "medium" across the board.
4. **State a Now capacity** in job-size points (pick a number and justify it briefly — e.g., "one person, one week, ~8 points of capacity").
5. **Build the Now/Next/Later roadmap** in `roadmap.md`, following Week 5's uncertainty-language rules: Now items are capacity-checked and named specifically; Next items use directional language naming a real dependency or risk, not a date; Later items get a one-sentence reason for being Later, not silence.
6. **Sequencing check** — if any item has a hard prerequisite (something else must ship first regardless of its own score), name the dependency explicitly and show it pulled ahead in your sequence, exactly as Week 5's sequencing rule requires.

## Expected outcome

A PRD whose Problem section a reader could trace, sentence by sentence, back to your discovery brief — and a roadmap whose Now bucket contains only items that trace back to the PRD's user stories, with the RICE and WSJF tables showing genuine disagreement on at least one item that you can explain, not just report.

## Done when…

- [ ] The PRD's Problem section explicitly references the discovery brief's problem statement or JTBD, not a rephrased-from-scratch version.
- [ ] Non-goals section has at least 3 specific exclusions with a reason each.
- [ ] The success metric is precise enough to write a `SELECT` for it without further clarification.
- [ ] The backlog has 6–8 items, all scored on both RICE and WSJF, with visible reasoning (not just numbers) for at least 2 Confidence scores.
- [ ] At least one item's RICE rank and WSJF rank meaningfully diverge, and you've explained why in one sentence.
- [ ] The Now bucket's items all trace to the PRD's in-scope user stories — nothing unscoped snuck in.
- [ ] Any hard dependency is named and correctly sequenced ahead of the item it blocks.

## Stretch

Run a Kano-style gut check (no survey needed — reason it through yourself) on your 2–3 v2/v3 items: which would be Must-be, One-dimensional, or Attractive if you built them? Write one sentence per item. This previews Challenge 1's experiment design — an Attractive-category item is a much better A/B test candidate than a Must-be item, since Must-be features' absence is what you'd notice, not their addition.

## Submission

Commit `prd.md` and `roadmap.md` to your portfolio under `c44-week-12/exercise-02/`.
