# Exercise 3 — Define Launch Success Metrics in SQL

**Goal:** Write the SQL queries that turn "is the Guest Access launch working" into checkable facts — an activation funnel, a per-org risk check, and a wave-readiness check — using the seed data, without copying Lecture 3's queries verbatim.

**Estimated time:** 90 minutes.

## Setup

Confirm the seed data is loaded (see the [week README](../README.md)) and the four sanity counts pass: `orgs` = 24, `rollout_exposures` = 24, `guest_invitations` = 32, `support_tickets` = 16.

Create a file `launch-queries.sql`. Put each answer under a `-- Task N` comment.

## Tasks

1. **Exposure by region.** For each `region` in `orgs`, count how many exposed orgs are in each rollout `phase`. *(You'll need to join `orgs` to `rollout_exposures`. Expected: 12 rows — all 4 regions appear in all 3 phases. US-East has the most orgs overall (8 across all phases); EU has the fewest (5).)*

2. **Guests per org.** For each org that has sent at least one guest invitation, show `org_name`, `segment`, and the count of invitations sent. Order by count descending. *(Expected: 24 rows — every org has sent at least one invitation. Fenwick & Co and Cascade Freight tie for the most, at 3 each.)*

3. **The activation funnel, by phase instead of by segment.** Adapt Lecture 3's Section 3.2 query (invited → accepted → took action) to group by rollout **phase** instead of segment. *(Expected: 3 rows, one per phase. `beta` should show the strongest `pct_of_accepted_that_activated`, since it's the most-engaged, hand-selected group.)*

4. **Never-accepted invites.** List every guest invitation where the guest was invited but **never accepted** — show `org_name`, `guest_email`, `invited_at`, and how many days have passed since the invite (`CURRENT_DATE` or `CURRENT_TIMESTAMP` minus `invited_at`, in whole days). *(Expected: 6 rows. This is your "stalled funnel" list — a real launch owner would follow up on these.)*

5. **The org-level risk check.** Without looking back at Lecture 3 Section 3.4, write your own version: for every org with **any** `support_tickets` row where `category LIKE 'guest_access%'`, show `org_name`, `segment`, `phase`, total ticket count, and count of `high`+`critical` tickets. Order by the high+critical count descending. *(Expected: one org — Cascade Freight — has a nonzero high+critical count. If your query doesn't surface it clearly at the top, check your `ORDER BY`.)*

6. **The wave-readiness percentage.** For each phase, compute the percentage of exposed orgs that have **zero** `guest_access%` tickets at all (a rough "clean org" rate). *(Expected: `beta` and `ga_25` should come out equal — 50% clean — and `ga_100` lower still, at 37.5% clean, even though `ga_100`'s raw ticket count isn't dramatically higher. Most of `ga_100`'s tickets are ordinary low-severity confusion, same as the earlier waves — it's Cascade Freight's 2 *critical* tickets on top of that baseline that should worry you, not the clean-rate dip alone.)*

## Expected result (spot checks)

- Task 1 → EU rows only exist for `beta` and `ga_25`, never `ga_100`.
- Task 2 → 24 rows total; org 4 (Fenwick & Co) and org 17 (Cascade Freight) tie for the highest, at 3 invitations each.
- Task 3 → 3 rows; `beta`'s activation percentage is the highest of the three phases.
- Task 4 → 6 rows.
- Task 5 → Cascade Freight is the only org with a nonzero `high`+`critical` count (2).
- Task 6 → `beta` and `ga_25` both come out at 50% clean; `ga_100` is lower, at 37.5%.

## Done when…

- [ ] `launch-queries.sql` has all 6 queries, each under a `-- Task N` comment.
- [ ] Task 3 and Task 5 are written from scratch — structurally similar to Lecture 3's queries, but adapted to a different grouping, not copy-pasted unchanged.
- [ ] Task 4 correctly excludes invitations that *were* accepted (only `accepted_at IS NULL` rows appear).
- [ ] Your row counts and the Cascade Freight result match the spot checks above.
- [ ] You can explain, in one sentence, why Task 6's "clean org rate" can drop even when the *raw ticket count* barely changes between phases (hint: it's about the denominator, not just the numerator).

## Stretch

Write a 7th query: for the org(s) flagged in Task 5, compute the number of **hours** between their first `guest_access%` ticket and the org's `flag_enabled_at` from `rollout_exposures` — i.e., how long after exposure did the first sign of trouble appear? *(Expected: under 48 hours for Cascade Freight — a fast-surfacing bug, which is part of why the pause-then-kill-switch response in Lecture 3 was appropriately quick rather than overreacting to a slow-burning pattern.)*

## Submission

Commit `launch-queries.sql` to your portfolio under `c44-week-09/exercise-03/`.
