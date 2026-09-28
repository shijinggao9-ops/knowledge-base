# Challenge 1 — Defend Killing a Well-Loved Idea

**Time:** ~90 minutes. **Difficulty:** Medium–Hard. **No single right answer.**

## The scenario

Loopline's "AI Daily Standup Summary" has been the most popular idea in the company for two quarters running. It comes up in nearly every internal roadmap discussion. The pitch: every morning, an AI-generated summary of what each team member did yesterday and what's blocking them, delivered automatically — "like a standup meeting, without the meeting."

The founder loves it and has mentioned it in two board updates. Sales says three prospects have asked about "something like that." Design has already made two exploratory mockups, unprompted, because an engineer built a rough prototype over a hack week. It is, without question, the single most *emotionally* popular idea at the company right now.

You've been asked to evaluate it seriously before it gets greenlit for next quarter — and after doing the work this week's lectures teach, you believe it should **not** be built next quarter. Not "never" — "not next quarter, given what we actually know."

Here's what your evaluation actually turned up:

- **No problem statement exists.** Nobody has written down, precisely, who needs this, what gap it closes, and why. The pitch has always been solution-first ("AI standup summary"), never problem-first.
- **No sizing has been attempted.** Nobody knows how many teams currently do daily standups at all inside Loopline (there's no "standup" feature — teams that do them do them outside the product, in Slack or in person). It's entirely possible the addressable population is small.
- **The 3 sales mentions are thin.** None of the three prospects made it a stated deal-blocker; two were general "would be cool" comments during a broader demo, and one was a direct question but the deal closed anyway without the feature.
- **It would compete directly for the same engineering team** that would otherwise build the import-friction fix from this week's sizing work — a fix with an actual measured $18,900–$29,400/year opportunity behind it (Exercise 2), against an idea with zero measured opportunity behind it so far.
- **There is a real, if smaller, opportunity possibly underneath it**, once you dig: async status updates in general (not necessarily AI-written, not necessarily "standup"-branded) came up as a genuine pain point in 2 of the 5 Week 2 user interviews, in the context of distributed teams struggling to know who's blocked on what. That's a thinner, but real, thread worth not entirely discarding.

## Your task

Write the memo you would actually send. Not a hedge, not "let's keep exploring both" — a clear, evidence-based recommendation to **not** build the AI Daily Standup Summary next quarter, that a founder who loves the idea would find hard to dismiss as "the PM just doesn't get it."

Structure your memo (`kill-memo.md`) with these sections:

1. **The ask, stated plainly.** One or two sentences: what's being requested, and what you're recommending instead.
2. **What we don't know yet.** The specific evidence gaps (no problem statement, no sizing, thin sales signal) — stated factually, not as an attack on the idea's supporters.
3. **What we do know, and what it costs.** The opportunity-cost argument: naming the *specific* alternative (this week's import-friction opportunity, with its real sizing) that the same engineering time would otherwise go to, and why that's a fairer comparison than "AI feature vs. nothing."
4. **What's worth keeping.** The thinner, real signal (async status updates as a genuine pain point) and what you'd need to validate it properly before it's a fundable opportunity — don't throw out the baby with the bathwater.
5. **The actual recommendation.** Not "never" — a specific, time-bound proposal: what would need to be true, and by when, for this to come back on the table.

## Constraints

- You may not simply say "there's no data" and stop — that reads as obstruction, not judgment, and it's not what the scenario supports. You have to engage with *why* three quarters of enthusiasm haven't produced a problem statement, and offer a path to get one if the idea is worth pursuing later.
- You may not attack the idea's supporters' judgment or motives. The founder, sales, and design are not wrong to be excited — popularity is a real signal, just not sufficient on its own. Your memo should read as respectful of that signal while being honest about its limits.
- Keep the memo to 400–600 words. A kill memo nobody reads because it's 1,500 words defeats its own purpose.

## Hints

<details>
<summary>On separating "popular" from "sized"</summary>

Popularity (internal enthusiasm, a few sales mentions) is real evidence of *something* — but it's evidence of interest, not evidence of size or of root cause. The strongest version of this memo doesn't dismiss the enthusiasm; it asks the enthusiasm to go do the same homework every other opportunity on the tree had to do (Lecture 1's problem statement, Lecture 2's sizing) before it gets scarce engineering time.

</details>

<details>
<summary>On the opportunity-cost framing</summary>

The most persuasive version of a kill memo rarely argues "your idea is bad." It argues "here is a *specific*, already-measured alternative use of the same three engineers, and here's why that comparison — not 'AI feature vs. nothing' — is the real decision in front of us." That reframes the conversation from taste to tradeoff.

</details>

## How success is judged

| Signal | Weak memo | Strong memo |
|--------|-----------|--------------|
| Tone | Dismissive of the idea or its supporters | Respectful of the enthusiasm, honest about the evidence gap |
| Evidence gap | Vague ("we don't have data") | Specific: no problem statement, no sizing, thin sales signal — named individually |
| Opportunity cost | Absent, or a generic "we have other priorities" | Names the specific alternative (import friction) with its actual sizing number |
| The real thread | Ignored or lumped in with the rejected idea | Separated out (async status updates), with a stated path to validate it |
| The ask | "No" with no path back | Specific, time-bound conditions under which it's reconsidered |

## Submission

Commit `kill-memo.md` to your portfolio under `c44-week-03/challenge-01/`.
