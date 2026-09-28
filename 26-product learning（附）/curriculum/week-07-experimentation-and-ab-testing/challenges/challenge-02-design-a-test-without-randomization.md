# Challenge 2 — Design a Test Where You Cannot Randomize

**Time:** ~90 minutes. **Difficulty:** Hard. **No single right answer.**

## The scenario

Loopline's pricing team wants to move from **monthly-only pricing display** to **annual-first pricing display** on the public pricing page — showing the annual price prominently (with monthly as a smaller toggle) instead of the current monthly-first layout, on the theory that anchoring visitors to the annual price will increase the share of new signups who choose an annual plan.

Loopline's legal and marketing teams both object to a standard randomized A/B test on this page:

- **Legal:** Loopline is a B2B SaaS company, and enterprise prospects sometimes compare notes — a sales rep in a call with one prospect referencing "the price on our pricing page" while another prospect on the same page saw a different layout is a real risk of appearing inconsistent or, worse, of looking like price discrimination in some jurisdictions. Legal has vetoed showing different visitors different pricing layouts at the same time.
- **Marketing:** the pricing page is a significant source of organic search traffic and has been carefully SEO-optimized; marketing is wary of any change that could affect how search engines and cached previews (Slack unfurls, social shares) render the page inconsistently, which argues against splitting traffic to two live URL variants.
- **Sales:** enterprise deals mostly don't come through the self-serve pricing page at all — an account executive negotiates those individually — so even if you could test the page, it wouldn't touch Loopline's biggest revenue segment.

You cannot run a standard randomized page-variant A/B test here. Your job is to design the most rigorous alternative you can.

## Your task

Write `challenge-02.md` covering all five parts below.

### Part 1 — Restate the hypothesis and metric

Using Lecture 1's if/then/because template, write the hypothesis this test is actually trying to evaluate. Name the primary metric precisely (be specific: "annual-plan mix" needs a precise definition — annual plans as a % of *what* denominator, over *what* time window, counted at signup or at first payment?).

### Part 2 — Rule out what you can't use, and say why

For each of the three quasi-experimental designs from Lecture 3 §4 (holdout, switchback, diff-in-diff/before-after), state whether it's usable here given the legal/marketing/sales constraints above, and why or why not. At least one of the three should turn out to be genuinely unusable given a specific constraint above — name which constraint kills it.

### Part 3 — Design the design you'd actually run

Pick the strongest option from Part 2 (or a combination) and specify it concretely:

- If **switchback**: what's the time unit (day? week?) and why? How many periods do you need, and how do you handle the fact that pricing-page traffic and conversion behavior likely differ by day-of-week and by calendar effects (e.g., end-of-quarter budget cycles for B2B buyers)? What would contaminate a switchback here — could a prospect who saw the annual-first layout on a Monday come back and convert on a Tuesday when it's flipped back, and how would you count that?
- If **diff-in-diff**: what's your comparison group? (Options to consider: a market/region Loopline isn't launching the change in yet, a different but similar SaaS pricing benchmark, Loopline's own trend from a prior comparable period.) What's your "parallel trends" argument — why should we believe the comparison group would have moved the same way as the treated group absent the change? How would you check this assumption using data from *before* the change, and what would make you distrust your own comparison group?
- Either way: what's your primary metric's exact SQL definition, and what guardrail(s) would you track (hint: think about what could look like a win in annual-mix but actually be a loss — e.g., total signups dropping because the annual-first price looks scarier at first glance even though the *mix* of who signs up shifts toward annual).

### Part 4 — Name the weaknesses honestly

Every quasi-experimental design is weaker evidence than true randomization. Write 3–4 sentences on the specific way your chosen design could mislead you — what confound could produce a result that *looks* like the pricing change worked, when really something else happened at the same time?

### Part 5 — Decision threshold

Because this design gives weaker evidence than a randomized test, would you set a *higher* bar before recommending a permanent rollout than you would for a normal A/B win (e.g., requiring the effect to hold across multiple periods/markets, or requiring convergence with a qualitative signal like sales team feedback)? State your bar explicitly.

## Constraints

- You may not propose a workaround that violates the stated legal constraint (no showing different prices/layouts to different visitors at the same time on the live public page). A clever-sounding trick that quietly does this anyway ("just cookie them so each *visitor* only sees one version consistently" is fine and is not a violation — you're welcome to use standard sticky-bucketing logic *within* whichever time-based or geography-based design you pick; what's off the table is a classic 50/50 concurrent live split of the one shared page).
- Your chosen design must produce a **falsifiable** prediction, per Lecture 1 §1 — "we'll know more when we look at the data" is not a design.
- State at least one number: a rough required number of periods (switchback) or a rough required duration (diff-in-diff), even if you have to state the assumptions behind the estimate explicitly, since you won't have a clean sample-size formula the way you did in Lecture 2.

## Hints

<details>
<summary>On why switchback is attractive here</summary>

Switchback keeps the "one live page, one version at a time" property legal needs, while still getting closer to a controlled comparison than a raw before/after — each period (with its own baseline traffic mix, marketing pushes, etc.) gets both conditions across the whole test, spreading out calendar confounds rather than pinning them entirely to a single before-period and a single after-period. The real design work is in period length: pricing decisions for B2B buyers often unfold over days or weeks (not single sessions), so switching daily risks measuring different visitors in different periods without capturing the actual decision-influencing exposure — a strong answer grapples with this rather than picking a period length arbitrarily.

</details>

<details>
<summary>On a comparison group for diff-in-diff</summary>

Loopline's own historical trend, split by whether a market/segment received the change or not, is usually a *stronger* comparison group than an external SaaS benchmark, because it shares your product, your sales motion, and your existing customer mix — an external company's pricing-page conversion trend could differ from yours for a dozen unrelated reasons. A strong answer explains this trade-off rather than reaching for the first available comparison.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Hypothesis precision | Vague ("annual plans will go up") | Falsifiable, with an exact metric definition |
| Constraint reasoning | Ignores or hand-waves the legal/marketing/sales limits | Explicitly ties each design choice back to a named constraint |
| Design specificity | "We'll do a diff-in-diff" with no detail | Names the actual comparison group, period length, and why |
| Honesty about weakness | Presents the quasi-experiment as equivalent to an A/B test | Names the specific confound that could fool this exact design |
| Decision threshold | No stated bar, or "if it looks good we ship it" | An explicit, higher bar than a standard A/B win, and why |

## Submission

Commit `challenge-02.md` to your portfolio under `c44-week-07/challenge-02/`.
