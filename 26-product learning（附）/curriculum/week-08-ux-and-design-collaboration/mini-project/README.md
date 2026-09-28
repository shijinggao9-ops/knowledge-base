# Mini-Project — Critique, Test, and Redesign Loopline's Guest Invite Flow

> Take one broken flow end to end: critique it against the heuristics, run a real 5-user usability test on it, and write the redesign spec a designer and an engineer could build from tomorrow — with prioritized fixes and success metrics that live in SQL, not a spreadsheet.

**Estimated time:** 3–3.5 hours, best done Saturday after this week's exercises and challenges.

This is the week's capstone, and it's the actual job: a support lead doesn't hand you a redesign — they hand you a pile of tickets and a flow that's clearly not working. Your value is turning that into evidence (a heuristic pass, a real test), a decision (a prioritized fix list), and a spec someone else can execute without another meeting.

---

## The scenario

Loopline's support queue has 340 open tickets this month tagged `guest-invite-confusion` — more than any other tag. The flow: an existing Loopline user invites an external guest (someone with no Loopline account) to view one shared board. Here's the flow as it stands today:

```
SCREEN 1 — Board Settings (inviter's view)
  "Invite a guest" field: enter an email, [Send Invite] button.
  No indication of what the guest will be able to see or do.

SCREEN 2 — Guest receives an email
  Subject: "You've been invited to Loopline"
  Body: "Click below to view the board."
  [View Board] button/link.

SCREEN 3 — Guest clicks the link, lands on a sign-up wall
  "Create a free Loopline account to continue."
  Fields: email (pre-filled, locked), password, confirm password.
  No explanation of WHY an account is required just to view one board.
  [Create Account] button. No "just let me view it" option anywhere.

SCREEN 4 — Guest creates account, redirected to Loopline's full app
  Guest lands on an EMPTY home dashboard — not the board they were
  invited to. The invited board is not visible anywhere on this
  screen; it's buried three clicks deep under "Shared with me."
  No callout, no notification, no arrow pointing anywhere.

SCREEN 5 — Guest eventually finds "Shared with me" (if they do)
  Board appears. Guest can view it. If they try to comment, a modal
  appears: "Upgrade required to comment on shared boards." No
  indication this restriction existed before they got this far.
```

Support's ticket themes, summarized from the queue: "the invite link asked me to make a whole account," "I couldn't find the board after signing up," "I thought I could comment, now it wants money," and — most common — "the guest never even finished signing up, can you just re-share it as a regular link."

---

## Deliverable

A directory in your portfolio `c44-week-08/mini-project/` containing:

1. `flow-map.md` — the current flow, mapped per Lecture 1, with every exit ramp marked.
2. `heuristic-evaluation.md` — a full heuristic pass, at least 6 violations, each with severity.
3. `usability-test/` — a subfolder with:
   - `test-script.md` — 3 goal-based tasks (put yourself in the *guest's* shoes — the inviter's side is not what's broken here) with written success criteria.
   - `sessions.sql` — real `INSERT` statements from **5 real sessions** you ran (recruit 5 people — they don't need a Loopline account; walk them through the screens above as a verbal/paper prototype if you can't build it live, same as Exercise 2 Option B).
   - `results-summary.md` — the output of your `GROUP BY` summary queries.
4. `redesign-spec.md` — the full spec (see structure below).
5. `notes.md` — a short reflection (see the end).

---

## Part 1 — Critique the current flow (45 min)

Map the flow and run a heuristic evaluation, same method as Exercise 1. You should find real violations at, at minimum: the unexplained account requirement (Screen 3), the guest landing somewhere other than the invited board (Screen 4), and the late-revealed comment restriction (Screen 5). Look for more — there are at least 6 total.

## Part 2 — Run a usability test (75 min)

Write 3 tasks that put a first-time guest through this flow (e.g., "you got an email invite to view a shared board — go see it," "try to leave a comment on something on the board"). Run it on 5 real people using the screens above as your script (they play "the guest," you read each screen's content and they tell you what they'd do). Log every result to the `usability_sessions` table from the [week README](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/README.md#set-up-the-usability-log-table), using `flow_name = 'guest_invite'`. Run the same three summary queries from Exercise 2 and save the output.

## Part 3 — Write the redesign spec (60 min)

`redesign-spec.md` must contain these sections, in order — this is the exact shape a real flow spec takes:

```markdown
# Redesign Spec — Guest Invite Flow

## Problem statement
(2-3 sentences: what's broken, backed by the ticket volume and your test data.)

## Current flow (link to flow-map.md)

## Findings, ranked
(Your severity x frequency table, pulling from BOTH the heuristic
evaluation AND the usability-test session data — cite which source
each finding came from.)

## Proposed new flow
(Numbered screens, same format as Exercise 1's map. For each
changed screen, one sentence tying it to a specific finding above.)

## What we are NOT changing, and why
(At least one thing you deliberately left alone, and why — e.g.,
maybe requiring SOME form of identity before commenting is
reasonable; the problem is WHEN and HOW it's revealed, not that
it exists at all.)

## Success metrics
(2-3 SQL-queryable metrics, same discipline as Challenge 1: exact
query shape, what result means "it worked," and one named trap
metric.)

## Open questions for engineering / design
(At least 2 real questions you can't answer alone — e.g., technical
feasibility of a magic-link view-only mode, or whether the
"upgrade to comment" paywall is a business requirement you can't
remove, only relocate earlier in the flow.)
```

## Part 4 — Reflection (`notes.md`, ~200 words)

1. What did the usability-test data tell you that the heuristic evaluation alone didn't?
2. Which finding, if you could only ship one fix, would you pick — and why (severity, frequency, or something else)?
3. What's one thing a real participant said or did that you didn't expect?
4. If Loopline's product team pushed back with "guests can't view without an account, that's a business requirement, not a UX bug" — how would you respond, using the trade-off framework from Lecture 3?

---

## Rules

- **Both critique methods, both required.** A redesign backed only by your own heuristic opinion, with no real test data, is an incomplete deliverable this week — the whole point is combining expert evaluation with real observed behavior.
- **All usability data goes in SQL**, queried with real `GROUP BY` statements you actually ran — no hand-tallied counts, no spreadsheet.
- **Every proposed screen change cites a specific finding.** No redesign choices introduced with no traceable justification.
- **Success metrics must be SQL-queryable** against an events table, matching this course's rule that product data lives in SQL, never a spreadsheet.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Heuristic evaluation quality | 20% | 6+ real violations, each with a specific heuristic and justified severity |
| Usability test execution | 25% | 5 real sessions, goal-based tasks, honest logging (including failures) to SQL |
| Redesign traceability | 20% | Every screen change in the new flow cites a specific finding |
| Success metrics | 15% | 2–3 SQL-queryable metrics, including a named trap metric |
| Spec clarity | 10% | A designer/engineer could start work from `redesign-spec.md` without a clarifying meeting |
| Reflection | 10% | Honest, specific answers — especially Question 4's push-back scenario |

---

## Why this matters

This is the full loop a PM runs every time a flow is quietly costing the business tickets, churn, or trust: notice the signal (340 tickets), ground your instinct in a structured evaluation (heuristics), replace instinct with evidence (a real test, logged where it can be queried honestly), and turn evidence into a spec someone else can execute. Every skill from this week — mapping, heuristics, testing, critique, accessibility trade-offs — shows up in that one loop, and you'll run it again for real the first time you're the PM on a flow nobody trusts.

When done: push, then take the [quiz](26-product%20learning（附）/curriculum/week-08-ux-and-design-collaboration/quiz.md) and start [Week 9 — Go-to-market & launch](../../week-09-go-to-market-and-launch/).
