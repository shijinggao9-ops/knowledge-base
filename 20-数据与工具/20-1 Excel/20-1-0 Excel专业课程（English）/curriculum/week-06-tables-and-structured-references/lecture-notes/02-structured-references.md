# Lecture 2 — Structured References

> **Duration:** ~2 hours. **Outcome:** You can write formulas that refer to a Table's columns by name — `Orders[Total]`, `[@Qty]`, `Orders[#Headers]` — instead of by cell address, both inside the Table and from other sheets, and you can explain exactly why these formulas keep working after a row or column is inserted while A1-style formulas don't.

Lecture 1 gave your `Orders` range a name and the ability to grow. This lecture gives you the formula syntax that makes that name actually useful — **structured references**, the bracket notation (`Table[Column]`) that replaces `D2:D25` with something that reads like English and never goes stale.

## 1. The problem structured references solve

Recall from Week 2: a named range (`TaxRate`) behaves like an absolute reference — self-documenting, but it's still just a name for one fixed block of cells. A Table's structured reference is different in kind: it's a name for a **column of the Table**, and it automatically tracks that column's current boundaries — however many rows the Table currently has, this second, next month, next year. You write the formula once. It's correct forever, as long as it's the Table that grows, not a boundary you typed by hand.

## 2. `[@Column]` — the current row

The single most common structured reference computes a value **in the same row the formula lives in**. Click into the `Total` column's first data cell (next to `1001`, `Webcam 1080p`) and replace its typed value with a real formula:

```
=[@Qty]*[@UnitPrice]
```

Press **Enter**. Two things happen immediately:

1. The result is **45** — `1 * 45.00` — matching the value you typed manually in the README setup. Good; that confirms the formula is right.
2. **Excel fills this formula down the entire `Total` column automatically.** You didn't select the range and fill down — typing one structured-reference formula inside a Table column fills the whole column, because every row of a Table column is expected to compute the same thing the same way. (Google Sheets Tables do this too, though the exact autofill trigger can lag a beat behind Excel's — if it doesn't propagate instantly, select the formula cell and use **Fill down** once, and it will propagate correctly on every future new row without prompting.)

`[@Qty]` means "the value in the `Qty` column, **this row**" — the `@` is what scopes it to the current row instead of the whole column. This is the structured-reference equivalent of what a relative reference (`D2`, not `$D$2`) did in Week 2, except you never have to think about which row you're on — `@` always means "here."

Verify: the checksum from the README, `SUM` of the `Total` column, should still read **5240.60** now that every row is a live formula instead of a typed number. If a row is off, check that row's `Qty`/`UnitPrice` weren't accidentally altered.

## 3. `Table[Column]` — the whole column, no `@`

Outside the Table — in an empty cell elsewhere on the sheet, or on a different sheet — reference an entire column of data (no row scoping) by dropping the `@`:

```
=SUM(Orders[Total])
```

This sums every data row's `Total` — all 24 (or however many exist *right now*, including any you've added since). Compare this directly to last week's and earlier weeks' `=SUM(D2:D25)`: same result today, radically different behavior tomorrow. Add row 25 to the Table and `SUM(Orders[Total])` **updates automatically** the instant you finish typing that row — no edit to the formula, ever.

Try a few more, anywhere outside the Table:

```
=COUNT(Orders[Qty])          -- how many rows have a numeric Qty (all 24)
=AVERAGE(Orders[UnitPrice])  -- average unit price across every order
=MAX(Orders[Total])          -- the single largest order (1745.00, the Standing Desk)
```

Each of these is a plain aggregate function wrapped around a structured reference instead of a cell range — the function doesn't know or care that its argument is a Table column rather than `A2:A25`; the only thing that changed is that the *reference itself* now grows with the data.

## 4. The special-item specifiers: `[#Headers]`, `[#Data]`, `[#Totals]`, `[#All]`

A Table has more than just its data rows — the header row and (if enabled) the Total Row are addressable too, using square-bracket keywords called **special item specifiers**:

| Specifier | Refers to |
|---|---|
| `Orders[#Headers]` | Just the header row (`OrderID`, `OrderDate`, … `Total`) |
| `Orders[#Data]` | Just the data rows — this is what a bare `Orders[Total]` already means by default |
| `Orders[#Totals]` | Just the Total Row, if enabled |
| `Orders[#All]` | Header + data + totals, the entire Table including the parts above |

You'll rarely need `[#Headers]` or `[#All]` in day-to-day formulas — they matter most when you're building a formula that needs to count or reference the Table's structure itself, not its values. One genuinely useful case: referencing the Total Row explicitly from elsewhere in the workbook, so a summary sheet cell always shows "whatever the Table's own Total Row currently says," even if you change which aggregate function that Total Row uses:

```
=Orders[[#Totals],[Total]]
```

This combines a specifier with a column name — read it as "the `Total` column, but only its `#Totals` row." That double-bracket form (`Table[[#Specifier],[Column]]`) is the general pattern any time you need to combine a specifier with a specific column instead of the whole row or whole table.

## 5. Combining columns and rows: a specific cell

You can also point at one exact intersection — a specific row **and** column — using a range-style structured reference:

```
=Orders[[#Headers],[Region]]
```

reads as "the header row, `Region` column only" — returns the text `"Region"`. This is a rare pattern in everyday formulas (you'd normally just type `"Region"` as a literal), but it matters when you're building something generic — a formula that needs to work correctly even if the Table's columns get reordered, because it looks up the header text rather than assuming a fixed position.

## 6. Referencing a Table from another sheet

Structured references work identically from any sheet in the workbook — you don't prefix them with a sheet name the way you would `Data!B2`, because the Table's name (`Orders`) is already workbook-scoped and unique. Add a new sheet tab called `Summary` and, anywhere on it, type:

```
=SUM(Orders[Total])
```

This works exactly like it did on the `Orders` sheet itself — no `Orders!` prefix needed, because `Orders` here refers to the **Table object**, not a sheet. (If you'd also named the sheet tab `Orders`, Excel disambiguates automatically since Table names and sheet names live in separate namespaces — but avoid the confusion and keep them distinct in your own workbooks, as this week's setup already does.)

## 7. Why structured references survive structural edits — and A1 references don't

This is the payoff. Test it directly:

1. **Insert a column.** Right-click the `Category` column header inside the Table → **Insert → Table Column to the Left**. A new blank column appears, and Excel names it `Column1` by default — rename it `Subcategory`. Check your `Total` formula: still `=[@Qty]*[@UnitPrice]`, completely unaffected, because it referenced columns by *name*, and neither `Qty` nor `UnitPrice` moved conceptually even though their physical column letters shifted one to the right.
2. **Insert a row in the middle.** Right-click any data row inside the Table (not the header, not the Total Row) → **Insert → Table Rows Above**. A blank row appears mid-Table, already formatted and already carrying the `Total` column's formula (Lecture 1, Section 3c). `SUM(Orders[Total])` elsewhere in the workbook is unaffected — it never pointed at a row count, only at the Table's data.

Now imagine you'd built this same report as a plain range with `=D2*E2` in the Total column and `=SUM(D2:D25)` in a summary cell. Insert a column to the left of `D` and every `D2*E2` formula silently shifts to reference the wrong columns — you'd have to notice and fix every one by hand. Insert a row in the middle of `D2:D25` and the `SUM` *does* auto-expand in Excel (ranges typed directly into functions do adjust for row insertion within their span) — but only because you got lucky with where you inserted; insert at the very top or bottom edge and it won't. Structured references remove the luck entirely: they're anchored to the Table's logical structure, not to a snapshot of cell addresses taken the day you wrote the formula.

```mermaid
flowchart TD
  A["Insert a column or row"] --> B{"Formula style"}
  B -->|"A1 reference: D2*E2"| C["Points at wrong cells now"]
  B -->|"Structured reference: [@Qty]*[@UnitPrice]"| D["Still correct — names didn't move"]
```

*Why a structural edit breaks A1-style formulas but leaves structured references untouched.*

## 8. Autocomplete makes this fast, not slow

Structured-reference syntax looks more verbose than `D2:D25` at first glance, but you almost never type it by hand. Start a formula with `=SUM(` and click a cell inside the `Orders` Table's `Total` column — Excel and Sheets both insert the correct `Orders[Total]` (or `[@Total]`, if you clicked while inside the Table) automatically, exactly the way clicking a cell on another sheet auto-inserts `Sheet!A1` syntax (Week 2). Typing formulas by pointing and clicking, not by memorizing bracket syntax, is the actual day-to-day workflow — the syntax matters for *reading* formulas correctly, not for typing them from scratch every time.

## 9. Check yourself

- What's the difference between `Orders[Total]` and `[@Total]`, and where would you use each?
- Write a formula, anywhere outside the Table, that averages the `UnitPrice` column.
- What does `Orders[[#Totals],[Qty]]` refer to, in plain English?
- You insert a new column between `Region` and `Product`. What happens to a `[@Qty]*[@UnitPrice]` formula in the `Total` column, and why?
- Why doesn't a structured reference need a sheet-name prefix like `Data!` the way a normal cross-sheet cell reference does?
- Contrast what happens to `=D2*E2` vs. `=[@Qty]*[@UnitPrice]` when a column is inserted to their left.

If those came quickly, Lecture 3 puts structured references to work — filtering and aggregating a Table by multiple criteria at once with `SUMIFS`, `COUNTIFS`, and `AVERAGEIFS`.

## Further reading

- **Microsoft — Using structured references with Excel tables:** <https://support.microsoft.com/en-us/office/using-structured-references-with-excel-tables-f5ed2452-2337-4f71-bed3-c8ae6d2b276e>
- **Microsoft — Table (structured) references overview:** <https://learn.microsoft.com/en-us/office/troubleshoot/excel/table-name-structured-reference>
- **Google — Use and format tables in Google Sheets:** <https://support.google.com/docs/answer/14471021>
