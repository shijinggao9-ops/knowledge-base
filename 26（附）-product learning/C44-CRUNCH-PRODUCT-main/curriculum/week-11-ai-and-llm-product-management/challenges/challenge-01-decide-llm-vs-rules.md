# Challenge 1 — Decide LLM vs. Rules for a Real Feature

**Time:** ~90 minutes. **Difficulty:** Medium. **No single right answer.**

## The scenario

Loopline's roadmap has five feature requests queued for next quarter, all pitched internally with some version of "let's use AI for this." Some genuinely should. Some are a rules engine wearing an AI costume — cheaper, faster, and more predictable if you build them that way, with none of the eval and guardrail overhead this week has walked through. Your job is to call each one honestly, using Lecture 1's five-question checklist, and defend a build-vs-buy pick from Lecture 1 Section 4 for whichever ones *do* need a model.

A senior PM and a junior PM will disagree on at least one of these five. The senior one writes down *why* they landed where they did, so the call is reviewable and reversible if new evidence shows up — not just asserted.

## Your task

For each request below:

1. **Run the five-question fit checklist** (Lecture 1, Section 3) — a yes/no and one clause of reasoning per question.
2. **Give a verdict**: LLM, rules engine, classic ML, or "don't build it as described." If LLM, name which build-vs-buy point (Lecture 1, Section 4) fits — almost always "prompt a foundation model API" for a first version, but defend it.
3. **Name the one thing that would change your mind** — what evidence, if it showed up in three months, would make you revisit this call?

Put all of this in `challenge-01.md`.

## The five requests

1. **"Auto-categorize every incoming support ticket into one of our 12 fixed categories (Billing, Bug, Feature Request, ...)."**
   *(The category list is fixed and small. Does that change your answer from a feature where the output space is genuinely open-ended?)*

2. **"Let users type a search query in plain English instead of picking filters, and have it find the right tasks."**
   *(Consider: is "plain English becomes a structured filter" closer to the enumerable end of question 1, or the genuinely open-ended end? What would make this harder than request 1?)*

3. **"Draft a first-pass weekly summary email for each workspace admin, highlighting what the team accomplished."**
   *(This is close in shape to Loopline Copilot. What's actually different about the risk profile — is a wrong or bland weekly summary as costly as a wrong task breakdown?)*

4. **"When a customer cancels, automatically generate a personalized win-back offer based on their usage history."**
   *(This one touches money and an external-facing message with no obvious human review point as pitched. Walk through what question 3 — tolerance for an imperfect answer with review — does to this one specifically.)*

5. **"Detect when a task description looks like it's missing key information (no due date, no assignee, vague title) and nudge the user to fill it in."**
   *("Looks like it's missing key information" sounds fuzzy, but look closer at what's actually being detected — is this closer to a handful of checkable structural conditions, or to open-ended judgment?)*

## Constraints

- Every verdict needs the full five-question walkthrough — a verdict with no checklist shown is an incomplete answer, even if the final call turns out to be right.
- At least one of your five verdicts should **not** be "prompt a foundation model API" — if all five land in the same place, go back and check whether you're defaulting to "AI" the same way Lecture 1's opening scenario warned against, just from the other direction.
- Where you'd want a rules engine or classic ML instead, say specifically what that would look like (a decision table, a small trained classifier, a set of regex/keyword checks) — "just use rules" with no shape is as incomplete as "just use AI."

## Hints

<details>
<summary>On request 1 (ticket categorization)</summary>

A fixed 12-category output space is a strong signal this could be a small trained classifier (classic ML) or even a keyword/rules-based first pass, rather than a full LLM call per ticket — especially at high ticket volume where per-call LLM cost adds up fast for a task this narrow. That said, an LLM can still be the pragmatic first version if you don't yet have labeled training data; the interesting question is what would justify moving off it later.

</details>

<details>
<summary>On request 4 (win-back offers)</summary>

Notice this request, as pitched, has **no stated human review point** — it says "automatically generate," not "draft for a rep to review." Fit-checklist question 3 should flag this hard. A strong answer doesn't just say "add human review" and move on — it explains specifically what changes about the verdict once you add it back in, versus what the risk looks like if the request is taken literally as fully autonomous.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Checklist rigor | Skips straight to a verdict | Shows all five questions, with reasoning, for every request |
| Calibration | Same verdict for all five | Verdicts vary based on genuine differences in the requests |
| HITL awareness | Doesn't notice request 4's missing review point | Explicitly flags it and explains how adding review changes the verdict |
| Rules/ML alternative | "Use rules instead" with no detail | Names the concrete shape (decision table, classifier, keyword list) |
| Reversibility | No mention of what would change the call | Names one specific, falsifiable piece of evidence per request |

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-11/challenge-01/`.
