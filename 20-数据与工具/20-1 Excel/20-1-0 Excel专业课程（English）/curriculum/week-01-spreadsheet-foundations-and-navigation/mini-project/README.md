# Mini-Project — Rebuild a Formatted Monthly Budget From a Blank Sheet

> Build a complete, professionally formatted personal monthly budget from a **blank workbook** — sections, headings, number formats, and frozen headers. **No formulas yet** — that's Week 2. This week is purely about structure and presentation: proving you can turn a blank grid into something a stranger could open and understand in ten seconds.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone. Every real spreadsheet you'll ever build — a budget, a sales tracker, a project plan — starts exactly like this: blank cells, a plan for the layout, and then careful, deliberate formatting before anyone even talks about formulas. Nail the structure now and Week 2 slots formulas straight into a workbook that's already easy to work in.

---

## Deliverable

A new workbook (or a clearly separated set of sheets in your `crunch-week1` workbook — your choice) containing:

1. A `Budget` sheet with the full layout described below, completely formatted.
2. A `Notes` sheet with a short reflection (see the end).
3. Everything entered **by hand, typed values only** — no formulas, no `SUM`, no cross-sheet references this week. You are typing every number, including any subtotal-looking number, as a literal value. (Yes, this means if you change a line item, the subtotal won't auto-update — that's deliberate; Week 2 fixes exactly this problem, and you'll feel *why* it's needed by living without it for one week.)

---

## The brief

You're building next month's personal budget from scratch for someone (real or fictional — your call) who currently tracks money in a paper notebook. They've asked for "something in a spreadsheet that's actually easy to look at." Structure, not math, is what you're delivering this week.

## Required sections (in this order, top to bottom on the `Budget` sheet)

### 1. Title block (rows 1–3)

- A large, bold title in `A1`: `Monthly Budget — [Month] [Year]` (pick a real month/year).
- A subtitle in `A2`, smaller/lighter: the person's name or household label, plus a "Last updated" date in a nearby cell, correctly formatted as a date.
- Leave row 3 blank as visual breathing room before the next section.

### 2. Income section (starting row 4 or 5)

- A section header (`INCOME`) — bold, filled background color, spans the width of your table via Center Across Selection (not merge — Lecture 3, section 2).
- A header row: `Source`, `Amount`.
- At least 3 income line items (e.g., `Salary`, `Freelance`, `Interest`) with realistic dollar amounts, Currency-formatted.
- A **Total Income** row — bold, top border, with a typed (not formula) sum of the line items above it.

### 3. Expenses section (immediately below, with a blank row of separation)

- A section header (`EXPENSES`) in the same style as Income, but a **different fill color** so the eye instantly distinguishes the two sections.
- A header row: `Category`, `Amount`.
- At least **8** expense line items across a realistic mix of categories: e.g., `Rent/Mortgage`, `Groceries`, `Utilities`, `Transportation`, `Insurance`, `Subscriptions`, `Dining Out`, `Savings`. All Currency-formatted.
- A **Total Expenses** row — bold, top border, typed sum.

### 4. Summary section (below Expenses, separated)

- A section header (`SUMMARY`).
- Rows for `Total Income`, `Total Expenses`, and `Net (Income − Expenses)` — the net value typed by hand (you calculated it yourself this week, on paper or in your head — Week 2 automates this).
- Apply conditional formatting to the `Net` cell: green fill if positive, red/pink fill if negative (Lecture 3, section 5) — even though you only have one value, set the rule up correctly so it *would* react if the number changed.

## Required formatting (applies across the whole sheet)

- Header row (column headers, not section headers) is bold with a bottom border, per section.
- All dollar amounts: consistent Currency format, 2 decimals, throughout the entire sheet — no column half-formatted.
- Column widths auto-fit; nothing truncates or shows `#####`.
- Row 1 (or whichever row holds the column headers you want pinned — your call, but state which) is frozen so it's visible as you scroll through a long expense list.
- Section headers (`INCOME`, `EXPENSES`, `SUMMARY`) are visually distinct from line-item rows and from each other (different fill colors, per the Expenses requirement above).
- At least one more conditional formatting rule beyond the Net cell — for example, highlighting any expense line item over a chosen threshold (your call — document the threshold and why you picked it).

## Layout sketch (adapt freely — this is a starting shape, not a rigid template)

```
 1  Monthly Budget — March 2026
 2  Household: The Ramirez Family              Last updated: 2026-03-01
 3
 4  INCOME
 5  Source              Amount
 6  Salary              $4,200.00
 7  Freelance           $650.00
 8  Interest            $12.00
 9  Total Income        $4,862.00
10
11  EXPENSES
12  Category            Amount
13  Rent/Mortgage       $1,500.00
14  Groceries           $480.00
15  Utilities           $210.00
16  Transportation      $180.00
17  Insurance           $220.00
18  Subscriptions        $65.00
19  Dining Out          $260.00
20  Savings             $500.00
21  Total Expenses      $3,415.00
22
23  SUMMARY
24  Total Income         $4,862.00
25  Total Expenses       $3,415.00
26  Net                  $1,447.00
```

---

## Milestones

- **Milestone 1 (30 min):** Title block + Income section, fully entered and formatted.
- **Milestone 2 (45 min):** Expenses section (8+ line items), fully entered and formatted, second fill color chosen.
- **Milestone 3 (30 min):** Summary section + both conditional formatting rules.
- **Milestone 4 (30–45 min):** Full polish pass — freeze panes, column widths, border consistency, a final side-by-side check against the "Required formatting" list above.
- **Milestone 5 (15–30 min):** `Notes` sheet reflection.

---

## Rules

- **No formulas this week.** Every number, including subtotals, is typed literally. (You'll feel the pain of this the moment you change one line item and the total doesn't move — that's intentional; hold onto that feeling for Week 2.)
- **Currency formatting must be consistent** across the entire sheet, not just some rows.
- **Every section must be visually distinguishable** from every other at a glance, without reading a single word.
- **Document your two conditional formatting rules** (the Net cell rule and your chosen threshold rule) in `Notes`.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|---------------------|
| Structure | 30% | All 4 required sections present, in order, clearly separated |
| Formatting consistency | 25% | Currency/number formats uniform; no truncation; auto-fit throughout |
| Visual hierarchy | 20% | Section headers, column headers, and line items are instantly distinguishable |
| Conditional formatting | 15% | Both rules present, correctly configured, and documented |
| Data entry types | 10% | Amounts stored as real numbers (right-aligned, Currency-formatted) — not text |

---

## Reflection (`Notes` sheet, ~200 words)

1. What was the hardest formatting decision — the one where you genuinely weren't sure what "looks right" meant?
2. Where did you almost let a numeric value get typed as text (or catch yourself entering something ambiguous, like a date)?
3. You typed every subtotal by hand this week. Describe, in your own words, exactly what will break the first time someone edits a line item — and why that's the problem Week 2 exists to solve.
4. Which keyboard shortcut from this week did you use the most while building this?

---

## Why this matters

A budget spreadsheet is one of the first "real" spreadsheets almost everyone builds in their life, and it's a perfect microcosm of this whole course: structure first, then formulas, then analysis, then automation. Keep this workbook — you're going to **rebuild this exact budget with live formulas** in Week 2's mini-project, and the contrast (typed totals vs. self-updating totals) is the clearest possible demonstration of why formulas matter.

When done: push/save your work, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/quiz.md) and start [Week 2 — Formulas & cell references](../../week-02-formulas-and-cell-references/).
