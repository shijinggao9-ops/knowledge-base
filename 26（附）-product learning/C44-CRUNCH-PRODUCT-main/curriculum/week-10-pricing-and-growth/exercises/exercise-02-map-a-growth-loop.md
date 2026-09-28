# Exercise 2 — Map and Instrument a Growth Loop

**Goal:** Query the raw `referral_events` data from Lecture 2 to compute Loopline's guest-invite loop's real funnel, k-factor, and cycle time — then draw the loop yourself and identify where the instrumentation has a gap.

**Estimated time:** 60–90 minutes.

## Setup

You should already have `referral_events` seeded from Lecture 2 ([lecture-notes/02-growth-loops-and-funnels.md](../lecture-notes/02-growth-loops-and-funnels.md), Section 5). If not, go run that `CREATE TABLE`/`INSERT` block first — this exercise assumes all 40 rows are already in your database.

Sanity check:

```sql
SELECT COUNT(*) FROM referral_events;   -- should print 40
```

## Tasks

1. **Reconstruct the funnel.** Write one query that returns, in a single row: invites sent, accepted, signed up, activated, became paid. (This is the query from Lecture 2, Section 5 — type it from memory if you can, then check it against the lecture.)

2. **Compute step-by-step conversion rates**, not just totals. In `funnel.md`, write out, as percentages:
   - sent → accepted
   - accepted → signed up
   - signed up → activated
   - activated → became paid
   - the full sent → became paid rate

   Each should be a single `SELECT` using `COUNT()` on the relevant nullable column, divided by the prior stage's count.

3. **Compute k-factor and cycle time** using the two queries from Lecture 2, Section 5. Confirm you get **k ≈ 0.75** and **avg cycle time ≈ 4.0 days**. If your numbers don't match, check whether you're dividing by `COUNT(*)` (all 40 invites) versus `COUNT(DISTINCT inviter_user_id)` (16 inviters) in the right places — this is the single most common mistake in this exercise.

4. **Find the weakest link.** Of the four step-by-step conversion rates from Task 2, which one is lowest? Write two sentences in `funnel.md`: what does that step's low conversion suggest about *where* in the loop Loopline should invest next — the invite itself, the guest-viewing experience, the signup prompt, or the paid-conversion nudge?

5. **Draw the loop.** In `loop-diagram.md`, redraw Lecture 2's ASCII loop diagram (trigger → action → output → new input) **in your own words**, replacing each generic label with the *specific* Loopline behavior at that stage (e.g., don't write "ACTION," write what the inviter is actually doing).

6. **Find the instrumentation gap.** The `referral_events` table logs `accepted_at`, `signed_up_at`, `activated_at`, and `became_paid_at` — but it does **not** log whether the *new* account (once created) goes on to send its own guest invites, which is the event that actually closes the loop back to "new input" in the diagram. Write one paragraph in `loop-diagram.md`: what new column or table would you add to close that gap, and what query would you then be able to run that you can't run today?

## Expected outcome (self-check)

- Funnel: **40 sent → 28 accepted (70%) → 19 signed up (67.9% of accepted) → 12 activated (63.2% of signups) → 6 became paid (50% of activated).**
- k-factor: **2.5 invites/inviter × 0.30 invite-to-active rate = 0.75.**
- Cycle time (invite sent → activated): **4.0 days average.**
- The weakest single-step conversion is **signed up → activated at 63.2%**, not the more commonly assumed weak point (accepted → signed up, actually the strongest step-to-step conversion in this data at 67.9%) — a guest who accepts an invite and signs up for their own account is already fairly bought in; the drop happens *after* signup, during onboarding. That should sound familiar — it's the same "signups climbing, activation lagging" pattern flagged all the way back in Week 1's metrics exercise.

## Done when…

- [ ] `funnel.md` has all five conversion rates and the weakest-link paragraph.
- [ ] Your computed k-factor and cycle time match the expected outcome above (or you can explain, with a specific query difference, why yours differs).
- [ ] `loop-diagram.md` has the redrawn, Loopline-specific loop and the instrumentation-gap paragraph.

## Stretch

- Rerun the k-factor query filtered to `WHERE inviter_account = 'Kingsford Software'` only. Is Kingsford's individual loop stronger or weaker than the company-wide average? What would you do differently for accounts whose loop performance looks like Kingsford's versus the company average?
- If Loopline could raise `invite_to_active_rate` from 0.30 to 0.40 through better onboarding for invited guests specifically (no change to how many invites get sent), what would the new k-factor be? Is that alone enough to cross k = 1?

## Submission

Commit `funnel.md` and `loop-diagram.md` to your portfolio under `c44-week-10/exercise-02/`.
