# Exercise 1 — Write a Positioning Statement

**Goal:** Write two positioning statements for Guest & External Collaborator Access — one per segment — using the template from Lecture 1, plus a feature-benefit-proof table a sales rep and a support agent could both pull phrasing from.

**Estimated time:** 90 minutes.

## Setup

Re-read Lecture 1, Sections 2–4, with the two worked examples in front of you. You will write statements for **different** segments than the lecture's worked examples, so copying won't work — you have to make the same five decisions yourself.

Create a file `positioning.md`.

## Part A — Two positioning statements (45 min)

Write a positioning statement for each of the two segments below, using the template:

> **For** [target segment] **who** [need/trigger], **[product]** is a **[category]** that **[benefit/differentiator]**. **Unlike** [alternative], **[product]** **[the specific thing that makes the difference true]**.

1. **Segment: Mid-Market operations teams working with subcontractors.** (Think Northgate Builders and Fairmount Realty from the seed data — construction/real-estate-adjacent businesses that regularly bring in subcontractors or brokers who need visibility into one job/project but are not employees.)
2. **Segment: Nonprofit and grant-funded teams reporting to external funders.** (Think Beacon Nonprofit — a program team that needs to give a funder or grant reviewer visibility into project progress without giving them a paid seat or a full data export.)

For each, write **one sentence** first stating your interpretation of the segment's need in plain English, *then* the formal positioning statement. State explicitly: what market category did you choose, and what's the real primary alternative this segment uses today (not a competitor product — the actual workaround)?

## Part B — Feature-to-benefit-to-proof table (30 min)

Build a table with three columns — Feature, Benefit, Proof — with at least **5 rows**, covering the following capabilities (you may phrase them however you like, but all five must appear):

- Guest role scoped to a single project
- No Loopline account required for the guest before being invited
- Every guest action logged
- Guests cannot be promoted to a full workspace role by another guest (guest permissions are a ceiling, not a starting point)
- The audit log (shipped ahead of this feature) is queryable by an org's admin

Use real, checkable proof points where the seed data gives you one (e.g., "median time from invite to accept" — compute it yourself from `guest_invitations` if you want a real number instead of inventing one; see the hint below).

<details>
<summary>Hint — computing a real proof point from the seed data</summary>

```sql
SELECT
    ROUND(AVG(
        (julianday(accepted_at) - julianday(invited_at)) * 24 * 60
    ), 0) AS avg_minutes_to_accept
FROM guest_invitations
WHERE accepted_at IS NOT NULL;
```

Use the number your query actually returns, not a guess — a proof point you can't defend under a follow-up question isn't a proof point.

</details>

## Part C — One sentence of self-critique (15 min)

For **one** of your two positioning statements, write a sentence identifying its weakest blank (the one you're least confident about) and why. This is not a trick — even strong positioning statements have a blank that was the hardest decision, and naming it is the skill; pretending every blank was equally easy is not.

## Expected outcome

- Two positioning statements, each hitting all five template elements, for segments genuinely different from each other (not just reworded).
- A category choice for each that is *not* simply "task management" or "collaboration software" — it should be specific enough to reveal who you're implicitly comparing against.
- A 5+ row feature-benefit-proof table where "Benefit" is always phrased as a customer outcome, never a restatement of the feature.
- At least one proof point computed from the actual seed data, not invented.

## Done when…

- [ ] `positioning.md` has both segments' plain-English interpretation sentences and both formal statements.
- [ ] Every "Unlike" clause names a real workaround, not a straw-man competitor.
- [ ] The feature-benefit-proof table has 5+ rows and covers all five listed capabilities.
- [ ] At least one proof point is a number you computed, with the query shown.
- [ ] The self-critique sentence names a genuine weak point, not a humble-brag.

## Stretch

Write a **third** positioning statement for a segment you believe is *not* well served by this feature as currently scoped (e.g., a segment that would want guests to have write access to multiple projects at once) — and explain in two sentences why forcing a positioning statement for a bad-fit segment is itself a useful exercise.

## Submission

Commit `positioning.md` to your portfolio under `c44-week-09/exercise-01/`.
