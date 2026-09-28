# Week 2 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 3. A mix of multiple-choice, "what's wrong with this question," and "what does this query return" — the answer key explains the *why*, not just the letter.

---

**Q1.** A team wants to know whether people can successfully complete checkout using a new prototype. This calls for:

- A) Generative research
- B) Evaluative research
- C) Neither — this needs an A/B test on live traffic only
- D) A diary study

<details>
<summary>Answer</summary>

**B** — testing a specific prototype for task success is evaluative research; you're validating a solution, not exploring a problem.

</details>

---

**Q2.** Which of these is a hallmark of **generative** research, as opposed to evaluative?

- A) You walk in with a specific prototype to test
- B) The output is a pass/fail verdict on a design
- C) You walk in without a fixed solution in mind, exploring a problem space
- D) It requires a statistically significant sample size

<details>
<summary>Answer</summary>

**C** — generative research explores without a fixed solution; evaluative research (A, B) tests one, and statistical significance (D) isn't what defines the family.

</details>

---

**Q3.** A PM skips interviews and goes straight to usability-testing a mockup of a proposed feature. The test goes well — people can use it — but the feature flops after launch. What's the most likely explanation, per Lecture 1?

- A) The usability test method was flawed
- B) The prototype was too polished
- C) The team never validated the underlying problem was real or a priority, so a usable solution to the wrong problem was still the wrong problem
- D) Usability tests are never predictive of launch outcomes

<details>
<summary>Answer</summary>

**C** — a usability test can only tell you whether people *can use* a solution, never whether it solves a problem worth solving. Skipping generative research means that second question never got asked.

</details>

---

**Q4.** Which question passes the Mom Test?

- A) "Would you use a feature that shows everyone's availability in one place?"
- B) "Tell me about the last time you needed someone to cover your shift."
- C) "Don't you think manager approval takes too long?"
- D) "Do you think a marketplace feature would help people like you?"

<details>
<summary>Answer</summary>

**B** — it asks about a specific past event, with no solution mentioned and no presupposed answer. A, C, and D all pitch a solution or presuppose a problem/opinion.

</details>

---

**Q5.** Per the Mom Test, why is "would you use X?" a weak interview question?

- A) It's grammatically incorrect
- B) It asks about hypothetical future behavior, which people are bad at predicting and prone to answering agreeably
- C) It's too short to yield a useful answer
- D) It can only be asked in a survey, not an interview

<details>
<summary>Answer</summary>

**B** — people are bad at predicting their own future behavior and tend to answer hypotheticals agreeably, since it costs them nothing.

</details>

---

**Q6.** A participant describes texting 30 coworkers in a group chat to find shift coverage instead of using the app's built-in messaging. Per Lecture 2, this workaround is:

- A) Irrelevant — it's not a stated opinion about the product
- B) Weak evidence, since it's just one person's habit
- C) Strong evidence of an unmet need — people don't build workarounds for problems that don't matter to them
- D) A usability bug report, not a research finding

<details>
<summary>Answer</summary>

**C** — a workaround is direct behavioral evidence of an unmet need; people invest effort in workarounds only for problems that actually matter to them.

</details>

---

**Q7.** In live interview note-taking, what's the difference between a `Q:` note and an `I:` note?

- A) `Q:` is a question you asked; `I:` is the participant's answer
- B) `Q:` is a verbatim quote (evidence); `I:` is your own in-the-moment interpretation (a provisional guess)
- C) There is no difference — both capture the same thing
- D) `Q:` is only used in surveys, `I:` only in interviews

<details>
<summary>Answer</summary>

**B** — `Q:` captures exact, verifiable evidence; `I:` flags your own real-time interpretation as provisional, so it doesn't quietly get treated as fact later.

</details>

---

**Q8.** Which survey item is written to avoid bias, per Lecture 3?

- A) "How much do you love the new schedule view?"
- B) "Is the app fast and easy to use?"
- C) "How would you rate the schedule view's loading speed, from very slow to very fast?"
- D) "Wouldn't a faster app help you get through your shift?"

<details>
<summary>Answer</summary>

**C** — neutral wording, a specific measurable dimension (speed), and labeled endpoints. A is loaded ("love"), B is double-barreled, D is leading/rhetorical.

</details>

---

**Q9.** What's wrong with the survey question "Is the app fast and easy to use?"

- A) It's a leading question
- B) It's double-barreled — a "no" answer doesn't tell you whether it's slow, hard to use, or both
- C) It uses absolute wording
- D) It's a hypothetical about future behavior

<details>
<summary>Answer</summary>

**B** — "fast and easy to use" bundles two separate dimensions into one question; a "no" is uninterpretable.

</details>

---

**Q10.** Given `survey_responses.would_pay` is `NULL` for every `shift_worker` row (because that question is only shown to managers), which query correctly counts how many managers said yes?

- A) `SELECT COUNT(*) FROM survey_responses WHERE would_pay = TRUE;`
- B) `SELECT COUNT(*) FROM survey_responses WHERE would_pay = TRUE AND segment = 'manager';`
- C) `SELECT COUNT(*) FROM survey_responses WHERE would_pay <> FALSE;`
- D) `SELECT COUNT(would_pay) FROM survey_responses;`

<details>
<summary>Answer</summary>

**B** — you must filter to `segment = 'manager'` and count `would_pay = TRUE`. A over-counts if any non-manager row somehow has `TRUE`; C is wrong because `NULL <> FALSE` evaluates to `NULL` (unknown), which `WHERE` never treats as true, so it would (correctly, by luck) exclude NULLs here but is confusing and non-obvious — B is the clear, correct, readable choice. D counts all non-null responses, not just the "yes" ones.

</details>

---

**Q11.** Why would writing `would_pay = FALSE` to mean "didn't say yes" be a mistake in this schema?

- A) `FALSE` is not a valid SQL value
- B) It would incorrectly count every shift-worker row (where the question was never asked, hence `NULL`) as an explicit "no"
- C) `would_pay` should be a `TEXT` column, not `BOOLEAN`
- D) It would cause a syntax error

<details>
<summary>Answer</summary>

**B** — `NULL` here means "not applicable / not asked." Treating it as `FALSE` recodes every shift-worker's *unasked* question as an explicit negative answer they never gave — a fabricated data point.

</details>

---

**Q12.** In affinity mapping, why does a strong finding lead with `COUNT(DISTINCT participant_id)` per theme rather than the raw count of quotes?

- A) `COUNT(DISTINCT ...)` runs faster
- B) One chatty participant repeating the same point shouldn't outweigh several different participants each independently raising it once
- C) Raw quote counts are not valid SQL
- D) There is no meaningful difference between the two counts

<details>
<summary>Answer</summary>

**B** — the whole point of affinity mapping is finding what's broadly true across many people, not what one person said the most; participant count protects against one loud voice skewing the read.

</details>

---

**Q13.** `SELECT theme, COUNT(*) FROM interview_quotes GROUP BY theme;` run against the seed data — what does this omit that a careful synthesis query should include, per Lecture 3?

- A) Nothing — this is already the correct synthesis query
- B) A `COUNT(DISTINCT participant_id)` column, and an `ORDER BY` to surface the most-corroborated theme first
- C) A `JOIN` to the `survey_responses` table, which is mandatory for any `GROUP BY`
- D) A `WHERE theme IS NOT NULL` clause, without which the query is a syntax error

<details>
<summary>Answer</summary>

**B** — the plain `GROUP BY` gives raw quote counts with no participant-independence signal and no ordering — both of which Lecture 3 says a synthesis query needs to avoid over-weighting one participant and to surface the strongest theme first. (`WHERE theme IS NOT NULL` is good practice but isn't required for the query to run — untagged rows would just show up as a `NULL` theme group, not cause an error.)

</details>

---

**Q14.** A finding says: "Manager approval is the primary bottleneck in shift swapping — we should build a swap marketplace that removes manager approval entirely." What's wrong with this as a *research finding*?

- A) Nothing — it's a well-evidenced finding
- B) It jumps from a validated problem straight to a specific solution, which the research described didn't actually test or validate
- C) It should have used a p-value
- D) "Bottleneck" is not a valid research term

<details>
<summary>Answer</summary>

**B** — the evidence supports "manager approval is a bottleneck" as a validated *problem*. It does not, by itself, establish that removing approval entirely (a specific solution) is the right fix — that requires its own research or reasoning, covered starting next week.

</details>

**Scoring:** 12+ → start Week 3. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's discipline compounds directly into every later week's research.

---
