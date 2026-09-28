# Challenge 1 — Redesign a Broken Checkout Flow

**Time:** ~90 minutes. **Difficulty:** Medium-hard. **No single right answer.**

## The scenario

Loopline's finance team just flagged the numbers: **checkout abandonment on the Team-plan upgrade is 61%** — more than three in five orgs that start the upgrade never finish it. Your heuristic evaluation from [Exercise 1](exercise-01-map-a-flow-and-friction.md) already found at least 8 real violations. Your VP wants a redesign proposal by end of week, not a list of complaints — a new flow, with reasoning, and a way to know if it actually worked.

## Your task

Produce a full redesign package for Loopline's Screens A–G2 (the checkout flow from Exercise 1). This is the shape of document you'd actually hand to a designer to start building from.

### 1. Carry-forward findings (10 min)

Pull your top 5 findings from Exercise 1's heuristic evaluation, ranked by severity × frequency-of-path (a screen every user passes through outweighs a rarer branch at equal severity). If you didn't do Exercise 1 yet, do it first — this challenge assumes it's done.

### 2. New flow map (35 min)

Write the redesigned flow, screen by screen, in the same numbered-list or Mermaid format from Lecture 1. For **every** change, write a one-sentence rationale tied to a specific finding — "moved seat count into a persistent summary bar because Exercise 1 found a severity-2 recognition-rather-than-recall violation at screens D and E" — not just "this is cleaner."

At minimum, your redesign must resolve:

- The seat-count-disappears problem (severity 2, hits everyone).
- The hardcoded "5 seats" bug on the summary screen.
- The zero-seats error-prevention gap (the stepper currently allows 0).
- The payment-failure screen giving no reason and no next step (severity 4).
- The failure screen losing all prior input on retry (severity 3).

You may restructure the screens entirely (combine steps, add a persistent summary, add inline validation) — you are not constrained to patching each screen in place. State clearly which screens you merged, split, or removed, and why.

### 3. Before/after friction count (15 min)

Re-run a mini heuristic pass on your *new* flow. Produce a two-row comparison table:

| | Violations found | Sum of severities | Worst single severity |
|---|---:|---:|---:|
| Before (Exercise 1) | | | |
| After (your redesign) | | | |

If your redesign doesn't measurably reduce this, say so honestly and explain what trade-off you made instead (e.g., you introduced one new minor violation in exchange for removing two severe ones — that can still be a net win, but say so explicitly).

### 4. Success metrics (20 min)

Define **2–3 metrics** that would tell you, after shipping, whether the redesign actually worked — each must be something queryable from a SQL events table (per this course's data-tooling rule — never "check the spreadsheet"). For each metric, state:

- The exact query shape you'd run (pseudo-SQL is fine — you don't have real event data this week).
- What result would count as "the redesign worked."
- One metric that could **rise** even if the redesign secretly made things worse (a trap metric) and how you'd guard against being fooled by it.

Example shape to follow:

```sql
-- Checkout completion rate: started checkout -> reached Success screen
SELECT
    DATE_TRUNC('week', started_at) AS week,
    COUNT(*) FILTER (WHERE reached_success) * 1.0 / COUNT(*) AS completion_rate
FROM checkout_attempts
GROUP BY 1
ORDER BY 1;
```

### 5. One-paragraph pitch (10 min)

Write the paragraph you'd actually say to your VP: what's broken, what you're changing, and what number you'll show them in three weeks to prove it worked.

## Constraints

- You may not simply delete steps that exist for a real reason (billing address is needed for tax calculation — don't just cut it; redesign around it).
- Every claim about *why* something is broken must trace back to a specific finding from Exercise 1 or a named heuristic — no new unsupported complaints introduced in this challenge.
- Your success metrics must be SQL-queryable, not "customer sentiment felt better" or anything requiring a spreadsheet tally.

## How success is judged

| Signal | Weak answer | Strong answer |
|---|---|---|
| Traceability | Redesign changes aren't tied to specific findings | Every change cites the exact finding it fixes |
| Completeness | Some of the 5 required fixes are missing or hand-waved | All 5 required fixes are addressed with a concrete new design |
| Honesty | Claims the new flow is perfect | Before/after table is run for real, including any new issue introduced |
| Metric quality | Vague or unmeasurable success criteria | 2–3 SQL-queryable metrics, including a named trap metric |
| Communication | Jargon-heavy, unclear pitch | The VP paragraph is something a non-PM could actually understand and act on |

## Submission

Commit `redesign-flow-map.md`, `before-after-comparison.md`, and `success-metrics.md` to your portfolio under `c44-week-08/challenge-01/`.
