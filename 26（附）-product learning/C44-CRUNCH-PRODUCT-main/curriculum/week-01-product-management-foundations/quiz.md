# Week 1 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before starting Week 2. A mix of multiple-choice and short scenario judgment calls — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Which of the following does a PM **own outright** (not merely influence)?

- A) The exact database schema engineering chooses
- B) The visual design of a specific screen
- C) The prioritization rationale for what ships next
- D) The engineering time estimate for a ticket

<details>
<summary>Answer</summary>

**C** — the prioritization rationale is squarely PM-owned (Lecture 1, Section 2). Schema (A), visual design (B), and estimates (D) are all things a PM *influences*, not owns.

</details>

---

**Q2.** A PM spends nearly all their time writing tickets and running standups, and skips talking to users before specs get written. Which part of the discovery/delivery/outcomes loop are they skipping?

- A) Delivery
- B) Outcomes
- C) Discovery
- D) None — this is a complete PM workflow

<details>
<summary>Answer</summary>

**C** — skipping user conversations before writing specs means skipping discovery. Delivery (writing tickets, running standups) is exactly what they *are* doing; outcomes comes after ship.

</details>

---

**Q3.** In classic Scrum, the Product Owner role is best described as:

- A) Identical to a full-scope PM in every company
- B) A backlog-and-sprint-priority-focused role, often a narrower slice of the full PM job
- C) A role with no relationship to product management at all
- D) Always a separate person from anyone doing discovery work

<details>
<summary>Answer</summary>

**B** — classic Scrum's Product Owner is backlog/sprint-focused, and is often a narrower slice of the full PM scope (discovery + strategy + backlog), sometimes split across two people on the same team.

</details>

---

**Q4.** Why is "PM is the CEO of the product" a risky metaphor if taken literally?

- A) PMs should never make any decisions
- B) A CEO has hiring/firing and budget authority a PM typically doesn't have, and taking the metaphor literally leads PMs to try to command people who don't report to them
- C) Only CEOs are allowed to talk to customers
- D) It's actually a completely accurate description with no risk

<details>
<summary>Answer</summary>

**B** — a CEO has real hiring/firing and budget authority; a PM almost never does. Taken literally, the metaphor leads PMs to try to command people outside their reporting line, which damages trust.

</details>

---

**Q5.** A segment groups users by:

- A) The job they're trying to get done
- B) Observable, shared traits like company size, role, or geography
- C) Their emotional state when using the product
- D) How much revenue they generate, exclusively

<details>
<summary>Answer</summary>

**B** — a segment is defined by observable shared traits. The job (A) is a separate, deeper layer covered by JTBD, not what a segment describes.

</details>

---

**Q6.** What is the core risk of building a persona from a single workshop, without grounding it in real interviews or usage data?

- A) Personas are always accurate regardless of source
- B) It becomes "fan fiction" — a confident-sounding composite with no evidence behind it
- C) There is no risk; personas are purely for internal communication
- D) It will automatically match every real user exactly

<details>
<summary>Answer</summary>

**B** — an ungrounded persona is "fan fiction with a stock photo" (Lecture 2, Section 2) — confident-sounding but unverified.

</details>

---

**Q7.** In the milkshake example from Lecture 2, why did demographic segmentation fail to explain milkshake purchases?

- A) Demographics are never useful for anything
- B) The real driver was the *job* — a filling, one-handed, long-lasting food for a boring commute — which cut across demographic groups
- C) Milkshakes were purchased equally by every demographic group
- D) The study found no pattern at all, of any kind

<details>
<summary>Answer</summary>

**B** — the job (filling, one-handed, long-lasting food for a boring commute) cut across demographic groups; that's exactly why demographic segmentation alone missed the real driver.

</details>

---

**Q8.** Which of these is a properly written JTBD statement (passes the disguised-feature-request test)?

- A) "I want a dark mode toggle in settings."
- B) "When I'm working late at night, I want to keep working without straining my eyes, so I don't fall behind by morning."
- C) "Add a button for exporting to PDF."
- D) "I want the Slack integration built next quarter."

<details>
<summary>Answer</summary>

**B** — it describes a durable outcome (not straining your eyes, not falling behind) with no product or feature name in it. A, C, and D all name a UI element or feature directly — solutions wearing a JTBD costume.

</details>

---

**Q9.** A "pain reliever" in a value proposition should:

- A) Be a vague promise like "helps you stay organized"
- B) Name a specific, checkable product behavior that addresses a named pain
- C) Always be a brand-new feature, never an existing one
- D) Only ever apply to paying customers

<details>
<summary>Answer</summary>

**B** — a real pain reliever names a specific, checkable behavior. "Helps you stay organized" (A) is a slogan, not a value proposition.

</details>

---

**Q10.** Which lifecycle stage is most associated with net revenue retention (NRR) and churn rate as the primary metrics?

- A) Discovery / inception
- B) Validation / early growth
- C) Growth
- D) Maturity

<details>
<summary>Answer</summary>

**D** — maturity is the stage where NRR and churn become the primary lens, since raw growth has slowed and defending/expanding existing revenue matters more (Lecture 3, Section 1).

</details>

---

**Q11.** A product's new signups are climbing every week, but activation rate and WAU/MAU ratio are both falling at the same time. What does Lecture 3 say this pattern most likely indicates?

- A) The product is unambiguously succeeding — signups are the only metric that matters
- B) The acquisition engine is working, but the underlying product/onboarding experience is degrading — a single rising metric doesn't prove health
- C) This pattern is statistically impossible
- D) WAU/MAU and activation rate always move together, so this can't happen

<details>
<summary>Answer</summary>

**B** — this is the exact pattern worked through in Lecture 3, Section 2: rising signups alone proves nothing if activation and stickiness are falling at the same time — the acquisition engine is outrunning a degrading product experience.

</details>

---

**Q12.** In the VVF+U lens, an idea that users clearly want, the business can clearly monetize, and the team can clearly build — but that almost nobody discovers or manages to complete — fails on:

- A) Value
- B) Viability
- C) Feasibility
- D) Usability

<details>
<summary>Answer</summary>

**D** — valuable, viable, and feasible but undiscoverable or too confusing to complete is a usability failure specifically (Lecture 3, Section 3's table).

</details>

---

**Q13.** Why is "we're doubling down on AI" not a strategy by the definition in Lecture 3?

- A) AI features are never a good strategic bet
- B) It has no claim, no reason to believe it, no specific bet, and no falsification condition — it's an aspiration, not a strategy
- C) A real strategy must always be exactly one sentence
- D) Strategies can never mention specific technologies

<details>
<summary>Answer</summary>

**B** — a real strategy needs a claim, a reason to believe it, a specific bet, and a falsification condition (Lecture 3, Section 4). "Doubling down on AI" has none of those.

</details>

---

**Q14.** Given a metrics table with a `commission_pct`-style nullable numeric column, what does `AVG(that_column)` do with `NULL` rows?

- A) Treats each `NULL` as `0`, dragging the average down
- B) Throws an error
- C) Ignores `NULL` rows entirely — averages only the non-null values
- D) Converts all `NULL`s to the column's maximum value

<details>
<summary>Answer</summary>

**C** — SQL aggregate functions like `AVG` ignore `NULL` values automatically; they don't need special handling, and they don't silently treat `NULL` as `0`.

</details>

---

**Q15.** Why does this course store product metrics and feature backlogs in SQL tables instead of spreadsheets?

- A) Spreadsheets are technically incapable of holding numbers
- B) A table with a schema enforces structure and supports reliable joins/filters as data grows; a spreadsheet has no such guarantees and breaks silently when someone re-sorts it
- C) SQL is required by law for business data
- D) There is no real difference; it's purely a style preference

<details>
<summary>Answer</summary>

**B** — a schema-backed table enforces structure and supports reliable filtering/joining as data grows; a spreadsheet has no such enforcement and breaks the moment someone sorts a range incorrectly (Lecture 3's data-tooling note, and this week's Exercises 2–3).

</details>

**Scoring:** 12+ → start Week 2. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's frameworks (own/influence, JTBD, lifecycle stage, VVF+U) are the vocabulary the entire rest of the course is built on.

---
