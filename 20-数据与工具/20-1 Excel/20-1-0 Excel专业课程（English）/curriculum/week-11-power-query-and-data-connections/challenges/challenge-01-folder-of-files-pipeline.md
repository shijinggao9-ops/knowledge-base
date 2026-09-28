# Challenge 1 — Combine a Folder of Files

**Time:** ~90 minutes. **Difficulty:** Medium. **You add the fourth file.**

## The scenario

Crunch Wholesale doesn't have three warehouses forever. It has three *this week*, and the distributor is actively opening a fourth in the Midwest. Whatever pipeline you build has to survive that — not by you editing a query in six months when the new warehouse's first export lands, but by the pipeline simply absorbing it the next time someone clicks Refresh. That's the actual test this challenge sets: build it once, then prove it scales without being touched.

## Your task

Build one Power Query pipeline, starting from `Data → Get Data → From File → From Folder` pointed at your `warehouse-exports` subfolder, that combines `North_Week1.csv`, `South_Week1.csv`, and `West_Week1.csv` into a single, correctly-typed output — then add a fourth file and refresh, with **zero edits** to any existing step.

### Requirements

1. **Use `From Folder`, not three separate imports.** This is the whole point of the challenge — a query that automatically enumerates whatever files exist in the folder, not a query hard-wired to three specific filenames.
2. **The combined output must have the correct types** on every column (`OrderDate` as a real date, `Qty` and `UnitCost` as numbers) — confirm the sample-file query Power Query builds behind the scenes handles South's differently-ordered columns correctly (it should, matching by name, per Lecture 3).
3. **Add a source column.** Before finishing, add a column (via `Add Column → Custom Column`, or by keeping the auto-generated `Source.Name` column that `From Folder` produces) that records which file each row came from — this is what lets you audit "how many orders came from which warehouse" later, something plain appending alone doesn't give you for free.
4. **Verify the 3-file baseline.** Sum `Qty × UnitCost` across the combined 14 rows — it must read **6934.50** before you touch a fourth file.
5. **The growth test.** Create a fourth file, `Midwest_Week1.csv`, in the same `warehouse-exports` folder, with **at least 4 rows** of data you invent yourself (same six-column schema: `OrderID`, `OrderDate`, `SKU`, `ProductName`, `Qty`, `UnitCost` — reuse existing SKUs from `Products.csv` so a later merge would still work). Click **Refresh** on your combined query. Confirm — and document in `challenge-01.md` — that:
   - The row count increased by exactly however many rows you added.
   - The new checksum equals **6934.50 plus your Midwest rows' `Qty × UnitCost` sum**, computed by hand and compared.
   - The `Source.Name` (or your custom source column) correctly shows `Midwest_Week1.csv` for the new rows.
   - You touched **zero** Applied Steps to make this happen — only Refresh.

## What "zero edits" actually means here

A pipeline fails this challenge if any of the following is true after adding the Midwest file:

- You had to open the query editor and adjust a step for the new rows to appear correctly.
- The new rows appear but with wrong types, a missing column, or under the wrong source label.
- The checksum doesn't match your hand-computed expectation.

If any of those happen, that's useful information, not a failure of the challenge — diagnose why (a common cause: the *sample file* Power Query chose to build the transform steps from had a quirk — a column order, a type — that the new file doesn't share in the same way; another common cause: a stray file, like a `.xlsx` you accidentally saved into the same folder, getting picked up and breaking the combine). Fix it, and document exactly what you found in `challenge-01.md`.

## Constraints

- All four files must live in the same `warehouse-exports` folder — no combining across multiple folders.
- The Midwest file must use the exact same header names as the other three (this challenge tests folder-combine mechanics, not column-name reconciliation — that's a natural extension you can attempt as a stretch, not a requirement).
- Do not delete or rebuild the query for the growth test — the whole point is that the *existing* query absorbs the new file.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Folder combine | Three files imported and appended manually | Genuine `From Folder` connector used from the start |
| Type correctness | Some columns left as `Text` or `Any` | Every column explicitly, correctly typed |
| Source tracking | No way to tell which row came from which file | A working `Source.Name` or custom source column |
| Growth test | Claimed to work, never actually tested | Fourth file actually added, refreshed, checksum verified by hand |
| Debugging | A mismatch left unexplained | Any discrepancy found and explained, with the fix documented |

## Submission

Commit the workbook plus `challenge-01.md` (your growth-test log, hand-computed checksum, and anything you had to fix) to your portfolio under `c41-week-11/challenge-01/`.
