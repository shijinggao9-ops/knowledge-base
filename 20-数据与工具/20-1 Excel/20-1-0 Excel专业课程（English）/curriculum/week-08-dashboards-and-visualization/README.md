# Week 8 — Dashboards & Visualization

> **Goal:** by Sunday you can design, build, and polish a single-screen interactive sales dashboard — slicers and a timeline that filter several pivot tables at once, KPI tiles and a title that react live to whatever the viewer selects, and in-cell sparklines and conditional-format visuals that make trends readable without a single extra chart. No scrolling, no explaining, no clutter — a dashboard someone can read correctly in five seconds.

Welcome back to **C41 · Crunch Excel**. Weeks 6 and 7 built the machinery: a real Table, `SUMIFS`-driven summaries, then pivot tables and pivot charts that answer questions on demand. Every one of those things is *correct*. None of them, on their own, is a **dashboard**. A pivot table answers one question at a time and asks you to already know which question to ask. A dashboard is built for someone who doesn't know the question yet — a manager, a client, your future self at 8 a.m. — and it has to hand them the answer to "how's the business doing" in the time it takes to glance at a phone screen. That's a completely different design problem from anything you've built so far, and it has its own rules: what goes at the top, what gets cut, how big a number should be, and how one click on a filter should ripple through every chart on the page at once.

This week you take the pivot tables and charts you already know how to build and wire them together into one screen: slicers and a timeline that filter every pivot simultaneously, KPI tiles that recompute and a title that rewrites itself the instant a filter changes, and sparklines and data bars that show a trend inside a single cell instead of burning a whole chart on it. By Saturday you'll have shipped a dashboard you could genuinely open in a meeting.

You work against **one seed dataset** all week — a full fiscal year of Crunch Retail sales orders, the same schema you built in Week 6 and pivoted in Week 7, extended to 48 orders across all twelve months of 2026. Paste it in once (below), then every lecture, exercise, challenge, and the mini-project builds on it.

## Learning objectives

By the end of this week, you will be able to:

- **Design a single-screen dashboard layout** with a clear visual hierarchy — title, KPI row, chart zone — sized and positioned so the most important number is also the most visually dominant one.
- **Wire slicers and a timeline** to filter multiple pivot tables at once, using **Report Connections** (Excel) / **Filter multiple ranges** (Sheets slicers) so one click updates everything on the page simultaneously.
- **Build KPI tiles** — large, formatted, formula-driven numbers (`GETPIVOTDATA`, `SUMIFS`) — and a **dynamic title** that rewrites itself in text (`="Sales — "&B1&" — "&TEXT(TODAY(),"mmm yyyy")`) to reflect whatever the current slicer selection is.
- **Add sparklines and in-cell visuals** — Excel's `Insert → Sparklines` (Line/Column/Win-Loss) and Google Sheets' `=SPARKLINE()` function, plus data bars, color scales, and icon sets — for compact trend context that doesn't need a full chart's worth of space.
- **Apply consistent color, spacing, and formatting** — a locked palette, aligned gridlines, gridlines-off canvas, uniform number formats — so the finished sheet reads as one designed object instead of a pile of separately-formatted parts.
- **Recreate an interactive dashboard in Google Sheets**, using its own slicer tool and `SPARKLINE()` function, and explain precisely where Sheets' dashboard tooling diverges from Excel's (no native `GETPIVOTDATA`, per-range slicer scoping, no pivot-connected sparklines).

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `BUS 4750` — Present an analysis as a single-screen interactive report: a clear visual hierarchy, headline figures, and controls that filter every view on the page at once. |
| Industry | Build the dashboard a manager opens each morning and acts on without first asking who refreshed it and when. |
| Beyond the bar | A measured constraint rather than a stylistic one — the entire dashboard visible with zero scrolling in either direction at named screen sizes — `challenges/challenge-01-single-screen-rule.md` |


## Prerequisites

- Weeks 1–7 complete. This week assumes fluency with Table structured references (Week 6) and, critically, **pivot tables, pivot fields, grouping, and pivot charts from Week 7** — you're not learning to build a pivot table this week, you're learning to make several of them work together on one screen.
- Comfort with `SUMIFS`/`COUNTIFS` (Week 6, Lecture 3) — KPI tiles fall back to these whenever `GETPIVOTDATA` is unavailable or awkward (notably in Google Sheets).
- Excel (365, 2021, or Excel for the web — Slicers require a Table or pivot source and have shipped since Excel 2010 for pivots, Excel 2013 for plain Tables) **and/or** Google Sheets (its native Slicer tool and `SPARKLINE()` function are both available on any free account).
- No prior "dashboard," BI-tool, or data-visualization design background assumed. If the closest thing you've built to a dashboard is a pivot table with a chart next to it, that is exactly where this week expects you to start.

## Set up your workspace (do this first)

Open a fresh workbook (Excel: `crunch-week8.xlsx`; Sheets: blank at <https://sheets.google.com>, renamed `crunch-week8`). Rename the first sheet tab **`Orders`**.

Starting at `A1`, type the header row exactly as shown, then paste (or type) the 48 rows of data beneath it. This is the same **Crunch Retail** schema from Week 6, extended to a full fiscal year so a monthly timeline and region/category slicers actually have something interesting to filter.

```
OrderID  OrderDate   Rep         Region  Product               Category         Qty  UnitPrice  Total
2001     2026-01-05  T. Osei     South   Standing Desk         Furniture        1    349.00     349.00
2002     2026-01-06  M. Chen     East    Antivirus License     Software         1    39.99      39.99
2003     2026-01-08  S. Kim      North   Webcam 1080p          Electronics      5    45.00      225.00
2004     2026-01-09  R. Diaz     South   Project Mgmt License  Software         3    59.00      177.00
2005     2026-02-10  R. Diaz     West    Bookshelf             Furniture        5    129.00     645.00
2006     2026-02-12  S. Kim      East    27in Monitor          Electronics      4    229.00     916.00
2007     2026-02-19  M. Chen     North   Notebook Pack         Office Supplies  5    12.50      62.50
2008     2026-02-21  J. Alvarez  West    Printer Paper         Office Supplies  2    34.75      69.50
2009     2026-03-05  J. Alvarez  South   Notebook Pack         Office Supplies  1    12.50      12.50
2010     2026-03-11  M. Chen     North   Wireless Mouse        Electronics      2    24.99      49.98
2011     2026-03-19  R. Diaz     West    Webcam 1080p          Electronics      3    45.00      135.00
2012     2026-03-22  T. Osei     West    Stapler               Office Supplies  3    6.99       20.97
2013     2026-04-01  M. Chen     East    Cloud Storage Plan    Software         1    19.99      19.99
2014     2026-04-02  S. Kim      East    Bookshelf             Furniture        5    129.00     645.00
2015     2026-04-04  T. Osei     West    Cloud Storage Plan    Software         1    19.99      19.99
2016     2026-04-22  J. Alvarez  South   Bookshelf             Furniture        1    129.00     129.00
2017     2026-05-05  J. Alvarez  West    Antivirus License     Software         1    39.99      39.99
2018     2026-05-15  R. Diaz     West    Stapler               Office Supplies  1    6.99       6.99
2019     2026-05-21  T. Osei     West    Webcam 1080p          Electronics      1    45.00      45.00
2020     2026-05-24  S. Kim      North   Bookshelf             Furniture        3    129.00      387.00
2021     2026-06-14  T. Osei     South   Whiteboard            Office Supplies  1    42.00      42.00
2022     2026-06-20  S. Kim      East    Office Chair          Furniture        2    189.50     379.00
2023     2026-06-21  R. Diaz     West    Stapler               Office Supplies  2    6.99       13.98
2024     2026-06-22  M. Chen     North   Wireless Mouse        Electronics      4    24.99      99.96
2025     2026-07-08  R. Diaz     South   Sticky Notes          Office Supplies  4    8.25       33.00
2026     2026-07-11  S. Kim      North   Cloud Storage Plan    Software         4    19.99      79.96
2027     2026-07-22  M. Chen     East    Standing Desk         Furniture        1    349.00     349.00
2028     2026-07-24  J. Alvarez  West    Standing Desk         Furniture        4    349.00     1396.00
2029     2026-08-06  J. Alvarez  South   Sticky Notes          Office Supplies  3    8.25       24.75
2030     2026-08-06  M. Chen     North   Webcam 1080p          Electronics      1    45.00      45.00
2031     2026-08-08  R. Diaz     South   Whiteboard            Office Supplies  1    42.00      42.00
2032     2026-08-15  T. Osei     West    Project Mgmt License  Software         5    59.00      295.00
2033     2026-09-04  S. Kim      East    Filing Cabinet        Furniture        2    159.00     318.00
2034     2026-09-12  M. Chen     North   Filing Cabinet        Furniture        2    159.00     318.00
2035     2026-09-24  T. Osei     South   Cloud Storage Plan    Software         4    19.99      79.96
2036     2026-09-24  J. Alvarez  South   Standing Desk         Furniture        3    349.00     1047.00
2037     2026-10-06  R. Diaz     South   Backup Software       Software         1    29.99      29.99
2038     2026-10-17  S. Kim      East    Stapler               Office Supplies  3    6.99       20.97
2039     2026-10-22  J. Alvarez  South   Wireless Mouse        Electronics      3    24.99      74.97
2040     2026-10-26  T. Osei     South   Bookshelf             Furniture        4    129.00     516.00
2041     2026-11-04  S. Kim      North   Whiteboard            Office Supplies  5    42.00      210.00
2042     2026-11-09  R. Diaz     South   Project Mgmt License  Software         1    59.00      59.00
2043     2026-11-13  M. Chen     East    Sticky Notes          Office Supplies  4    8.25       33.00
2044     2026-11-13  T. Osei     West    Bookshelf             Furniture        2    129.00     258.00
2045     2026-12-03  R. Diaz     West    Filing Cabinet        Furniture        2    159.00     318.00
2046     2026-12-16  M. Chen     East    Standing Desk         Furniture        1    349.00     349.00
2047     2026-12-17  J. Alvarez  West    Whiteboard            Office Supplies  1    42.00      42.00
2048     2026-12-19  S. Kim      East    Filing Cabinet        Furniture        2    159.00      318.00
```

Notes on entering it:

- **Already have last week's workbook?** If your Week 7 `crunch-week7.xlsx` already has an `Orders` Table and pivots built against a shorter version of this dataset, the cleanest path is to **replace the Orders Table's data** with the 48 rows above (select the old body rows, delete, paste these in — the Table auto-expands) rather than starting a new file. Every pivot connected to that Table will pick up the new rows the next time you refresh (`Alt+F5` / right-click → Refresh).
- **Starting fresh this week?** Paste the data as a plain range first, then convert it to a Table (`Ctrl+T`, "My table has headers" checked) exactly as you did in Week 6 — name it `Orders` (Table Design → Table Name).
- **`OrderDate`** — type as `2026-01-05` etc.; both apps recognize `YYYY-MM-DD` as a real date. Right-aligned after entry means it landed as a real date; left-aligned means it landed as text — fix before continuing.
- **`UnitPrice`** and **`Total`** — format as **Currency**.
- Sanity check — the range is `A1:I49` (header + 48 rows). `=SUM(I2:I49)` must show **10786.94**. If it doesn't, recheck your entries against the table above — the entire week's pivots, slicers, and KPI tiles are built to match this exact number.

Once the Table is confirmed correct, build (or confirm you already have) these **four pivot tables**, each on its own new sheet tab, all sourced from the `Orders` Table — this is Week 7 territory, so treat it as a quick rebuild, not new material:

| Pivot sheet tab | Rows | Values |
|---|---|---|
| `PivotByRegion` | `Region` | Sum of `Total` |
| `PivotByCategory` | `Category` | Sum of `Total` |
| `PivotByRep` | `Rep` | Sum of `Total`, Count of `OrderID` |
| `PivotByMonth` | `OrderDate` grouped by **Month** | Sum of `Total` |

These four pivots are the raw material Lecture 2 wires slicers into and Lecture 3 polishes. Build all four before starting Lecture 1's design work.

## Weekly schedule

The schedule below adds up to approximately **27 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Dashboard design principles; sketching zones | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Slicers, timelines, report connections | 2.5h | 1.5h | 0h | 0.5h | 1h | 0h | 5.5h |
| Wednesday | KPI tiles, dynamic titles, `GETPIVOTDATA` | 0h | 1.5h | 0h | 0.5h | 1h | 0h | 3h |
| Thursday | In-cell visuals, sparklines, theming, polish | 2h | 0h | 1h | 0.5h | 1h | 1h | 5.5h |
| Friday | Single-screen constraint; Google Sheets rebuild | 0h | 0h | 2h | 0.5h | 1h | 1.5h | 5h |
| Saturday | Mini-project (full interactive dashboard) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6.5h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **27h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it, and everything assumes the four pivots from the setup step above already exist.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-dashboard-design.md](01-dashboard-design.md) | Audience-first layout, visual hierarchy, the single-screen rule, choosing the numbers that matter | 2h |
| 2 | [lecture-notes/02-interactivity-with-slicers.md](02-interactivity-with-slicers.md) | Slicers, timelines, connecting one control to many pivots, dynamic titles, KPI tiles | 2.5h |
| 3 | [lecture-notes/03-in-cell-and-polish.md](03-in-cell-and-polish.md) | Sparklines, data bars, icon sets, consistent theming, the finishing 10% | 2h |
| 4 | [exercises/exercise-01-layout-a-dashboard.md](exercise-01-layout-a-dashboard.md) | Sketch a dashboard wireframe, then build the empty zoned skeleton | 1h |
| 5 | [exercises/exercise-02-wire-up-slicers.md](exercise-02-wire-up-slicers.md) | Insert and connect slicers + a timeline to all four pivots at once | 1.5h |
| 6 | [exercises/exercise-03-kpi-tiles.md](exercise-03-kpi-tiles.md) | Build four formula-driven KPI tiles and a dynamic title | 1.5h |
| 7 | [challenges/challenge-01-single-screen-rule.md](challenge-01-single-screen-rule.md) | Fit the entire dashboard on one screen, no scrolling, at a real laptop resolution | 1h |
| 8 | [challenges/challenge-02-dashboard-in-sheets.md](challenge-02-dashboard-in-sheets.md) | Rebuild the dashboard in Google Sheets and document every divergence | 2h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/mini-project/README.md) | Ship the full one-screen interactive sales dashboard | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Look at a blank sheet and sketch a dashboard's zones — title, KPI row, chart area — before touching a single formula.
- Insert a slicer, connect it to four pivot tables at once via Report Connections, and watch every chart on the page update from one click.
- Build a KPI tile that shows the right number for whatever the current slicer selection is, with a title that rewrites its own text to match.
- Add a sparkline inside a single cell that shows twelve months of trend without a chart's worth of space.
- Explain exactly what Google Sheets' slicer and `SPARKLINE()` tools share with Excel's equivalents, and what a dashboard loses (or must rebuild differently) crossing from one to the other.
- Ship a dashboard that fits on one screen, uses one consistent color language, and answers "how's the business doing" in five seconds.

## Up next

Week 9 — Financial & what-if modeling (`NPV`/`IRR`, `PMT`, Goal Seek, scenarios) — once you can show *what happened*, the course turns to *what should happen next*: loan models, investment projections, and asking the spreadsheet "what if" instead of just "what was."

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
