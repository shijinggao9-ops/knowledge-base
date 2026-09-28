# Challenge 1 — Design the Capstone Experiment Plan

**Goal:** Pick one real bet from your own roadmap and design an experiment for it — with an honest sample-size estimate, real guardrail metrics, and a decision rule written down before any data exists — the way Week 7 taught, applied to something you specced yourself instead of a planted scenario.

**Estimated time:** 90 minutes.

## The scenario

You don't need a planted scenario this time — you have a real one. Open your `roadmap.md` from Exercise 2. Somewhere in your Now or Next bucket is an item where you genuinely don't know, in advance, whether your proposed solution will actually move your PRD's success metric. That's your experiment candidate. (If every item in your roadmap feels certain to work, you scoped your MVP too conservatively — go back and find the item you're least sure about, even if it's uncomfortable to admit uncertainty about your own plan.)

## Tasks

Write your answers in `c44-week-12/challenge-01/experiment-plan.md`.

1. **Name the bet as a testable hypothesis**, in the form: *We believe [change] will cause [metric] to move by [direction/magnitude], because [reasoning tied to your discovery brief or PRD].* Vague hypotheses ("we believe this will help") fail this task — you must commit to a direction and, ideally, a rough magnitude.

2. **Choose the experiment design** — A/B test (if you'd have enough simultaneous users to randomize) or a pre/post comparison with a stated confound-mitigation plan (if you wouldn't). Justify the choice in 2–3 sentences using Week 7's criteria: does your product have enough concurrent users for a real control group, or would splitting traffic starve both arms of a meaningful sample?

3. **Estimate a realistic sample size.** Using Week 7's power-analysis approach (baseline conversion rate estimate, minimum detectable effect, standard significance/power thresholds), estimate how many users or sessions you'd need per arm. State your assumed baseline rate and minimum detectable effect explicitly — an estimate with invisible assumptions can't be checked or trusted by a reader.

4. **Name your guardrail metrics** — at least 2 metrics that must NOT get meaningfully worse even if your primary metric improves (e.g., a change that boosts activation but tanks a different retention metric is not a clean win). Guardrails should come from your PRD or dashboard, not be invented for this task alone.

5. **Write the decision rule, pre-registered** — the exact statement of what result leads to ship, what result leads to kill, and what result is genuinely ambiguous and needs a follow-up decision (not "we'll see how it goes"). This must be written as if you do not yet know the result.

6. **Name the wrinkle.** Every real experiment plan has at least one complicating factor working against a clean read. Pick the one most relevant to your situation and address it directly: a very small user base (can you even reach your sample size in a reasonable window?), a novelty effect (would users try something new regardless of real value, the way this week's AI Task Summaries dataset showed strong day-0 activation that didn't hold?), a network/social effect (does one user's behavior affect another's, breaking independence assumptions), or a seasonality risk (is your observation window unusually representative or unrepresentative). State the wrinkle and what you'd do about it — ignoring it, or don't design an experiment for it, are both real options; state which and why.

## Expected outcome

An experiment plan specific enough that a real engineer could implement it and a real analyst could grade the result against your own pre-registered decision rule, without needing to ask you what you meant.

## Done when…

- [ ] The hypothesis names a direction and (at least roughly) a magnitude, not just "will help."
- [ ] The A/B vs. pre/post choice is justified against your own product's realistic user volume, not asserted without reasoning.
- [ ] The sample-size estimate states its baseline rate and minimum detectable effect assumptions explicitly.
- [ ] At least 2 real guardrail metrics are named, sourced from your PRD or dashboard.
- [ ] The decision rule is written in pre-registered form — as if the result is still unknown — with a ship condition, a kill condition, and an ambiguous-result condition.
- [ ] The wrinkle section names a real, relevant complicating factor for *your specific* product, not a generic caveat that could apply to any experiment.

## Stretch

If your sample-size estimate reveals you couldn't realistically reach significance in a sane observation window (a common, honest outcome for an early-stage zero-to-one product with few users) — don't hide it. Write a second paragraph proposing what you'd do instead: a qualitative alternative (structured user interviews with a decision rule of their own), a longer observation window with a stated cost, or a proxy metric with a faster signal and an honest note on what it can't tell you. This is a realistic and valuable finding, not a failure of the exercise.

## Submission

Commit `experiment-plan.md` to your portfolio under `c44-week-12/challenge-01/`.
