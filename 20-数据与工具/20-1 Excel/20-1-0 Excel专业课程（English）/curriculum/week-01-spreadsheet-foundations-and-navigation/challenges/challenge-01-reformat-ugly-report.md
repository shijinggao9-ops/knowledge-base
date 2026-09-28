# Challenge 1 — Reformat an Ugly Report to Readable

**Time:** ~60 minutes. **Difficulty:** Medium. **No single right answer.**

## The scenario

Someone on your team exported a report straight out of an old system and forwarded it to you with the message "can you make this readable before the Monday meeting?" That's this challenge. You're not adding any new data or formulas — you're taking genuinely bad formatting and making it something a VP can glance at and understand in five seconds.

## Build the ugly report

First, recreate the mess. Add a new sheet, name it `Challenge 1 — Before`. Enter this data **and deliberately apply the bad formatting described** so you're practicing the *fix*, not just starting from a blank slate:

| Region | rep_name | units | price | total |
|---|---|---|---|---|
| east | alvarez, m. | 42 | 19.99 | 839.58 |
| east | byrne, k. | 31 | 19.99 | 619.69 |
| west | chen, l. | 58 | 21.5 | 1247 |
| west | diallo, a. | 27 | 21.5 | 580.5 |
| north | evans, r. | 19 | 18.75 | 356.25 |
| north | evans, r. | 19 | 18.75 | 356.25 |
| south | fischer, t. | 0 | 22 | 0 |

Now make it deliberately ugly:

1. Set the **entire sheet's font** to a default that looks cramped (leave it as whatever the default is, but don't widen any columns — leave every column at its default narrow width so several values truncate or show `#####`).
2. Leave the header row **not bold**, same formatting as the data.
3. Leave `units`, `price`, and `total` as **General** format — no currency symbols, no consistent decimals (notice `total` already has inconsistent decimals in the raw data above — 1247 has none, others have two).
4. Do not freeze anything.
5. Leave the duplicate `north / evans, r.` row exactly as-is (it's a real duplicate export row — this challenge is about formatting, not data cleaning, but you should *notice* it).

Take a mental (or literal) screenshot — this is your "before."

## Your task

Duplicate the sheet (Lecture 2, section 5 — "Duplicate a sheet"), rename the copy `Challenge 1 — After`, and fix it. You decide the exact choices, but your result must satisfy every constraint below.

### Constraints (all must be true in "After")

- Header row is visually distinct from data (bold, fill color, and/or border — your call).
- Every column is wide enough that nothing truncates or shows `#####`.
- `price` and `total` use a consistent currency format (same symbol, same decimal places, throughout).
- `units` uses a consistent whole-number format.
- `rep_name` values are presented in a consistent, readable case — decide whether `alvarez, m.` becomes `Alvarez, M.` or something else, and apply it consistently. *(You may need to retype these by hand — that's fine, this challenge is about the formatting decision, not a text-function shortcut, which comes in Week 4.)*
- The header row is frozen.
- At least one conditional formatting rule flags something meaningful (your call — zero units? the highest total? your choice, but state *why* you picked it).

### Judgment calls you must make and document

Write your answers in a `challenge-01-notes.md` file (or a text box/comment on the sheet):

1. **Region casing** — did you capitalize `east/west/north/south`? Why or why not?
2. **The duplicate row** — you weren't asked to delete it (data cleaning is Week 5), but does leaving an obvious duplicate visually unflagged undermine the "readable" goal? What did you decide, and why?
3. **Borders** — how heavy did you go? Defend your choice against "too noisy" and "too plain."
4. **Zero-units row (south / fischer)** — is this an error, a real data point, or ambiguous? How does your formatting treat it, and why?

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Legibility | Still requires squinting or horizontal scrolling to read | Every value readable at a glance, no truncation |
| Consistency | Mixed decimal places or symbols within a column | Every column format is uniform top to bottom |
| Restraint | Every cell has a border and three colors | Formatting draws the eye to what matters, nothing more |
| Judgment | No stated reasoning | All four judgment calls documented with a real "why" |
| Fidelity | Also changed the underlying numbers | Only formatting/presentation changed — values are untouched (except the deliberate `rep_name` case fix, which is presentation, not data) |

## Submission

Keep both `Challenge 1 — Before` and `Challenge 1 — After` sheets in your workbook, plus `challenge-01-notes.md`, so the improvement — and your reasoning — is visible side by side.
