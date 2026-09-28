# Week 3 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before starting Week 4. A mix of multiple-choice and short "what would you do" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Which of these is a properly formed **problem statement**, not a solution or a bare symptom?

- A) "We need a bulk CSV importer."
- B) "Import tickets are up 12% this month."
- C) "New trial teams who try to import an existing backlog fail often enough that many never get their real work into the product, and these teams convert to paid at a quarter the rate of teams whose import succeeds."
- D) "Import is broken."

<details>
<summary>Answer</summary>

**C** — specific population, root-cause-adjacent framing, no baked-in solution, and a quantified impact. A is solution-shaped, B is a bare symptom, D is vague and unfalsifiable.

</details>

---

**Q2.** The Five Whys technique is used to:

- A) Confirm that a proposed solution will work
- B) Trace a symptom back to its root cause before proposing a fix
- C) Calculate the size of an opportunity
- D) Score a solution against Value/Viability/Feasibility/Usability

<details>
<summary>Answer</summary>

**B** — Five Whys traces a symptom back toward its root cause; it's a diagnostic technique, not a sizing or scoring tool.

</details>

---

**Q3.** What's the fastest test for whether a "problem statement" is actually a solution in disguise?

- A) Check if it's longer than two sentences
- B) Check if it names a specific UI element, feature, or fix an engineer could start building from
- C) Check if a stakeholder said it out loud in a meeting
- D) Check if it has a number in it

<details>
<summary>Answer</summary>

**B** — if the statement already names a feature/UI/fix, it's a solution wearing a problem statement's clothes, per Lecture 1's checklist.

</details>

---

**Q4.** In the who/what/why/impact structure, the "impact" component should be:

- A) A subjective feeling ("this really matters")
- B) A measurable, ideally quantified consequence
- C) A list of possible solutions
- D) The name of the team responsible for fixing it

<details>
<summary>Answer</summary>

**B** — impact should be measurable/quantified (or have an honest plan to quantify it), not a subjective feeling.

</details>

---

**Q5.** A JTBD (jobs-to-be-done) statement differs from a problem statement mainly by:

- A) Being written from the user's point of view, emphasizing situation and motivation, rather than the team's evidence-forward framing
- B) Never including any evidence
- C) Always being shorter
- D) Being required only for enterprise products

<details>
<summary>Answer</summary>

**A** — JTBD is the same underlying insight written from the user's situation/motivation/outcome, used to keep the team anchored in the user's experience; the problem statement is the evidence-forward version for justifying the work.

</details>

---

**Q6.** TAM, SAM, and SOM stand for, in order:

- A) Total Available Market, Sized Addressable Market, Sold Obtainable Market
- B) Total Addressable Market, Serviceable Available Market, Serviceable Obtainable Market
- C) Target Audience Metric, Segment Analysis Model, Sales Opportunity Model
- D) Total Actual Market, Segment Available Market, Serviceable Owned Market

<details>
<summary>Answer</summary>

**B** — Total Addressable Market, Serviceable Available Market, Serviceable Obtainable Market.

</details>

---

**Q7.** Which of TAM, SAM, or SOM should most directly influence a near-term roadmap decision?

- A) TAM, because bigger is always more convincing
- B) SAM, because it's the middle ground
- C) SOM, because it's scoped to what you specifically could realistically capture
- D) None of them — roadmap decisions shouldn't use market sizing

<details>
<summary>Answer</summary>

**C** — SOM is scoped to what *you*, specifically, given your current size and reach, could realistically capture — the number that should actually inform a near-term decision. TAM is context, not a decision input.

</details>

---

**Q8.** Given `signup_cohort`: 46.7% of signups attempt an import, and 42.9% of those attempts fail. What percent of **all** signups end up as a failed import?

- A) 89.6% (you just add the two percentages)
- B) 46.7% (the attempt rate alone)
- C) 42.9% (the failure rate alone)
- D) 20.0% (you multiply the two rates together)

<details>
<summary>Answer</summary>

**D** — chain the rates: 0.467 × 0.429 ≈ 0.20, i.e., 20.0% of all signups. Adding them (A) is meaningless; using either rate alone understates or misrepresents the combined effect.

</details>

---

**Q9.** Why is bottom-up sizing built from an observed conversion-rate gap (like succeeded-import vs. failed-import teams) best treated as an **upper bound**, not a guaranteed number?

- A) SQL aggregate functions are inherently imprecise
- B) The gap could be partly explained by a confounding variable (like team size) rather than fully caused by the thing you're measuring
- C) Bottom-up sizing is always wrong
- D) `AVG()` ignores `NULL` values

<details>
<summary>Answer</summary>

**B** — an observed gap could be partly or fully explained by a confound (e.g., bigger teams both import successfully *and* convert better for unrelated reasons), so the true causal effect of fixing the import could be smaller than the raw gap suggests.

</details>

---

**Q10.** You find that a top-down estimate is roughly 10x a bottom-up estimate for the same general opportunity area. The best next step is:

- A) Average the two numbers and report that
- B) Always trust the bigger number — it shows more upside
- C) Always trust the smaller number — it's more conservative
- D) Audit both chains' assumptions to find which one is doing the most work, and explain the gap with specifics

<details>
<summary>Answer</summary>

**D** — audit the assumptions behind both chains and find which one is doing the most work; averaging (A) is mathematically meaningless when the two methods measure different things, and blindly trusting either extreme (B, C) skips the actual investigation.

</details>

---

**Q11.** In an opportunity-solution tree, what sits at the root?

- A) A list of features
- B) A measurable, product-level outcome
- C) The engineering team's current sprint
- D) A single chosen solution

<details>
<summary>Answer</summary>

**B** — a measurable, product-level outcome (a number you want to move), not a feature list or a single solution.

</details>

---

**Q12.** Why can't a solution attach directly to the outcome at the root of an opportunity-solution tree, skipping the opportunity level?

- A) Mermaid diagrams don't support that many levels
- B) It would mean building something with no stated customer need or evidence behind it
- C) Solutions are always more expensive than opportunities
- D) Outcomes can only have one branch

<details>
<summary>Answer</summary>

**B** — skipping the opportunity level means committing engineering time to something with no stated customer need or evidence behind it — exactly the failure mode this week's lectures warn against.

</details>

---

**Q13.** "Killing a branch loudly, not silently" on an opportunity-solution tree matters mainly because:

- A) It looks more thorough in a slide deck
- B) Silent deletion means the same rejected idea gets re-proposed later by someone who never saw the reasoning that killed it
- C) Loud kills are required by most product management certifications
- D) It increases the tree's node count, which is good for stakeholder confidence

<details>
<summary>Answer</summary>

**B** — silent deletion means the same idea gets re-litigated from scratch later by someone who never saw why it was killed; a visible, reasoned kill prevents that churn.

</details>

---

**Q14.** A stakeholder says "search is slow" and a support ticket count backs it up. What's the single most important thing missing before this becomes a fundable problem statement?

- A) A prettier chart of the ticket volume
- B) A specific, bounded population and a root cause — "slow for whom, and why" — not just a symptom count
- C) Approval from the CFO
- D) A Mermaid diagram

<details>
<summary>Answer</summary>

**B** — "slow" and a ticket count is a symptom, not yet a problem statement; it's missing a specific bounded population and a stated (even hypothesized) root cause.

</details>

---

**Q15.** A kill memo for a popular-but-unvalidated idea is strongest when it:

- A) Argues the idea's supporters have bad judgment
- B) Simply says "there's no data" and stops
- C) Names a specific alternative use of the same resources with real sizing behind it, and states time-bound conditions under which the idea could be revisited
- D) Avoids mentioning any numbers, to keep it diplomatic

<details>
<summary>Answer</summary>

**C** — the strongest kill memos reframe the decision as a real tradeoff against a specific, sized alternative, and leave a concrete, time-bound path back to reconsideration — rather than attacking the idea's supporters (A), stopping at "no data" (B), or hiding the numbers (D).

</details>

**Scoring:** 12+ → start Week 4. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; sizing and tree-building compound directly into Week 4's spec-writing.

---
