# Week 8 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 9. A mix of multiple-choice and short "what's wrong here" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In a flow map, what is a "decision point"?

- A) A screen with a lot of text
- B) A fork where the next screen depends on a choice or condition
- C) The final screen in a flow
- D) A place the user can exit the flow

<details>
<summary>Answer</summary>

**B** — a decision point is a fork where the next screen depends on a choice or condition (e.g., "does the org have a saved card?").

</details>

---

**Q2.** The most common flow-mapping mistake beginners make is:

- A) Using too much detail
- B) Only mapping the happy path and forgetting the unhappy/failure path
- C) Using a diagram instead of a numbered list
- D) Including too many exit ramps

<details>
<summary>Answer</summary>

**B** — the single most common flow-mapping mistake is mapping only the golden/happy path and never writing down the failure branch, which is usually where the worst friction lives.

</details>

---

**Q3.** Which of Nielsen's heuristics does a spinner with no time estimate and no feedback violate?

- A) #4 Consistency and standards
- B) #1 Visibility of system status
- C) #7 Flexibility and efficiency of use
- D) #10 Help and documentation

<details>
<summary>Answer</summary>

**B** — heuristic #1, visibility of system status: the system should keep users informed with reasonable feedback in reasonable time. A spinner with nothing to say violates this directly.

</details>

---

**Q4.** A usability-problem severity rating of **4** on Nielsen's 0–4 scale means:

- A) Cosmetic only, fix if there's time
- B) Not a usability problem at all
- C) Major, should be high priority
- D) Catastrophe — imperative to fix before release

<details>
<summary>Answer</summary>

**D** — 4 is "catastrophe, imperative to fix before release." (0 = not a problem, 1 = cosmetic, 3 = major.)

</details>

---

**Q5.** What is the core difference between a usability test and an A/B test?

- A) A usability test needs a bigger sample size
- B) A usability test answers *why* people struggle; an A/B test answers *which* variant performs better on average
- C) They are two names for the same method
- D) A/B tests are qualitative, usability tests are quantitative

<details>
<summary>Answer</summary>

**B** — usability tests are qualitative and explain *why*; A/B tests are quantitative and tell you *which* version wins, at scale. They're complementary, not interchangeable.

</details>

---

**Q6.** Which of these is a properly written goal-based usability-test task?

- A) "Click the gear icon, then Billing, then Update card."
- B) "Your team grew to 12 people — get everyone paid access."
- C) "Tell me if you like the checkout flow."
- D) "Rate this screen from 1 to 5."

<details>
<summary>Answer</summary>

**B** — it states the user's goal in their own language and doesn't leak the UI path. A is a leaky task (tells them exactly where to click), C and D aren't tasks at all — they're opinion questions.

</details>

---

**Q7.** During a think-aloud session, a participant is silent and visibly stuck for 30 seconds. What should the moderator do?

- A) Immediately tell them where to click
- B) End the session
- C) Stay quiet and let the struggle continue; only intervene if truly stuck for 60–90+ seconds, and log it as a failure if you do
- D) Ask "do you like this screen?"

<details>
<summary>Answer</summary>

**C** — stay quiet through normal struggle; only step in once someone is genuinely stuck for 60–90+ seconds, and treat any rescue as a logged failure for that task, not a success.

</details>

---

**Q8.** The "5-user rule" claims that testing with 5 users:

- A) Guarantees you'll find 100% of usability problems
- B) Finds about 85% of a flow's usability problems, with diminishing new findings per additional user beyond 5
- C) Is only valid for A/B tests
- D) Replaces the need for a heuristic evaluation entirely

<details>
<summary>Answer</summary>

**B** — roughly 85% of usability problems surface with 5 users, with sharply diminishing new findings from additional users beyond that. It's a heuristic, not a guarantee, and it doesn't replace a heuristic evaluation — they're complementary methods.

</details>

---

**Q9.** Why does this course require usability-test results to be logged in a SQL table rather than a spreadsheet?

- A) Spreadsheets can't store text
- B) SQL is required by law for user research
- C) A `GROUP BY` query produces a reproducible, auditable aggregate; a spreadsheet pivot or manual tally is easy to get silently wrong
- D) Spreadsheets are slower to open

<details>
<summary>Answer</summary>

**C** — the whole reason: a `GROUP BY` query is reproducible and auditable by anyone who re-runs it; a spreadsheet pivot table or hand tally is one silent range-selection mistake away from a confidently wrong number.

</details>

---

**Q10.** Rank by priority: Issue A (severity 4, hit 1 of 5 sessions) vs. Issue B (severity 1, hit 5 of 5 sessions). What's the right way to reason about this?

- A) Issue B always wins because it's more frequent
- B) Issue A always wins because severity outranks frequency
- C) There's no formula — weigh what the severity-4 issue actually costs (e.g., a lost payment) against how many people the severity-1 issue annoys, and judge
- D) They're equal, flip a coin

<details>
<summary>Answer</summary>

**C** — there's no fixed formula; you weigh the actual cost of the rare-but-severe issue against the actual cost of the common-but-minor one and make a judgment call, which is exactly why severity × frequency is a lens, not an algorithm.

</details>

---

**Q11.** What's the correct structure of an "I Wish" statement in a critique session?

- A) A vague preference ("I wish this looked nicer")
- B) A specific problem, tied to a user goal or heuristic, not a taste preference
- C) An instruction telling the designer exactly what to build instead
- D) A comparison to a competitor's product with no explanation

<details>
<summary>Answer</summary>

**B** — an "I Wish" names a specific problem tied to a user goal or heuristic. Vague preferences (A) aren't actionable; dictating the exact solution (C) oversteps into the designer's job.

</details>

---

**Q12.** According to WCAG AA, the minimum contrast ratio for normal-size body text is:

- A) 2:1
- B) 3:1
- C) 4.5:1
- D) 7:1

<details>
<summary>Answer</summary>

**C** — 4.5:1 for normal-size text under WCAG AA (3:1 applies to large text, 18pt+/14pt+ bold).

</details>

---

**Q13.** A finding is a total blocker for keyboard-only users (they cannot complete the flow at all, not just with more effort). Under the four-input trade-off framework, which input does this most strongly affect?

- A) Cost only
- B) User impact — a total blocker for a class of users outweighs cost/effort considerations in most cases
- C) Reversibility only
- D) None of the four inputs apply to blockers

<details>
<summary>Answer</summary>

**B** — a total blocker is a user-impact issue of the highest order; it changes the calculus even against a large cost estimate, because "some users literally cannot use this at all" outweighs most cost/effort arguments.

</details>

---

**Q14.** Why is "we'll fix accessibility later" not a neutral, no-decision default?

- A) It isn't a real sentence
- B) Choosing to defer a fix is itself a prioritization decision — silence just means nobody owns it or committed to a date
- C) Accessibility fixes are always free, so there's no reason to ever defer them
- D) Legal compliance makes this choice automatically for you in every jurisdiction

<details>
<summary>Answer</summary>

**B** — deferring is itself a decision, made by whoever controls the roadmap; treating it as "no decision" just means nobody has committed to a date or owns the risk of shipping without the fix.

</details>

**Scoring:** 12+ → start Week 9. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; critique and trade-off reasoning compounds into every later week of this course.

---
