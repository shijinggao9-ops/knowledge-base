# Week 8 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on dashboard-building, a diagnostic exercise, and a written explanation. Keep each in its own tab within a `crunch-week8-homework` workbook, separate from your main mini-project dashboard.

---

## Problem 1 — Sketch three dashboards, build none (45 min)

Without opening a spreadsheet, sketch (on paper or in a text file) wireframes for three *different* dashboards, each for a different governing question, using the same Crunch Retail `Orders` dataset:

1. A dashboard for a **regional sales manager** — governing question: *"Is my region hitting target this quarter?"*
2. A dashboard for a **product/category buyer** — governing question: *"Which category should I stock more of next quarter?"*
3. A dashboard for a **finance/ops lead** — governing question: *"Are we trending toward a strong or weak year overall?"*

For each, write down: the one headline KPI, the three-to-four supporting KPIs, and which chart(s) get the largest chart-zone space. Notice how the same underlying data produces three genuinely different layouts once you take the audience and governing question seriously (Lecture 1, Sections 2-5) — that's the actual point of this problem.

---

## Problem 2 — KPI formula drills (60 min)

In a `KPIDrills` tab, using your four pivots, write and verify each formula. Predict the result before checking, per this course's usual discipline:

1. `GETPIVOTDATA` for the FY2026 grand total sales.
2. `GETPIVOTDATA` for `Count of OrderID` filtered specifically to the `Software` category (temporarily filter the pivot to check, then clear it).
3. A `SUMIFS` formula reading the `Orders` Table directly, filtered to `Region = "West"` and `Category = "Furniture"` simultaneously — confirm it matches what the connected pivots show under the same two-filter combination.
4. An `INDEX`/`MATCH` formula that returns the **lowest**-performing region by total sales (adapt this week's Top Region formula from `MAX` to `MIN`).
5. A month-over-month change formula: `(This month's total - last month's total) / last month's total`, computed for any two adjacent months in `PivotByMonth`, formatted as a percentage.
6. Wrap #5 in `IFERROR` to guard against a zero-value previous month, and explain in a comment cell what specific situation would actually trigger that guard.

---

## Problem 3 — Diagnose five broken dashboards (60 min)

In a `Diagnose` tab, for each broken symptom below, write **one sentence** naming the most likely cause and **one sentence** naming the fix — draw on Lecture 2's connection mechanics and Lecture 3's polish concepts:

1. A slicer's buttons visibly highlight when clicked, but none of the four pivot tables change.
2. A KPI tile shows `#DIV/0!` only when a specific two-slicer combination is selected, but works fine otherwise.
3. Two charts on the same dashboard use completely different, uncoordinated color schemes for what should be the same category (e.g., "Software" is blue in one chart and orange in the other).
4. A dashboard that looked complete on a designer's ultrawide monitor requires horizontal scrolling when a manager opens it on a standard laptop.
5. A dynamic title correctly changes when a slicer is clicked, but shows the raw text `(All)` instead of a friendly phrase when no filter is active.

---

## Problem 4 — Build a second, smaller dashboard (90 min)

In a `RepDashboard` tab, build a **compact, single-purpose** dashboard answering just one question: *"How is each sales rep performing this year?"* Required elements:

1. A Rep slicer, connected to a `PivotByRep`-based pivot chart (bar chart, one bar per rep, sales totals).
2. One KPI tile: **Top Rep by Sales**, using `INDEX`/`MATCH` against the filtered pivot.
3. A sparkline or data-bar treatment showing each rep's month-by-month trend or relative ranking (Lecture 3).
4. The whole thing fits in roughly a **quarter** of a normal screen — this is intentionally a much smaller, single-question dashboard than the full mini-project, to practice scaling the same techniques down.

**Deliver** the working `RepDashboard` tab plus one sentence on what you deliberately left out of this smaller dashboard that the full mini-project dashboard includes, and why it wasn't needed here.

---

## Problem 5 — Written: dashboard vs. report (45 min)

In `dashboard-vs-report.md`, answer in prose (no more than 400 words total):

1. In your own words, what's the functional difference between a "report" and a "dashboard," beyond just "a dashboard has more charts"?
2. Describe a real (or realistic, invented) situation where building a full interactive dashboard would actually be the *wrong* choice, and a simpler report or a single pivot table would serve better. What made you decide that?
3. Of the two apps this week (Excel and Google Sheets), which one's dashboard tooling did you find more capable for building the *interactive* pieces specifically (slicers/timeline/KPI formulas) — and name the one specific feature gap that drove your answer.
4. Why does a dashboard's *unfiltered, default* state need to be just as polished as any filtered view, given that filters are the whole point of building it interactively?

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 45 min |
| 2 | 60 min |
| 3 | 60 min |
| 4 | 90 min |
| 5 | 45 min |
| **Total** | **~5 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/mini-project/README.md).
