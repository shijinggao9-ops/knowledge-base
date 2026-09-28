# Mini-Project — A Validated Problem Brief

> Produce a single, complete problem brief for the import-friction opportunity — the artifact you'd actually hand to a leadership team asking to greenlight engineering time — combining a JTBD problem statement, root-cause reasoning, a SQL-backed opportunity size, and a placement on an opportunity-solution tree. One opportunity, fully worked, end to end.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it's deliberately narrower than a whole roadmap: **one opportunity, done completely**, rather than many opportunities done shallowly. That's realistic — most weeks, a working PM produces exactly one or two problem briefs this thorough, not twenty. The value isn't breadth here, it's rigor: every claim in the brief should trace back to either a Five Whys chain, a SQL query you ran, or an explicitly labeled assumption.

---

## Deliverable

A directory in your portfolio `c44-week-03/mini-project/` containing:

1. `problem-brief.md` — the full brief (structure below).
2. `sizing.sql` — the SQL queries backing your opportunity size (you may extend your Exercise 2 queries, but this file should stand on its own — a reader shouldn't have to go find Exercise 2 to understand your numbers).
3. `opportunity-tree.md` — the tree section of the brief may live here, reused/extended from Exercise 3 if you want, but it must include the import-friction branch with your finalized sizing numbers.

Everything runs against the `signup_cohort` table from the [week README](../README.md#set-up-this-weeks-seed-dataset). Note which engine (PostgreSQL or SQLite) you used.

---

## `problem-brief.md` — required sections

### 1. Problem statement (Lecture 1 structure)

Write the full who/what/why/impact problem statement for the import-friction opportunity. This can build on Lecture 1's worked example, but rewrite it in your own words — don't copy it verbatim. Include a short (3–4 step) Five Whys chain showing how you got from the symptom ("import fails") to the stated root cause.

### 2. JTBD statement

The companion JTBD statement (situation / motivation / outcome), written from the perspective of a specific persona you name (e.g., "Priya, an ops lead migrating a 6-person team from a shared spreadsheet").

### 3. Opportunity size — bottom-up (SQL-backed)

At minimum, your `sizing.sql` must answer:

- What share of all signups end up as a failed import? (chained correctly — see Lecture 2 and Exercise 2, Task 2, for why the naive unchained number is wrong)
- What is the conversion-rate gap between succeeded and failed imports, and the average MRR for each group?
- Does the gap survive a check for the seats-size confound (Exercise 2, Task 5), at least directionally?
- A final ranged annual estimate (low/base/high), with your monthly-signups assumption stated explicitly and justified in one sentence.

In `problem-brief.md`, report the **results** in plain language (a stakeholder reads the brief, not the SQL) with the numbers inline — e.g., "teams whose import fails convert at roughly a quarter of the rate of teams whose import succeeds ($X range in recovered annual MRR if closed)."

### 4. Opportunity size — top-down sanity check

A brief (not deeply developed — 4–6 lines) top-down TAM/SAM/SOM estimate, with your own stated assumptions (you may reuse Lecture 2's structure and numbers, or invent your own more conservative or more aggressive chain — your choice, but say which and why). State the ratio between your top-down and bottom-up numbers and give one honest sentence on what, if anything, explains the gap.

### 5. Opportunity-solution tree placement

Show where this opportunity sits on a tree rooted at a stated outcome (you may reuse Exercise 3's outcome or the lecture's). Include at least two candidate solutions underneath it, each with a one-line cost/complexity note — you are not committing to a solution in this brief, only showing that more than one was considered.

### 6. Recommendation

One paragraph: greenlight, kill, or "not yet — here's what we need first"? Defend it using the size, the evidence strength, and what it would cost to get a better number, the same reasoning you practiced in the challenges.

### 7. Assumptions log

A short bulleted list of **every** number in the brief that is a stated assumption rather than a direct query result (monthly signups, top-down chain inputs, anything else) — collected in one place so a skeptical reader can find and challenge each one without hunting through your prose.

---

## Milestones

- **Milestone 1 (45 min):** Sections 1–2 (problem statement + JTBD). Get the qualitative framing solid before touching SQL.
- **Milestone 2 (60 min):** Section 3, all SQL in `sizing.sql`, run and verified against the expected values from Exercise 2.
- **Milestone 3 (30 min):** Section 4, the top-down sanity check — keep it brief, it's a check, not the main event.
- **Milestone 4 (30 min):** Sections 5–7 — the tree, the recommendation, the assumptions log.

---

## Rules

- **No spreadsheet, anywhere in this deliverable** — sizing lives in `sizing.sql`, not a `.xlsx` or a table pasted from Excel. This is the rule stated in the [week README](../README.md#prerequisites) and it's non-negotiable for this course.
- **Every number in the brief must be traceable** — either to a query in `sizing.sql`, or to an explicit line in the assumptions log. A number with neither is not allowed in the final brief.
- **State ranges, not false-precision single numbers**, per Lecture 2 — "$18,900–$29,400/year," not "$24,150/year."
- **The tree must show more than one solution** under the opportunity — a tree with exactly one leaf isn't demonstrating that alternatives were considered (Lecture 3).

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Problem statement quality | 20% | Specific population, no solution words, root cause traced, falsifiable |
| SQL rigor | 25% | Queries are correct, chained rates handled correctly, confound check addressed honestly |
| Sizing communication | 20% | Ranged, assumption-labeled, plain-language translation of the SQL results |
| Tree + recommendation | 20% | At least 2 solutions considered; recommendation logically follows from the evidence, not asserted |
| Assumptions log | 15% | Every non-queried number is present and traceable |

---

## Reflection (add to the end of `problem-brief.md`, ~150 words)

1. Which section was hardest to make properly falsifiable/evidence-backed, and why?
2. If you had one more week before presenting this brief, what's the single piece of evidence you'd go get next?
3. Compare this brief to the vaguer version of the same idea ("import is broken, we should fix it") you might have written before this week. What changed?

---

## Why this matters

This is the exact shape of the document that separates a PM who gets roadmap slots funded from one who gets told "let's revisit next quarter." A stakeholder doesn't need to see your SQL to trust your number — they need to see that a number exists, that it's honestly ranged, and that you know exactly which of its inputs are solid and which are assumptions. Keep this brief; Week 4 (PRDs & specs) picks up exactly where this leaves off — turning a greenlit opportunity into a shippable spec.

When done: push, then take the [quiz](../quiz.md) and start [Week 4 — PRDs & specs](../../week-04-prds-and-specs/).
