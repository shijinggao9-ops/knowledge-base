# Week 9 Homework

Extra practice, spread across the week. Unlike the exercises, these are meant to be done in short sessions alongside the main material — pick them up after each lecture rather than saving them all for one sitting. None of these require new seed data beyond what's already in the [week README](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/README.md) unless noted.

## After Lecture 1 (Positioning and Messaging)

**H1. Rewrite a positioning statement you've actually seen.** Find a real SaaS product's homepage headline (any product you use — your task tool, your email client, anything). In 4–5 sentences: reconstruct what you believe their positioning statement is, using the five-blank template, even though they'll never phrase it that formally in public copy. Then critique it — is the segment specific, or is it "for everyone"? Is the "unlike" clause naming a real alternative or a vague swipe at "old tools"?

**H2. Write a third Guest Access positioning statement.** Beyond the two segments from Exercise 1 (Mid-Market subcontractor teams, nonprofits reporting to funders) and the two from Lecture 1 (enterprise compliance, agencies), pick a **fourth** segment implied by the seed data — legal services (Silverline Legal, org 15, uses guest access for co-counsel and expert witnesses) — and write its positioning statement. What's different about the trigger event for a law firm versus an agency?

**H3. One paragraph: why category choice matters.** Explain, to someone who's never taken this course, why calling Guest Access a "permissions feature" versus an "external collaboration workflow" changes who evaluates it and how. Use a concrete example of a stakeholder who'd react differently to each framing.

## After Lecture 2 (Launch Tiers and Channels)

**H4. Re-tier three Week 5 backlog items.** For `dark_mode`, `bulk_task_reassignment`, and `public_api_webhooks` (all from [Week 5's backlog](26-product%20learning（附）/curriculum/week-05-prioritization-and-roadmapping/README.md)), assign each a launch tier sequence (does it even need a private beta, or can it go straight to full GA?) and justify each in one sentence using the four risk questions. Notice which of the three needs the *least* tiering, and say why.

**H5. Build a one-paragraph RACI justification.** Pick one row from Lecture 2's RACI table (Section 3) and write a paragraph defending why that specific role — not a different one — should be Accountable. What would go wrong if Accountability sat with a different role instead?

**H6. Channel audit.** For the `ga_25` wave of Guest Access, list every channel from Lecture 2's table that should **not** be used yet, and for each, the one sentence explaining why using it early would undermine the tiered approach.

## After Lecture 3 (Instrumented Rollouts)

**H7. Adapt the ticket-rate query for a single segment.** Modify Lecture 3 Section 3.4's query to filter to `Enterprise`-segment orgs only. Run it. Does the result change? Why or why not, given which org triggered the original result?

**H8. Write your own rollback trigger table.** For a hypothetical Loopline feature — bulk task reassignment (item 4 in Week 5's backlog) — propose 2 rollback triggers appropriate to *that* feature's risk profile (accidental mass reassignment is a data-integrity risk, not a security-exposure risk — how should the triggers differ from Guest Access's?).

**H9. Postmortem practice.** Using Lecture 3 Section 5's five-part structure, write a 5-sentence (one per part) skeleton postmortem for a **hypothetical** incident: a `dark_mode` CSS bug that made text unreadable for colorblind users in `ga_100`. This is much lower-stakes than the Cascade Freight incident — practice writing a blameless postmortem for something small before you ever have to write one for something big.

## Mixed practice

**H10. The "unlike" audit.** Go back through every positioning statement you wrote this week (Exercise 1, Homework H1, H2). For each, circle the "unlike" clause and ask: could a skeptical reader name a *better* alternative than the one you picked? If yes, revise it.

**H11. SQL speed drill.** Without looking at Lecture 3 or Exercise 3, write from memory: a query that counts `guest_invitations` by `org_id`, ordered descending, limited to the top 5. Then check it against your Exercise 3 Task 2 answer — did you get the same top orgs?

## Submission

Homework isn't formally submitted, but keep your answers — several (H2, H4, H8) are useful raw material if you choose Mini-Project Option B.
