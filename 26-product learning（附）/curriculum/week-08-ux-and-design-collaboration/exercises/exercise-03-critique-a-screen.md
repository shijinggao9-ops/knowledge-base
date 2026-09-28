# Exercise 3 — Critique a Screen Against Heuristics

**Goal:** Give structured, actionable critique on a single screen — grounded in the heuristics and an accessibility pass, not personal taste.

**Estimated time:** 60 minutes.

## The screen: Loopline's Order Summary (Screen E)

This is Screen E from the checkout flow in [Exercise 1](exercise-01-map-a-flow-and-friction.md), described in more visual detail this time:

```
┌─────────────────────────────────────────┐
│  Loopline                          [x]   │
│                                           │
│  Order Summary                           │
│                                           │
│  5 seats x $14/mo  ─────────────  $70/mo │   <- light gray text, 14px
│                                           │
│  By confirming, you agree to the Terms   │   <- light gray text, 14px
│  of Service and authorize Loopline to    │      (SAME size/color/weight
│  charge your card monthly until you      │       as the price line above)
│  cancel. Taxes calculated at checkout    │
│  based on your billing address. See our  │
│  Refund Policy for details.              │
│                                           │
│         [ Confirm and pay ]              │   <- outline button, same
│                                           │      gray as [Continue] on
│                                           │      every earlier screen
└─────────────────────────────────────────┘
```

Notes for your critique:

- The "5 seats" is hardcoded and does not reflect whatever seat count the user actually picked on Screen C — a real bug, not a design choice.
- The legal paragraph and the price line are visually identical in weight (same 14px, same gray).
- The `[x]` close button top-right has no label — screen readers announce it only as "button."
- The `[Confirm and pay]` button uses the same outline style as every non-final "Continue" button earlier in the flow.

## Part 1 — Heuristic-grounded critique (25 min)

Using the [heuristic-grounded critique](03-critique-and-tradeoffs.md#heuristic-grounded-critique) method, write one entry per violation you find, in this format:

```
Heuristic: #<n> <name>
Observation: <what's on the screen>
Consequence: <what it does to the user>
Severity: <0-4>
```

Find at least **4** distinct heuristic violations. (Hint: look hard at the visual weight of the legal text vs. the price, the unlabeled close button, and the button style not signaling "this is the final, money-committing step.")

## Part 2 — I Like / I Wish / What If (15 min)

Write one full I Like / I Wish / What If pass on the whole screen (Lecture 3, Section 2). You must have **at least one genuine "I like"** — find something that's actually working (e.g., the price-per-seat math being shown inline is legitimately useful) before you list what's wrong. A critique with no "I like" reads as an attack, not feedback a designer can use.

## Part 3 — Accessibility pass (15 min)

Check this screen against three of the five common issues from [Lecture 3, Section 4](03-critique-and-tradeoffs.md#the-most-common-issues-youll-actually-find-ranked-by-how-often-they-show-up):

1. **Color contrast** — is 14px light-gray-on-white plausibly passing WCAG AA's 4.5:1 ratio for normal text? (You don't need exact hex values — reason about it: light gray on white is a very common contrast failure. State your judgment and why.)
2. **Alt text / labeling** — what's wrong with the `[x]` close button specifically for a screen-reader user, and what should its accessible label say?
3. **Visual hierarchy for low-vision users** — if the legal text and the price are the same visual weight, what does that do to a low-vision user skimming quickly, beyond what it does to anyone else?

Write 2–3 sentences per point.

## Done when…

- [ ] At least 4 heuristic violations, each with a numbered heuristic, observation, consequence, and severity.
- [ ] One complete I Like / I Wish / What If pass, including a genuine "I like."
- [ ] All 3 accessibility questions answered with real reasoning, not "looks fine."
- [ ] Every "I wish" and every heuristic violation names a specific element on the screen — nothing generic like "the design feels off."

## Submission

Commit your critique as `critique.md` to your portfolio under `c44-week-08/exercise-03/`.
