# Exercise 1 — Design a Three-Tier Pricing Table

**Goal:** Apply Lecture 1's Good/Better/Best packaging framework to design your **own** three-tier pricing structure for Loopline — before you see the canonical tier set used in Exercise 3 and Lecture 3's modeling. There is no single right answer here; the point is a defensible, value-metric-gated design you can argue for.

**Estimated time:** 60–90 minutes.

## Context you have

Loopline currently charges every account **$12/seat/month**, flat, no tiers, no free plan. From this week's and prior weeks' material, you know:

- **Shipped features** as of today: core task management, recurring tasks, custom fields, dark mode, bulk task reassignment, stuck-alert digest mode, configurable stuck thresholds, task templates, advanced search/filters, **guest & external collaborator access**, and **audit log for compliance** (the last two shipped together, per Week 5's dependency chain).
- **Not yet shipped** (later backlog items, still in progress): mobile push notifications, a paid time-tracking add-on, a public API/webhooks, AI task summaries.
- **Customer segments** (from the `subscriptions` data you'll see in full in Exercise 3): early-stage startups (2–6 seats), agencies (6–18 seats), mid-size software teams (17–40 seats), and enterprise accounts (45–200 seats, several with negotiated discounts).
- **Two real churn reasons already on file:** a 3-seat startup churned citing cost ("too high for pre-seed team"), and a 45-seat enterprise account churned because Loopline had no SSO/SAML or audit log *at the time* — those features didn't exist yet.

## Your task

Design **three tiers** — name them whatever you want (Starter/Team/Business, or your own names) — and produce a `pricing-design.md` with:

1. **A pricing table** — one column per tier, with at minimum: price per seat per month, any seat cap or minimum, and 4–6 features/capabilities gated into that tier (not a copy of the full feature list — pick the ones that actually differentiate the tiers).
2. **A one-paragraph justification per tier** naming the **value metric** each tier gates on (Lecture 1, Section 2) and which segment(s) you expect to land there. "It felt about right" is not a justification — name the evidence (a segment's typical seat count, a specific shipped feature they'd need, a churn reason you're addressing).
3. **An anchoring statement** — one paragraph explaining which tier you expect most existing accounts to land in, and how the existence of your top tier makes that middle tier look reasonable by comparison (Lecture 1, Section 3).
4. **A migration plan for the two churned accounts** — in one sentence each, would your new tiers have kept Silverpine AI (cost-sensitive startup) and Vantage Manufacturing (needed SSO/audit log) as customers? If not, say what would have to change for them to fit.

## Constraints

- **At least one tier must be cheaper than the current $12/seat flat rate.** Somewhere in Loopline's base, a segment is being overcharged relative to what they need — find it and price for it.
- **At least one tier must gate on the SSO/audit-log capability specifically** — that's the clearest value-metric gate available in Loopline's current shipped feature set (Lecture 1, Section 2's compliance-gate discussion), and ignoring it in your design is a missed opportunity the exercise expects you to catch.
- **No more than 3 tiers, no fewer than 3.** Two collapses the anchoring effect; four or more usually signals you're packaging by internal team instead of by customer segment (Lecture 1, Section 2).

## Stretch — run a mini Van Westendorp

Pick your **middle** tier. Write down four fictional-but-plausible answers (from four different imagined customers, one per segment) to the Van Westendorp four questions from Lecture 1, Section 4:

1. "So cheap you'd question quality" price
2. "Bargain" price
3. "Getting expensive, but you'd still consider it" price
4. "Too expensive, you would not consider it" price

You don't need real respondents or a formal plotted curve for this drill — just four rows of four numbers each, followed by two sentences: does your chosen middle-tier price sit inside the range most of your four imagined respondents implied was acceptable? If it doesn't, say whether you'd move the price or accept that this tier isn't meant for that respondent's segment.

## Expected outcome (self-check)

- Your three tiers should **not** all be roughly the same price — if your cheapest and most expensive tier are within $3/seat of each other, the anchoring effect (Lecture 1, Section 3) has no room to work, and you should widen the spread.
- You should be able to point to at least one **real row of evidence** (a segment's seat range, a specific churned account's reason) behind every price point — not four abstract numbers with no connection to Loopline's actual customers.
- If your top tier doesn't mention SSO or audit log by name, re-read Lecture 1 Section 2's packaging-gate discussion before finalizing.

## Done when…

- [ ] `pricing-design.md` has all three tiers, each with a price, a value-metric gate, and a named justification.
- [ ] The anchoring paragraph explains why the top tier's existence helps sell the middle tier.
- [ ] Both churned accounts (Silverpine AI, Vantage Manufacturing) are addressed by name.
- [ ] (Stretch) Four Van Westendorp rows plus your two-sentence read on your middle tier's price.

## Submission

Commit `pricing-design.md` to your portfolio under `c44-week-10/exercise-01/`.
