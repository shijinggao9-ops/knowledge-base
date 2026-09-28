# Exercise 1 — Write Acceptance Criteria for a Story

**Goal:** Take a Stuck Task Alerts story and write Given/When/Then acceptance criteria precise enough that two engineers reading independently would build identical behavior, and a tester could write pass/fail tests straight from your text.

**Estimated time:** 60–75 minutes.

## Setup

Reread Lecture 2's five acceptance criteria for Story 1 (the core alert). You will **not** write those again — instead, you're writing acceptance criteria for **Story 2**, which Lecture 2 named but never spec'd:

> **Story 2:** As an engineering manager, I want to snooze a stuck-task alert for a specific task, so that I don't get re-alerted on something I've already decided to deal with later.

Create a file `story-02-acceptance-criteria.md`.

## Tasks

1. **Write the story in full template form** at the top of your file: `As a <role>, I want <capability>, so that <outcome>.` Use the version above, or improve its wording if you think it's imprecise — say what you changed and why, in one sentence.

2. **Run the INVEST test** on the story as written. For each of the six letters, write one sentence: does it pass, and why? If any letter fails, rewrite the story so it passes before moving to acceptance criteria — you cannot write good acceptance criteria for a story that fails INVEST.

3. **Write at least 6 acceptance criteria** in Given/When/Then form, covering:
   - The **happy path** — a manager snoozes a specific stuck alert and it doesn't re-fire during the snooze window.
   - **At least one exact-boundary case** — what happens right at the edge of the snooze duration (does it use the same care as Lecture 2's AC2, which tested "47 hours 55 minutes")?
   - **At least one "does NOT happen" case** — something that must explicitly *not* occur (e.g., snoozing one task does not suppress alerts for the manager's *other* stuck tasks).
   - **At least one interaction with an existing behavior from Lecture 2's Story 1** — e.g., what happens if the task becomes un-stuck (marked done) *during* the snooze window — does the snooze become moot, and how would a test verify that?
   - **One case involving who is allowed to snooze** — can *any* team member snooze the alert, or only the specific manager it was addressed to? State it explicitly; don't leave it implied.

4. **Self-review your own criteria** against this test from the lecture: for each acceptance criterion, could it be copy-pasted as the story's "so that" clause with no loss of information? If yes, rewrite it — it isn't adding anything beyond the story yet.

5. **Write the definition-of-done checklist** (3–5 items) that would apply to this story specifically, on top of whatever DoD already applies to Story 1's alert-delivery pipeline (assume that pipeline already exists and is tested — this DoD is only for the *new* snooze behavior).

## Expected outcome (self-check)

- Your INVEST analysis (Task 2) names a *specific* reason for each letter — not just "yes, it's independent" with no justification.
- Every acceptance criterion (Task 3) contains a **number, a duration, or an exact condition** — no criterion should be checkable only by "feel."
- At least one criterion explicitly states what does **not** happen, not only what does.
- Your snooze-duration boundary case (Task 3) mirrors the precision of Lecture 2's AC2 — testing a moment just *before* the boundary, not just "snoozing works."

## Done when…

- [ ] `story-02-acceptance-criteria.md` has the story, INVEST analysis, 6+ acceptance criteria, and a definition-of-done checklist.
- [ ] Every acceptance criterion follows Given/When/Then form.
- [ ] At least one criterion tests a precise boundary (a specific minute/hour), not just the happy path.
- [ ] You could hand this file to someone who has never read the lecture and they could tell you, in one sentence, exactly what "snooze" means for this feature.

## Stretch

- Write acceptance criteria for a **third** story: "Manager can turn off Stuck Task Alerts entirely." Pay particular attention to what happens to tasks that are *already* mid-stuck-period when the manager opts out — does the in-flight alert still fire?
- For your Story 2 criteria, identify which single acceptance criterion, if it were silently dropped from the spec, would cause the most confusing production bug. Explain why in two sentences.

## Submission

Commit `story-02-acceptance-criteria.md` to your portfolio under `c44-week-04/exercise-01/`.
