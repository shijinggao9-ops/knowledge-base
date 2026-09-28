# Week 5 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 6. A mix of multiple-choice and short "what does this actually mean" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** The RICE formula is:

- A) `(Reach + Impact + Confidence) / Effort`
- B) `Reach × Impact × Confidence / Effort`
- C) `Reach × Impact / (Confidence × Effort)`
- D) `(Reach × Impact) − (Confidence × Effort)`

<details>
<summary>Answer</summary>

**B** — `Reach × Impact × Confidence / Effort`. Note it's a product over the first three, divided by Effort — not a sum, and not Confidence in the denominator.

</details>

---

**Q2.** Holding Reach, Impact, and Confidence fixed, what happens to a RICE score as Effort increases?

- A) It increases proportionally
- B) It decreases
- C) It's unaffected — Effort is informational only
- D) It becomes negative

<details>
<summary>Answer</summary>

**B** — more Effort in the denominator directly lowers the score; RICE rewards value achieved *per unit of work*, not raw value.

</details>

---

**Q3.** In RICE, "Confidence" is meant to measure:

- A) How enthusiastic a stakeholder is about the feature
- B) How certain you are that the Reach and Impact estimates are accurate
- C) How confident engineering is that the effort estimate is right
- D) The probability the feature ships on time

<details>
<summary>Answer</summary>

**B** — Confidence measures how sure you are about the Reach and Impact *estimates themselves*, not stakeholder enthusiasm or timeline certainty (those are different, real, but separate concerns).

</details>

---

**Q4.** In this week's seed data, Loopline's `dark_mode` request has 1,800 forum upvotes but ranks near the bottom on WSJF and comes out mostly **Indifferent** on Kano. What does this combination most directly demonstrate?

- A) RICE and Kano always agree with each other
- B) A large Reach number (even from real engagement, like votes) doesn't guarantee real business urgency or Kano-measured satisfaction impact
- C) Dark mode is technically difficult to build
- D) The survey respondents didn't understand the questions

<details>
<summary>Answer</summary>

**B** — a big, even genuine, Reach signal (votes) doesn't automatically translate into business urgency (WSJF) or real satisfaction impact (Kano) — that gap is this week's central lesson.

</details>

---

**Q5.** This week's seed survey classifies `recurring_tasks` as dominantly which Kano category?

- A) Attractive (delighter)
- B) Indifferent
- C) Must-be (basic)
- D) Reverse

<details>
<summary>Answer</summary>

**C** — Must-be. The seed survey's tally (M=9 of 20, the plurality) reflects a feature that's become table stakes: its absence would be noticed, its presence isn't a delighter.

</details>

---

**Q6.** In the Kano evaluation matrix, a respondent who answers **1 (like it)** to the functional question and **5 (dislike it)** to the dysfunctional question lands in which category?

- A) Attractive
- B) One-dimensional
- C) Must-be
- D) Questionable

<details>
<summary>Answer</summary>

**B** — One-dimensional. Row "1 (like)", column "5 (dislike)" is the O cell: satisfaction/dissatisfaction scales with how well it's done, in both directions.

</details>

---

**Q7.** The Kano **Better** coefficient is calculated as:

- A) `(A + O) / (A + O + M + I)`
- B) `(M + I) / (A + O + M + I)`
- C) `-(O + M) / (A + O + M + I)`
- D) `A / (A + O + M + I + R + Q)`

<details>
<summary>Answer</summary>

**A** — `(A + O) / (A + O + M + I)`. Better measures the satisfaction *upside* of building it well.

</details>

---

**Q8.** A strongly **negative Worse** coefficient on a feature tells a PM:

- A) Users are indifferent to the feature entirely
- B) Building the feature well will delight users significantly
- C) *Not* having the feature causes significant dissatisfaction — it behaves like a Must-be
- D) The survey data is unreliable

<details>
<summary>Answer</summary>

**C** — Worse is negative by convention; a large magnitude (strongly negative) means skipping the feature causes real dissatisfaction — the signature of a Must-be.

</details>

---

**Q9.** The WSJF formula is:

- A) `Cost of Delay × Job Size`
- B) `Cost of Delay / Job Size`
- C) `Job Size / Cost of Delay`
- D) `(Cost of Delay + Job Size) / 2`

<details>
<summary>Answer</summary>

**B** — `Cost of Delay / Job Size`. Same value-over-effort shape as RICE, but the numerator is explicitly about value-weighted-by-urgency.

</details>

---

**Q10.** Which WSJF cost-of-delay component would best capture the value of `public_api_webhooks` — a feature with small direct Reach but that unlocks a future class of integrations?

- A) User-Business Value
- B) Time Criticality
- C) Risk Reduction / Opportunity Enablement
- D) Job Size

<details>
<summary>Answer</summary>

**C** — Risk Reduction / Opportunity Enablement is the component built for exactly this case: value that's mostly indirect, via what the item unlocks for future work, rather than direct user-facing value today.

</details>

---

**Q11.** In this week's data, `guest_external_access` ranks near the bottom on RICE but **#1** on WSJF. The best explanation is:

- A) RICE was calculated incorrectly
- B) WSJF always outranks RICE for Sales-requested items
- C) WSJF's Time Criticality component captures the urgency of three signed, closing-date-bound deals in a way RICE's Reach (only 20 teams) does not
- D) The item's Effort score was different in each formula

<details>
<summary>Answer</summary>

**C** — WSJF's Time Criticality captures that these deals have closing dates; RICE has no time-awareness at all, so a small Reach number (20 teams) can't reflect that three of them are signed and waiting.

</details>

---

**Q12.** A backlog item ranks #1 on WSJF, but its hard prerequisite ranks #7. What does this week's sequencing rule say to do?

- A) Ship the #1 item first regardless; dependencies are advisory only
- B) Skip the #1 item entirely and never build it
- C) Schedule the prerequisite first, even though it "jumps the queue" on its own score, then the #1 item
- D) Average their two ranks and schedule accordingly

<details>
<summary>Answer</summary>

**C** — dependencies are a hard constraint; you pull the prerequisite forward in the schedule even though its own score would place it later, then schedule the item that needed it.

</details>

---

**Q13.** Which of these is correct "Next" column language for a roadmap, per this week's uncertainty rules?

- A) "Shipping March 15th."
- B) "We expect to work on this next quarter, pending [named dependency/risk]."
- C) "This is fully committed and capacity-checked."
- D) "TBD, no further information."

<details>
<summary>Answer</summary>

**B** — directional language naming a condition, with no date. (A) is Now-level commitment language used incorrectly; (C) overclaims certainty for Next; (D) under-explains — Later gets a *reason*, not silence.

</details>

---

**Q14.** This week's roadmap assumes a stated Now capacity of 20 job-size points. Why does stating that number explicitly (rather than leaving it implicit) matter?

- A) It has no real effect — capacity is always understood
- B) It makes the roadmap's hard tradeoffs visible and arguable with a specific number, instead of hidden inside an unstated assumption
- C) It's required by the RICE formula
- D) It converts Now into a legally binding commitment

<details>
<summary>Answer</summary>

**B** — an explicit capacity number is what forces (and makes visible) the real tradeoffs in what's Now vs. Next vs. Later; without it, prioritization decisions are unfalsifiable.

</details>

---

**Q15.** In Challenge 2's scenario, a colleague raises `ai_task_summaries`'s Confidence from 0.2 to 0.9 with the justification "we're confident the exec wants this." What's the correct diagnosis?

- A) This is a legitimate re-estimate — strong sponsorship is good evidence
- B) A category error — Confidence should reflect certainty in the Reach/Impact estimates, not certainty that a stakeholder wants the feature built
- C) This is actually an Effort change, not a Confidence change
- D) RICE doesn't use a Confidence input, so this doesn't affect the score

<details>
<summary>Answer</summary>

**B** — a classic category error: sponsorship affects the *chance a feature gets built regardless of score*, not the *evidence behind the Reach/Impact numbers*. Conflating the two is one of the harder-to-catch forms of RICE gaming precisely because it doesn't feel dishonest.

</details>

**Scoring:** 13+ → start Week 6. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; this week's frameworks compound directly into Week 6's analytics and Week 9's launch planning.

---
