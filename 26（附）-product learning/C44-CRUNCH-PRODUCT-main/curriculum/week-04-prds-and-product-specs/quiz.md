# Week 4 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 5. A mix of multiple-choice and short "what's wrong with this spec" questions — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In the seven-section PRD skeleton from Lecture 1, which section should usually be the **shortest**?

- A) Requirements
- B) Non-goals
- C) Context
- D) Edge cases

<details>
<summary>Answer</summary>

**C** — Context should be short (3–6 sentences); non-goals and requirements are typically the *longest* sections, not context.

</details>

---

**Q2.** A PRD's non-goals section exists primarily to:

- A) List every feature the product will never build, ever
- B) Explicitly name adjacent things deliberately excluded from *this* iteration, so scope creep has to be argued for instead of assumed
- C) Make the document look more thorough to leadership
- D) Replace the need for a success-metrics section

<details>
<summary>Answer</summary>

**B** — Non-goals explicitly name things deliberately out of scope *for this iteration*, turning silent scope creep into something that has to be argued for on the record.

</details>

---

**Q3.** Which of these is a properly formed user story?

- A) "Add Slack notifications for stuck tasks."
- B) "As an engineering manager, I want to be notified in Slack when a task goes stuck, so that I can intervene before the sync."
- C) "Build the notification microservice."
- D) "Notifications should be fast."

<details>
<summary>Answer</summary>

**B** — the only option in full `As a / I want / so that` form, naming a role, a capability, and an outcome. (A) and (C) are feature/task descriptions; (D) is an unfalsifiable quality claim.

</details>

---

**Q4.** A story reads: "Refactor the alert-delivery pipeline to use a message queue." Which INVEST letter does it most clearly fail?

- A) Independent
- B) Estimable
- C) Valuable (no direct user benefit stated)
- D) Small

<details>
<summary>Answer</summary>

**C** — Valuable. There's no user benefit named — "refactor the pipeline" serves an engineering goal, not a user's job. (It may also arguably fail Estimable/Small depending on scope, but Valuable is the clearest, most direct failure.)

</details>

---

**Q5.** Which acceptance criterion is written correctly, in Given/When/Then form, with a checkable condition?

- A) "The alert should feel timely."
- B) "Given a task has been untouched for 48 hours, when the threshold is crossed, then a Slack message is sent within 5 minutes."
- C) "Notifications work correctly."
- D) "The manager is happy with the alert."

<details>
<summary>Answer</summary>

**B** — has a real Given/When/Then structure and a checkable number ("within 5 minutes"). The others are unfalsifiable feelings.

</details>

---

**Q6.** Why is it useful for a story's acceptance criteria to include at least one boundary case (e.g., testing "47 hours 55 minutes," not just "48 hours")?

- A) It isn't useful — happy-path criteria are sufficient.
- B) Boundary cases are where off-by-one and timing bugs actually live; testing only the exact threshold misses whether the logic fires *early*.
- C) QA requires a minimum of two criteria per story regardless of content.
- D) Boundary cases replace the need for a non-goals section.

<details>
<summary>Answer</summary>

**B** — boundary cases catch off-by-one and premature-firing bugs that a single "at the threshold" test would miss entirely.

</details>

---

**Q7.** What is a "definition of done" (DoD), and how does it differ from acceptance criteria?

- A) They're the same thing, just different names.
- B) DoD is a floor that applies across every story in a feature (e.g., "instrumented," "flagged for gradual rollout"); acceptance criteria are specific to one story's behavior.
- C) DoD only applies to bugs, not new features.
- D) Acceptance criteria are optional if a DoD exists.

<details>
<summary>Answer</summary>

**B** — DoD is a floor across every story (instrumentation, rollout, no P0 bugs); acceptance criteria are specific, per-story pass/fail behavior. Both are needed; they serve different purposes.

</details>

---

**Q8.** Which of these is an example of a genuine **edge case**, per Lecture 3's five categories, rather than a happy-path requirement?

- A) "When a task crosses 48 hours untouched, send an alert."
- B) "When a task is reassigned one hour before the alert threshold, does the stuck-clock reset?"
- C) "The alert should include the task title."
- D) "Managers can view their team's tasks."

<details>
<summary>Answer</summary>

**B** — a real edge case: a timing/reassignment scenario at the story's boundary. (A), (C), (D) are core happy-path requirements, not edge cases.

</details>

---

**Q9.** Why does Lecture 3 insist that an unhandled edge case is "a decision made by accident," rather than just an oversight to fix later?

- A) Because QA is legally required to catch every edge case.
- B) Because every edge case implies *some* system behavior will occur whether or not a PM chose it — silence doesn't prevent the behavior, it just means nobody deliberately chose it.
- C) Because edge cases never actually occur in production.
- D) Because engineers always choose the correct behavior by default.

<details>
<summary>Answer</summary>

**B** — some behavior will occur regardless of whether a PM specified it; not deciding doesn't prevent the behavior, it just means the behavior wasn't chosen deliberately.

</details>

---

**Q10.** In the instrumentation section of a PRD, why write the actual SQL queries for your success metrics *during* spec writing, rather than after launch?

- A) SQL syntax is required by most PRD templates.
- B) Writing the query early can surface a real instrumentation gap (e.g., no way to link an alert to the task it was about) while it's still cheap to fix, instead of after launch when the data is unrecoverable.
- C) It replaces the need to write acceptance criteria.
- D) Engineers require pre-written SQL before they'll estimate a story.

<details>
<summary>Answer</summary>

**B** — writing the query early exposes real gaps (e.g., missing linkage between an alert and its outcome) while they're still cheap and easy to fix, rather than discovering "we can't actually measure this" after launch.

</details>

---

**Q11.** A feature's events are stored in a generic table with an `event_name` column and a flexible JSON `properties` column (as in this week's seed schema). What is the main advantage of this pattern over adding a brand-new rigid table per event type?

- A) It's required by SQL syntax.
- B) It lets you add new event types and event-specific fields without a schema migration for every new event, which is convenient early on — though very high-volume events may later justify dedicated typed columns for performance.
- C) JSON columns are always faster to query than typed columns.
- D) It removes the need for a `team_id` or `user_id` on each event.

<details>
<summary>Answer</summary>

**B** — flexible JSON properties avoid a migration per new event type early on; the trade-off (mentioned in Exercise 3's stretch) is that very high-volume, frequently-queried fields may eventually justify dedicated typed columns for performance.

</details>

---

**Q12.** A success metric in a PRD reads: "Managers love the feature (measured via NPS)." What's the main problem with this as a *feature-specific* success metric?

- A) NPS surveys are never a valid research method.
- B) It's not falsifiable against this specific feature's behavior — it's a broad sentiment metric that isn't tied to a specific, nameable event or query the feature itself produces.
- C) NPS should only be measured once per year.
- D) There is no problem; it's a fine success metric as written.

<details>
<summary>Answer</summary>

**B** — "managers love it" via general NPS isn't tied to any specific, measurable behavior this feature produces — it's not falsifiable *against this feature* specifically.

</details>

---

**Q13.** What is a "guardrail metric," and why does Lecture 1's Stuck Task Alerts example include one (opt-out rate)?

- A) A guardrail metric replaces the primary success metric.
- B) A guardrail metric tells you if the feature is doing *harm* even while the primary metric looks fine — e.g., managers opting out en masse would mean the alert is too noisy, a signal the primary "time to resolution" metric alone wouldn't catch.
- C) Guardrail metrics are only used in A/B testing, never in a PRD.
- D) A guardrail metric is another name for a non-goal.

<details>
<summary>Answer</summary>

**B** — a guardrail catches harm the primary metric wouldn't reveal on its own; opt-out rate rising would mean the feature is working "successfully" by one measure while actively annoying users by another.

</details>

---

**Q14.** An open question in a PRD reads: "Should alerts fire during a manager's off-hours?" What makes this a *well-formed* open question, per Lecture 1?

- A) It has an assigned owner and a point by which it needs to be resolved — an open question with no owner tends to never get answered.
- B) It doesn't need an owner; open questions are informational only.
- C) It should be answered inside the PRD itself before publishing, never left open.
- D) Open questions are a sign the PRD isn't ready to share.

<details>
<summary>Answer</summary>

**A** — a well-formed open question names an owner and a resolve-by point; an ownerless open question tends to sit unresolved indefinitely.

</details>

**Scoring:** 12+ → start Week 5. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; this week's technique compounds directly into Week 5's prioritization work and Week 6's SQL analytics.

---
