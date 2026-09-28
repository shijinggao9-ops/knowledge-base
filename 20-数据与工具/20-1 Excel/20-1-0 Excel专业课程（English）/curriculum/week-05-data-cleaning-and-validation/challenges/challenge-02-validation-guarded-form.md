# Challenge 2 — Build a Validation-Guarded Entry Form

**Time:** ~60 minutes. **Difficulty:** Medium. **No single right answer.**

## The scenario

The cleanup from Challenge 1 is a one-time fix. Unless Crunch Outfitters changes *how new orders get entered*, the exact same mess reappears next quarter. Your job this time is to design the **guard rail**: a genuinely robust order-entry form that makes most of Challenge 1's problems impossible to create in the first place, using only Data Validation, dependent drop-downs, and conditional formatting — no macros, no external tools.

This is a design challenge as much as a build challenge. There's no single "correct" set of rules — there's a defensible set, and a sloppy set, and the rubric at the bottom tells you which is which.

## Your task

Build a sheet named `Ch2-EntryForm` for a new order-entry form covering the same domain as Challenge 1 (customer orders for outdoor gear). At minimum, it must include:

1. **`Order ID`** — guarded against duplicates (custom formula, uniqueness).
2. **`Customer Name`** — guarded against being left blank (custom formula or a required-field convention you document — plain Data Validation can't force non-blank on its own in every version, so state clearly how you're enforcing this, even if it's partly a conditional-formatting flag rather than a hard block).
3. **`Phone`** — guarded so it can **only** be entered in one consistent format. *(Hint: a custom-formula rule checking the text matches a fixed pattern — e.g., exactly 12 characters with dashes in the right positions — is more robust than hoping people type it right. Decide what "right" means and enforce exactly that.)*
4. **`State`** — a List validation drawing from a clean 4-value reference list (reuse Challenge 1's canonical states).
5. **`Item Category`** then **`Item`** — a genuine **dependent drop-down pair**: pick a category (`Apparel`, `Footwear`, `Gear` — or design your own reasonable set covering the items from Challenge 1), and `Item` only offers items within that category.
6. **`Qty`** — a Decimal/Whole-Number validation that **rejects negative and zero values outright** (a direct fix for Challenge 1's Task 6 ambiguity — decide here whether returns/refunds get a *separate* field instead of a negative `Qty`, and if so, add it).
7. **`Unit Price`** — a Decimal validation with a sane minimum and maximum for this product line (you decide the bounds; document why you picked them).
8. **`Order Date`** — a Date validation that rejects dates before the business existed (pick a reasonable founding year) and rejects dates in the future.

On top of the validation rules, add **at least three conditional-formatting flags** that catch things validation structurally can't prevent — for example: a row whose `Item` no longer matches its `Item Category` after a parent field was changed (Lecture 3, Section 6/Exercise 3's staleness case), a suspiciously high `Qty × Unit Price` total worth a second look, or a `Customer Name` that's a near-duplicate (by your Lecture-1 normalized-key technique) of one already in the sheet — a soft warning, since blocking new customers outright would be too aggressive for a live validation rule.

## Stress test

Once built, deliberately try to break your own form with **at least 8 bad entries** — one attempt per guarded field, plus at least one combined "chaos" row that tries to violate several rules simultaneously. For each attempt, record: what you tried to enter, what happened (rejected outright / accepted but flagged / accepted with no warning), and whether that outcome is what you intended. Finding a hole in your own design and being honest about it in this log is worth more credit than a report claiming everything worked perfectly on the first try.

## Constraints

- Every validation rule needs an **Input Message** explaining what's expected — a rule with no explanation just produces a confused user staring at a rejected cell with no idea why.
- Every rule needs a documented reason for its **Stop vs. Warning** choice (Lecture 3, Section 2) — don't default to Stop everywhere without thinking about which fields genuinely need a hard block versus a soft nudge.
- The dependent drop-down (Task 5) must be built with the `FILTER`-based (or `INDIRECT`-fallback) technique from Lecture 3 — a pair of independent, unlinked drop-downs that merely *happen* to look related does not satisfy this requirement.

## Hints

<details>
<summary>On enforcing a strict phone format (Task 3)</summary>

`=AND(LEN(A2)=12, MID(A2,4,1)="-", MID(A2,8,1)="-", ISNUMBER(VALUE(LEFT(A2,3))), ISNUMBER(VALUE(MID(A2,5,3))), ISNUMBER(VALUE(RIGHT(A2,4))))` checks the total length, both dash positions, and that all three digit groups are actually numeric — rejecting `555.402.1187`, `(555) 402-1188`, and a too-short or too-long entry, while accepting only `555-402-1188`-shaped input.

</details>

<details>
<summary>On the "returns get a separate field" design decision (Task 6)</summary>

A common real-world pattern: keep `Qty` strictly positive, and add a separate `Order Type` drop-down (`Sale` / `Return`) so a return is a **labeled** row, not a sign-flipped number that a `SUM` formula might silently net against sales without anyone noticing. If you go this route, say so explicitly — it's a legitimate and arguably *better* design than allowing negative quantities at all.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Coverage | Some of the 8 required fields lack any real guard | All 8 fields have a genuine, working rule |
| Dependent drop-down | Two unlinked lists that happen to look related | A real `FILTER`/`INDIRECT`-driven cascade, tested and working |
| Stop vs. Warning reasoning | Every rule defaults to Stop with no explanation | Each choice is deliberate and justified in one sentence |
| Stress test honesty | Claims everything worked with no evidence | 8+ documented attempts, including at least one genuine hole found and acknowledged |
| Conditional-formatting flags | Fewer than 3, or duplicate the validation rules exactly | 3+ flags that catch what validation structurally cannot |

## Submission

Commit `Ch2-EntryForm` and your stress-test log to your portfolio under `c41-week-05/challenge-02/`.
