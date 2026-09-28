# Exercise 2 — Build a Cross-Functional Launch Checklist

**Goal:** Build a launch checklist for Guest & External Collaborator Access that a real go/no-go meeting could run from — organized by function, with a named owner and a pass/fail state per item, gated per tier.

**Estimated time:** 90 minutes.

## Setup

Re-read Lecture 2 in full, especially Section 3 (RACI) and Section 4 (go/no-go gates). Create a file `launch-checklist.md`.

## Part A — Tier and risk justification (20 min)

Before the checklist itself, write 3–5 sentences answering:

1. Which of the four launch tiers (internal, private beta, limited GA, full GA) does Guest Access need, and why — walk through the four risk questions from Lecture 2 Section 1 (blast radius, reversibility, support cost, brand exposure) explicitly.
2. Name the two "yes, this is risky" answers that most strongly justify **not** skipping straight to full GA.

## Part B — The checklist (50 min)

Build a table (or a nested checklist — your choice of format) with these columns: **Item / Function / Owner (role, not a name) / Tier it gates / Done criteria**.

Cover **at least these categories**, with a minimum of 2 items each:

- **Product** (e.g., feature flag configured and tested for targeted enable/disable; rollback runbook written)
- **Engineering** (e.g., monitoring/alerting live for the specific failure mode from Lecture 3's Cascade Freight case study; load-tested for the `ga_100` org count)
- **Marketing** (e.g., positioning finalized from Exercise 1; docs/help center article published)
- **Sales** (e.g., battlecard shipped; the 3 blocked-deal AEs briefed with a specific date)
- **Support** (e.g., macro/runbook shipped; support team trained on the permission model before beta starts)
- **Legal/Security** (e.g., security review sign-off current for the segment about to be exposed; data processing implications reviewed for guest accounts)

For each item, be specific about **which tier boundary it gates** — an item that must be true before *private beta* starts is different from one that only needs to be true before `ga_100`. A checklist where everything gates "launch" generically is not useful in a real go/no-go meeting, because nobody can tell what's actually blocking *this* tier transition.

## Part C — The go/no-go criteria for one tier boundary (20 min)

Pick **one** tier boundary (e.g., private beta → `ga_25`). Write the specific go/no-go criteria for that boundary, using Lecture 2 Section 4 as a template, but make at least 2 of the criteria **numeric and checkable against the seed data** (e.g., "invite → accept rate across beta orgs ≥ 30%" — then actually check it against `guest_invitations`).

## Expected outcome

- A checklist with 6 functional categories, 2+ items each (12+ items total), each with an owner role and a tier gate.
- At least 3 items reference something specific to Guest Access (the permission model, the audit log dependency, the 3 blocked deals) — a checklist that's fully generic and could apply to any feature hasn't engaged with this launch's actual risk.
- A go/no-go section for one tier boundary with at least 2 numeric, checkable criteria.

## Done when…

- [ ] `launch-checklist.md` has the tier justification, the full checklist, and the one tier-boundary go/no-go section.
- [ ] Every checklist item has a named owner role (not "TBD" or "someone").
- [ ] At least one item explicitly references the Cascade Freight-style failure mode (a monitoring/alerting item for permission-scope bugs) — you're writing this checklist with Lecture 3's incident already in mind, even though the checklist itself is meant to run *before* launch.
- [ ] The go/no-go criteria include at least 2 numbers you can actually check against the seed data, and you show the check.

## Stretch

Add a **"known risks we're accepting"** section — 2–3 risks you identified but decided not to gate the launch on, and one sentence each on why. A checklist that pretends zero risk remains at launch is dishonest; a strong checklist names what's left over and why that's an acceptable trade.

## Submission

Commit `launch-checklist.md` to your portfolio under `c44-week-09/exercise-02/`.
