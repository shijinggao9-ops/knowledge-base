# Week 9 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before starting Week 10. A mix of multiple-choice and short scenario questions — the answer key explains the *why*, not just the letter.

---

**Q1.** What is the primary difference between **positioning** and **messaging**?

- A) Positioning is for customers; messaging is for employees.
- B) Positioning is an internal strategic statement that changes rarely; messaging is the external, per-audience translation of it that changes more often.
- C) They are the same thing, just different names used by different teams.
- D) Positioning is written by sales; messaging is written by legal.

<details>
<summary>Answer</summary>

**B** — positioning is the internal, strategic, rarely-changing foundation; messaging is the external, audience-specific, more-frequently-updated translation of it.

</details>

---

**Q2.** In the five-blank positioning statement template, what does the "Unlike" clause require you to name?

- A) A made-up rival product, for dramatic effect.
- B) Every competitor in the market.
- C) The real primary alternative the customer uses today — often a manual workaround, not a competitor.
- D) The previous version of your own product.

<details>
<summary>Answer</summary>

**C** — the real primary alternative, which for a genuinely new capability is often a manual workaround (a full paid seat, an emailed spreadsheet), not a fictional competitor.

</details>

---

**Q3.** Why did Lecture 1 write **two separate** positioning statements for Guest & External Collaborator Access instead of one?

- A) Legal required two versions for compliance reasons.
- B) One statement, averaged across an enterprise-compliance segment and an agency segment, would be specific to neither and persuasive to nobody.
- C) A/B testing requires at least two versions of any statement.
- D) The template only works when applied twice.

<details>
<summary>Answer</summary>

**B** — an enterprise-compliance buyer and an agency buyer have different jobs-to-be-done; one averaged statement fits neither well. Segment-specific positioning is more persuasive than one-size-fits-all.

</details>

---

**Q4.** In a feature-to-benefit-to-proof table, what's wrong with listing "industry-leading" as a proof point?

- A) Nothing — it's a strong, motivating claim.
- B) It's an adjective, not a checkable fact — a real proof point is something a skeptical reader could go verify.
- C) Proof points must always be a percentage.
- D) "Industry-leading" belongs in the benefit column, not the proof column.

<details>
<summary>Answer</summary>

**B** — "industry-leading" can't be checked by a skeptical reader. A real proof point is a specific, verifiable fact (a number, a passed review, a measured time).

</details>

---

**Q5.** Rank the four launch tiers from smallest to largest audience.

- A) Full GA → limited GA → private beta → internal
- B) Private beta → internal → limited GA → full GA
- C) Internal → private beta → limited GA → full GA
- D) Internal → limited GA → private beta → full GA

<details>
<summary>Answer</summary>

**C** — internal (smallest, employees only) → private beta (a named handful of customers) → limited GA (a growing percentage) → full GA (everyone eligible).

</details>

---

**Q6.** Which of the four risk questions (Lecture 2) is most directly about whether you can instantly undo a launch if it goes wrong?

- A) Blast radius
- B) Reversibility
- C) Support cost
- D) Brand exposure

<details>
<summary>Answer</summary>

**B** — reversibility is specifically about whether you can instantly undo exposure (e.g., flip a flag off) versus damage that's already done and can't be undone.

</details>

---

**Q7.** Why should a channel's reach never exceed its tier's intended audience — for example, why not post a public changelog entry during private beta?

- A) Public changelogs are technically difficult to publish.
- B) It would generate demand from customers who aren't yet eligible for a feature still being validated with a small, hand-picked group.
- C) Changelogs are reserved exclusively for bug fixes.
- D) There's no real reason; it's just convention.

<details>
<summary>Answer</summary>

**B** — a channel with more reach than the tier's audience creates demand from ineligible customers for something still being validated with a small group — defeating the purpose of having a tier at all.

</details>

---

**Q8.** In a RACI matrix, how many people/roles should be **Accountable** for a given work stream?

- A) As many as are involved — Accountable should be shared broadly.
- B) Exactly one — shared accountability functions as no accountability.
- C) Zero — Accountable is optional if Responsible is filled in.
- D) The most senior person in the room, regardless of the work stream.

<details>
<summary>Answer</summary>

**B** — exactly one Accountable owner per work stream. Shared accountability means, in practice, nobody is actually accountable.

</details>

---

**Q9.** What does a feature flag primarily decouple?

- A) Frontend code from backend code.
- B) The deploy of code from the release of a feature to users.
- C) Marketing from engineering.
- D) SQL from Python.

<details>
<summary>Answer</summary>

**B** — flags decouple *deploying* code (it exists in production) from *releasing* it (it's actually turned on for users) — that's what makes instant, targeted rollback possible.

</details>

---

**Q10.** A rollout's activation funnel shows: 32 invitations sent, 26 accepted, 20 took a first action. What is the "accepted → took action" percentage, rounded to one decimal?

- A) 62.5%
- B) 76.9%
- C) 81.3%
- D) 20.0%

<details>
<summary>Answer</summary>

**B** — 20 / 26 = 76.9%. (Note this uses the accepted count as the denominator, not the invitations-sent count — that's the "of accepted, how many activated" metric, distinct from the "of invited, how many accepted" metric, which would be 26/32 = 81.3%, choice C, a common mix-up worth double-checking your denominator on.)

</details>

---

**Q11.** Why does a strong rollback-trigger table treat a single **critical**-severity ticket much more seriously than a low invite-accept rate?

- A) Critical tickets are always about billing.
- B) A safety/data-exposure problem justifies an immediate, low-threshold response; a slow adoption rate is an investigation-worthy signal, not usually a safety issue, so it doesn't get the same hair-trigger response.
- C) Accept-rate data is unreliable and should be ignored entirely.
- D) There's no meaningful difference; both should trigger the same response.

<details>
<summary>Answer</summary>

**B** — safety/data-exposure signals justify an immediate, low-threshold response because the cost of being slow is high and hard to undo; a slow accept rate is worth investigating (is it a messaging problem?) but isn't itself dangerous, so it doesn't get the same automatic trigger.

</details>

---

**Q12.** In the Cascade Freight case study, why did the team escalate from "pause the rollout" to a full **kill switch** rather than stopping at pause?

- A) Pausing was technically impossible.
- B) The root cause (a cache-invalidation bug) was generic enough that any exposed org could hit it next, not just Cascade Freight — so limiting exposure only for *future* orgs wasn't enough.
- C) The VP demanded it without a technical reason.
- D) Kill switches are always used instead of pauses, never alongside them.

<details>
<summary>Answer</summary>

**B** — because the bug's root cause (a caching issue tied to a specific sequence of actions) wasn't unique to Cascade Freight's data, any exposed org performing the same sequence could trigger it — so a pause (stopping *future* exposure) wasn't sufficient; existing exposure needed to be shut off too.

</details>

---

**Q13.** What is the purpose of a **blameless** postmortem?

- A) To determine which individual should be reprimanded.
- B) To document the mechanism that caused the failure and what will change, so people report problems honestly next time instead of hiding them out of fear.
- C) To avoid ever discussing what went wrong.
- D) To satisfy a legal requirement only, with no operational value.

<details>
<summary>Answer</summary>

**B** — a blameless postmortem's entire value is in surfacing the true mechanism and the fix, which only happens reliably if people aren't afraid that reporting a problem will get them blamed.

</details>

---

**Q14.** A `LEFT JOIN` from `rollout_exposures` to `support_tickets` (as in Lecture 3's Section 3.5 wave-health query) is necessary instead of an inner `JOIN` because:

- A) `LEFT JOIN` runs faster in every database engine.
- B) An inner join would silently drop every org that has **zero** matching tickets, which is exactly the "clean" data point the query needs to count.
- C) SQLite doesn't support inner joins.
- D) There's no real difference; either works identically here.

<details>
<summary>Answer</summary>

**B** — an inner join only returns rows where both sides match, so an org with zero tickets would vanish entirely from the result — exactly the wrong behavior when the query's purpose is to count "clean" orgs (those with no matching tickets) alongside orgs that do have them.

</details>

---

**Q15.** A launch checklist item reads: "Security review sign-off current." Which of these is the strongest way to make this item actually checkable in a go/no-go meeting, per Lecture 2 and Exercise 2's guidance?

- A) Leave it as-is — it's already clear enough.
- B) Add a named owner role and specify exactly which tier boundary it gates (e.g., "must be current before the `ga_100` wave, not just before beta").
- C) Remove it — security review isn't a product concern.
- D) Move it to the "known risks accepted" section instead of the checklist.

<details>
<summary>Answer</summary>

**B** — a checklist item without a named owner and an explicit tier gate can't actually drive a go/no-go decision — "current" doesn't say current *for which upcoming wave*, and no owner means no one is responsible for confirming it.

</details>

**Scoring:** 12+ → start Week 10. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's judgment calls compound directly into Week 10's pricing and growth decisions.

---
