# Lecture 1 — Power Query: Repeatable ETL

> **Duration:** ~2 hours. **Outcome:** You can open Power Query against a real file, understand what the editor's four regions are for, build and read a short sequence of Applied Steps, and explain — concretely, with this week's data — why that sequence beats doing the same cleanup by hand every time a new export arrives.

## 1. The problem this week solves

Every earlier week in this course started the same way: a "Set up your workspace" section told you to type or paste a dataset into a sheet, by hand, once. That was a deliberate simplification — it let each week focus on the technique being taught (formulas, lookups, cleaning, Tables, pivots) without also fighting the mechanics of getting data *in*. But it hid a real cost. Look back at Week 5's mini-project: you spent nearly an hour auditing and cleaning one 32-row CSV dump by hand — trimming whitespace, standardizing categories, deduping, fixing dates. That work was correct and necessary. It was also **completely wasted the moment a second, equally messy export arrives next week**, because nothing you did was saved as a repeatable procedure — you have to notice the same problems and fix them the same way, again, from scratch, forever.

This week's seed files make the pattern concrete. `North_Week1.csv` isn't clean — Exercise 1 uses a messier version of it with header junk, a blank row, and a `Qty` value stored as `"8 units"` instead of a number. A real distributor doesn't get one such file; it gets one **every week**, forever, from a system nobody at Crunch Wholesale controls. The question this lecture answers is: how do you clean *that* file once, and have the cleanup apply itself automatically to next week's file too?

## 2. What Power Query actually is

Power Query is a data-transformation engine built into Excel, exposed through the **Data** tab's "Get & Transform Data" group (in Excel 2010–2013 it's a separate free add-in with the same engine and a nearly identical interface). Its job, in the classic ETL vocabulary:

- **Extract** — pull raw data from a source: a file (CSV, Excel workbook, text, JSON, XML), a folder of files, a web page, a database (SQL Server, Access, and dozens more via connectors), or another query already inside the same workbook.
- **Transform** — reshape it: rename and reorder columns, change data types, split or merge columns, filter rows, remove duplicates and errors, unpivot, group and aggregate, merge in a second source, append more rows.
- **Load** — decide where the finished result goes: a new worksheet Table, the Excel **Data Model** (for pivot tables spanning multiple sources — Week 7's pivot skill, supercharged), or **Connection Only** (the result stays inside Power Query, available for other queries to build on, but is never itself written to a visible sheet).

Crucially, every transform step you apply is **recorded, named, and kept in order** — not executed once and discarded like a manual Find & Replace. That recorded sequence is a *query*, and a query is a small program, written for you automatically in a language called **M** as you click, that can be re-run from scratch against a *newer* copy of the same-shaped source with one click: **Refresh**.

```mermaid
flowchart LR
  A["Extract raw data"] --> B["Transform: clean, split, merge"]
  B --> C["Load: Table, Data Model, or Connection Only"]
  C --> D["Refresh against newer file"]
  D --> A
```
*The Power Query ETL cycle — each Refresh re-runs Extract through Load against whatever copy of the source file exists right now.*

## 3. Opening the editor against a real file

Open a blank workbook, save it as `crunch-week11.xlsx` inside your `crunch-wholesale` folder (from the README setup), and import `North_Week1.csv`:

**Excel:** **Data** tab → **Get Data** → **From File** → **From Text/CSV** → select `North_Week1.csv`.

A preview dialog appears first, showing the first handful of rows and a **Delimiter** detector (it should already say "Comma"). Two buttons matter here: **Load** (skip the editor, dump the data straight onto a sheet as-is — fine for already-clean data, which is exactly what `North_Week1.csv` is) and **Transform Data** (open the full Power Query Editor before loading anything). Click **Transform Data** — this week is about the editor, not the shortcut.

## 4. The four regions of the Power Query Editor

The editor window that opens has four regions worth knowing by name, because every lecture and exercise this week refers back to them:

1. **The ribbon** (top) — grouped by task: **Home** (the everyday operations: remove rows/columns, split column, group by, merge/append queries, close & load), **Transform** (type conversion, pivot/unpivot, text/number/date transforms applied to existing columns), **Add Column** (build a *new* column from existing ones — a custom formula column, a conditional column, an index column), and **View** (toggle the formula bar, the dependency diagram, and a few display options).
2. **The Queries pane** (left) — every query that exists in this workbook, listed by name. Right now it shows one: `North_Week1`. As this week goes on, this list grows — every imported source and every intermediate transformation becomes its own named entry here.
3. **The data preview** (center) — a live, scrollable sample of what the query currently produces, updating instantly after every step you apply. This is *not* the actual output range on a sheet — it's a preview inside the editor, safe to experiment against.
4. **The Applied Steps pane** (right) — the beating heart of Power Query. Every operation you perform gets added here, top to bottom, as a named, clickable step: `Source`, `Promoted Headers`, `Changed Type`, and so on. Click any step and the preview jumps back in time to show the data exactly as it looked right after that step ran — this is how you debug a broken pipeline, by clicking backward until you find the step that introduced the problem.

## 5. Reading and editing Applied Steps

`North_Week1.csv` is clean, so the editor auto-generated only two steps: `Source` (the raw file connection) and `Changed Type` (Power Query's automatic best-guess type detection — it correctly inferred `Qty` and `UnitCost` as numbers and `OrderDate` as a date, because the file has no junk rows confusing that guess). Click each step in the Applied Steps pane now and watch the preview change — `Source` shows the rawest possible read of the file; `Changed Type` shows the same data with column headers now bold and each column's data-type icon (`ABC` for text, `#` for whole number, a calendar for date) set correctly in the column header.

```mermaid
flowchart LR
  A["Source"] --> B["Promoted Headers"]
  B --> C["Changed Type"]
  Click["Click any step"] -.-> A
  Click -.-> B
  Click -.-> C
```
*Clicking a step in the Applied Steps pane jumps the preview back to exactly that point in the pipeline — how you debug a broken chain.*

Three things you can do to any step, right-clicked from the Applied Steps pane:

- **Rename** — the auto-generated names (`Changed Type`, `Changed Type1` if you convert types twice) get confusing fast in a longer query; renaming to something like `Set Qty and Cost to Number` makes the pipeline self-documenting.
- **Delete** — removes that one step. Note: deleting a step in the *middle* of a chain can break every step after it, if a later step referenced a column name or shape that only existed because of the step you just deleted. Power Query will show a red error banner in the preview when this happens — that's not a crash, it's a pointer at exactly what to fix.
- **Insert Step After** (the small `fx` icon in the formula bar, or right-click → "Insert Step After") — lets you add a new operation in the *middle* of an existing sequence rather than only ever at the end. Use this sparingly at first; it's easy to break a downstream step's assumptions this way, and beginners are safer appending new steps at the end until they're comfortable reading the ripple effects.

## 6. The formula bar and a first taste of `M`

Turn on **View → Formula Bar** if it isn't already visible. Click the `Changed Type` step and look at the formula bar above the preview:

```
= Table.TransformColumnTypes(#"Promoted Headers",{{"OrderID", type text}, {"OrderDate", type date}, {"SKU", type text}, {"ProductName", type text}, {"Qty", Int64.Type}, {"UnitCost", type number}})
```

This is **M**, the functional query language every Power Query step compiles down to. You are not expected to write M by hand this week — every operation you'll do is available through the ribbon and preview interactions — but recognizing its shape matters for two reasons. First, it demystifies what's actually happening: each step is a plain function call, taking the *previous* step's output (`#"Promoted Headers"` here) as its first argument and returning a new table. Second, it's your escape hatch: any time the ribbon can't quite do what you need, you can hand-edit this formula bar directly, and advanced Power Query users do exactly that for the small fraction of transforms that don't have a dedicated button.

## 7. Close & Load — where the result goes

With `North_Week1` looking correct in the preview, go to **Home → Close & Load**. The dropdown arrow next to it (**Close & Load To…**) matters more than the default button — it opens a dialog with three destination choices:

- **Table** — the query's result is written to a new worksheet as a real Excel Table (Week 6), refreshable, auto-typed, ready for formulas.
- **PivotTable Report** — skips the intermediate Table and builds a pivot (Week 7) directly against the query's output.
- **Only Create Connection** — the query is saved and available to other queries (as a merge/append source, for instance) but nothing is written to any sheet. You'll use this constantly starting in Lecture 3, once queries start referencing *other* queries instead of raw files.

Choose **Table**, loaded to the current worksheet. A new Table named `North_Week1` appears, showing all five North rows, correctly typed. Verify: sum the `Qty × UnitCost` for all five rows (add a helper column or a `SUMPRODUCT`) — it must read **1949.00**, matching the README checksum.

## 8. Refresh — the entire point

Right-click anywhere inside the loaded Table (or select it and go to **Table Design → Refresh**, or **Data → Refresh All**) and click **Refresh**. Nothing visibly changes — because the source file hasn't changed. That's expected, and it's the proof this lecture is building toward: **the whole import-and-transform sequence you just watched happen once in the editor just silently re-ran, from `Source` through `Changed Type`, against the current copy of `North_Week1.csv` on disk.** If you edited that CSV file right now — in a text editor, outside of Excel entirely — added a sixth row, saved it, and clicked Refresh again, the new row would appear in your Table with zero additional work. That's the payoff manual copy-paste cleaning can never give you: a pipeline that survives the *next* file, not just this one.

## 9. Check yourself

- Name the four regions of the Power Query Editor and what each one is for.
- What's the difference between clicking **Load** and clicking **Transform Data** in the initial import dialog?
- You click a step three rows up in the Applied Steps pane. What does the data preview show, and why is this useful for debugging?
- What does **Close & Load To… → Only Create Connection** actually do, and why would you ever want a query that never appears on any sheet?
- In your own words: what specifically does clicking **Refresh** cause Power Query to do?

If those came quickly, Lecture 2 puts real transform steps to work — split, unpivot, type conversion, filtering, and grouping — against data messier than `North_Week1.csv`.

## Further reading

- **Microsoft — Power Query overview:** <https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query>
- **Microsoft — Quickstart: Using Power Query in Excel:** <https://support.microsoft.com/en-us/office/quickstart-using-power-query-in-excel-27ff4d76-d19a-4802-a3ea-2eb852be4d5f>
- **Microsoft — Power Query M formula language overview:** <https://learn.microsoft.com/en-us/powerquery-m/power-query-m-language-specification>
