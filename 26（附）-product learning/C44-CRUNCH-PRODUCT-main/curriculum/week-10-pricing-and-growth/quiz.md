# Week 10 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before starting Week 11. A mix of multiple-choice and short scenario judgment calls — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** A product's value scales roughly linearly with how many people on a team use it, and the team collaboration itself is the main source of value. Which pricing model best fits that shape?

- A) Usage-based
- B) Seat-based
- C) Freemium only, with no paid tier
- D) Flat subscription regardless of team size

<details>
<summary>Answer</summary>

**B** — seat-based pricing fits products whose value genuinely scales with headcount, which is exactly Loopline's collaboration-driven value shape (Lecture 1, Section 1).

</details>

---

**Q2.** Why does Twilio charge per SMS/call sent instead of a flat monthly fee?

- A) It's simpler to bill
- B) Its cost-to-serve scales with usage, and usage is a reasonable proxy for the value a customer is getting
- C) Usage-based pricing always produces more revenue than flat pricing
- D) Twilio has no other option under its business model

<details>
<summary>Answer</summary>

**B** — usage-based pricing fits when cost-to-serve scales with usage and usage is a reasonable value proxy; that's Twilio's whole billing logic (Lecture 1, Section 1).

</details>

---

**Q3.** What is the single biggest structural problem with Loopline's original $12/seat flat plan?

- A) $12 is too low for any SaaS product
- B) A flat price systematically overcharges customers who need little and undercharges customers who need (and would pay for) a lot more
- C) Flat pricing is illegal in most jurisdictions
- D) There is no problem; flat pricing is always optimal

<details>
<summary>Answer</summary>

**B** — a flat price can't distinguish a 2-seat startup from a 200-seat enterprise account's actual need or willingness to pay, so it structurally over- and undercharges at the same time (Lecture 1's opening framing and Section 1).

</details>

---

**Q4.** Why do most mature SaaS pricing pages converge on exactly three tiers rather than two or five?

- A) Three is required by software licensing law
- B) Three creates a workable anchor (a "Best" tier makes "Better" look reasonable) without fragmenting into an org-chart-driven feature list
- C) Two tiers always convert better in practice
- D) There's no real reason; it's arbitrary tradition

<details>
<summary>Answer</summary>

**B** — three tiers gives a workable anchor via the top tier without fragmenting into an org-chart-driven feature list, which is what happens past four tiers (Lecture 1, Section 2).

</details>

---

**Q5.** A "good" packaging gate is one that:

- A) Splits a single coherent workflow randomly across two tiers to force upgrades
- B) Reflects a value metric the customer experiences directly and would agree justifies the price difference
- C) Is always based on feature count, regardless of what the features do
- D) Should never include compliance capabilities like SSO or audit logs

<details>
<summary>Answer</summary>

**B** — a real packaging gate reflects a value metric the customer experiences and would agree justifies the price step; SSO/audit-log gating is the cleanest example in this week's material, not an exception to avoid (Lecture 1, Section 2).

</details>

---

**Q6.** In the Van Westendorp Price Sensitivity Meter, why does the method ask four separate questions instead of one direct "how much would you pay?" question?

- A) Four questions take longer and therefore produce better data automatically
- B) A direct price question tends to produce a defensively low anchor or a meaningless "sure, sounds fine" that doesn't survive a real invoice
- C) Van Westendorp requires exactly four respondents
- D) The four questions are simply a historical convention with no methodological reason

<details>
<summary>Answer</summary>

**B** — a direct "how much would you pay" question tends to produce a defensively low or meaningless answer; Van Westendorp's four questions sidestep that (Lecture 1, Section 4).

</details>

---

**Q7.** What is the one-sentence test that distinguishes a growth loop from a funnel?

- A) Loops always involve social media; funnels never do
- B) A loop's own output becomes its own next input; a funnel's input always has to come from outside the system
- C) Funnels are free; loops always cost money
- D) There is no meaningful distinction — they're the same thing under different names

<details>
<summary>Answer</summary>

**B** — the defining test is whether the system's own output becomes its own next input; that's what separates loops from funnels, no matter how many steps a funnel has (Lecture 2, Section 1).

</details>

---

**Q8.** Why does Lecture 2 argue that a "paid loop" (revenue reinvested into ad spend) isn't really a self-reinforcing loop in the same sense as a viral or content loop?

- A) Paid acquisition never works
- B) It's not self-reinforcing on the user side — turn the ad spend off and the mechanism stops immediately, unlike a loop whose users keep triggering it on their own
- C) Paid loops are actually stronger than viral loops in every case
- D) Reinvesting revenue is against SaaS industry norms

<details>
<summary>Answer</summary>

**B** — a paid loop is not self-reinforcing on the user side; the mechanism halts the moment ad spend stops, unlike a loop whose existing users keep triggering it on their own (Lecture 2, Section 2).

</details>

---

**Q9.** Loopline's guest-invite loop measures k = 0.75 (2.5 invites per active inviter × a 0.30 invite-to-activation rate). What does a k below 1 mean for this loop?

- A) The loop is worthless and should be shut down
- B) The loop alone can't sustain exponential growth by itself, but it's still a strong, often-free source of new activated users that lowers blended CAC
- C) k below 1 means the loop is losing the company money
- D) k must always be recalculated to exceed 1 before a loop is worth measuring

<details>
<summary>Answer</summary>

**B** — k below 1 means the loop can't carry exponential growth alone, but it's still a valuable, often-zero-CAC source of new activated users that lowers blended CAC across the business (Lecture 2, Section 4).

</details>

---

**Q10.** Given two loops with the identical k-factor, why might one still produce dramatically more growth over 6 months than the other?

- A) They can't differ if k is identical
- B) A shorter cycle time lets the same k-factor compound more times within the same window, producing a much larger effective growth rate
- C) Cycle time is irrelevant once k-factor is known
- D) Only the loop with the higher CAC will grow faster

<details>
<summary>Answer</summary>

**B** — a shorter cycle time lets the same k-factor compound more times within the same window, producing a larger effective growth rate even with an identical k (Lecture 2, Section 4; modeled directly in Lecture 3, Section 5).

</details>

---

**Q11.** Why should MRR be computed off the *net* price (`price_per_seat * (1 - discount_pct)`) rather than the list price?

- A) List price is always identical to net price in practice
- B) Using list price overstates MRR for every account with a negotiated discount, which in Loopline's data is most of the Agency, Mid-size, and Enterprise segments
- C) Net price is a marketing term with no accounting meaning
- D) Discounts should be added to, not subtracted from, the list price

<details>
<summary>Answer</summary>

**B** — using list price instead of net price overstates MRR for every discounted account, and in this week's data most Agency/Mid-size/Enterprise accounts carry a negotiated discount (Lecture 3, Section 2).

</details>

---

**Q12.** What's the difference between logo churn rate and revenue churn rate, and why did it matter for Vantage Manufacturing (45 seats) versus Silverpine AI (3 seats) in this week's data?

- A) They're the same metric with different names
- B) Logo churn counts each churned account equally regardless of size; revenue churn weights by dollars — so Vantage's churn represented far more lost MRR than Silverpine's, even though both count as "1 churned account" in logo terms
- C) Revenue churn only applies to Enterprise accounts
- D) Logo churn is always higher than revenue churn

<details>
<summary>Answer</summary>

**B** — logo churn counts accounts equally; revenue churn weights by dollars, so the 45-seat Vantage Manufacturing churn represented far more lost MRR than the 3-seat Silverpine AI churn despite both counting as "1" in logo terms (Lecture 3, Section 2).

</details>

---

**Q13.** In Exercise 3's risk-adjusted pricing model, the naive projection showed +37.3% MRR growth, but the risk-adjusted projection showed only +12.9%. What does that roughly $2,283/month gap represent?

- A) A calculation error that should be fixed by using the naive number instead
- B) The expected revenue given up to migration-churn risk, concentrated mostly in the Enterprise/Business-tier accounts facing the largest (50%) price increase
- C) Tax withholding on the projected revenue
- D) The cost of running the SQL queries themselves

<details>
<summary>Answer</summary>

**B** — the gap is the expected revenue given up to migration-churn risk, driven mostly by Enterprise/Business-tier accounts facing the largest price increase (Lecture 3, Section 4; Exercise 3).

</details>

---

**Q14.** A CASE-based tier assignment maps every account with `segment = 'Enterprise'` straight to the Business tier, regardless of seat count. Why key the Business-tier gate off `segment` instead of just `seats > 40` or similar?

- A) Segment and seat count always produce identical groupings, so it doesn't matter
- B) The value metric that matters for Business (compliance need — SSO, audit log) correlates with the customer's segment/profile, not strictly with how many seats they have
- C) SQL cannot filter on seat count in a CASE expression
- D) Enterprise accounts are defined exclusively by having over 40 seats

<details>
<summary>Answer</summary>

**B** — the value metric behind the Business tier (compliance need) correlates with the customer's segment/profile more directly than with raw seat count, which is exactly why the CASE expression keys off `segment` first (Lecture 3, Section 3).

</details>

---

**Q15.** Why does this week's mini-project insist that the final recommendation state an expected effect on **Weekly Active Teams**, not just MRR or signups?

- A) MRR and signups are not real numbers
- B) A pricing or growth decision can look good on a revenue or signup metric while quietly working against the durable-value metric (North Star) the rest of the product organization is aligned around — stating the WAT effect forces you to check that the two models don't undermine each other
- C) Weekly Active Teams is required by generally accepted accounting principles
- D) There is no meaningful difference between MRR and Weekly Active Teams as metrics

<details>
<summary>Answer</summary>

**B** — a decision can look good on MRR or signups while quietly undermining the durable-value North Star; stating the WAT effect forces the two models (pricing and growth) to be checked against the same metric instead of graded separately (Lecture 3, Section 6; mini-project Part 5).

</details>

**Scoring:** 12+ → start Week 11. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's vocabulary (pricing models, packaging gates, anchoring, loop vs. funnel, k-factor, cycle time, risk-adjusted MRR, North Star alignment) is what Week 11's AI-feature pricing and adoption questions build on directly.

---
