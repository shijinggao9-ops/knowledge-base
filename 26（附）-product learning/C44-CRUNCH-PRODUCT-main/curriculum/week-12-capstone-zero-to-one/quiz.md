# Week 12 — Quiz

Fifteen questions covering the whole capstone: narrative coherence, North Star selection, the AI Task Summaries dataset's SQL, experiment design, and stakeholder presentation. Lectures closed. Aim for 13/15 — this is the last quiz of the course, and it's cumulative in spirit even though every question is scoped to this week's material.

---

**Q1.** In this week's five-act product narrative, which act does Week 5 (RICE, WSJF, Kano, roadmapping) correspond to?

- A) Discover
- B) Spec
- C) Prioritize
- D) Measure

<details>
<summary>Answer</summary>

**C** — Prioritize. Week 5's RICE, WSJF, Kano, and Now/Next/Later roadmapping all answer "given limited capacity, what ships first" — Act 3 in this week's table.

</details>

---

**Q2.** Lecture 1 defines an "orphaned artifact" as:

- A) Any document that hasn't been reviewed by a stakeholder
- B) An artifact (PRD, roadmap item, metric, next bet) that can't be traced back to the artifact before it in the chain
- C) A backlog item that scored zero on RICE
- D) A feature that was cut during scoping

<details>
<summary>Answer</summary>

**B** — an orphaned artifact is any output that can't be traced to what should have produced it: a PRD not traceable to research, a roadmap item not traceable to the PRD, a metric not traceable to a stated goal, a next bet not traceable to evidence.

</details>

---

**Q3.** In this week's `mvp_launch_events` dataset, what is the day-0 activation rate (users who generated a summary the same day they were exposed)?

- A) 88.9% (16 of 18)
- B) 61.1% (11 of 18)
- C) 38.9% (7 of 18)
- D) 100% (18 of 18)

<details>
<summary>Answer</summary>

**B** — 61.1% (11 of 18). This is the day-0 rate specifically; 88.9% (16 of 18) is the *ever-tried* rate across the full two weeks, a different, higher number for a different question.

</details>

---

**Q4.** The Weekly Active Summary Users (WASU) trend in the seed data goes from 16 in week 1 to 7 in week 2. What does Lecture 2 identify as the correct reading of this pattern?

- A) The launch failed outright and the feature should be killed immediately
- B) The launch succeeded outright; week 2's lower count is just fewer new users trying it for the first time
- C) A strong top-of-funnel trial number is hiding a real habit-formation problem — trial and retention are answering different questions
- D) WASU is not a valid metric for a two-week-old feature and should be discarded

<details>
<summary>Answer</summary>

**C** — the correct reading holds both numbers at once: a strong pitch (trial) sitting on top of a real, diagnosable habit-formation gap (retention). Neither A (overreacting to retention alone) nor B (ignoring retention because trial was good) is the lesson.

</details>

---

**Q5.** Why does Lecture 2 prefer WASU over "total summaries generated" as the North Star for AI Task Summaries?

- A) WASU is easier to compute in SQL
- B) Total summaries generated rewards intensity from a few power users and can't distinguish broad habit formation from a handful of heavy users
- C) Total summaries generated requires a JOIN and WASU doesn't
- D) WASU was the metric used in Week 6, so consistency required reusing it

<details>
<summary>Answer</summary>

**B** — total volume conflates a few power users' intensity with broad adoption; WASU specifically counts distinct users, which is what "is this becoming a habit across the base" requires.

</details>

---

**Q6.** In the seed data, pro-plan users retain the feature into week 2 at what rate, compared to free-plan users?

- A) The same rate — plan has no effect
- B) About 2x — 50% for pro vs. 25% for free
- C) Free-plan users retain at a higher rate than pro-plan users
- D) Retention cannot be computed by plan without additional data

<details>
<summary>Answer</summary>

**B** — pro retains at 50% (5 of 10) vs. free at 25% (2 of 8), roughly double — a segmentation finding with a direct pricing/packaging implication (tying back to Week 10).

</details>

---

**Q7.** Users 17 and 18 never generated a single summary but did have `login` events early in the observation window. What does Lecture 2 say this rules out as an explanation for their non-adoption?

- A) It rules out that the feature itself is the problem
- B) It rules out general app churn — they were confirmed active in the app, so their non-adoption is feature-specific, not evidence of leaving the product entirely
- C) It rules out that they were ever exposed to the feature at all
- D) It proves the feature was technically broken for them

<details>
<summary>Answer</summary>

**B** — confirmed `login` activity rules out general app abandonment as the explanation; since they were active in the app and still didn't try the feature, the non-adoption is feature-specific.

</details>

---

**Q8.** Lecture 3's five-part launch narrative structure is, in order:

- A) Metrics, problem, solution, learnings, ask
- B) Problem+evidence, what we built (and didn't), did it work (honest number), what we learned (falsifiable hypothesis), the next-quarter bet
- C) Ask, problem, solution, roadmap, metrics
- D) Solution, problem, metrics, roadmap, ask

<details>
<summary>Answer</summary>

**B** — problem+evidence, what we built/didn't, did it work (honest), what we learned (falsifiable), the next-quarter bet — in that order, every time.

</details>

---

**Q9.** Per Lecture 3, when a launch readout's headline number is genuinely bad, the correct move is:

- A) Lead with a different, better-looking metric instead
- B) Omit the number and focus only on qualitative feedback
- C) State it plainly and use the metric tree to show what's healthy and what's the specific, diagnosable problem — if the evidence actually supports that read
- D) Delay the readout until the number improves

<details>
<summary>Answer</summary>

**C** — state the bad number plainly, then use the metric tree to distinguish a genuinely diagnosable, fixable problem from a fundamentally weak result — but only when the evidence actually supports that read; overclaiming a "diagnosable" story with no evidence is spin, not honesty.

</details>

---

**Q10.** A "next-quarter bet," per Lecture 3 Section 4, must include which three elements?

- A) A budget, a timeline, and a named owner
- B) A specific action, a specific metric and threshold, and a specific decision date
- C) A risk assessment, a cost estimate, and a stakeholder sign-off
- D) A hypothesis, a survey, and a follow-up meeting

<details>
<summary>Answer</summary>

**B** — a specific action, a specific metric and threshold, and a specific decision date. Without all three, it's a hope, not a bet that can be evaluated later.

</details>

---

**Q11.** Why does Lecture 3 say a presenter should volunteer their own study's limitations (e.g., a small sample size) before being asked?

- A) It's a legal requirement for internal presentations
- B) A presenter who volunteers limitations unprompted is trusted more, not less, than one who waits to be caught
- C) It shortens the Q&A session
- D) It has no effect on stakeholder trust either way

<details>
<summary>Answer</summary>

**B** — volunteering a real limitation before being asked builds trust; a stakeholder who catches an un-volunteered weakness later trusts the presenter's future readouts less.

</details>

---

**Q12.** In Exercise 2, why does the PRD's Problem section need to explicitly cite the discovery brief rather than restate the problem from scratch?

- A) Restating from scratch is against course formatting rules
- B) It's the specific mechanism that prevents an orphaned Act 2 — a PRD that doesn't trace to validated research is fiction with a template
- C) Citation is only required for graded assignments, not real PRDs
- D) It makes the PRD longer, which is preferred

<details>
<summary>Answer</summary>

**B** — explicit citation is the actual mechanism (not just a formatting nicety) that prevents Act 2 from becoming an orphaned artifact disconnected from real evidence.

</details>

---

**Q13.** Challenge 1 asks you to choose between an A/B test and a pre/post comparison. Per Week 7's criteria (referenced in this week's challenge), what's the deciding factor?

- A) Whichever design is faster to implement
- B) Whether the product has enough concurrent users to randomize into a real control group without starving both arms of a meaningful sample
- C) A/B tests are always preferred regardless of user volume
- D) Pre/post comparisons are always preferred for early-stage products

<details>
<summary>Answer</summary>

**B** — concurrent user volume is the deciding factor: enough simultaneous users supports a real randomized control group; too few means splitting traffic would starve both arms of a usable sample, favoring a pre/post design instead.

</details>

---

**Q14.** A "guardrail metric" in an experiment plan is:

- A) The same thing as the primary success metric, restated
- B) A metric that must not meaningfully worsen even if the primary metric improves
- C) A metric used only to calculate sample size
- D) A metric that replaces the primary metric if the experiment is inconclusive

<details>
<summary>Answer</summary>

**B** — a guardrail must not meaningfully worsen even as the primary metric improves; it's a check against winning on one metric while quietly breaking something else that matters.

</details>

---

**Q15.** Per Lecture 1 Section 5, why does a capstone that reports only good news, with zero setbacks or ambiguous results, raise a flag rather than impress?

- A) Good news is against the course's formatting requirements
- B) It usually means the student picked metrics that couldn't fail, which is itself a tell — real zero-to-one stories have a rough patch, and reading it well is the actual skill being measured
- C) Grading rubrics require at least one negative result
- D) It suggests the student didn't do enough work

<details>
<summary>Answer</summary>

**B** — an all-good-news capstone usually means the chosen metrics couldn't fail, which is itself a red flag; real zero-to-one launches produce ambiguous or setback-laden results, and reading those correctly — not avoiding them — is what this week actually measures.

</details>

**Scoring:** 13+ → your capstone judgment is solid; finish the mini-project with confidence. 10–12 → re-read the lecture sections behind your misses before finalizing your capstone's weakest section. <10 → re-read all three lectures from the top before submitting the mini-project; this week's frameworks are the synthesis of the entire course, and gaps here usually trace back to a specific earlier week worth revisiting.

---
