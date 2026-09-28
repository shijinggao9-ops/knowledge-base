# Challenge 1 — Draw the PM/PO/Eng-Lead Responsibility Line

**Time:** ~75 minutes. **Difficulty:** Medium. **No single right answer.**

## The scenario

You've just joined Loopline as a PM. The company is 45 people, growing fast, and — like most companies this size — its org chart has more titles than clean role definitions. You'll spend your first month watching decisions happen and quietly noting who actually made the call versus who was supposed to. Your job in this challenge is the hardest and most valuable skill from Lecture 1: **drawing the responsibility line before the ambiguity causes a real conflict.**

There is no answer key. A thoughtful PM and a thoughtful engineering lead might draw slightly different lines for the same scenario — the value isn't in reaching a universal answer, it's in **stating your reasoning clearly enough that a reasonable person could push back on a specific claim**, not just your vibe.

## Your task

For each scenario below:

1. **State who should own the final call** — PM, PO (if Loopline has a separate PO — decide whether it does, and say why), engineering lead, or "shared, with [specific person] as tiebreaker."
2. **Name the one sentence of reasoning** behind that call, referencing what that role structurally owns (Lecture 1, Section 2–4).
3. **Note the failure mode** if the wrong person made this call instead — what specifically goes wrong?

Put all of this in `challenge-01.md`.

## The scenarios

1. **A customer's contract renewal depends on shipping SSO by end of quarter. Engineering says the honest estimate is 6 weeks, not the 4 the sales team promised the customer.** Who decides whether to commit to 4 weeks, slip the date, or descope something else to make room?

2. **Design wants a full onboarding redesign (3 weeks) to fix the activation drop from Lecture 3's worked example. Engineering has a targeted fix (half a day) that addresses the specific hypothesis from the user interviews.** Who decides which one ships first — and is "both, in sequence" a legitimate answer, or a way to avoid the decision?

3. **Two engineers are mid-argument about whether the new Slack integration should be built as a polling job or a webhook listener.** Where's the line — should the PM have an opinion here at all?

4. **A single enterprise prospect (a $400K/year potential deal) asks for a custom feature that no other segment has requested.** Who decides whether Loopline builds one-off customer-specific work, and what's the risk of getting this call wrong in either direction?

5. **The backlog for next sprint has 14 candidate tickets and capacity for 8.** Who orders them — and is this a PM decision, a PO decision, or genuinely both, depending on how Loopline is structured?

6. **An engineer, mid-sprint, discovers the "quick fix" from Scenario 2 actually requires a schema migration that risks downtime.** Does this change who owns the call from Scenario 2? Why or why not?

7. **Marketing wants three specific UI states screenshot-ready for a launch campaign two weeks before the actual ship date — meaning some visual work has to be locked early, before engineering has finished the underlying logic.** Whose job is it to negotiate that tension, and what does "no" cost if nobody owns saying it?

8. **A well-liked, senior individual contributor engineer proposes a feature they're personally excited to build, with no user evidence behind it yet.** How does the PM say no (or "not yet") without the org reading it as "the PM doesn't value engineering's ideas"?

## Constraints

- You must give a real answer for every scenario — "it depends" alone is not a submission; say what it depends on and where *you'd* land given Loopline's context (45 people, fast-growing, from the course's running example).
- At least **two** of your eight answers must explicitly note that reasonable people could draw the line differently — and say what would change your answer (e.g., "if Loopline had a dedicated project manager, Scenario 7 shifts to them").
- Reference specific ownership language from Lecture 1 (own vs. influence) at least three times across your eight answers — don't just assert a role, ground it in what that role structurally owns.

## Hints

<details>
<summary>On Scenario 1 (the SSO commitment)</summary>

This tests whether you'll let a sales commitment override an honest engineering estimate. The PM owns the trade-off decision (Lecture 1, Section 2, item 4) but does **not** own the estimate itself — overriding an estimate because sales already promised it is a classic way to burn engineering trust and ship something broken to hit a date. A strong answer separates "who decides the trade-off" from "who gets to invent a fake number."

</details>

<details>
<summary>On Scenario 4 (the one-off enterprise feature)</summary>

This is a viability question dressed as a feature request (Lecture 3's VVF+U lens). A strong answer doesn't just say yes or no — it asks what this decision does to the *next twenty* prospects who'll ask for their own one-off, and whether $400K justifies permanently forking the roadmap around one account.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Ownership clarity | Names a role with no reasoning | States who owns it **and** why, tied to what that role structurally owns |
| Failure mode | Skipped or vague ("it would be bad") | Names the *specific* thing that breaks if the wrong person decides |
| Honesty about ambiguity | Every answer sounds equally certain | At least 2 answers explicitly flag where reasonable people would disagree, and what would change the call |
| Grounding | Answers feel like opinion | Answers reference Lecture 1's own/influence framework by name |

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-01/challenge-01/`.
