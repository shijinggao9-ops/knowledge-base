# Challenge 2 — Write a Recovery Plan for a Failed Launch

**Time:** ~90 minutes. **Difficulty:** Hard. **No single right answer.**

## The scenario

It's `2026-03-03`, `17:40`. You are the PM for Guest & External Collaborator Access. Forty minutes ago, per Lecture 3's case study, you and the engineering lead pulled the kill switch — the feature flag is now off for **all** orgs, not just Cascade Freight — after confirming a project-membership cache bug let a guest at Cascade Freight briefly see tasks from a second, unrelated project they weren't invited to. The immediate fire is out: no new exposure is possible while the flag is off. Now the harder part starts. You have a VP asking "are we safe to re-launch this," a Cascade Freight account team asking what to tell the customer, and an engineering team that wants to just ship the fix and flip the flag back on tonight.

Your job is to write the recovery plan that gets this right — not fast, right.

## Your task

Write `recovery-plan.md` covering all of the following.

### 1. Immediate actions (what's already true, what's still open)

In a short table or list, separate what's **already done** (per Lecture 3's timeline: flag off, Cascade Freight contacted, engineering has reproduced the bug) from what's **still open** in the next 24 hours. At minimum, address: has the exposure window been fully scoped (which guests, which projects, exactly how long was the bug live before Cascade Freight reported it)? Has legal/security determined whether this is a reportable incident? Have the other 23 exposed orgs been checked for the same failure mode, even though only Cascade Freight reported it?

### 2. Customer communication — Cascade Freight

Draft the actual message (2–4 sentences, the kind that would really go out) to Cascade Freight's account owner to relay to the customer. It should: acknowledge what happened without over-explaining internal mechanics, avoid speculating about scope before it's confirmed, and state a concrete next step and timeline. Then write a **second**, shorter message for the other 23 exposed orgs — should they get the same message, a lighter one, or none at all? Justify your choice; this is a real judgment call, and "tell everyone everything" and "tell no one anything" are both defensible in different circumstances — say which you picked and why.

### 3. Root cause and the SQL behind it

In 1–2 sentences, restate the technical root cause from Lecture 3 (cache invalidation on project re-assignment) in language a non-engineer stakeholder could understand. Then write the SQL query you'd run to answer the VP's first question — **"how many other guests were invited, removed from a project, and re-invited to a different one during the window this bug was live?"** — against the seed data's `guest_invitations` table. (You don't have a "removed and re-invited" column in the seed schema — say what column or event you'd need engineering to add to actually answer this, since this is exactly the kind of gap a real postmortem surfaces: the data you need to fully scope an incident often doesn't exist yet.)

### 4. Prevention — what changes before re-launch

List at least 3 concrete changes, and classify each as **must-have before re-launch** vs. **should-have soon after**. At least one must be a specific automated test for the exact reproduction sequence; at least one must be a monitoring/alerting change (what would need to be true so this is caught by an alert within minutes next time, instead of waiting for a customer to notice and file a ticket).

### 5. Re-launch criteria

State the specific, numeric or checkable conditions that must be true before the flag goes back on — and be specific about **for whom**. Does re-launch restart at `beta` with a fresh soak period, or resume directly at `ga_100` once the fix is verified? Justify your choice using Lecture 2's tier-sizing logic (risk, reversibility, blast radius) rather than "whichever is faster."

### 6. The blameless postmortem — one paragraph

Write the "what happened" summary paragraph you'd put at the top of the postmortem doc, in the blameless style from Lecture 3 Section 5 — describing the mechanism, not attributing fault to a person or team.

## Constraints

- Do not write a plan that re-enables the flag same-day. A same-day re-launch of a feature that had a live data-exposure bug, without a fresh test and a defined soak period, is exactly the kind of pressure-driven shortcut this challenge is testing whether you'll resist.
- Your Section 3 query must actually run against the seed schema as given — if the data you need doesn't exist in the current tables, say so explicitly rather than inventing a column that silently doesn't match the seed data.

## Hints

<details>
<summary>On Section 2's "other 23 orgs" decision</summary>

Two defensible positions exist. One: since the bug is generic (a caching issue, not something specific to Cascade Freight's data), any of the 24 exposed orgs could theoretically have hit it, so transparency to all of them is the safer and more trustworthy choice even without a confirmed second incident. Two: notifying 23 orgs about a bug that (so far) affected exactly one of them risks manufacturing alarm disproportionate to confirmed impact, and a narrower internal-monitoring-only approach for the other 23 is defensible if you're confident in your ability to detect a second occurrence quickly. Either is acceptable here — what's being judged is whether you reasoned about it, not which one you picked.

</details>

<details>
<summary>On Section 3's missing data</summary>

The current `guest_invitations` schema tracks one row per invitation, not a full history of a guest's project memberships over time. To actually answer "who was removed from one project and re-invited to another," you'd need an event log of membership changes (add/remove events with timestamps), not just the invitation snapshot this table gives you. Naming that gap honestly is the correct answer — it mirrors the real experience of running a postmortem and discovering the telemetry you need doesn't exist yet.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Pacing | Re-launches same day, or offers no soak period | Re-launch criteria include a fresh, justified soak period appropriate to the tier chosen |
| Customer comms | Vague, over-technical, or speculative about scope | Concrete, appropriately scoped, honest about what's confirmed vs. still being investigated |
| Data honesty | Invents a query against columns that don't exist | Correctly identifies the schema gap and states what telemetry is actually needed |
| Prevention | Generic ("be more careful") | Specific test + specific monitoring change, each tied to the actual failure mode |
| Tone | Assigns blame to a person/team | Describes the mechanism; blameless per Lecture 3 |

## Submission

Commit `recovery-plan.md` to your portfolio under `c44-week-09/challenge-02/`.
