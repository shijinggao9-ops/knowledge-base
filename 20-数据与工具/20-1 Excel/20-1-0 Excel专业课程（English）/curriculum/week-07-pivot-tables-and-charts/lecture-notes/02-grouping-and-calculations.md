# Lecture 2 — Grouping & Calculated Fields

> **Duration:** ~2 hours. **Outcome:** You can group a date field into months/quarters and a numeric field into custom bins, add a calculated field that derives a new metric inside the pivot, and use "Show Values As" to turn raw sums into % of total, running totals, and rank — in both Excel and Google Sheets.

Lecture 1 got you a pivot that answers "by region, what is total revenue?" That's already useful, but real questions are rarely that clean. "By **month**, what's the trend?" needs grouping — your source has an exact date in every row, not a month. "What's each category's **share** of total revenue?" needs a percentage the raw Sum doesn't give you. This lecture covers both.

## 1. Grouping dates

`OrderDate` in `Transactions` holds 86 distinct exact dates. Put it straight into Rows and you get 86 one-row groups — useless. You want the pivot to **group** those dates into a coarser bucket: month, quarter, or year.

**Excel:**

1. Drag `OrderDate` into Rows. It'll show every distinct date.
2. Right-click any date value in the pivot → **Group…**
3. In the Grouping dialog, select **Months** (and optionally **Quarters** or **Years** at the same time — Excel lets you multi-select, which nests Year above Month automatically). Click OK.
4. The pivot now shows one row per month: `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`.

**Google Sheets:**

1. Drag `OrderDate` into Rows.
2. Click the field in the Rows section of the pivot editor → next to it you'll see a small dropdown appear on the pivot grid itself once you click a date cell, or open the field's settings — Sheets offers a built-in **date grouping** option directly in the Rows field (click the field, choose "Group by" → Month / Quarter / Year / Month-Year / Day of Week, etc.).
3. Choose **Month** for a monthly trend, or **Quarter** to collapse further.

Build the monthly revenue trend now — `OrderDate` grouped by Month in Rows, `TotalRevenue` (Sum) in Values:

| Month | Sum of TotalRevenue |
|-------|---------------------:|
| Jan | 2,959.38 |
| Feb | 1,896.26 |
| Mar | 6,252.45 |
| Apr | 4,356.33 |
| May | 6,666.61 |
| Jun | 5,363.96 |
| **Grand Total** | **27,494.99** |

February was the slowest month; May was the strongest — a fact that was completely invisible in the 86-row flat table and took two drags plus one grouping click to surface.

**A grouping gotcha:** grouping by month collapses *all years* with that month together — January 2024 and January 2025 would land in the same "Jan" bucket unless you also group by Year (or group by "Month-Year" as one combined level, which Sheets offers directly and Excel achieves by selecting both Months and Years in the Group dialog). Since `Transactions` only covers 2025, this doesn't bite you this week — but it's the first thing to check when a real multi-year dataset's monthly trend looks wrong.

## 2. Grouping numbers into bins

The same Group feature works on numeric fields, bucketing continuous numbers into fixed-size ranges instead of one row per exact value.

**Excel:** drag `Units` into Rows → right-click any value → **Group…** → set **Starting at** `1`, **Ending at** `6`, **By** `2`. That produces bins `1-2`, `3-4`, `5-6`.

**Google Sheets:** click the `Units` field in Rows → "Group by" → choose a bucket size (Sheets prompts for a bin size directly, e.g., `2`, and generates the same style of ranges).

Pair that with Count of `OrderID` in Values to see order-size distribution:

| Units (binned) | Count of OrderID |
|-----------------|------------------:|
| 1–2 | 27 |
| 3–4 | 33 |
| 5–6 | 26 |

*(Exact counts depend on your bin boundaries — the point is the shape: most orders cluster in the middle, not at the extremes, which is a genuinely useful thing to know if you're planning bulk-shipping discounts.)*

Numeric binning turns "every individual order size" (useless, too granular) into "small / medium / large orders" (a distribution a human can reason about) — the exact same collapsing principle as date grouping, just on a different data type.

## 3. Calculated fields

Sometimes the metric you want isn't a raw column at all — it's a **formula involving other columns**. `Transactions` doesn't have a "revenue per unit" column, but you can compute it inside the pivot instead of adding a helper column to the source.

**Excel — PivotTable Analyze → Fields, Items & Sets → Calculated Field:**

1. Click inside the pivot.
2. **PivotTable Analyze → Fields, Items & Sets → Calculated Field…**
3. Name it `RevenuePerUnit`, formula: `=TotalRevenue/Units`.
4. Click **Add**, then **OK**. A new field, `RevenuePerUnit`, appears in the field list and can be dropped into Values like any other field.

A critical nuance: a calculated field computes on the **totals**, not row-by-row-then-averaged. `RevenuePerUnit` for a group equals `SUM(TotalRevenue) / SUM(Units)` for that group — the aggregate of the aggregates — not the average of each row's individual per-unit price. For this dataset the two happen to be close, but they are not guaranteed to match, and conflating them is a classic pivot table mistake. When it matters, verify by spot-checking one group by hand.

**Google Sheets — calculated field via the Values section:**

1. In the pivot editor, under **Values**, click **Add**.
2. Scroll to the bottom of the field list → **Calculated field**.
3. Give it a name and a formula referencing the source columns exactly as they're named, e.g. `=TotalRevenue/Units`.
4. It appears as a new value field, same aggregation caveat as Excel — it aggregates the underlying columns first, then divides.

## 4. "Show Values As" — reframing a sum without a new formula

Every value field has a second, independent setting beyond its aggregation: **how to display it relative to the rest of the pivot.** This is where raw sums turn into the numbers stakeholders actually want: percentages, running totals, and ranks — with zero formulas.

```mermaid
flowchart LR
  A["Sum of TotalRevenue"] --> B["No Calculation: raw sum"]
  A --> C["% of Grand Total"]
  A --> D["% of Row/Column Total"]
  A --> E["Running Total In"]
  A --> F["Rank Largest to Smallest"]
```
*The same underlying Sum, reframed five different ways via "Show Values As" — no new formula needed.*

**Where it lives:** Excel — right-click the value field in the pivot → **Show Values As**. Google Sheets — click the value field in the editor's Values section → **"Show as"** dropdown.

| Show Values As option | What it computes | Example question it answers |
|---|---|---|
| **No Calculation** | The raw aggregation (default) | "What's total revenue by category?" |
| **% of Grand Total** | Each cell ÷ the overall total | "What share of all revenue does each category represent?" |
| **% of Column Total** | Each cell ÷ its column's total | "Within Online sales specifically, what's each category's share?" |
| **% of Row Total** | Each cell ÷ its row's total | "For this region, what % of its revenue came from each channel?" |
| **Running Total In** | Cumulative sum as you move through the field's order | "What's our cumulative revenue through each month?" |
| **Rank Largest to Smallest** | The group's rank, 1 = biggest | "Which rep is #1 by revenue?" |
| **Difference From** / **% Difference From** | Delta vs. a chosen baseline item | "How does March compare to January?" |

Build the category % of grand total. Category in Rows, `TotalRevenue` (Sum) in Values, then Show Values As → % of Grand Total:

| Category | % of Grand Total |
|----------|-------------------:|
| Camping | 31.0% |
| Electronics | 24.7% |
| Footwear | 21.0% |
| Apparel | 16.7% |
| Accessories | 6.6% |

Now build a **running total** — Month in Rows, `TotalRevenue` (Sum) in Values, Show Values As → Running Total In (Month):

| Month | Sum | Running Total |
|-------|----:|---------------:|
| Jan | 2,959.38 | 2,959.38 |
| Feb | 1,896.26 | 4,855.64 |
| Mar | 6,252.45 | 11,108.09 |
| Apr | 4,356.33 | 15,464.42 |
| May | 6,666.61 | 22,131.03 |
| Jun | 5,363.96 | 27,494.99 |

The last running-total value always equals the grand total — a built-in sanity check worth remembering: if your running total's final row doesn't match the pivot's grand total, something about the sort order or grouping is off.

Finally, rank the sales reps — `SalesRep` in Rows, `TotalRevenue` (Sum) in Values twice (once No Calculation, once Rank Largest to Smallest), sorted descending:

| SalesRep | Sum of TotalRevenue | Rank |
|---|---:|:-:|
| Jack Rivera | 6,353.65 | 1 |
| Priya Shah | 5,209.48 | 2 |
| Tom Baker | 3,515.18 | 3 |
| Marcus Lee | 3,457.45 | 4 |
| Sam Chen | 3,435.18 | 5 |
| Elena Ruiz | 2,156.28 | 6 |
| Wendy Kim | 1,866.37 | 7 |
| Nadia Osei | 1,501.40 | 8 |

No `RANK()` formula, no helper column — the pivot computed it directly from the same Sum field, displayed a second way.

## 5. Combining grouping + calculation + Show Values As

These three tools compose. A genuinely useful pivot might have: `OrderDate` grouped by Month in Rows, `Category` in Columns, a calculated `RevenuePerUnit` field in Values set to Show Values As "% of Row Total" — answering "within each month, which category commanded the highest average price relative to the others that month?" in one pivot, built entirely by dragging and clicking, no formula bar involved.

## 6. Check yourself

- Why does grouping `OrderDate` by Month alone (without also grouping by Year) become dangerous on a multi-year dataset?
- What's the bin size you'd set to group `Units` into buckets of 1–2, 3–4, 5–6?
- A calculated field `RevenuePerUnit = TotalRevenue/Units` for a group — does it compute the average of each row's per-unit price, or the group's total revenue divided by the group's total units? Why does the distinction matter?
- Which "Show Values As" option would you use to answer "what % of March's channel mix was Wholesale"?
- Why does the last value in a "Running Total In" column always equal the grand total — and what does it mean if it doesn't?

Lecture 3 takes everything you can now compute and turns it into a chart someone can actually read.

## Further reading

- **Microsoft — Group or ungroup data in a PivotTable:** <https://support.microsoft.com/en-us/office/group-or-ungroup-data-in-a-pivottable-74506f17-16d3-4551-a15d-c9752cbcbb64>
- **Microsoft — Calculate values in a PivotTable:** <https://support.microsoft.com/en-us/office/calculate-values-in-a-pivottable-350b0961-2a26-4c99-bfa3-1f96e3a3f5a9>
- **Microsoft — Show values as a percentage of grand total (Show Values As):** <https://support.microsoft.com/en-us/office/show-values-in-a-pivottable-90b56b4d-7dea-42e0-8871-cfa42bf1531b>
- **Google — Group dates, times, or numbers in a pivot table:** <https://support.google.com/docs/answer/9309261>
