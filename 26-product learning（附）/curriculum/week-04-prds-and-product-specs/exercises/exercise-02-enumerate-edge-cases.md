# Exercise 2 — Enumerate a Feature's Edge Cases

**Goal:** Apply Lecture 3's five-category edge-case checklist (empty, error, loading, permission, timing/concurrency) to a *new* Loopline feature you haven't seen worked through — proving you've learned the method, not memorized the Stuck Task Alerts example.

**Estimated time:** 60 minutes.

## Setup

This exercise uses a different feature: **Task Handoff**, a small Loopline capability where a task's assignee can hand it off directly to a teammate (instead of a manager reassigning it), with an optional note explaining why.

> **Story:** As a task assignee, I want to hand off my task directly to a teammate with a short note, so that work doesn't stall while I wait for my manager to reassign it.

Create a file `task-handoff-edge-cases.md`.

## Tasks

1. **Write one edge case per category** (five categories, five minimum rows) using the table format from Lecture 3 (`Scenario | Expected behavior | Rationale`). For each, the scenario must be specific to Task Handoff — not a copy of a Stuck Task Alerts case with the words swapped.

   Categories to cover:
   - **Empty state** — e.g., what does the handoff UI show if the assignee's team has no other members to hand off to?
   - **Error state** — e.g., what happens if the teammate being handed off to has since left the team/workspace?
   - **Loading/in-progress state** — e.g., what if the original assignee starts a handoff and, before it completes, the manager reassigns the task through a different flow at the same moment?
   - **Permission/boundary state** — e.g., can a task be handed off to someone *outside* the current team? Can the manager veto or undo a handoff after the fact?
   - **Timing/concurrency state** — e.g., can a task be handed off twice in quick succession (A → B → C within one minute) — is that allowed, rate-limited, or blocked?

2. **For each row, write the "rationale" honestly** — if you genuinely don't know the right product answer, don't fake confidence. Write the row as an **open question** instead (see Lecture 1's Open Questions section) and state what information you'd need to decide. A spec that honestly flags "I don't know yet, here's who should decide" is stronger than one that guesses and states it as fact.

3. **Add two more edge cases of your own invention** — cases the five-category checklist doesn't obviously suggest but that you noticed by imagining a real user using this feature carelessly, angrily, or by accident (e.g., handing off a task to *themselves*, or hitting the handoff button twice fast by mimicking a slow network).

4. **Rank your full list (7 rows total)** by how *damaging* it would be to ship without handling it, most damaging first. One sentence per row justifying its rank.

## Expected outcome (self-check)

- You have exactly 5 category-driven rows (Task 1) plus 2 self-found rows (Task 3) — 7 total.
- At least one row is honestly marked as an open question rather than a confident guess (Task 2) — if all 7 have confident answers, go back and find the one you're actually unsure about; there's always at least one.
- Your ranking (Task 4) puts something involving **data loss or the wrong person seeing/getting something** near the top — those are almost always the most damaging category of edge case in a collaboration feature.

## Done when…

- [ ] `task-handoff-edge-cases.md` has 7 distinct, Task-Handoff-specific edge cases in table form.
- [ ] Every row has a scenario, an expected behavior (or explicit open question), and a rationale.
- [ ] The 7 rows are ranked by damage-if-unhandled, with a one-sentence justification each.
- [ ] None of your 7 rows are a copy of a Stuck Task Alerts case with different nouns.

## Stretch

- Pick your #1-ranked (most damaging) edge case and write full Given/When/Then acceptance criteria for the correct handling of it, using Lecture 2's format.
- Loopline's existing `events` table (from the week README) doesn't have a `task_handed_off` event yet. Write the `INSERT` statement for one, including whatever properties you think a PM would need to later answer "are handoffs actually unblocking work, or just passing the stall along?"

## Submission

Commit `task-handoff-edge-cases.md` to your portfolio under `c44-week-04/exercise-02/`.
