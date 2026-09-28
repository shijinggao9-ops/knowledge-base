# Challenge 2 — Cost-Cap an AI Feature Without Breaking It

**Time:** ~90 minutes. **Difficulty:** Medium–Hard. **No single right answer.**

## The scenario

Loopline Copilot launches. It goes well — a well-known productivity newsletter features it in a "5 AI features actually worth using" roundup, and Loopline gets a real traffic spike: workspace signups and Copilot usage both jump hard for about 72 hours before settling to a new, higher baseline (genuine growth, not a fluke). The eval work from Lecture 2 and the guardrails from Lecture 3 are already in place — quality and safety aren't the problem. The problem lands on your desk from Finance: *"AI spend this month is 6x what we modeled. Is this a bug, or is this just... success? And either way, what do we do about it before next month?"*

This is the tension every cost guardrail eventually has to resolve: a cap that's too tight throttles a feature at the exact moment it's proving its value; a cap that's too loose (or nonexistent) means a genuine growth spike and a runaway retry bug look financially identical until someone investigates. You have to design a response that works for **both** possibilities without waiting to find out which one it is first.

## Your task

Write `challenge-02.md` covering all four parts:

### Part 1 — Model the spike (using SQL/pandas reasoning, not a spreadsheet)

Using the `ai_usage_log` schema and pricing intuition from [Lecture 3](../lecture-notes/03-guardrails-cost-and-safety.md), estimate: if daily Copilot call volume went from a modeled baseline of ~30 calls/day (roughly the seed data's week) to 6x that sustained for 30 days, what's the rough monthly cost multiple versus the original budget? Show your arithmetic — this doesn't require a live database, but it does require actual numbers, not "a lot more."

### Part 2 — Diagnose before you throttle

Propose a **specific SQL query** (write the real SQL, don't just describe it in prose) you'd run against `ai_usage_log` first, before touching any limit, to distinguish "genuine broad-based growth" from "a few workspaces spamming the endpoint" (the pattern Exercise 3 found in workspace 41). What does the query look at, and what result would point to each explanation?

### Part 3 — Design a response that doesn't just throttle everyone

A flat "cut everyone's rate limit by 80%" response punishes the genuine growth you were hoping for. Propose a **tiered response** instead — at minimum, address:

- What happens for workspaces whose usage pattern looks like organic growth (real users, varied call times, high `accepted`/`edited` outcome rates)?
- What happens for workspaces whose usage pattern looks like the workspace-41 anomaly (concentrated bursts, high `error` rate, one user)?
- Is there a **model-tier lever** here — could you route some or all traffic to a cheaper tier during the spike without breaking the eval pass rate from Lecture 2, and how would you know if you'd broken it?
- What's the **user-visible experience** for anyone who does get rate-limited — silent failure, a clear message, a graceful degrade to the fallback from Exercise 1? A cap with a bad failure UX creates a support-ticket problem to replace the cost problem you just solved.

### Part 4 — Decide what you tell Finance

Write the two-to-three sentence answer you'd actually give Finance, given everything above: is this a bug or success, what did you do about it this week, and what's the plan if the new higher baseline is real and permanent (hint: a modeling problem from Week 10 is hiding in here — a genuinely higher sustained baseline isn't a "cap it" problem, it's a "the budget model was wrong" problem).

## Constraints

- Part 2's query must be real, runnable SQL against the `ai_usage_log` schema from Lecture 3 — not a description of what a query "would" do.
- Part 3's tiered response must name at least two distinct workspace-usage patterns and a different action for each — a single blanket action for all workspaces doesn't count as tiered.
- Don't reach for "just ask Engineering to add more budget" as your answer to Part 4 without first showing, from Parts 1–3, that you've ruled out (or fixed) the abuse/bug explanation. Asking for more budget is a legitimate answer *only after* that diagnostic work.

## Hints

<details>
<summary>On Part 1's arithmetic</summary>

You don't need exact current provider pricing — use the illustrative per-call cost from Lecture 3's seed data (roughly $0.007–$0.01 per successful call) as your baseline, and reason proportionally. The point of this part isn't precision, it's the habit of actually running the multiplication before reacting, instead of pattern-matching "6x calls" to "we're doomed" or "it's fine" without checking.

</details>

<details>
<summary>On Part 3's model-tier lever</summary>

Routing to a cheaper model tier during a spike is a real, common move — but Lecture 2 gave you the tool to check whether it's safe: rerun (or reason about rerunning) the golden eval set against the cheaper tier before routing real traffic to it. A cost fix that quietly breaks the `adversarial` category's pass rate from Lecture 2's `v2` run is not actually a fix — it's trading a cost incident for a safety incident nobody's watching for yet.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Quantification | "Costs will go up a lot" | Real arithmetic showing the actual multiple, with stated assumptions |
| Diagnosis | Jumps straight to a fix | A real, runnable SQL query that would actually distinguish growth from abuse |
| Tiered response | One blanket action for everyone | Named, different actions for at least two distinct usage patterns |
| Guardrail interaction | Ignores Lecture 2's eval work | Explicitly checks whether a cost fix (e.g., cheaper tier) risks a quality/safety regression |
| Communication | Vague reassurance to Finance | A tight, evidence-backed answer that names what was done and what's still open |

## Submission

Commit `challenge-02.md` to your portfolio under `c44-week-11/challenge-02/`.
