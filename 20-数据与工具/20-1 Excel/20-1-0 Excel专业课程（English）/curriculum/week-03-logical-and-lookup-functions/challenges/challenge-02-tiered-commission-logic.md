# Challenge 2 — Build Tiered Commission Logic

**Time:** ~60 minutes. **Difficulty:** Medium-High. **Two valid designs — you must pick one and defend it.**

## The scenario

Crunch's sales manager hands you this policy, verbatim, the way real policies get written — mostly clear, with two genuine ambiguities you have to resolve and document:

> "Commission is based on total quarterly sales. Under \$20,000, no commission. \$20,000 up to \$50,000, 4%. \$50,000 up to \$100,000, 6%. \$100,000 and above, 8%. Reps who hit **any** tier at 6% or higher also get a flat \$500 bonus. New reps (less than 6 months tenure) are capped at the 4% tier regardless of sales, to keep ramp-up incentives sane."

## Build the data

```
       A          B              C            D
1    Rep        QuarterSales   TenureMonths
2    Amara      112000         18
3    Devon      48000           4
4    Priya      61000          22
5    Malik      19500           9
6    Sofia      95000           3
7    Kenji      50000           7
8    Tomas      201000         11
```

## Your task

1. **Resolve the boundary ambiguity.** "\$20,000 up to \$50,000" — is \$50,000 exactly in the 4% tier or the 6% tier? The policy text is genuinely ambiguous at every boundary. Pick one consistent rule (commonly: the tier a number lands in is the one where it's `>=` the tier's floor) and **state it explicitly** in your writeup before writing any formula. Apply that same rule at all three boundaries.

2. **Build the base commission rate.** Using your stated boundary rule, write a formula (`IFS`, nested `IF`, or an approximate-match lookup table — your choice, see the design question below) that returns the correct rate (`0`, `0.04`, `0.06`, or `0.08`) for each rep's `QuarterSales`. Test it against every row, including `Kenji` (`50000`) and `Devon` (`48000`) — they're one dollar apart from a boundary on purpose.

3. **Apply the new-rep cap.** Wrap or extend your formula so any rep with `TenureMonths < 6` is capped at the 4% tier **even if their sales would otherwise put them at 6% or 8%**. Sofia (`95000`, `3` months) is the deliberate trap here — her sales alone would put her at 6%, but her tenure caps her at 4%.

4. **Compute the bonus flag.** Add a column that returns `"Bonus"` if the rep's **uncapped** tier (their sales-based tier, before the tenure cap) was 6% or higher, `""` otherwise. This is deliberately based on the *sales* tier, not the *final capped* rate — read that carefully, it's the second trap: Sofia's sales alone (`95000`) qualify her for the bonus even though her *paid rate* is capped at 4%. Decide whether that's what the policy actually intends, state your interpretation, and build accordingly (or argue for the opposite reading — either is defensible if you justify it).

5. **Compute the payout.** Add a final column: `QuarterSales * (final capped rate)` + `500` if bonus-flagged, `+0` otherwise.

## Design question — answer in your writeup

Build the rate lookup **two ways** and compare:

- **Way A:** `IFS`/nested `IF` with the thresholds hard-coded directly in the formula.
- **Way B:** a small tier table (`MinSales`/`Rate`, three or four rows) plus `XLOOKUP` with `match_mode = -1` (approximate, next-smaller) or `INDEX`/`MATCH`.

Get both working, confirm they give identical results across all 7 reps, then answer: if the sales manager comes back next quarter and changes the 6% tier to 7%, which design (A or B) is faster and safer to update, and why? Which design would you actually choose for a workbook you expect to hand off to someone else? There's a real, defensible argument for each — pick one and justify it, don't just describe both and shrug.

## Constraints

- State your boundary-inclusion rule (Task 1) in writing **before** any formula — a formula with no stated rule behind it isn't verifiable.
- Every rep's final payout must be traceable: someone reading only your writeup (not your formulas) should be able to hand-verify at least Sofia's and Tomas's numbers.
- No `VLOOKUP` — this challenge is downstream of Challenge 1 on purpose.

## Hints

<details>
<summary>On Sofia's bonus (Task 4)</summary>

Both readings are defensible: "the bonus rewards reps who *earned* a top tier by performance, even if tenure caps their pay" vs. "the bonus is meant to reward reps who are *actually being paid* at 6%+, so a capped rep shouldn't get it." The policy text doesn't say. Pick one, and write one sentence on what real-world consequence your reading has (e.g., "under my reading, a brand-new rep with a huge first quarter gets a $500 bonus on top of a capped rate, which might be exactly the onboarding incentive intended — or might be a loophole").

</details>

<details>
<summary>On the tier table (Way B)</summary>

Your table should look like `MinSales: 0, 20000, 50000, 100000` / `Rate: 0, 0.04, 0.06, 0.08` — four rows, not three, because "no commission" below \$20,000 is itself a tier with a floor of `0`.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|---------------|
| Boundary rule | Inconsistent across the three thresholds | One stated rule, applied identically everywhere |
| Tenure cap | Caps the wrong thing, or caps everyone | Only sub-6-month reps capped, others unaffected, Sofia correctly caught |
| Bonus logic | Based on final rate, contradicting the stated design | Matches whichever interpretation was explicitly chosen and justified |
| Design comparison | Builds only one of Way A / Way B | Both built, both verified identical, a real justified recommendation given |

## Submission

Commit your workbook and `challenge-02.md` (boundary rule, bonus interpretation, and the A-vs-B recommendation) to your portfolio under `c41-week-03/challenge-02/`.
