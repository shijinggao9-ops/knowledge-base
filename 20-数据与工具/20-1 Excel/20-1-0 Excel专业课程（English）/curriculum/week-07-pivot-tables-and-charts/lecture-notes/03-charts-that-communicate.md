# Lecture 3 — Charts That Communicate

> **Duration:** ~2 hours. **Outcome:** You can match a chart type to the question being asked, build both a standalone chart and a pivot chart in Excel and Google Sheets, and strip a chart down to the elements that actually help the reader — recognizing and removing common chart-junk.

A pivot table is precise but slow to read — someone has to scan rows and compare numbers. A chart trades a little precision for a lot of speed: the right chart lets someone absorb the finding in three seconds without reading a single digit. That trade only pays off if the chart type actually matches the question. The wrong chart type doesn't just look worse — it can make a true number *look* false, or hide the one comparison the reader needed to see. This lecture is about picking correctly and building cleanly.

## 1. Match the chart type to the question, not the data

Don't ask "what chart works with this data" — almost any chart type technically accepts almost any data. Ask **what question the chart needs to answer**, and let the question dictate the type.

```mermaid
flowchart TD
  Q["What question does the chart need to answer?"] --> Q1["Compare categories right now"]
  Q --> Q2["Track change over time"]
  Q --> Q3["Show part-to-whole breakdown"]
  Q --> Q4["Relationship between two measures"]
  Q1 --> C1["Bar / column chart"]
  Q2 --> C2["Line chart"]
  Q3 --> C3["100% stacked bar/column"]
  Q4 --> C4["Scatter plot"]
```
*Letting the question shape — not the data — decide the chart type.*

| Question shape | Right chart | Why |
|---|---|---|
| "How do these categories compare to each other, right now?" | **Bar / column chart** | Length is the easiest visual quantity for humans to compare accurately, and it works for any number of categories |
| "How did this measure change over time?" | **Line chart** | Position-over-a-continuous-axis is what a viewer's eye tracks as a trend; a line chart makes the direction of change immediate |
| "How does the whole break down into parts, and how did that mix shift?" | **100% stacked bar/column** | Shows both the part-to-whole share *and* lets you compare that share across categories or time — better than a pie for anything with more than ~2 slices being compared side by side |
| "What's the relationship between two numeric measures?" | **Scatter plot** | Only a scatter plot puts two continuous measures on two axes simultaneously so correlation is visible |
| "What does the whole add up to, and how much of the whole is this one slice?" (2–4 slices, single snapshot) | **Pie chart** — used sparingly | Works only when there are few slices and you're not asking anyone to compare it to another pie |
| "What's the distribution of order sizes / values?" | **Histogram** (bar chart of binned data — Lecture 2's Group-by-bins feeds this directly) | Shows shape and spread, not just a single average |

Apply this to `Transactions`: "revenue by category" is a comparison snapshot → **bar chart**. "Revenue trend Jan–Jun" is change over time → **line chart**. "Channel mix within each region" is part-to-whole across several groups → **100% stacked column**, not four separate pie charts.

### The pie chart trap

Pie charts are the most over-used and most misused chart type in business reporting. Human eyes are measurably worse at comparing *angles* and *areas* than at comparing the *length* of bars starting from a common baseline. A pie with 5 categories is borderline readable; `Transactions` has exactly 5 categories, so this is a good week to feel the difference directly — build the Category revenue pivot as both a pie chart and a bar chart and compare how fast you can answer "which is bigger, Footwear or Electronics" in each. The bar chart answer is close to instant; the pie chart answer requires you to consciously compare two wedge angles.

**Rule of thumb:** if you're ever tempted to build a pie chart with more than 4–5 slices, or to compare two pie charts side by side, use a bar chart instead. There's no exception worth memorizing beyond that.

## 2. Building a chart from a pivot table (a "pivot chart")

A **pivot chart** is a chart wired directly to a pivot table's data — when the pivot's fields, filters, or grouping change, the chart updates automatically. This is different from building a normal chart that happens to point at a pivot's output range, which will silently break the moment the pivot's shape changes (rows added, a filter changed, etc.).

**Excel — PivotChart:**

1. Click inside your pivot table.
2. **PivotTable Analyze → PivotChart** (or **Insert → PivotChart** directly, which creates the pivot and chart together in one step).
3. Choose a chart type in the dialog (Clustered Column is the default and correct choice for most category comparisons).
4. The resulting chart has its own mini field buttons overlaid on it (filter/legend/axis buttons) — these let you filter directly from the chart, and the change also filters the underlying pivot table. They're genuinely convenient but easy to leave visible by accident in a shared report; **Chart Design → hide field buttons** before presenting.

**Google Sheets — chart from the pivot editor:**

1. Build your pivot table first.
2. Select the pivot table's output range, or click the pivot and use **Insert → Chart** — Sheets will usually detect the pivot as the source and suggest an appropriate chart type.
3. In the Chart editor's **Setup** tab, confirm the data range is the pivot's output (not the raw `Transactions` range), and pick the chart type.
4. Like Excel, this chart updates automatically when the pivot's underlying configuration changes, because its data range is the pivot's live output.

Build the monthly revenue trend as a pivot chart now (Month grouped in Rows, Sum of `TotalRevenue` in Values, Line chart) and confirm: change the pivot's grouping from Month to Quarter, and watch the chart collapse from 6 points to 2 without you touching the chart at all.

## 3. Design choices that make a chart readable

A chart with correct data and the wrong presentation still fails to communicate. These choices matter more than most people think:

- **Title the finding, not the field.** `"Sum of TotalRevenue by Category"` (auto-generated) tells the reader nothing they couldn't get from the axis labels. `"Camping gear drove 31% of H1 revenue"` tells them the finding immediately — the chart becomes supporting evidence for a sentence, not a puzzle to solve.
- **Start bar/column axes at zero.** Truncating a bar chart's y-axis (starting at, say, 4,000 instead of 0) visually exaggerates small differences into what looks like a dramatic gap. This is the single most common way charts mislead, intentionally or not. Line charts tracking a trend can sometimes justify a non-zero baseline (to show variation in a tight range) — bar/column charts almost never can, because bar length *is* the visual signal, and a truncated baseline breaks the length-to-value mapping the whole chart type depends on.
- **Sort categorical bars by value, not alphabetically**, unless the category has a natural order (like months). A bar chart of regions sorted North/South/East/West alphabetically forces the reader to hunt for the tallest bar; sorted descending, the ranking is obvious at a glance.
- **Prefer direct labels over a legend when there are only a few series.** A legend forces the eye to bounce between the chart and a key; a data label or line-end label placed right next to what it describes removes that round trip entirely. Both Excel and Sheets let you add data labels (Chart Design/Add Chart Element → Data Labels in Excel; the Customize tab's Series section in Sheets).
- **One consistent color per category, everywhere it appears.** If "Camping" is teal in one chart, keep it teal in every chart in the same report. Random re-coloring per chart forces the reader to relearn the legend every time.
- **Avoid dual axes unless there's no alternative.** A chart with two y-axes (e.g., revenue on the left, order count on the right) can visually align two series that have no real relationship, purely because of how the two scales happened to be chosen. If you must use one, label both axes explicitly and say so in the title.
- **Turn off 3D.** 3D bar, column, and pie variants distort length and angle perception for no benefit — the "depth" carries no data. Both tools default to flat 2D charts; resist the temptation to make a 3D chart because it looks fancier. It communicates worse, not better.
- **Remove gridlines and borders you don't need.** A light single set of horizontal gridlines can help the reader read values off a bar chart; a heavy grid, a chart border, and a background fill on top of that adds visual noise with zero informational value. Default chart styles in both Excel and Sheets already lean fairly clean — when in doubt, remove an element and see if the chart got harder to read; if not, leave it removed.

## 4. Worked example — one dataset, three questions, three chart types

Using `Transactions`, build all three of these back to back and notice how differently each one *feels* to read, even though they share a data source:

1. **"Which region sold the most?"** → Region in Rows, Sum of `TotalRevenue` in Values, sorted descending → **column chart**. Answer readable in under 2 seconds: North, then West, then South, then East.
2. **"Is revenue growing month over month?"** → Month (grouped) in Rows, Sum of `TotalRevenue` in Values → **line chart**. The dip in February and the peak in May are both immediately visible as shape, not as numbers you'd have to compare one by one.
3. **"How does each region's channel mix differ?"** → Region in Rows, Channel in Columns, Sum of `TotalRevenue` in Values → **100% stacked column chart**. West's noticeably larger Wholesale slice versus North's much smaller one jumps out as a shape difference — a table of the same numbers requires actually computing each row's percentages by hand to see it.

Same source data, three genuinely different questions, three genuinely different — and each individually correct — chart choices.

## 5. Check yourself

- A stakeholder asks "how did revenue change month by month?" Which chart type, and why is a pie chart wrong for this specific question?
- What's the practical difference between a pivot chart and a normal chart built from a pivot's output range?
- Why is truncating a bar chart's y-axis (not starting at 0) considered misleading, while doing the same on a line chart is sometimes acceptable?
- You have 5 product categories to compare by revenue. Bar chart or pie chart — and at what number of categories would you reconsider?
- Name three specific chart elements this lecture recommends removing by default, and what job (if any) each one does when it's actually needed.

That's the full pivot-and-chart toolkit for this week. The exercises apply it directly to `Transactions`; the challenges and mini-project ask you to choose correctly under less guidance.

## Further reading

- **Microsoft — Create a chart from a PivotTable (PivotChart):** <https://support.microsoft.com/en-us/office/create-a-chart-from-a-pivottable-r-report-7d0e4939-472e-4d3f-8b62-8b676ff30cd7>
- **Microsoft — Chart types in Excel:** <https://support.microsoft.com/en-us/office/available-chart-types-in-office-a6187218-807e-4103-9e0a-27cdb19afb90>
- **Google — Create and edit charts:** <https://support.google.com/docs/answer/63824>
- **Google — Insert a chart from a pivot table:** <https://support.google.com/docs/answer/1272900>
