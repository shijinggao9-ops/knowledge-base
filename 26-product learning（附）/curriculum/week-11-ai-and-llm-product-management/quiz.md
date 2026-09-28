# Week 11 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 12. A mix of multiple-choice and short "what would you do" scenarios — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** What is the core structural problem with a brief like "can we get some AI in the product by next sprint"?

- A) It's too short to be a real brief.
- B) It names a technology before naming a user problem, leaving no scope or success metric to spec against.
- C) It doesn't mention a deadline.
- D) It should have come from Engineering, not the VP of Product.

<details>
<summary>Answer</summary>

**B** — "some AI by next sprint" names a solution with no user problem, scope, or metric attached, which is why Lecture 1 opens by insisting you name the job before the tool.

</details>

---

**Q2.** Which of these is the clearest sign a feature is a **deterministic**, not probabilistic, problem?

- A) Two competent people would draft somewhat different, both-reasonable answers.
- B) The input is open-ended free text.
- C) The same input always has exactly one correct, computable output.
- D) The task benefits from general-purpose reasoning.

<details>
<summary>Answer</summary>

**C** — determinism means the same input always maps to exactly one correct, computable output; (A) and (B) are signals pointing toward probabilistic/LLM territory instead.

</details>

---

**Q3.** Per the five-question fit checklist, a feature request whose input can only ever be one of six enumerable cases should generally be built as:

- A) A frontier-tier LLM call, because more capability is always safer
- B) A `CASE WHEN`/rules-based branch, not an LLM call
- C) A fine-tuned model trained from scratch
- D) A human-reviewed manual process only

<details>
<summary>Answer</summary>

**B** — a small, enumerable input space (fit-checklist question 1 failing) is the classic signal for a rules-based branch, not a model call.

</details>

---

**Q4.** In the build-vs-buy spectrum from Lecture 1, why is fine-tuning usually a *later* move rather than a first version?

- A) Fine-tuning is not possible on foundation models.
- B) It requires evidence of a specific, persistent gap that prompting alone hasn't closed — evidence you don't have yet on day one.
- C) It's always more expensive than every other option, in every case.
- D) It doesn't require any training data.

<details>
<summary>Answer</summary>

**B** — fine-tuning is a data-driven investment you make once you have evidence prompting alone has plateaued on a specific, recurring gap; you don't have that evidence on day one.

</details>

---

**Q5.** Why must cost per model call always be reasoned about together with expected call volume, not alone?

- A) Cost per call is always the same regardless of model tier.
- B) A cheap-per-call feature at massive volume can cost more in total than an expensive-per-call feature at low volume, and vice versa.
- C) Volume never actually affects total spend.
- D) Latency and cost are unrelated to volume.

<details>
<summary>Answer</summary>

**B** — cost per call alone tells you nothing about total spend; a cheap feature at huge volume and an expensive feature at tiny volume can land at similar total cost, or wildly different ones — you need both numbers together.

</details>

---

**Q6.** Loopline Copilot ships as "suggest-only." What does that mean for how much model quality is strictly required to ship safely?

- A) Model quality becomes irrelevant since a human reviews everything.
- B) Model quality must be higher than a full-autonomy version, since users see every mistake.
- C) The blast radius of a bad output is small (the user just ignores/edits a bad draft), which lowers the quality bar needed to ship responsibly compared to a full-autonomy version of the same feature.
- D) Suggest-only and full-autonomy require identical guardrails.

<details>
<summary>Answer</summary>

**C** — suggest-only keeps a human between the model's output and any real effect, shrinking the blast radius of a bad output and lowering how much quality is strictly required to ship responsibly, compared to the same model quality shipped with full autonomy.

</details>

---

**Q7.** Why is reporting one blended eval pass-rate average across all categories dangerous for a feature like Copilot?

- A) Averages are mathematically invalid for eval scores.
- B) It can hide a severe, specific weakness (e.g., near-0% on adversarial cases) behind a reassuring-looking overall number.
- C) Categories should never be scored separately.
- D) LLM-as-judge grading cannot produce a blended average.

<details>
<summary>Answer</summary>

**B** — Lecture 2's `v1` run showed this exactly: a blended ~55–60% average sounds like "needs polish," while the true story (near-0% on adversarial, near-100% on happy_path) is a serious, specific safety gap the average buries.

</details>

---

**Q8.** What is the main risk of relying on LLM-as-judge grading with no human spot-checking at all?

- A) LLM-as-judge cannot score anything numerically.
- B) It's always slower than human grading.
- C) The judge model can itself be wrong or drift, and with no human check, that drift goes undetected.
- D) LLM-as-judge only works on adversarial cases.

<details>
<summary>Answer</summary>

**C** — an LLM judge is itself a probabilistic system that can be wrong or drift over time; without periodic human spot-checks, nothing catches that drift.

</details>

---

**Q9.** What's the difference between offline and online evaluation?

- A) They are the same thing with different names.
- B) Offline evaluation runs a fixed golden set before shipping a change; online evaluation monitors real production traffic after shipping — and neither replaces the other.
- C) Online evaluation is only used for cost tracking, never quality.
- D) Offline evaluation requires a live production database.

<details>
<summary>Answer</summary>

**B** — offline evaluation is your pre-ship gate against a fixed golden set; online evaluation is your post-ship smoke detector on real traffic; you need both because offline testing can't cover every real input.

</details>

---

**Q10.** In the `ai_usage_log` data from Lecture 3, what specifically distinguished workspace 41's activity from normal usage?

- A) It had the highest total token count of any workspace.
- B) A concentrated burst of calls in seconds-apart succession, all ending in `error`, unlike the naturally spread-out, mostly-successful pattern from other workspaces.
- C) It used a different, more expensive model tier than everyone else.
- D) It was the only workspace on the free plan.

<details>
<summary>Answer</summary>

**B** — the tell wasn't token count or model tier, it was the cadence (seconds apart) combined with a 100% error rate concentrated in one workspace — the signature of a stuck retry loop, not organic use.

</details>

---

**Q11.** Why is "the prompt is built only from the requesting user's own goal text, with no cross-workspace data available to reason over" a stronger guardrail than an instruction telling the model not to leak other workspaces' data?

- A) It isn't stronger — instructions and architecture are equally reliable.
- B) It removes the failure mode structurally (there's nothing sensitive available to leak) rather than merely discouraging the model from a failure mode it technically still has access to.
- C) Instructions are always more reliable than architecture.
- D) It makes the feature cheaper to run.

<details>
<summary>Answer</summary>

**B** — removing the data from the prompt entirely eliminates the failure mode structurally; an instruction merely asks the model not to use access it still technically has, which is weaker.

</details>

---

**Q12.** A rate-limit rule for Copilot should be set at a threshold that is:

- A) As low as technically possible, to minimize all risk
- B) Loose enough to never block any legitimate usage pattern seen in real data, but tight enough to catch an anomalous burst early
- C) Based purely on the most expensive model tier's price, regardless of usage patterns
- D) Irrelevant, since a kill switch makes rate limits unnecessary

<details>
<summary>Answer</summary>

**B** — the rate limit has to be calibrated against real legitimate usage patterns in the data (loose enough not to block them) while still being tight enough to catch an anomaly early — a threshold picked with no reference to real data is just a guess.

</details>

---

**Q13.** A cost-cap response to a traffic spike that cuts every workspace's rate limit by the same percentage, regardless of usage pattern, is a weak response mainly because:

- A) It's technically impossible to implement.
- B) It punishes genuine, legitimate growth exactly as hard as it punishes an abuse or bug pattern, instead of distinguishing between them.
- C) Rate limits can only be applied per-user, never per-workspace.
- D) It always costs more to implement than a spend cap.

<details>
<summary>Answer</summary>

**B** — a flat percentage cut treats a genuine growth spike and an abuse/bug pattern identically, throttling the exact success you were hoping the feature would produce along with the actual problem.

</details>

---

**Q14.** What should an acceptance criterion for a probabilistic (LLM-backed) feature's launch readiness look like?

- A) "The model works correctly on all inputs" — no further detail needed.
- B) Something unverifiable, since output isn't deterministic and can't be tested.
- C) A specific, checkable threshold tied to something you actually built — e.g., "adversarial category pass rate ≥ 90% on the golden eval set" — not a vague promise the feature is "good."
- D) Identical to a deterministic feature's acceptance criteria, word for word.

<details>
<summary>Answer</summary>

**C** — a real acceptance criterion for a probabilistic feature is a specific, checkable threshold tied to an artifact you built (an eval pass rate, a rate-limit behavior, a fallback flow) — not an unverifiable claim that the feature "works" or "is good."

</details>

**Scoring:** 12+ → start Week 12. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's concepts compound directly into the capstone spec.

---
