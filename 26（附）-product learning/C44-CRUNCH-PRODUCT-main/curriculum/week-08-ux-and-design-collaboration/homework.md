# Week 8 — Homework

Five problems, ~5 hours total, spread across the week. These push this week's skills onto a product you actually use — the fastest way to feel how much friction is hiding in plain sight everywhere, once you know how to look.

---

## Problem 1 — Heuristic-audit a flow you use daily (60 min)

Pick a real flow from a product you use at least weekly (your bank's app, a food-delivery app, a work tool, a streaming service's cancel-subscription flow — canceling flows are a rich source of deliberate friction, which makes them a great pick). Map it (Lecture 1 format) and run a full 10-heuristic evaluation.

**Deliver** `homework-01-heuristic-audit.md`: the flow map, at least 6 violations with severity, and one paragraph on whether any of the friction you found looks *deliberate* (e.g., a cancel flow designed to be hard to complete) versus *accidental* (a genuine oversight) — and how you can tell the difference.

---

## Problem 2 — Run a mini usability test on a real product (90 min)

Recruit 3 people (fewer than the full 5-user test this week, since this is homework) and run a task-based think-aloud test on a real flow — could be the same one from Problem 1, or a different one. Write 2–3 goal-based tasks with success criteria first.

Log every result into a SQL table. Reuse the `usability_sessions` schema from the [week README](./README.md#set-up-the-usability-log-table), or create a lighter version if you prefer — either way, it must be a real table you `INSERT` into and `SELECT` from, not a spreadsheet or a bulleted list.

**Deliver** `homework-02-mini-test.sql` (your `CREATE TABLE`/`INSERT` statements) and `homework-02-findings.md` (a short severity × frequency table plus one paragraph on what surprised you).

---

## Problem 3 — Critique your own work (45 min)

Find a screenshot of something you built or designed yourself — for a class, a side project, a past job, anything with real UI. Write a full I Like / I Wish / What If critique of it, as if a colleague were reviewing it, being as honest as you'd want a real design partner to be with you.

**Deliver** `homework-03-self-critique.md`. Include the screenshot (or a described equivalent if you don't have one saved) and note: does it feel harder or easier to critique your own work honestly, compared to critiquing Loopline's flows this week? Why?

---

## Problem 4 — Run a real accessibility check (60 min)

Pick any public webpage (your own portfolio site, a company site, anything) and run a free automated accessibility scanner on it — [WAVE](https://wave.webaim.org/) or the Lighthouse accessibility audit built into Chrome DevTools (see [`resources.md`](./resources.md) for both). Automated tools catch maybe 30–40% of real issues (they're great at contrast and missing labels, blind to things like "does this actually make sense with a screen reader"), so also do a 5-minute manual pass: unplug your mouse and try to Tab through the page's main interactive elements.

**Deliver** `homework-04-a11y-check.md`: the tool's top 3 flagged issues, plus your own manual finding (something the automated tool didn't catch), each with a WCAG POUR category and a rough severity guess.

---

## Problem 5 — Write a trade-off negotiation script (45 min)

Using the four-input framework (impact, cost, risk, reversibility) from Lecture 3, write a short negotiation script — the kind you'd actually say out loud — for a real or invented scenario where you're asking an engineering lead to prioritize a UX fix over a scheduled feature. Follow the structure from Lecture 3's example script: claim (grounded in evidence), cost estimate, proposed decision, and an explicit fallback.

**Deliver** `homework-05-negotiation-script.md`, plus 2–3 sentences on what you'd expect the engineering lead's strongest counter-argument to be, and how you'd respond to it.

---

## Time budget

| Problem | Time |
|--------:|-----:|
| 1 | 60 min |
| 2 | 90 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 45 min |
| **Total** | **~5 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
