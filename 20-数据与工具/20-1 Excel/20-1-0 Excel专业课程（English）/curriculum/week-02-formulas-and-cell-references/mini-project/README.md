# Mini-Project — A Self-Calculating Invoice

> Build a real invoice — line items, quantities, unit prices, a locked tax rate, and a grand total — that recalculates live as you type. Change any quantity, any price, or the tax rate itself, and every downstream number updates instantly, correctly, with zero manual re-entry. This is the week's capstone: every reference concept from all three lectures, combined into one document you could genuinely hand to a client.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

An invoice is the perfect proof of this week's skills because it fails loudly and obviously if you get references wrong — a line total that doesn't update when you change a quantity, a tax that applies the wrong rate to one row, a grand total that's off by a few cents. Get the references right and the sheet becomes something you'd actually trust to send to a real client.

---

## Deliverable

A sheet tab (or standalone workbook) `Invoice` containing a complete, working invoice built to the spec below, plus a short `notes.md` reflection (see the end).

---

## Required structure

Build the invoice in this layout, starting at `A1`. Exact cell addresses aren't graded — the *behavior* is — but keep a clean, readable layout resembling a real invoice.

### Header block

```
Crunch Consulting LLC
Invoice #: 2026-0142
Date: [today's date, typed]
Bill To: [a fictional client name and address, 2-3 lines]
```

### Line items table

A table with these columns, and **at least 6 line items** of your own invention (consulting hours, products, services — your choice, make it realistic):

| Description | Qty | Unit Price | Line Total |
|---|---|---|---|
| *(your item 1)* | *(number)* | *(currency)* | **formula** |
| *(your item 2)* | *(number)* | *(currency)* | **formula** |
| … | … | … | … |

**`Line Total` must be a formula** (`Qty * Unit Price`) using a **relative reference** — filled down the whole column, each row computing independently from its own `Qty` and `Unit Price`.

### Rate block (off to the side, clearly labeled)

```
Tax Rate:          8.25%
Discount Rate:     0%       (0 by default; some invoices will use this — see Stretch)
```

Format these cells as **Percentage**, not raw decimals, so they display correctly (recall Week 1, Lecture 1, section 4 — type `8.25%` directly, or type `0.0825` and apply Percentage format).

### Totals block

Four formulas, each building on the last:

1. **Subtotal** — `SUM` of the entire `Line Total` column.
2. **Tax** — Subtotal multiplied by the Tax Rate, using an **absolute reference** to the tax rate cell so it survives being part of a larger formula and stays correct if you insert more line items above it later.
3. **Grand Total** — Subtotal plus Tax (or equivalently, `Subtotal * (1 + Tax Rate)` — pick one, and be able to justify it).
4. **Amount Due** — same as Grand Total for this project (a placeholder row real invoices use for "amount already paid," subtracted — you don't need a payments column, just the row structure).

## Required behaviors (test these yourself before submitting)

- [ ] **Insert a 7th line item** in the middle of the table (not at the bottom). Every formula — `Line Total` for the new row, and the `Subtotal` at the bottom — must update correctly and automatically include the new row. *(If your `Subtotal` formula was `=SUM(D2:D7)` and you inserted a row inside that range, Excel/Sheets automatically expands the range to `D2:D8` — confirm this happened; if you inserted at the very bottom edge instead, the range may not auto-expand, which is exactly why this test matters.)*
- [ ] **Change one line item's `Qty`.** Only that row's `Line Total` changes; every other row is unaffected; `Subtotal`, `Tax`, and `Grand Total` all ripple correctly.
- [ ] **Change the `Tax Rate`** from `8.25%` to `10%`. `Tax` and `Grand Total` update instantly; nothing else changes.
- [ ] **Delete a line item row.** The invoice still computes correctly — no `#REF!` anywhere. *(If you get `#REF!` here, a formula somewhere referenced that specific row directly instead of through the range-based `Subtotal`.)*

## Naming requirement

At minimum, name the **Tax Rate** cell (e.g., `TaxRate`) and use the name — not a raw `$`-locked address — in your Tax formula. This is non-negotiable for this project: it's the one piece of Lecture 3 the invoice specifically exercises.

## Formatting requirements

- All money values (`Unit Price`, `Line Total`, `Subtotal`, `Tax`, `Grand Total`, `Amount Due`) formatted as **Currency**, consistent decimal places.
- The rate cells formatted as **Percentage**.
- Header row of the line-items table bold, with a bottom border.
- Frozen top rows so the header block stays visible if you scroll (Week 1 skill, still relevant).

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 30% | All totals compute correctly; the four required-behavior tests all pass |
| Reference discipline | 25% | Relative refs on line totals, absolute/named ref on the tax rate, no hardcoded numbers where a reference belongs |
| Resilience | 20% | Inserting/deleting a line item doesn't break anything — ranges expand, nothing shows `#REF!` |
| Named ranges | 10% | Tax rate is named and the name is used in the formula, not a raw `$` address |
| Formatting/readability | 15% | Currency/percentage formats applied correctly; header is clean and client-presentable |

## Reflection (`notes.md`, ~150–200 words)

1. Which required behavior test (insert a row, change a rate, delete a row) was hardest to get right, and why?
2. Where did you choose an absolute reference over a named range, or vice versa, and why?
3. If you were handing this invoice template to a coworker who'd never seen it, what's the one thing about your formulas you'd want to explain first?

## Stretch goals

- **Wire up the Discount Rate.** Add a `Discount` line between Subtotal and Tax that subtracts `Subtotal * DiscountRate` before tax is calculated — decide whether tax should apply to the pre- or post-discount amount, and state your assumption.
- **A second invoice, same template.** Duplicate the sheet tab, change every line item and the client name, and confirm the tax rate and formula structure survive the duplication cleanly (watch for named ranges scoped to "workbook" vs. "sheet" — this is exactly where that distinction from Lecture 3 matters).
- **Line-item numbering.** Add a leftmost `#` column that auto-numbers rows 1, 2, 3… using a formula (`=ROW()-1` is a clean approach) so renumbering after inserting/deleting a row is automatic too.

## Why this matters

Every dashboard, report, and financial model in the rest of this course is this exact same pattern at larger scale: relative references for row-by-row math, absolute or named references for shared constants, and formulas that survive structural edits (inserted rows, deleted rows, changed inputs) without needing to be retyped. An invoice that breaks the moment someone edits it isn't a spreadsheet — it's a trap. An invoice that survives real editing is the actual skill this week was teaching.

When done: push/save your work, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/quiz.md), and start [Week 3 — Logical & lookup functions](../../week-03-logical-and-lookup-functions/).
