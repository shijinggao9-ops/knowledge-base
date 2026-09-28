# Mini-Project — A Full Go-to-Market and Launch Plan

> Write the complete go-to-market and launch plan for a v1 feature: positioning, launch tiers and channels, a cross-functional checklist, a phased GA schedule, and SQL-instrumented success metrics with rollback criteria. This is the week's capstone — everything from Exercises 1–3 and both challenges feeds directly into it.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

A launch plan that only exists in someone's head is not a launch plan — it's a hope. Your job this week, twenty times smaller than a real launch but structurally identical, is to produce the single document a cross-functional team could actually execute against: who this is for, how we're telling them, in what order, checked against what data, with a plan for when it goes wrong.

---

## Choose your feature

Pick **one** of the following. Whichever you choose, you'll build the plan from a blank page — this is not a rehash of an exercise or challenge answer, though you should absolutely reuse work you're proud of from Exercises 1–3.

**Option A — Guest & External Collaborator Access, done properly.** Take everything scattered across Exercises 1–3 and Challenge 2 this week and assemble it into one coherent, standalone plan — as if you were handing it to a new PM joining the team who has never seen any of this week's work. This option is about **synthesis**: pulling positioning, checklist, SQL dashboard, and incident learnings into a single, well-organized document.

**Option B — A different Week 5 backlog item.** Pick any other item from [Week 5's backlog](../../week-05-prioritization-and-roadmapping/README.md) (recurring tasks, mobile push notifications, custom fields, audit log, dark mode, etc.) and build its launch plan from scratch, including your own seed-data-style success metrics design (you don't need to write full seed SQL — describe the tables/columns you'd track and write the queries you'd run against them, as if the data existed).

Most students should pick **Option A** — it's the deeper synthesis exercise and directly usable as a portfolio piece. Pick Option B if you want the extra stretch of designing the instrumentation from nothing.

---

## Deliverable

A directory in your portfolio `c44-week-09/mini-project/` containing:

1. `positioning-and-messaging.md` — final positioning statement(s) and the feature-benefit-proof table.
2. `launch-plan.md` — tier justification, channel plan per tier, and the cross-functional checklist with owners and gates.
3. `success-metrics.sql` (Option A) or `success-metrics-design.md` (Option B) — the queries (or the described schema + queries) that define and monitor launch success, including explicit rollback/kill criteria.
4. `rollout-schedule.md` — the phase-by-phase rollout plan: who's in each wave, roughly when, and the go/no-go criteria between waves.
5. `retro.md` — a short reflection (see the end).

---

## Requirements

Your plan must include all of the following, wherever they land across the five files:

### Positioning & messaging
- At least **two** positioning statements for two genuinely different segments, using the Lecture 1 template.
- A feature-benefit-proof table with at least 5 rows, benefits stated as customer outcomes, proof points that are checkable facts.
- One sentence naming which claim you're deliberately **not** making, and why (borrow the discipline from Challenge 1's Section 3, even if your feature isn't AI-based — every feature has a claim that's tempting to overstate).

### Launch tiers & channels
- A risk assessment against all four Lecture 2 questions (blast radius, reversibility, support cost, brand exposure), with a tier sequence that's actually justified by that assessment, not assumed.
- A channel plan **per tier**, not one generic list — show how the channel mix grows or narrows as the tier's audience changes.

### Cross-functional checklist
- At least 6 functional categories (Product, Engineering, Marketing, Sales, Support, Legal/Security), 2+ items each, each with an owner role and a tier gate.
- A "known risks we're accepting" section naming at least 2 risks you decided not to gate the launch on.

### SQL-instrumented success metrics
- An activation-funnel query (or design) and a rollback-trigger query (or design), each with the specific numeric threshold that would pause or stop the rollout.
- At least one **leading** indicator and one **lagging** indicator, explicitly labeled as which is which and why you'd react differently to each.

### Phased rollout schedule
- A named sequence of waves (who's in each, roughly how large, roughly how much soak time between them) with go/no-go criteria at each boundary.
- If you're on Option A, this should reflect what actually happened in the seed data (beta → `ga_25` → `ga_100`) but written as a *forward-looking plan document*, not a retelling of the incident.

---

## Milestones

Pace yourself; don't try to do all five files in one sitting.

- **Milestone 1 (45 min):** `positioning-and-messaging.md` — this is the foundation everything else's language builds on.
- **Milestone 2 (45 min):** `launch-plan.md` — tiers, channels, and the checklist.
- **Milestone 3 (45 min):** `success-metrics.sql` / `success-metrics-design.md` — the data side.
- **Milestone 4 (30 min):** `rollout-schedule.md` — tie the tiers to an actual sequence with go/no-go gates.
- **Milestone 5 (15 min):** `retro.md`.

---

## Rules

- **No spreadsheets as the system of record.** Your success-metrics file is SQL (or a described schema + SQL, for Option B) — not a spreadsheet formula chain. A spreadsheet may be a fine *presentation* of a dashboard's output to an exec; it is never where this week's data should live.
- **Every claim in your positioning needs a defensible "unlike."** No positioning statement without a real, named alternative.
- **Every rollback criterion needs a number.** "Monitor closely" is not a criterion.
- **State your assumptions.** Judgment calls (tier boundaries, soak times, who gets notified in an incident) get one written sentence of justification each.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Positioning quality | 20% | Two genuinely distinct, defensible statements; category and alternative choices reveal real thought |
| Launch tier & channel logic | 20% | Tier sequence follows from the stated risk assessment, not assumed; channels scale with tier audience |
| Checklist completeness | 15% | 6+ categories, named owners, explicit tier gates, honest "risks accepted" section |
| SQL/data rigor | 25% | Queries (or query designs) are correct, numeric thresholds are specific and defensible |
| Rollout sequencing | 10% | Waves and go/no-go gates are concrete, not just "beta then GA" with no detail |
| Stated assumptions | 10% | Every judgment call is named and justified in one sentence |

---

## Reflection (`retro.md`, ~200 words)

1. Which part of the plan forced you to make the hardest judgment call, and what did you decide?
2. If you picked Option A: having now assembled the whole thing, what would you change about the *order* you did this week's exercises in, if you were doing it again?
3. If you picked Option B: what was the biggest difference between planning a launch for a feature with existing seed data (Guest Access) versus designing the instrumentation from a blank page?
4. Name one thing in your plan you're **least** confident about, and what would make you more confident (a specific piece of data, a specific stakeholder conversation, a specific test).

---

## Why this matters

Every real launch you'll ever run has this same shape: a positioning decision, a risk-sized tier plan, a checklist real people can execute, and a way to know — with data — whether it's working or hurting someone. Most PMs learn this by getting burned once. This mini-project is the rehearsal. Keep it; the shape of this document barely changes between a 24-org feature launch and a 24-million-user one — only the numbers get bigger.

When done: push, then take the [quiz](../quiz.md) and start [Week 10 — Pricing & growth](../../week-10-pricing-and-growth/).
