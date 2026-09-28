# Challenge 2 — Design a Metric Tree for a Real Product

**Time:** ~60–75 minutes. **Difficulty:** Medium. **No single right answer — the point is a defensible tree, not the "correct" one.**

## The scenario

Every product has exactly one team that has to answer "is this thing actually working?" with more than a shrug. This challenge puts you in that seat for a product you actually use — not Loopline this time. Pick something you have real opinions about: a note-taking app, a fitness tracker, a food delivery app, a streaming service, a B2B tool you use at work, a game. Anything with users doing repeated actions over time.

## Your task

Produce `metric-tree.md` containing:

1. **The product**, named, with one sentence on what it's for and who uses it.
2. **The North Star Metric**, stated as a precise count-or-rate-per-time-window (Lecture 1 §1–2 shows the exact phrasing pattern — "Weekly Engaged Users: distinct users who complete at least one task in a trailing 7-day window" is the template to match, not to copy).
3. **Three rejected alternatives** — plausible NSM candidates you considered and did *not* pick, with one sentence each on why they lost. At least one rejected candidate must be a **vanity metric** (Lecture 1 §3) and at least one must be a metric you'd reject specifically because it's **gameable** (Lecture 1 §4) — name the gaming behavior a team under pressure could pull off, and name the guardrail metric you'd pair with it if you were forced to keep it anyway.
4. **A full metric tree**, at least two levels deep, in the same nested-list shape as Lecture 1 §5's Loopline example. Every leaf node must be something you could plausibly query from an events table — no leaf may be a vague phrase like "better UX."
5. **One worked "why did the number move" scenario**: invent a plausible week where your NSM dropped 15%, and walk through your tree branch by branch, in the order you'd check them, explaining what each check would tell you.

## Constraints

- Your NSM must pass all three tests from Lecture 1 §1: it reflects customer value (not company convenience), it's a leading indicator (not pure revenue/churn), and it's a single trackable number, not a dashboard.
- Every branch in your tree must be phrased so a data engineer could turn it into a `WHERE event_name = '...'` clause without asking you what you meant. "Engagement" is not a branch; "sessions per week per retained user" is.
- Don't just copy Loopline's growth-accounting shape (New/Retained/Resurrected/Churned) node-for-node — that structure fits a task app well because its NSM is a weekly rate. If your product's NSM is a different shape (e.g. a completion rate, a per-transaction value, a content-consumption metric), your tree's top-level branches should reflect *that* metric's actual drivers, not Loopline's.

## Hints

<details>
<summary>If you're stuck picking a North Star</summary>

Ask: what is the single repeated action that, if a user stopped doing it, would mean the product had genuinely failed them — not "they're busy this week," but "this product no longer does its job for them"? For a fitness tracker, that's probably not "opened the app" (too weak) or "burned calories" (unmeasurable/ungameable in a useful way) — it's closer to "logged a workout" at some minimum weekly frequency. Notice this is the same reasoning Lecture 1 §2 walked through for Loopline; you're running the same process on a different product.

</details>

<details>
<summary>On avoiding a fake-precise tree</summary>

A common failure mode is a tree that *looks* rigorous (boxes, arrows, three levels) but whose leaf nodes are still unmeasurable ("user delight," "brand affinity"). Test every leaf with: "if I had this product's real event log in front of me right now, could I write the `SELECT` for this leaf in under two minutes?" If not, it's not a metric yet — decompose it further or replace it.

</details>

## How success is judged

| Signal | Weak submission | Strong submission |
|---|---|---|
| NSM choice | Picks a lagging or company-convenience metric (revenue, DAU alone) without testing it against the three criteria | Explicitly checks the NSM against all three tests from Lecture 1 §1 |
| Rejected alternatives | Lists alternatives with no reasoning | Explains *why* each lost, and correctly tags the vanity one and the gameable one (with its guardrail) |
| Tree structure | Two or three vague boxes | Two-plus levels deep, every leaf phrased as a queryable event-table condition |
| Worked scenario | Restates the tree without applying it | Walks the "NSM dropped 15%" scenario branch by branch, in a sensible investigation order |
| Judgment | Copies Loopline's tree shape wholesale | Adapts the tree's top-level shape to fit the chosen product's actual NSM |

## Submission

Commit `metric-tree.md` to your portfolio under `c44-week-06/challenge-02/`.
