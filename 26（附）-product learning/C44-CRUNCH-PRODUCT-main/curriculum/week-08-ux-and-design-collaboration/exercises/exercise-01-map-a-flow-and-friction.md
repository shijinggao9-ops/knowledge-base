# Exercise 1 — Map a Flow and Its Friction

**Goal:** Turn a written flow into a numbered map with decision points and exit ramps called out, then run a full heuristic evaluation against it, scoring every violation you find.

**Estimated time:** 90 minutes.

## The flow: Loopline's "Upgrade to Team plan" checkout

Here is the flow as it currently exists, screen by screen. Read it once straight through as a first-time user would (Lecture 1, step 1 of a heuristic evaluation), then come back and work the tasks below.

```
SCREEN A — Team Settings
  "You're on the Free plan (up to 5 members)."
  [Upgrade] button, small, gray, bottom-right of the card.

SCREEN B — Plan comparison
  Three columns: Free / Pro / Team. Team column highlighted.
  Team: "$14/seat/mo. Unlimited members, admin roles, SSO."
  [Choose Team] button under the Team column.
  (No visible way back except the browser back button.)

SCREEN C — Seat count picker
  "How many seats do you need?" [ - ] 5 [ + ]  (stepper, starts at 5)
  Small gray text below: "$14 x 5 = you'll see the total at checkout."
  [Continue] button.
  (Stepper allows 0; nothing stops the user from decrementing to 0.)

SCREEN D — Billing details
  Fields: Card number, Expiry, CVC, Name on card, Billing address (4 lines).
  No indication anywhere on this screen of how many seats were chosen
  or what the price will be.
  [Continue] button.

SCREEN E — Order summary
  "5 seats x $14/mo = $70/mo" <- always shows 5, ignores what was
  actually picked on Screen C (known bug, not yet fixed).
  Below it, a gray paragraph of legal/tax text, same font size and
  color weight as the price line above it.
  [Confirm and pay] button, same visual style as [Continue] on
  every prior screen (no added visual weight for the final,
  money-committing action).

SCREEN F — Processing
  A spinner. No text. No estimate of how long this takes.

SCREEN G1 — Success (on payment success)
  "You're all set!" Redirects to Team Settings after 2 seconds.

SCREEN G2 — Failure (on payment failure)
  "Payment failed." No reason given. [Try again] button returns
  the user all the way back to SCREEN D (billing details), with
  every field blank — including the seat count, which is gone.
```

## Part 1 — Map the flow (30 min)

Using either the numbered-list or Mermaid format from [Lecture 1](../lecture-notes/01-flows-friction-and-heuristics.md#mapping-notation), write a complete flow map of Screens A through G2. Your map must explicitly show:

- Every screen, in order.
- The decision point after Screen F (success vs. failure) as a named branch, not a footnote.
- Every exit ramp you can find — anywhere the user could plausibly leave without finishing. (There are at least three; find them.)

Save this as `flow-map.md`.

## Part 2 — Run a heuristic evaluation (45 min)

Walk the flow a second time, this time against Nielsen's 10 heuristics, one heuristic at a time (not all ten screen-by-screen — that's how you miss things; see Lecture 1). For every violation you find, log a row:

| Screen | Heuristic # + name | Description | Severity (0–4) |
|---|---|---|---:|

You should find **at least 8 violations** across the flow — several are seeded deliberately (the seat-count stepper allowing 0, the summary screen's hardcoded "5 seats" bug, the failure screen losing all data). Some are subtler (visual weight of the CTA, the missing back path from Screen B). Look hard at Screens E, F, and G2 — the summary, wait, and failure states carry more violations than the earlier screens.

Save this as `heuristic-evaluation.md`.

## Part 3 — Written summary (15 min)

In 150–200 words, answer: **which single screen would you fix first, and why** — using severity and frequency reasoning (a screen everyone passes through with a severity-2 issue vs. a rarer path with a severity-4 issue), not just "it felt the worst."

Append this to the bottom of `heuristic-evaluation.md` under a `## Summary` heading.

## Done when…

- [ ] `flow-map.md` shows all 9 screens (A, B, C, D, E, F, G1, G2), the success/failure branch, and at least 3 exit ramps.
- [ ] `heuristic-evaluation.md` has at least 8 rows, each citing a specific numbered heuristic (not "this feels bad").
- [ ] Every row has a severity rating with a one-clause justification, not just a bare number.
- [ ] The `## Summary` makes a severity × frequency argument for one fix-first screen.

## Submission

Commit `flow-map.md` and `heuristic-evaluation.md` to your portfolio under `c44-week-08/exercise-01/`.
