# Mini-Project — Turn a Raw CSV Dump Into a Clean, Validated Dataset

> Take a genuinely messy 32-row export — duplicates, blank rows, inconsistent categories, mixed date/phone formats, and a few outliers — and produce a tidy, deduplicated, standardized dataset with drop-down-guarded input columns and outlier flags, ready to hand to Week 7's pivot tables without anyone double-checking it first.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it deliberately mirrors real analyst work: nobody hands you a clean table and asks you to pivot it. They hand you an export, a Friday deadline, and an assumption that whatever you hand back is trustworthy. This project asks you to prove that, end to end, on one dataset — audit, clean, standardize, guard, and flag — and to document every judgment call along the way, the same discipline both challenges asked of you.

---

## Deliverable

A workbook (or clearly separated sheet set in your `crunch-week5` workbook) containing:

1. `RawDump` — the raw data below, typed in exactly as given, untouched.
2. `CleanData` — your final cleaned, standardized, deduplicated result.
3. `ValidatedEntry` — a small guarded entry area (Data Validation + at least one dependent drop-down) that a new row could be added through going forward, built on the same categories as `CleanData`.
4. `report.md` (or a `Report` sheet) — your audit findings, every judgment call and its reasoning, and your final row-count reconciliation (how many raw rows in, how many clean rows out, and exactly what happened to the difference).
5. `notes.md` — a short reflection (see the end).

---

## The raw dataset

Build a sheet named `RawDump` with this data, typed in **exactly as shown**:

```
OrderID,Customer,Email,State,MembershipTier,Category,Item,Qty,UnitPrice,OrderDate
9001,  Diego Ramos ,diego.ramos@mail.com,CO,gold,Gear,Trail Backpack,1,89.99,3/1/2025
9002,Lauren Kessler,lauren.kessler@mail.com,Colorado,Gold,Footwear,Hiking Boots,1,110.00,03/02/2025
9003,Diego Ramos,diego.ramos@mail.com,co,GOLD,Gear,Trail Backpack,1,89.99,2025-03-01
9004,Sam Whitfield,sam.whitfield@mail.com,UT,silver,Apparel,Rain Shell,2,44.99,3/4/25
9005,Lauren  Kessler,LAUREN.KESSLER@MAIL.COM,CO,Gold,Footwear,Hiking Boots,1,110.00,2025-03-02
9006,Mei Lin,mei.lin@mail.com,utah,Silver,Gear,Camp Stove,1,52.00,03/07/2025
9007,,jenna.park@mail.com,UT,bronze,Footwear,Sandals,1,38.00,3/9/2025
9008,Carlos Ibarra,carlos.ibarra@mail.com,CO,Bronze,Apparel,Base Layer Top,3,24.00,03/11/2025
9009,Mei Lin,mei.lin@mail.com,UT,Silver,Gear,Camp Stove,1,52.00,3/7/25
9010,Jenna Park,jenna.park@mail.com,Utah,Bronze,Footwear,Sandals,1,38.00,2025-03-09
9011,,,,,,,,,
9012,Priya Deshmukh,priya.deshmukh@mail.com,WY,platinum,Gear,Sleeping Bag,1,64.50,03/15/2025
9013,Owen Baxter,owen.baxter@mail.com,wy,Platinum,Apparel,Down Jacket,1,199.00,3/16/2025
9014,Diego Ramos,diego.ramos@mail.com,CO,Gold,Footwear,Trail Runners,1,105.00,04/02/2025
9015,Sofia Reyes,sofia.reyes@mail.com,Wyoming,Platinum,Gear,Tent 4-Person,1,199.00,03/18/2025
9016,Nathan Voss,nathan.voss@mail.com,CO,gold,Gear,Trekking Poles,-1,38.00,03/20/2025
9017,Priya Deshmukh,priya.deshmukh@mail.com,wy,Platinum,Gear,Sleeping Bag,1,64.50,3/15/25
9018,Carlos Ibarra,carlos.ibarra@mail.com,co,BRONZE,Apparel,Base Layer Top,3,24.00,2025-03-11
9019,Ravi Kumar,ravi.kumar@mail.com,UT,Silver,Footwear,Wool Socks,5,9.99,03/22/2025
9020,Bethany Cole,bethany.cole@mail.com,CO,gold,Apparel,Fleece Pullover,1,2499.00,03/23/2025
9021,Nathan Voss,nathan.voss@mail.com,co,Gold,Gear,Trekking Poles,1,38.00,3/20/25
9022,Alicia Ferreira,alicia.ferreira@mail.com,UT,silver,Gear,Water Bottle,2,12.00,03/25/2025
9023,Marcus Yoon,marcus.yoon@mail.com,WY,Bronze,Footwear,Hiking Boots,1,110.00,03/27/2025
9024,Bethany Cole,bethany.cole@mail.com,CO,Gold,Apparel,Fleece Pullover,1,49.00,03/23/25
9025,Ravi  Kumar,RAVI.KUMAR@MAIL.COM,Utah,Silver,Footwear,Wool Socks,5,9.99,3/22/2025
9026,Yuki Tanaka,yuki.tanaka@mail.com,CO,Gold,Gear,Camp Stove,1,52.00,03/29/2025
9027,Alicia Ferreira,alicia.ferreira@mail.com,ut,Silver,Gear,Water Bottle,2,12.00,2025-03-25
9028,Marcus Yoon,marcus.yoon@mail.com,wyoming,bronze,Footwear,Hiking Boots,1,110.00,3/27/25
9029,Devon Marsh,devon.marsh@mail.com,CO,Silver,Apparel,Rain Shell,1,44.99,03/30/2025
9030,Yuki Tanaka,yuki.tanaka@mail.com,co,GOLD,Gear,Camp Stove,1,52.00,3/29/25
9031,Isabel Suarez,isabel.suarez@mail.com,UT,Gold,Gear,Trail Backpack,1,89.99,04/01/2025
9032,Devon Marsh,devon.marsh@mail.com,Colorado,Silver,Apparel,Rain Shell,1,44.99,3/30/25
```

This dataset was built with the following problems **deliberately** planted — you're not told which rows they're in, finding them is the audit:

- Several **exact** and **near-duplicate** orders (same customer, same order, entered twice — sometimes with a casing or date-format difference).
- One row with a **missing customer name** (9007) and one **completely blank** row (9011).
- `State` fragmented across postal code / full name / mixed casing, covering four real states.
- `MembershipTier` fragmented across casing variants of four real tiers.
- `OrderDate` mixed across three text/date formats.
- At least one **negative `Qty`** (9016) and at least one **outlier `UnitPrice`** that's wildly out of line with the same item's price elsewhere in the data (compare 9020's Fleece Pullover price against 9024's).

---

## Requirements

### 1. Audit (`report.md`, Section 1)

Using Lecture 1's techniques, report: total raw rows, count of exact duplicates, count of near-duplicates, count of blank/incomplete rows, the distinct-value fragmentation count for `State` and `MembershipTier` before cleaning, and every `OrderDate` cell that failed an `ISNUMBER` check (i.e., wasn't a true date).

### 2. Clean (`CleanData`)

Apply the full Lecture 2 sequence, in order: fix structure (none needed here — the shape is already tidy), strip whitespace/invisible characters, standardize categories (`State` → 4 canonical full names; `MembershipTier` → 4 canonical Title-Case values), standardize `OrderDate` to one true-date format, then dedupe last.

Handle the two judgment-call rows explicitly in `report.md`: the blank row (9011 — delete, obviously) and the missing-name row (9007 — state and justify your decision, same as Challenge 1 Task 1).

Handle the negative `Qty` (9016) and the price outlier (9020 vs. 9024) explicitly too — state your interpretation and what you did about each.

### 3. Guard (`ValidatedEntry`)

Build a small entry area with, at minimum: `State` as a plain List validation from your 4 clean states, `Category` → `Item` as a genuine `FILTER`-driven **dependent** drop-down pair (reuse the categories/items already present in the cleaned data — `Gear`, `Footwear`, `Apparel`), `Qty` restricted to positive whole numbers only, and `OrderID` guarded against duplicates with a custom-formula uniqueness rule.

### 4. Flag (`CleanData`, conditional formatting)

Add at least three conditional-formatting rules on the final `CleanData` sheet: duplicate `OrderID` (should find none, post-cleaning — this is your final proof, not a discovery step), a `UnitPrice` outlier flag (a price for a given `Item` that differs by more than, say, 3x from that item's typical price elsewhere in the sheet — you decide and document the exact threshold), and a blank-required-field flag on `Customer`/`State`.

---

## Milestones

- **Milestone 1 (40 min):** `RawDump` typed in exactly; full audit complete and documented in `report.md`.
- **Milestone 2 (60 min):** `CleanData` — structure, whitespace, category standardization, date standardization complete.
- **Milestone 3 (30 min):** Dedupe pass on `CleanData`, judgment calls (9007, 9016, 9020/9024) documented, final audit re-run and confirmed clean.
- **Milestone 4 (40 min):** `ValidatedEntry` built and tested with at least 3 test rows, including one deliberate failed entry per guarded field.
- **Milestone 5 (20 min):** Conditional-formatting flags added to `CleanData` and confirmed to fire correctly on a test case you introduce on purpose, then remove.
- **Milestone 6 (10–20 min):** `notes.md` reflection.

---

## Rules

- **Clean in the Lecture 2 order** — structure, then whitespace, then categories, then dedupe last. Deduping first on this dataset will under-count duplicates, because several near-duplicates only become exact matches *after* standardization.
- **Every judgment call gets one documented sentence** in `report.md` — the blank row, the missing name, the negative quantity, and the price outlier all require one.
- **`OrderDate` must end up as real dates**, verified with `ISNUMBER`, not text that merely displays correctly.
- **The dependent drop-down must be genuinely dependent** — `Item` options must visibly change when `Category` changes, tested and confirmed, not just two independent lists.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|---------------------|
| Audit completeness | 20% | All planted problems found and counted before cleaning begins |
| Cleaning correctness | 25% | Categories fully standardized, dates uniformly real, dedupe run last and complete |
| Judgment-call documentation | 15% | All four flagged decisions stated with clear reasoning |
| Validation guard | 20% | All required `ValidatedEntry` fields present, dependent drop-down genuinely working, tested with both valid and invalid entries |
| Conditional-formatting flags | 10% | 3+ rules present, correctly scoped, tested to fire and clear correctly |
| Final row reconciliation | 10% | `report.md` states raw-row count, clean-row count, and accounts for every row removed or merged |

---

## Reflection (`notes.md`, ~200 words)

1. Which planted problem took the longest to find during the audit — and what would have caught it faster?
2. Where did standardizing *before* deduping change your duplicate count, compared to what a naive Remove Duplicates pass (run first, on raw data) would have found?
3. Of the four validation techniques this week (List, number-range, date-range, custom-formula), which felt most natural, and which still feels like you're translating rather than writing fluently?
4. If this dataset arrived monthly instead of once, what would you want to change about your process to make next month's cleanup faster than this one? (Foreshadows Tables in Week 6 and Power Query in Week 11.)

---

## Why this matters

This mini-project is the complete arc of Week 5 in one file: find the mess, fix the mess, and build a door that keeps the mess from coming back — with every non-obvious decision written down so someone else could pick up your work and trust it. That trustworthiness is what separates a spreadsheet from a *toy* spreadsheet, and it's exactly the foundation Week 6's Tables (which auto-expand and carry your validation/formatting rules automatically as new rows are added) build directly on top of.

When done: push/save your work, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-05-data-cleaning-and-validation/quiz.md) and start [Week 6 — Tables & structured references](../../week-06-tables-and-structured-references/).
