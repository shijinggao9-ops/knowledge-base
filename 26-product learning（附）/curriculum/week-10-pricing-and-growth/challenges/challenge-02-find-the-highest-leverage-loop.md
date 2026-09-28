# Challenge 2 — Find the Highest-Leverage Growth Loop

**Time:** ~90 minutes. **Difficulty:** Medium. **No single right answer.**

## The scenario

Loopline's leadership team is looking at the `growth_channels` table from Lecture 2, Section 6, and the conversation has stalled into two camps. The VP of Marketing wants to double the Paid Search budget — "it's already bringing in the most signups, just give it more money." The Growth engineer who built the guest-invite instrumentation thinks that's a mistake — "the loop is free and it compounds, why are we still paying $38 a head." Both have a real point, and both are missing half the picture. You've been asked to settle it with a specific, numbers-backed recommendation for where the *next* dollar or engineering-hour of growth investment should go — not a vague "it depends," and not just picking whichever number is biggest.

## Your task

Write `challenge-02.md` covering all of the following:

1. **Compute a same-units comparison across all three channels** in `growth_channels`. At minimum, for each channel, derive: **activated users per month** (`monthly_new_signups × activation_rate`) and, where CAC is nonzero, **cost per *activated* user** (not cost per raw signup — a $38 signup that never activates is not worth $38 of value). Show your work as a small table in `challenge-02.md`.

2. **Estimate lifetime value (LTV) using this week's other dataset.** Using the blended ARPU from the `subscriptions` table (Lecture 3, Section 2: **$10.31/seat/month**) and a stated assumption about average customer lifetime in months (pick a number — 18, 24, 36 — and say why), compute a rough LTV per activated user. Then compute **LTV:CAC** for Paid Search specifically (the only channel with a nonzero CAC). State explicitly: is this ratio healthy, marginal, or bad? (A commonly cited SaaS rule of thumb is LTV:CAC ≥ 3:1 — you don't have to accept that rule uncritically, but engage with it.)

3. **Model each loop's 6-month trajectory**, not just its current monthly snapshot. For the two loop-type channels (Guest Invite, Public Shared-Board SEO), use the `k_factor` and `cycle_time_days` columns to reason — in prose, a rough table, or a small script, your choice — about how each one's monthly contribution changes over 6 months if left alone (no new investment), versus how Paid Search's monthly contribution changes over 6 months if its budget stays flat. Which channel's *shape* over time — not just its current size — makes it the better investment target?

4. **Make the call.** Write a one-paragraph recommendation, addressed to both the VP of Marketing and the Growth engineer, stating which channel gets the next investment (money, engineering time, or both — be specific about which resource), and — critically — **what you'd do with the other two channels** (kill, maintain flat, or invest a smaller amount, and why).

5. **Name the missing data.** In two sentences: what real data does Loopline *not* have in this table that would most change your recommendation if it existed — and how would you go get it in the next two weeks?

## Constraints

- You must engage with **all three** channels — a recommendation that only discusses the channel you picked and ignores the other two is not a comparison, it's a preference.
- Your LTV:CAC calculation must show its inputs (ARPU, assumed lifetime, resulting LTV) explicitly — a bare ratio with no visible math is not acceptable here.
- If your final recommendation is "invest in Paid Search," you must directly address why the VP of Marketing's instinct (biggest raw number) is not, by itself, sufficient reasoning — even if you land on the same channel they'd pick, your reasoning needs to be sturdier than theirs.

## Hints

<details>
<summary>On "cost per activated user" versus "cost per signup"</summary>

CAC is almost always quoted as cost-per-signup because it's the easier number to report, but a signup that never activates has delivered approximately zero product value and, per Lecture 3's North Star discussion, doesn't move Weekly Active Teams at all. Recomputing CAC against activated users (not raw signups) is a small change in the formula that can meaningfully change which channel looks efficient.

</details>

<details>
<summary>On the 6-month trajectory</summary>

This is the crux of the whole challenge. A channel that looks smaller today but compounds will eventually outpace one that looks bigger today but is flat — the entire "loops are the new funnels" argument from Andrew Chen's essay (Lecture 2's further reading) is about exactly this crossover point. You don't need a precise month-by-month spreadsheet-grade model here (that's Lecture 3's pandas exercise, applied differently) — a clear, reasoned description of the shape of each curve is enough, as long as it's grounded in the actual `k_factor` and `cycle_time_days` values, not just asserted.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Same-units comparison | Compares raw `monthly_new_signups` across channels | Compares activated users and cost-per-activated-user, showing the arithmetic |
| LTV:CAC | Cites the 3:1 rule with no computed ratio | Shows ARPU × assumed lifetime = LTV, then LTV:CAC, with the assumption stated |
| Trajectory reasoning | Treats all three channels' current monthly numbers as static | Reasons about compounding vs. flat, grounded in `k_factor`/`cycle_time_days` |
| The call | Picks a channel with no resource specificity | Names the resource (budget/engineering time), the amount or direction, and what happens to the other two channels |
| Honesty | No missing-data gap named | Names one specific, gettable-in-two-weeks piece of missing data |

## Submission

Commit `challenge-02.md` to your portfolio under `c44-week-10/challenge-02/`.
