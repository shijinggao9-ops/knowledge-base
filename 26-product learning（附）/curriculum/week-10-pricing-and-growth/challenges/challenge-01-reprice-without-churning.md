# Challenge 1 — Reprice a Product Without Mass Churn

**Time:** ~90 minutes. **Difficulty:** Medium–Hard. **No single right answer.**

## The scenario

Exercise 3's risk-adjusted model showed a real problem: migrating every account straight to the new Starter/Team/Business tiers produces an expected **+12.9%** MRR lift — solid, but it comes with real churn risk concentrated almost entirely in the 5 Enterprise accounts facing a 50% list-price jump. Loopline's CEO likes the +37.3% naive number (of course she does) and wants to "just flip the switch on the new prices next month." You are the PM who has to turn "just flip the switch" into a rollout that doesn't blow up Loopline's biggest, most concentrated revenue segment — remember, 5 Enterprise accounts carry 62% of total MRR (Lecture 3, Section 2). Losing even one of them to a repricing shock would be a worse outcome than the entire naive projection's upside.

This is one of the most common real situations in B2B SaaS: the pricing math is sound, but the **rollout mechanics** are where deals (and trust) get lost.

## Your task

Write `challenge-01.md` covering all of the following:

1. **Pick a rollout mechanism** and defend it against at least one alternative. Consider (you don't have to use these exact options, but address the trade-off space):
   - **Grandfathering** existing accounts at their current price indefinitely (new tiers apply only to new signups).
   - **Grandfathering with an expiration** — existing accounts keep the old price for N months/at their next renewal, then migrate.
   - **Phased/staggered rollout** — migrate the lowest-risk segment first (per Exercise 3's risk table), watch actual churn for a full billing cycle, then proceed to higher-risk segments only if the low-risk migration held.
   - **Price increase caps** — cap any single account's year-over-year increase at some percentage (e.g., no account's bill rises more than 20% in one cycle), even if their "correct" new tier price implies more, with the rest phased in over subsequent renewals.
   - Immediate, all-at-once migration (the CEO's instinct) — and a specific, numbers-based argument for why you would or wouldn't recommend it.

2. **Apply your mechanism to the 5 real Enterprise accounts** from the `subscriptions` table (Rosemont Enterprises, Stonebridge Financial, Thackeray Holdings, Underwood Insurance, Wickford Global). For each, state: what they pay in month 1 of your rollout, and what they pay once fully migrated, under your plan.

3. **Recompute the risk-adjusted revenue** for your rollout's **first 3 months**, using Exercise 3's churn-risk brackets (or your Task 6 revision from Exercise 3, if you changed them) applied to whatever price change each account actually experiences in month 1 under your plan — not the full jump to the final tier price, if your plan phases it.

4. **Communicate the change.** Draft the actual email (150–250 words) Loopline would send to an Enterprise account like Stonebridge Financial (140 seats, currently $12/seat with a 20% negotiated discount) announcing the change. It must state the new price, the timeline, and **something a real customer would read as a genuine value justification**, not just a price-increase notice — tie it to what actually shipped (SSO, audit log) per Lecture 1's framing of the compliance gate as a real value-metric, not an excuse.

5. **Name your failure mode.** In two sentences: what specifically would tell you, within the first 3 months, that your rollout plan is failing worse than the risk model predicted — and what would you do the moment you saw that signal?

## Constraints

- Your plan must result in a **lower** month-1 risk-adjusted revenue impact than the naive all-at-once approach — if it doesn't, you haven't actually mitigated anything, you've just relabeled it.
- The customer email (Task 4) must not use the words "we're excited" or "we've listened to your feedback" unless you can point to a specific piece of Enterprise-segment feedback it's responding to — vague enthusiasm is not a value justification.
- You must address **all 5** Enterprise accounts by name in Task 2, even if your plan treats them identically — don't skip the exercise of applying the mechanism concretely.

## Hints

<details>
<summary>On choosing a rollout mechanism</summary>

There's rarely one "correct" mechanism — the strongest submissions usually combine two (e.g., grandfather existing accounts through their current contract term, but cap the increase at renewal rather than jumping straight to list). What separates a strong answer from a weak one isn't which mechanism you pick, it's whether you can show, with the actual account data, that your choice measurably lowers the risk concentration Exercise 3 flagged.

</details>

<details>
<summary>On the customer email</summary>

A repricing email that leads with the price change reads as an attack. A repricing email that leads with what the customer is now getting that they weren't getting before (SSO, audit log — capabilities that likely mattered enough to a security-conscious Enterprise buyer that their internal review process asked for them) reframes the same price change as an upgrade the customer already wanted. Same facts, very different reception — this is packaging communication, not spin.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Mechanism defense | Picks an approach with no comparison to alternatives | Names at least one alternative and a specific reason it's worse for Loopline's Enterprise concentration |
| Applied to real accounts | Talks about "Enterprise accounts" abstractly | Names all 5 accounts with month-1 and fully-migrated prices |
| Numbers | Vibes-based confidence that churn will be "fine" | A real risk-adjusted month-1 revenue figure computed against the actual price change under the plan |
| Communication | Generic price-increase email | Leads with value delivered, states the number plainly, no hollow enthusiasm |
| Honesty | No failure mode named | A specific, checkable early-warning signal and a stated response |

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-10/challenge-01/`.
