# Challenge 2 — Turn an Ambiguous Ask into a Buildable Spec

**Time:** ~90 minutes. **Difficulty:** Medium-hard. **No single right answer.**

## The scenario

You're the PM on Loopline. Your VP of Sales messages you directly on Slack, no context, no ticket, no meeting:

> **VP of Sales, 4:47pm:** "hey — had 2 calls this week where the prospect asked if Loopline can 'integrate with our CRM.' can we just add that? feels like it should be quick. losing deals over it, need something we can tell prospects soon"

This is a real category of request every PM eventually gets: high urgency, low precision, a business consequence attached ("losing deals"), and an implicit assumption that it's simple ("feels like it should be quick" — famous last words). Your job is not to say yes or no yet. Your job is to turn this into something a team could actually scope, using every technique from this week.

## Your task

In `challenge-02.md`:

1. **List everything genuinely ambiguous in this one message.** Aim for at least 6 distinct ambiguities — not just "which CRM," go deeper. (Some starting angles: what does "integrate" mean — one-way sync, two-way sync, just a link-out? Which direction does data flow? Is this about *Loopline* tasks appearing in the CRM, or CRM *contacts/deals* appearing in Loopline? Which CRM(s) — did both prospects name the same one? What does "losing deals over it" actually mean — is this a hard blocker or a nice-to-have prospects mention? Is this two data points enough to justify building, or do you need to validate demand further per Week 3's opportunity-sizing method?)

2. **Write the clarifying questions you'd actually send back** — not to the VP necessarily (some questions need the actual prospects, sales calls, or research), organized into: questions for the **VP directly** (fast, same-day), questions that need **more research** (Week 2/3 techniques — a few more sales calls, checking win/loss data), and questions that are **your own product judgment to make**, not anyone else's to answer. For this last category, name at least one and explain why it's your call, not a question to ask someone else.

3. **Assume the most likely, most conservative reading** (state which reading you're assuming and why it's the conservative one) and draft a **PRD skeleton** for that narrower interpretation — not a full PRD, but real context + 2 goals + 3 non-goals + 2 story titles (no full acceptance criteria needed). This is the piece that turns "add CRM integration" from a vague, dangerous-sounding commitment into something with an actual, boundaried shape.

4. **Write the non-goals with special care.** This is the highest-value part of this exact scenario: "CRM integration" as stated could balloon into supporting five different CRMs, real-time bidirectional sync, custom field mapping, and OAuth flows for each — a multi-quarter platform investment disguised as a "quick" feature. Your non-goals section is what prevents that silent scope explosion. Write at least 4 non-goals, each with a one-clause reason.

5. **Write the one-paragraph reply you'd actually send the VP** — plain English, no jargon, that (a) doesn't say a flat "no," (b) doesn't over-promise "sure, quick fix," and (c) tells them concretely what you need and by when to scope it properly. This paragraph is the real deliverable of the whole exercise — a PM who can't translate spec discipline back into a two-sentence Slack reply hasn't actually solved the organizational problem.

## Constraints

- You cannot ask the VP a question you could instead answer yourself with product judgment — if you find yourself about to ask "should this be two-way sync?", stop and decide whether that's actually your call (with a stated reason) before punting it upward.
- Your PRD skeleton (Task 3) must pick **one** concrete interpretation and commit to it in writing — "it depends" is not an acceptable goals section.
- Assume this is real budget/time pressure — "let's do more discovery for three weeks first" without any concrete near-term offer to the VP is not, by itself, a complete answer to Task 5.

## Hints

<details>
<summary>On the "most conservative reading"</summary>

A one-way, read-only integration ("show a link to the matching CRM contact/deal from inside a Loopline task") is almost always vastly smaller than two-way sync, and might already answer what "losing deals" is actually about — sales reps wanting Loopline visibility *inside their existing CRM workflow*, not full data migration. That's one defensible narrow reading; you don't have to pick this one, but if you pick something else, be equally deliberate about why.

</details>

<details>
<summary>On separating "your call" from "ask the VP" from "needs research"</summary>

Which CRM to build for first is arguably **your call** if you have usage/market data (or a reasonable proxy) to rank CRMs by prevalence among prospects — that's a product/data decision, not a sales decision. Whether "losing deals" means a hard deal-blocker versus a nice-to-have mentioned in passing is something **only more research** (checking actual win/loss notes, or a few more sales calls) can answer honestly — the VP's paraphrase alone isn't strong enough evidence to build on, per Week 3's opportunity-sizing standards.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Ambiguity-finding | Lists 2–3 surface ambiguities | 6+ distinct, non-overlapping ambiguities, some non-obvious |
| Question routing | Sends everything back to the VP | Correctly separates VP-questions, research-questions, and your-own-judgment-calls |
| Scope commitment | PRD skeleton hedges ("it depends") | Commits to one concrete interpretation in writing |
| Non-goals | Vague or missing | 4+ specific, reasoned non-goals that visibly prevent scope explosion |
| Stakeholder reply | Over-promises or flatly stalls | Concrete, honest, moves the conversation forward with a specific ask |

## Submission

Commit `challenge-02.md` to your portfolio under `c44-week-04/challenge-02/`.
