# Week 7 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 8. A mix of multiple-choice and short reasoning — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Which of these is a properly formed hypothesis, per Lecture 1's if/then/because template?

- A) "This feature will improve engagement."
- B) "If we add a Quick Add button, then session-level task-creation rate will increase by roughly 3 points, because it removes the multi-click friction that currently causes users to skip logging small tasks."
- C) "Users will probably like the new button."
- D) "We should ship the Quick Add button and see what happens."

<details>
<summary>Answer</summary>

**B** — it names the change, the metric, a rough magnitude, and a causal mechanism, and is falsifiable. (A) is vague with no metric or mechanism; (C)/(D) aren't hypotheses at all.

</details>

---

**Q2.** Why can an experiment have only **one** primary metric, but several guardrail metrics?

- A) Statistical software can only test one metric at a time.
- B) Checking many metrics and picking whichever moved inflates the false-positive rate (multiple comparisons); guardrails only veto, they don't independently declare a win.
- C) Guardrail metrics are always less important than the primary metric.
- D) There's no real difference — it's just naming convention.

<details>
<summary>Answer</summary>

**B** — checking many metrics and picking a winner is a multiple-comparisons problem that manufactures false positives; guardrails exist only to veto a ship decision, not to offer alternate ways to declare success.

</details>

---

**Q3.** Loopline is testing a change to a Slack alert that posts to a shared team channel. Why is randomizing by **individual user** (rather than by team) the wrong unit of randomization here?

- A) Individual randomization is always statistically weaker.
- B) Slack doesn't support per-user message targeting.
- C) A treated user's alert is visible to the whole shared channel, so untreated ("control") teammates on the same team would also be exposed — contaminating the comparison (a SUTVA violation).
- D) Users can't be tracked individually in analytics tools.

<details>
<summary>Answer</summary>

**C** — the shared Slack channel means a "control" team member can still be exposed to the alert's effect through a treated teammate, which is exactly the SUTVA contamination Lecture 1 §3 describes. Team-level randomization avoids this because the whole team shares one assignment.

</details>

---

**Q4.** What does a **minimum detectable effect (MDE)** represent, and who should set it?

- A) The largest effect a statistician thinks is plausible; set by the data science team.
- B) The smallest true effect the test should reliably be able to detect; set as a business decision about what magnitude would actually change the ship decision.
- C) The average effect size found in past experiments; set by looking at historical data alone.
- D) A fixed statistical constant that never changes between tests.

<details>
<summary>Answer</summary>

**B** — MDE is a business call about the smallest effect worth detecting (i.e., worth changing the ship decision), made *before* the power calculation, not derived from statistics alone.

</details>

---

**Q5.** Holding the baseline rate, α, and power fixed, if you cut your target MDE in half, the required sample size roughly:

- A) Halves
- B) Stays the same
- C) Doubles
- D) Quadruples

<details>
<summary>Answer</summary>

**D** — sample size is roughly inversely proportional to the *square* of the MDE, so halving the MDE roughly quadruples the required sample (Lecture 2's worked table: 2pp→7,356, 5pp→1,221 — almost a 6× difference for less than a 3× change in MDE).

</details>

---

**Q6.** What does **α = 0.05** protect against, specifically?

- A) A 5% chance of missing a real effect
- B) A 5% chance of wrongly declaring a win when there is truly no effect
- C) A guarantee the result is correct 95% of the time
- D) A 5% margin of error on the sample size calculation

<details>
<summary>Answer</summary>

**B** — α is the tolerance for a false positive: wrongly rejecting the null (declaring a win) when there's truly no effect.

</details>

---

**Q7.** What does **power = 0.80** mean?

- A) 80% of your users will convert.
- B) If a true effect of exactly your MDE exists, you'll correctly detect it (reach significance) about 80% of the time.
- C) You need 80% of your planned sample size to get a valid result.
- D) There's an 80% chance your hypothesis is correct.

<details>
<summary>Answer</summary>

**B** — power is the probability of correctly detecting a real effect of the assumed size (your MDE), not a statement about your users or your hypothesis's truth.

</details>

---

**Q8.** An experiment finishes with p = 0.001. Which statement correctly describes what that p-value means?

- A) There is a 99.9% chance the hypothesis is true.
- B) If there were truly no effect, a result this extreme (or more) would occur about 0.1% of the time by chance alone.
- C) The effect size is definitely large enough to matter for the business.
- D) The test needs 99.9% more data to be trustworthy.

<details>
<summary>Answer</summary>

**B** — a p-value is a statement about how surprising the observed data (or more extreme) would be *if the null hypothesis were true* — not a probability that the hypothesis is true or false. Options A, C, and D all misstate what a p-value measures.

</details>

---

**Q9.** A test's result is p = 0.02 (significant) with a 95% CI on the lift of [0.05%, 0.15%]. What's the most accurate read?

- A) It's not significant, since the interval is narrow.
- B) It's statistically significant, but the effect may be too small to be practically meaningful — check the CI's lower bound against your original MDE.
- C) A significant p-value always means the result matters for the business.
- D) The confidence interval is irrelevant once you have a p-value.

<details>
<summary>Answer</summary>

**B** — statistical significance and practical significance are different questions; a very narrow, very small CI can be "significant" yet too small to matter for the business. Always compare the CI's lower bound to your original MDE.

</details>

---

**Q10.** An experiment was randomized by **team** (20 control, 20 treatment teams), but each team logged several individual "stuck incidents." Why is it wrong to pool every incident across all teams into one large proportion test instead of comparing team-level rates?

- A) Proportion tests only work with exactly two groups.
- B) Incidents from the same team aren't independent of each other (a team's overall conditions affect all its incidents together), so pooling pretends you have far more independent samples than you do — pseudoreplication — which artificially shrinks the p-value.
- C) SQL can't aggregate incidents by team.
- D) It's not wrong; pooling is always more accurate with more data points.

<details>
<summary>Answer</summary>

**B** — incidents within the same team share team-level conditions and aren't independent; pooling them inflates the apparent sample size and shrinks the p-value artificially (pseudoreplication). The correct analysis compares team-level rates, matching the unit of randomization.

</details>

---

**Q11.** A PM checks an experiment's cumulative p-value every day and stops the test the first day it dips below 0.05, even though the test was planned to run 14 days. What trap is this, and what does it do to the true false-positive rate?

- A) Multiple comparisons; it has no effect on the false-positive rate as long as α = 0.05 is used each time.
- B) Peeking / optional stopping; it inflates the true false-positive rate well above the nominal 5%, because you're effectively running many tests and keeping the best-looking one.
- C) Novelty effect; it causes the effect to be understated.
- D) Sample ratio mismatch; it means the randomization was broken.

<details>
<summary>Answer</summary>

**B** — this is peeking / optional stopping. Stopping at the first significant-looking day (out of many looks) means you're effectively running many tests and keeping the best result, which inflates the true false-positive rate well above the nominal 5% — exactly what Lecture 3's simulated null-effect dataset demonstrated (3 of 14 days crossed p < 0.05 with zero true effect).

</details>

---

**Q12.** You check 20 different metrics/segments after a test with no pre-registered primary metric, and one comes back at p = 0.04. Using a simple Bonferroni correction for 20 comparisons, what p-value would that single finding actually need to clear to be treated as significant?

- A) 0.05 (no change needed)
- B) 0.0025 (0.05 ÷ 20)
- C) 1.0 (Bonferroni makes everything significant)
- D) 0.04 exactly, since that's what was observed

<details>
<summary>Answer</summary>

**B** — Bonferroni divides α by the number of comparisons: 0.05 ÷ 20 = 0.0025. A p = 0.04 finding does not clear that corrected bar and should not be treated as significant on its own.

</details>

---

**Q13.** What's the key difference between a **novelty effect** and a **primacy effect**, and which one causes you to *overstate* a feature's true long-run benefit if you only measure the first few days?

- A) They're the same thing; both overstate the benefit.
- B) Novelty effect (a temporary spike from users trying something new) overstates the benefit if measured too early; primacy effect (initial friction from an unfamiliar change) tends to understate it.
- C) Primacy effect always overstates; novelty effect always understates.
- D) Neither affects early measurement — both only matter after months.

<details>
<summary>Answer</summary>

**B** — a novelty effect is a temporary spike from users trying something new, which fades — measuring only the first few days overstates the durable effect. A primacy effect is initial friction/unfamiliarity that recovers over time, which tends to understate the true effect if measured too early.

</details>

---

**Q14.** Loopline can't randomize a pricing-page redesign (legal has vetoed showing different visitors different prices concurrently), but it can toggle the whole page between the old and new layout over alternating weeks. Which design is this, and what's its main statistical cost compared to a standard randomized test?

- A) A holdout group; the cost is a permanently withheld control slice.
- B) A switchback design; the cost is far fewer independent data points (time periods, not individual users), so it typically needs either many periods or a much larger MDE, and it's vulnerable to calendar confounds between periods.
- C) A diff-in-diff design; the cost is needing an external comparison company.
- D) A standard A/B test; there is no added cost.

<details>
<summary>Answer</summary>

**B** — this is a switchback design. Its cost is that the unit of analysis becomes time periods rather than individuals, giving far fewer independent data points and requiring either many periods or a larger tolerable MDE, plus exposure to day-of-week/calendar confounds between periods.

</details>

---

**Q15.** In a difference-in-differences (diff-in-diff) analysis, what does subtracting the comparison group's before/after change accomplish that a simple treated-group before/after cannot?

- A) It removes anything that would have happened anyway (seasonality, broader trends, unrelated events) that affected both groups, isolating the effect attributable to the change.
- B) It doubles the statistical power automatically.
- C) It eliminates the need for a large sample size.
- D) It converts the analysis into a true randomized experiment.

<details>
<summary>Answer</summary>

**A** — diff-in-diff subtracts the comparison group's own trend (which captures seasonality, broader product trends, unrelated events) from the treated group's before/after change, isolating the portion of the change plausibly caused by the treatment — something a raw before/after on the treated group alone cannot do, since it can't distinguish "caused by our change" from "would have happened anyway."

</details>

**Scoring:** 13+ → start Week 8. 10–12 → re-read the lecture sections behind your misses, especially Lecture 2 §4 (unit of analysis) and Lecture 3 §1 (peeking) if those were among them. <10 → re-read all three lectures from the top; this week's concepts compound directly into how you'll read every experiment result for the rest of your PM career.

---
