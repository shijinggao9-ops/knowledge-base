# Challenge 2 — Expose a Gamed RICE Score

**Time:** ~90 minutes. **Difficulty:** Medium-high. **No single right answer, but a real, findable truth.**

## The scenario

A colleague — a PM on the growth pod who reports to the same exec who's been pushing `ai_task_summaries` since Week 4 — sends you a "quick RICE refresh" ahead of the roadmap review, saying the original numbers were "too conservative" and they've updated them based on "additional context." Here's their version, run as a query against a *modified* copy of the backlog:

```sql
-- Colleague's "refreshed" numbers for ai_task_summaries.
-- Original seed values (week README) are in a comment beside each for comparison —
-- do not trust the comment either; verify it yourself against backlog_items.
SELECT
    'ai_task_summaries' AS item_key,
    950   AS reach,        -- "impressions across all active teams, not just distinct teams"
    3     AS impact,       -- "this is a board priority, that's massive impact by definition"
    0.9   AS confidence,   -- "we're confident the exec wants this, so we're confident it'll work"
    8     AS effort_weeks, -- "if we cut the eval/guardrail work described in Week 11's prereqs, it's faster"
    ROUND(950 * 3 * 0.9 / 8, 2) AS new_rice_score;
```

That query returns a RICE score of **320.63** — which would make `ai_task_summaries` the **#1** item in the entire backlog, ahead of `recurring_tasks` (190.0) and `dark_mode` (150.0), and comfortably clear of where it actually sits today (14.6, 8th of 14 — respectable, but nowhere near #1).

Something about this doesn't sit right. Your job is to find out exactly what, and put it in writing.

## Your task

Produce `challenge-02.md` with four sections:

### 1. Line-by-line audit

For **each of the four inputs** (Reach, Impact, Confidence, Effort), compare the colleague's "refreshed" number to the original value in `backlog_items` (query it — don't trust the inline comment). For each of the four, state:

- The original value and the new value.
- Which of the four gaming patterns from Lecture 1 §2 (inflated Reach, inflated Impact, inflated Confidence, deflated Effort) it matches.
- Whether the colleague's stated justification (in the SQL comment) is a legitimate reason to change the number, or a rationalization. Be specific about *why*.

### 2. Quantify the damage

Compute, in SQL, **how much of the score inflation comes from each individual input**, by changing them back to the original value one at a time and recomputing. (E.g., "reverting only Reach, holding the other three at the colleague's numbers, drops the score from 320.63 to ___.") This isolates which single change did the most damage to the score's honesty — it's rarely all four equally.

### 3. The Effort number deserves special scrutiny

Look closely at the Effort justification: *"if we cut the eval/guardrail work described in Week 11's prereqs, it's faster."** This isn't a scoring error in the same sense as the other three — it's proposing to change what's actually being built (a version of the feature with less safety/eval work) while keeping the *name* of the backlog item the same. Write 3–4 sentences: why is this the most dangerous kind of gaming to catch, compared to simply overstating Reach?

### 4. Your recommendation

State the RICE score you'd actually defend in the roadmap review, with the original, unmodified inputs, and where that places `ai_task_summaries` in the full ranking. Then propose **one concrete process change** (not just "trust people more") that would make this kind of quiet re-scoring harder to slip into a roadmap review unnoticed next quarter. Your proposal should be specific enough that someone could implement it — e.g., a rule about what evidence is required to move Confidence above a certain threshold, a required audit column, a second-reviewer sign-off, or something else concrete.

## Constraints

- Every number you cite must be traceable to a query you actually ran. "That seems too high" is not evidence — "the seed's `confidence` column is 0.2, not 0.9, verified with `SELECT confidence FROM backlog_items WHERE item_key = 'ai_task_summaries'`" is.
- Don't just say "this is gamed, ignore it." Assume the colleague and the exec are acting in good faith, not maliciously — your writeup should be something you could actually send *to* the colleague, not just about them.
- You are not being asked whether `ai_task_summaries` is a bad feature. You're being asked whether **this specific scoring exercise honestly represents it.** Those are different questions — keep them separate in your writeup.

## Hints

<details>
<summary>On "we're confident the exec wants this, so we're confident it'll work"</summary>

This is a category error worth naming explicitly in your writeup: Confidence in RICE is about confidence in the **Reach and Impact estimates** — will this actually reach that many people and move the needle that much — not confidence that a stakeholder wants it built. A powerful sponsor increases the *chance it gets built regardless of score*; it does not increase the *evidence* behind the Reach/Impact numbers one bit. Conflating the two is one of the most common — and hardest to call out in the room — forms of RICE gaming, precisely because it doesn't feel like lying.

</details>

<details>
<summary>On isolating which input did the most damage</summary>

Original: 950 × 1 × 0.2 ÷ 13 = 14.6. Colleague's: 950 × 3 × 0.9 ÷ 8 = 320.63. Four numbers changed at once; the honest audit changes them back one at a time to see which reversal moves the score the most.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|---|---|---|
| Verification | Trusts the inline SQL comments | Independently queries `backlog_items` to confirm original values |
| Isolation | Reports only the final gamed-vs-honest gap | Isolates the contribution of each individual input change |
| Judgment | Calls everything "gaming" indiscriminately | Distinguishes a legitimate re-estimate from a rationalization, with reasons |
| The Effort trap | Treats the Effort change like the other three | Recognizes it as scope-shrinking disguised as re-estimation, and explains why that's worse |
| Process fix | "Be more careful next time" | One specific, implementable safeguard |

## Submission

Commit `challenge-02.md` to your portfolio under `c44-week-05/challenge-02/`.
