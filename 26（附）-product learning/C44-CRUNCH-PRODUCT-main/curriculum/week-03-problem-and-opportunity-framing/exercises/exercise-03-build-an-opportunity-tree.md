# Exercise 3 — Build an Opportunity-Solution Tree

**Goal:** Build a complete opportunity-solution tree from scratch — one outcome, at least four opportunities of varying evidence strength, and at least two solutions under your strongest opportunity — and use it to make and defend a real prioritization call.

**Estimated time:** 1.5 hours.

## Setup

No database needed for this one, but keep your Exercise 2 results (`sizing.sql`) open — you'll cite the numbers from it directly. Create a file `opportunity-tree.md`.

## Part 1 — Choose an outcome (10 min)

Lecture 3 used *"increase week-1 activation rate for new trial teams (38% → 50%)."* For this exercise, use a **different** outcome so you're not just copying the lecture. Pick one:

- *Increase trial-to-paid conversion rate for teams that complete onboarding (currently ~35%, target 45%).*
- *Reduce time-to-first-task (the time between signup and creating the first real task) from a median of 40 minutes to under 10.*
- *Increase 90-day retention for teams that convert to paid (currently ~60%, target 75%).*

State your chosen outcome as the root of your tree, with the current baseline and target, exactly as specific as the examples above.

## Part 2 — Populate at least 4 opportunities (30 min)

For each opportunity, write:

- The opportunity itself, phrased from the customer's point of view (not a feature).
- Its evidence level: **Strong** (behavioral/data-backed), **Moderate** (qualitative, multiple sources), or **Weak** (anecdotal, single source).
- The source of that evidence (be specific — "3 of 5 Week 2 interviews," "the `signup_cohort` conversion gap," "1 sales call," etc. — inventing a plausible source is fine, but it must be specific, not "some users said").

At least one of your four opportunities **must** be the import-friction opportunity from this week, tied explicitly to your Exercise 2 numbers — even if your chosen outcome (Part 1) is different from the lecture's, argue whether or how import friction plausibly connects to it. (If you genuinely think it doesn't connect to your chosen outcome, that's a valid finding — say so, and don't force it onto the tree.)

## Part 3 — Solutions under your strongest opportunity (20 min)

Pick the opportunity with the strongest evidence on your tree. Write **at least two** candidate solutions under it — different enough from each other that choosing between them is a real decision, not two names for the same idea. For each solution, one sentence on its rough cost/complexity (Low/Medium/High) and one sentence on what you'd need to learn before committing to it.

## Part 4 — Draw the tree (15 min)

Represent your full tree as **either**:

- Indented Markdown (like Lecture 3's first example), or
- A Mermaid `graph TD` code block (like Lecture 3's second example).

Both are plain text — no drawing tool, no spreadsheet, no slide.

## Part 5 — Make and defend the call (15 min)

In 150–250 words, answer:

1. Which opportunity are you pursuing first, and why — reference the scoring dimensions from Lecture 3 (evidence strength, whether it's sized, whether it's cheap or expensive to strengthen further, how directly it serves the outcome).
2. Which opportunity are you explicitly **not** pursuing this quarter, and what evidence (not vibes) would change your mind?
3. If your strongest opportunity turned out to be the import-friction one, does the sizing range from Exercise 2 feel large enough, relative to your chosen outcome, to justify pursuing it first? If it's a different opportunity, explain honestly that you don't yet have a sized number for it — what would you need to get one?

## Done when…

- [ ] The tree has one clearly stated outcome with a current baseline and a numeric target.
- [ ] At least 4 opportunities, each labeled with an evidence level and a specific source.
- [ ] At least 2 solutions under the strongest opportunity, each with a cost/complexity note.
- [ ] The tree is drawn as plain text (Markdown indentation or Mermaid), not a screenshot or a slide.
- [ ] Part 5's defense references at least one specific number from your Exercise 2 SQL work.

## Stretch

Add a fifth branch: an opportunity you're fairly confident is **not real** — something a stakeholder insists is a problem but for which you'd predict the evidence, once gathered, will come back weak or contradicted. Say what evidence you'd expect to see if you're right, and what would surprise you into changing your mind. This is the discipline Challenge 1 asks you to fully write up.

## Submission

Commit `opportunity-tree.md` to your portfolio under `c44-week-03/exercise-03/`.
