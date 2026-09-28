# Exercise 1 — Scope an AI Feature and Its Fallback

**Goal:** Turn a second vague "add AI" request into a properly scoped feature — run it through Lecture 1's fit checklist, pick a human-in-the-loop pattern, and design a deterministic fallback for when the model can't be trusted. This is the muscle the mini-project runs at full scale.

**Estimated time:** 1.5 hours.

## Setup

No database needed for this one — read [Lecture 1](01-when-to-use-an-llm.md) and [Lecture 3, Section 2](03-guardrails-cost-and-safety.md#2-human-in-the-loop-design-patterns) before starting. Create a file `scope.md`.

## The request

This one comes from Support, not Sales: *"Customers keep writing long, rambling bug reports in the support widget, and our team spends 10+ minutes just figuring out what they're actually asking for before they can even start troubleshooting. Can the AI just summarize it for them?"*

## Tasks

1. **Name the actual job**, not the technology. Write one sentence describing the user problem *without the word "AI" or "summarize" in it* — what does a support agent actually need, and why does the current rambling report fail to provide it quickly? *(This mirrors Lecture 1 Section 1's point about a brief that names the solution before the problem.)*

2. **Run it through the five-question fit checklist** from Lecture 1, Section 3. For each of the five questions, write one sentence of reasoning and a yes/no. State your overall verdict: is this a genuine LLM candidate?

3. **Name the specific bounded task** the model would perform if you proceed — be as narrow as you can. ("Summarize the ticket" is too broad; "extract the customer's stated problem, the product area, and any error message they quoted, into three labeled fields" is a bounded task.)

4. **Pick a human-in-the-loop pattern** from Lecture 3, Section 2's table (suggest-only, confirm-to-act, confidence-gated autonomy, full autonomy) for this feature, and justify the choice against the other three. What's the worst thing that happens if the model's output is wrong, under your chosen pattern?

5. **Design the deterministic fallback.** If the model call fails, times out, or the feature is disabled by the kill switch from Lecture 3, what does the support agent see instead? It must be a real, usable path — not just an error message with no way forward. *(Hint: what did support agents do before this feature existed? That's usually your fallback, wired back in.)*

6. **Estimate volume and pick a model tier**, using Lecture 1 Section 5's reasoning. How many support tickets per week does Loopline plausibly receive? Given that volume and the bounded task from Task 3, which tier (small/mid/frontier) do you pick, and why?

7. **Write two rubric sentences** — what would a *good* summary output look like for this bounded task, and what would a clearly *bad* one look like? You don't need a full eval set yet (that's Exercise 2) — just enough of a rubric to know one when you see it.

## Expected outcome

- A one-sentence problem statement with no technology names in it.
- A five-question checklist walkthrough with an explicit yes/no per question and a clear overall verdict.
- A named, bounded task (not "summarize the ticket").
- A chosen HITL pattern with a stated worst-case under that pattern.
- A concrete, usable fallback path — something a support agent can actually do if the feature is down, not a dead end.
- A volume estimate and a model-tier pick with one sentence of reasoning.
- Two rubric sentences (good example, bad example).

## Done when…

- [ ] `scope.md` has all seven tasks.
- [ ] The fit-checklist verdict follows logically from the five individual answers — you're not asserting a conclusion the reasoning doesn't support.
- [ ] The fallback in Task 5 is something a real support agent could actually do today, not a placeholder.
- [ ] Task 3's bounded task is narrow enough that you could write a rubric for it without hand-waving.

## Stretch

- Sketch (in words, no diagram needed) what the confirm-to-act version of this feature would look like instead of your chosen pattern, and name one scenario where confirm-to-act would actually be the better choice.
- If Loopline's support volume were 50x higher, would your model-tier answer change? Why or why not?

## Submission

Commit `scope.md` to your portfolio under `c44-week-11/exercise-01/`.
