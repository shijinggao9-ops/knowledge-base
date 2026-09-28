# Challenge 1 — Clean a Real-World CSV Dump

**Time:** ~60 minutes. **Difficulty:** Medium–Hard. **No single right answer.**

## The scenario

Crunch Outfitters just migrated off an old point-of-sale system, and the vendor handed you a raw CSV export of last quarter's in-store repair-and-order log — a file nobody has looked at closely since it was exported, combining months of manual staff entry, imports from two older systems, and at least one accidental double-export. This is the closest thing this course gives you to an actual file landing in your inbox with a note that says "can you clean this up before Friday?"

Unlike the exercises, this dataset combines **every problem from this week at once**, some of them layered on top of each other, and a few new ones the lectures only mentioned in passing. Nothing here is telling you which techniques to apply where — that judgment is the point.

## The raw data

Add a sheet named `Ch1-RawDump` and type this in **exactly as shown**, including every space, casing choice, and format quirk:

```
OrderID,CustomerName,Phone,State,Item,Qty,UnitPrice,OrderDate
5001,  Wendy Carter ,555.402.1187,CA,Trail Backpack,1,89.99,2025-01-08
5002,Marcus Diallo,(555) 402-1188,California,Sleeping Bag,2,64.50,01/09/2025
5003,Wendy Carter,555-402-1187,ca,Trail Backpack,1,89.99,1/8/2025
5004,Lena Ostrowski,555.402.1189,NV,Camp Stove,1,52.00,1/12/25
5005,Marcus  Diallo,555-402-1188,CA,Sleeping Bag,2,64.50,2025-01-09
5006,,555.402.1190,NV,Tent 4-Person,1,199.00,01/14/2025
5007,Hana Suzuki,555-402-1191,nevada,Hiking Boots,1,110.00,2025-01-15
5008,Carlos mendez,555.402.1192,OR,Rain Shell,3,44.99,01/18/2025
5009,Wendy Carter,555-402-1187,CA,Water Bottle,4,12.00,1/20/2025
5010,Priya Chandra,555.402.1193,oregon,Trekking Poles,1,38.00,2025-01-21
5011,Bill Nakashima,555-402-1194,OR,Camp Stove,1,52.00,01/22/2025
5012,Carlos Mendez,555.402.1192,or,Rain Shell,3,44.99,1/18/25
5013,Fatima Al-Rashid,555-402-1195,NV,Sleeping Bag,1,64.50,2025-01-25
5014,Priya  Chandra,555.402.1193,OR,Trekking Poles,1,38.00,01/21/2025
5015,,,,,,,
5016,Grace Feldman,555-402-1196,CA,Boots Sandals,2,55.00,01/29/2025
5017,Marcus Diallo,555.402.1188,CA,Water Bottle,-1,12.00,02/01/2025
5018,Hana Suzuki,555-402-1191,NV,Hiking Boots,1,110.00,02/03/2025
5019,Fatima AlRashid,555-402-1195,nv,Sleeping Bag,1,64.50,1/25/25
5020,Ivan Petrov,555.402.1197,WA,Fleece Pullover,2,,02/05/2025
```

## Your task

Produce a clean `Ch1-CleanDump` sheet and a short `Ch1-Notes.md` (or a `Notes` sheet) documenting every judgment call. Specifically:

1. **Handle the fully blank row** (5015) and the row with a **missing customer name** (5006) — decide and document whether a missing name means "discard the row" or "keep it and flag it for manual follow-up." There's a real argument for either; state yours.

2. **Dedupe.** There are at least three sets of duplicate/near-duplicate orders in here. At least one pair (5001/5003, Wendy Carter's backpack) looks like a true duplicate order — same customer, same item, same date, different phone *formatting* only. At least one other pair (5002/5005, Marcus Diallo's sleeping bags) has the **exact same order** entered on two consecutive-looking dates — is that a duplicate, or two real orders one day apart? Decide, document, and be consistent about how you decide it for every ambiguous pair you find (there are more than the two called out here — find them).

3. **Standardize `State`.** Collapse every state to one of exactly four canonical values: `California`, `Nevada`, `Oregon`, `Washington`.

4. **Standardize `Phone`.** Pick **one** consistent format (e.g., `555-402-1187`) and normalize every phone number to it — you'll need to strip out dots, parentheses, and spaces, then re-insert your chosen separator. `SUBSTITUTE` (chained) is the right tool; a single `TRIM`/`Find & Replace` pass won't fully solve this one, since the raw formats use three *different* separator characters (`.`, `-`, and `(555) `-style parentheses-plus-space).

5. **Standardize `OrderDate`.** Every date needs to end up as a real, uniformly formatted date value — not a mix of text strings in three different patterns. Confirm with `ISNUMBER` that every cell in your final column is a true date, not text that merely looks like one.

6. **Handle the negative `Qty`** (order 5017, `Qty = -1`). Is that a data-entry error, or could it represent a legitimate return/refund line in a real point-of-sale export? State your interpretation and either fix or flag it accordingly — don't just delete it without a documented reason.

7. **Handle the missing `UnitPrice`** (order 5020). You have enough information elsewhere in the sheet to reasonably infer it — do that, and explain your method (don't just type in a guess with no basis).

8. **Final audit.** Re-run frequency-count and duplicate-flag formulas from Lecture 1 against your finished `Ch1-CleanDump`. Screenshot or paste the "all clear" result into your notes.

## Constraints

- Every non-obvious decision gets one sentence in your notes: what you decided, and why. A cleaned sheet with no documentation of judgment calls is an incomplete answer, even if every formula is technically correct.
- Prefer the formula → verify → paste-as-values cycle from Lecture 2 over silent manual retyping — your work should be reconstructable by someone else reading your formulas before you converted them to values.
- Don't touch the raw `Ch1-RawDump` sheet — all cleaning happens on the copy.

## Hints

<details>
<summary>On the phone-number normalization (Task 4)</summary>

Strip every non-digit character first, then re-insert dashes at fixed positions. One path: `=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B2,".",""),"-",""),"(",""),")","")` strips the four punctuation variants down to bare digits (you'll also need to handle the literal space in `"(555) 402-1188"` — that's a fifth `SUBSTITUTE`). Once you have 10 clean digits, rebuild the dashed format with `LEFT`/`MID`/`RIGHT` (Week 4 skills): `=LEFT(digits,3)&"-"&MID(digits,4,3)&"-"&RIGHT(digits,4)`.

</details>

<details>
<summary>On inferring the missing UnitPrice (Task 7)</summary>

Order 5020 is a `Fleece Pullover`. Does any *other* row in the dump sell the same item, and if so, at what price? A quick `XLOOKUP`/`COUNTIF` scan of the `Item` column for a matching price elsewhere is a defensible, documented method — better than an unexplained guess.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Completeness | Fixes the obvious problems, misses the subtler dupes/negative qty | Finds and addresses every issue listed, including the ambiguous ones |
| Judgment | Deletes anything odd without comment | Every non-obvious call gets a documented reason |
| Consistency | Different dedupe logic applied to different ambiguous pairs | One clearly stated rule applied uniformly |
| Verifiability | Final sheet is just typed values with no trace of method | Formula scaffolding visible or referenced in notes before paste-as-values |
| Final state | Audit formulas still flag something | Frequency count and duplicate flags come back fully clean |

## Submission

Commit `Ch1-CleanDump` and your notes to your portfolio under `c41-week-05/challenge-01/`.
