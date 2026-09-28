# Challenge 1 — Resolve a Sales-vs-Engineering Roadmap Conflict

**Time:** ~90 minutes. **Difficulty:** Medium-high. **No single right answer.**

## The scenario

You've built the Now/Next/Later roadmap from Lecture 3 and Exercise 3. Now is: `guest_external_access`, `audit_log_compliance`, `configurable_stuck_threshold`, `bulk_task_reassignment`, `stuck_alert_digest_mode` — 20 points, capacity-full. You post it in the #roadmap-review Slack channel. Two messages come in within the hour.

**From the Sales VP:**

> Love that guest access and the threshold made it in — those deals are real. But I need `custom_fields` and `time_tracking_integration` in Now too, not "Later." I've got **$400K in pipeline** sitting on both of these across four prospects who all asked for them independently in the last two weeks. This isn't a nice-to-have, this is quota. If it doesn't make Now, I need to know that today so I can manage expectations with my prospects.

**From the Engineering lead:**

> Before we add anything else to Now — we're already at capacity, and I want to flag that `public_api_webhooks` keeps getting pushed to "Later" every quarter, and every quarter that makes the *next* thing that depends on it (like the AI summaries exec keeps asking about) more expensive to build later, not less. We built the whole event pipeline for Stuck Task Alerts as a one-off last quarter specifically because API/webhooks wasn't prioritized, and now we're going to have to redo pieces of it. I'd rather trade one of the smaller Now items for a real slice of the API work than keep deferring it. Also — just so it's said — "the customer asked for it" isn't the same as "it's validated." Half of what Sales calls blocking pipeline turns out to be a nice-to-have once the deal actually closes.

Both messages have real substance. Both stakeholders will be in the roadmap review meeting in two days, and they are not going to agree with each other in the room. You go first.

## Your task

Write a **mediation memo** (`challenge-01.md`, 500–800 words) that you would actually send to both stakeholders before the meeting. It must:

1. **Separate fact from claim, explicitly.** `guest_external_access` is backed by three *signed* deals — that's a fact you can verify (Confidence = 1.0 in the seed data). The Sales VP's "$400K in pipeline" is a claim about unsigned prospects — treat it with the same skepticism this week's lectures taught you to apply to any unvalidated Reach/Impact/Confidence number. Say so, without being dismissive of it.
2. **Use real numbers from the backlog**, not vibes. Pull the actual RICE, WSJF, and (where relevant) Kano data for `custom_fields`, `time_tracking_integration`, and `public_api_webhooks`, and reference specific scores in your reasoning.
3. **Address the Engineering lead's structural point directly.** Is "keeps getting deferred, gets more expensive later" a legitimate argument inside this week's frameworks, or outside them? If it's legitimate, which component (RR-OE? Time Criticality?) is supposed to capture it — and is it currently scored high enough to reflect that argument?
4. **Make an actual recommendation**, not a non-answer. Does anything change about Now? Does anything move in Next? If you're saying no to one or both stakeholders, say so plainly and explain the tradeoff you're protecting by saying no — don't hide a "no" inside vague process language.
5. **Propose one concrete next step for the unresolved claim** — specifically, what would it take to turn the Sales VP's "$400K in pipeline" into something as solid as `guest_external_access`'s signed-deal status? (Hint: this is a Confidence problem, and Confidence problems have a standard fix — go get evidence.)

## Constraints

- You may **not** simply expand Now's capacity to fit everyone. Capacity constraints exist precisely so this negotiation has to happen; "just do more" is not an available answer this week.
- You may recommend swapping an item **out** of Now to make room for something else, but if you do, name the specific item you'd cut and defend it with numbers.
- Stay in-scope: you're mediating *this* roadmap conversation, not redesigning the whole prioritization process.

## Hints

<details>
<summary>On the Sales VP's pipeline claim</summary>

Notice the seed data already scores `custom_fields` and `time_tracking_integration` at Confidence = 0.5 — the PM who built this backlog already treated these as unvalidated before the Sales VP's message ever arrived. That's not a coincidence; it's exactly the kind of case this week's material warns you to watch for. The right response usually isn't "no," it's "here's what it would take to raise Confidence to where `guest_external_access` already sits."

</details>

<details>
<summary>On the Engineering lead's "gets more expensive later" argument</summary>

Re-read Lecture 2 section 6 on cost of delay compounding. Ask yourself: if deferring `public_api_webhooks` measurably increases the future cost of `ai_task_summaries`, does that belong in `public_api_webhooks`'s own Time Criticality score (raising its own priority) or is it a separate argument about sequencing that a score alone doesn't capture well? Both are defensible positions — pick one and argue it.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|---|---|---|
| Fact vs. claim | Treats "$400K pipeline" as equally solid as signed deals | Explicitly separates verified commitments from unvalidated claims, using this week's Confidence concept |
| Use of real numbers | Vague ("the scores support this") | Cites specific RICE/WSJF/Kano numbers for the specific items in dispute |
| Structural argument | Ignores or hand-waves the Engineering lead's compounding-cost point | Engages it directly and locates it (or explains why it doesn't fit) within the WSJF components |
| Decisiveness | "We'll take it under advisement" | A clear yes/no on each ask, with the tradeoff stated |
| Path forward | No next step for the unresolved claim | A concrete, checkable way to convert the Sales VP's claim into evidence |

The best submissions read like something a real engineering lead and a real Sales VP would both, grudgingly, respect — not because it gives them everything they asked for, but because it's honest about the tradeoff and backed by numbers either of them could check themselves.

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-05/challenge-01/`.
