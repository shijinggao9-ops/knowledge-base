# Week 10 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of writing, structured judgment, and two small SQL/pandas problem sets. Commit each.

---

## Problem 1 — Classify five real pricing pages (60 min)

Pick five real SaaS products you can look up (pricing pages are public — no signup needed to view them). For each, in `pricing-page-audit.md`:

1. Name the primary pricing model (flat subscription, usage-based, freemium, seat-based, or a named blend) — cite the specific evidence from the page (a per-seat price, a usage meter, a free tier's limits).
2. Count the tiers and name what each one appears to gate on (a value metric, or — if you can't tell — say so; not every real pricing page gates cleanly, and noticing that is itself the skill).
3. Identify one clear anchoring choice on the page (a highlighted "Most Popular" tier, an annual-vs-monthly toggle, a top tier that exists mostly to make the middle tier look reasonable).

Include at least one product each from: a developer/infrastructure tool (likely usage-based), a team collaboration tool (likely seat-based), and a consumer-facing tool with a free tier (likely freemium).

**Deliver** `pricing-page-audit.md`.

---

## Problem 2 — Loop or funnel? Ten growth mechanisms, classified (45 min)

For each of the ten growth mechanisms below, classify it as a **loop** or a **funnel** (Lecture 2, Section 1), and write one sentence stating the specific evidence for your classification — what becomes the next cycle's input, or why nothing does.

1. A podcast ad campaign driving app downloads.
2. Instagram's "suggested accounts to follow," populated from who your existing follows follow.
3. A cold-outbound sales team calling a purchased list of leads.
4. Airbnb hosts inviting friends to become hosts, each new host listing more properties that attract more guests, some of whom become hosts themselves.
5. A conference booth handing out demo signups.
6. GitHub's public repository README badges linking back to the tool that generated them.
7. A billboard advertisement.
8. Duolingo's streak-and-leaderboard mechanic driving daily return visits (careful — is this acquisition or something else entirely?).
9. A SaaS tool's public API documentation, which developers link to from their own public GitHub repos, which search engines index.
10. An affiliate marketing program paying a commission per converted signup.

**Deliver** `loop-or-funnel.md` — 10 classifications, each with its one-sentence evidence.

---

## Problem 3 — Recompute the tier migration with a different rule (75 min)

Using the `subscriptions` table from Lecture 3, write a modified tier-assignment query where the Starter/Team cutoff is **15 seats instead of 10** (Business/Enterprise stays the same rule). In `alternate-tier-cutoff.sql`:

1. Write the modified `CASE` query and record the new tier assignment for every active account.
2. Compute the new naive total MRR under this cutoff and compare it to both the original $9,344.40 baseline and Lecture 3's original-cutoff naive total of $12,830.85.
3. In 3–4 sentences: which accounts moved tiers because of the cutoff change, and does raising the Starter cutoff to 15 seats make the pricing more defensible to a customer at the boundary, less defensible, or does it depend on which boundary account you ask? Name a specific account from the table in your answer.

**Deliver** `alternate-tier-cutoff.sql` plus your written answer at the bottom of the same file (as a SQL comment) or in a companion `alternate-tier-cutoff.md`.

---

## Problem 4 — Van Westendorp on your own subscription (45 min)

Think of a real subscription **you personally pay for** (streaming, software, a gym, anything recurring). Answer Lecture 1, Section 4's four Van Westendorp questions **honestly, about yourself**:

1. So cheap you'd question the quality?
2. A bargain — clearly worth it?
3. Getting expensive, but you'd still pay it?
4. Too expensive — you'd cancel?

Then in `my-van-westendorp.md`, answer: where does the price you *actually* pay today fall in your own range? Is it closer to your "bargain" number or your "too expensive" number — and does that match how you actually feel about the subscription day to day?

**Deliver** `my-van-westendorp.md`.

---

## Problem 5 — Extend the growth loop model (75 min)

Using `growth-model.py`'s structure from the mini-project (or Lecture 3, Section 5, if you haven't started the mini-project yet), extend the pandas projection to **18 months instead of 12**, and add a second scenario where `k` improves from 0.75 to 0.90 starting in month 7 (representing a hypothetical onboarding improvement to the guest-invite flow, addressing the weakest-link finding from Exercise 2).

1. Plot or tabulate both scenarios (`k` flat at 0.75 for all 18 months vs. `k` rising to 0.90 at month 7) side by side.
2. In 3–4 sentences: by month 18, roughly how much bigger is the improved-k scenario's active-user count than the flat scenario's, in absolute users and in percent? Is a permanent 0.15 increase in k-factor worth prioritizing engineering time on the guest-onboarding flow, based on this gap alone?

**Deliver** `extended-loop-model.py` with both scenarios and your written answer as a comment block at the bottom.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 60 min |
| 2 | 45 min |
| 3 | 75 min |
| 4 | 45 min |
| 5 | 75 min |
| **Total** | **~5 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
