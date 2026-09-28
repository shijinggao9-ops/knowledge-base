# Challenge 1 — Plan a Phased Rollout for a Risky Launch

**Time:** ~90 minutes. **Difficulty:** Hard. **No single right answer.**

## The scenario

Pull up Week 5's backlog. Item 14 is **AI-Generated Task Summaries**: an exec board-meeting ask, RICE `impact = 1`, RICE `confidence = 0.2` (the lowest confidence of any item in the backlog — nobody is sure this will actually work well), and a hard dependency on `public_api_webhooks` (needed so the summarizer can consume a stable event feed instead of the old internal-only pipeline). Six months have passed since Week 5. `public_api_webhooks` shipped. Engineering has built a first version: an LLM-generated one-paragraph summary of a task's comment thread, shown on the task detail page, regenerated whenever new comments are added.

This is a fundamentally different risk profile than Guest Access. Guest Access could leak data if the permission model had a bug — bad, but a **binary** correctness failure (the guest either could or couldn't see the wrong thing, and a bug is a bug). AI Task Summaries can be **wrong in degrees**: mostly right but missing a key detail, subtly misrepresenting who agreed to what, confidently stating something that never happened. A summary that's wrong 2% of the time isn't "2% broken" the way a permission bug is — it's a feature where **every single user has to decide, forever, how much to trust it**, and getting that wrong even occasionally can quietly erode trust in the whole product, not just this feature.

Your job: plan this launch from a blank page, the way you would have planned Guest Access in Weeks 1–2 of this unit, before anything shipped.

## Your task

Write `challenge-01.md` covering all of the following.

### 1. Risk assessment (the four questions from Lecture 2, applied honestly)

Walk through blast radius, reversibility, support cost, and brand exposure for AI Task Summaries specifically — and be honest that this is a **different kind of risk** than Guest Access, not just "also risky." What's genuinely reversible here (can you turn summaries off instantly?) and what isn't (can you undo the damage of a user having already acted on a wrong summary)?

### 2. Launch tiers, with a twist

Design the tier sequence (internal → private beta → ...). For this feature specifically, decide: should the private beta include a **feedback mechanism on individual summaries** (e.g., a thumbs-up/down or "this is wrong" flag) as a **launch requirement**, not a nice-to-have? Defend your answer — what would you be flying blind on without it?

### 3. Positioning — and what you will NOT claim

Write a one-paragraph positioning statement for AI Task Summaries (use the Lecture 1 template). Then write a second short paragraph: **what will you explicitly avoid claiming or implying**, and why? (Hint: think about words like "accurate," "always," "understands" — words that set an expectation an LLM-based feature can't reliably meet, and that make a wrong summary feel like a broken promise instead of an expected occasional miss.)

### 4. Kill criteria, defined before launch

Lecture 3 defined Guest Access's rollback triggers around *security* signals (critical tickets). AI Task Summaries needs triggers around a **different kind of signal** — quality and trust. Propose at least 3 numeric or checkable kill/pause criteria appropriate to an AI feature (examples to react to, not copy verbatim: a spike in "this is wrong" feedback above some rate; a specific category of error reported more than N times, like fabricating a decision that was never made; a support ticket explicitly citing the summary as the cause of a customer-facing mistake). For each, state the threshold and the action.

### 5. Channels — what's different this time

Which channels from Lecture 2's list need to change for this launch, and why? (Consider: does this warrant a more cautious in-product framing — e.g., a persistent "AI-generated, may be inaccurate" label — that Guest Access never needed? Does Support need different training — how to handle a customer who says the AI told them something false?)

## Constraints

- You may not simply copy the Guest Access launch plan and swap the feature name. If a section of your plan reads identically to how you'd have written it for Guest Access, that section needs more thought — this feature's risk shape is different, and the plan should show it.
- Every kill criterion must be specific enough that two different people looking at the same data would agree on whether it was crossed. "Users seem unhappy" is not a kill criterion.

## Hints

<details>
<summary>On the feedback mechanism (Section 2)</summary>

Without a lightweight way for a user to flag "this summary is wrong," your only signal that the feature has a quality problem is a support ticket — which means by the time you know, a customer was frustrated enough to go out of their way to tell you. A one-click flag captures the 95% of wrong summaries a user notices but doesn't bother escalating. If your plan doesn't have some version of this before beta, that's a real gap worth naming even if you decide to accept the risk anyway.

</details>

<details>
<summary>On what not to claim (Section 3)</summary>

"Accurate" is a word an enterprise buyer's legal team will hold you to. A stronger, honestly defensible framing tends to describe the feature as a starting point a human reviews, not a source of truth — the same posture as spell-check or a first-draft generator, not an oracle.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Risk framing | Treats this like "Guest Access but AI" | Names the specific ways a degrees-of-wrong failure differs from a binary bug |
| Kill criteria | Vague ("monitor for problems") | Numeric, checkable, and specific to quality/trust failure modes |
| Positioning | Overclaims capability | States a clear benefit while explicitly avoiding words that promise more than an LLM can reliably deliver |
| Tier design | Copies Guest Access's tier plan unchanged | Adds or changes something (like a mandatory feedback mechanism) that responds to this feature's actual risk |

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-09/challenge-01/`.
