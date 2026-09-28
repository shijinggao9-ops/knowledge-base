# Exercise 3 — Two-Way INDEX/MATCH Lookup

**Goal:** Build a live "type a rep and a quarter, get the sales figure" panel with `INDEX`/`MATCH`, solve a left-lookup that `VLOOKUP` can't do, and wrap both in `IFERROR`/`IFNA`.

**Estimated time:** 1.5 hours.

## Setup

Use the `SalesMatrix` sheet from Lecture 3. Confirm all 5 reps and 4 quarters are there:

```
      A          B         C         D         E
1   Rep        Q1        Q2        Q3        Q4
2   Amara      41200     38900     52100     47700
3   Devon      29800     31200     33500     30100
4   Priya      55600     58200     61000     59400
5   Malik      22100     24800     26300     25900
6   Sofia      37400     39100     41200     40800
```

Add an employee directory table further down the same sheet, in `A10:C14`, with the return column deliberately placed to the **right** of the lookup column:

```
       A              B             C
10   FullName       Region        RepID
11   Amara Osei     West           R-201
12   Devon Ward     Midwest        R-202
13   Priya Nair     East           R-203
14   Malik Diallo   South          R-204
15   Sofia Reyes    West           R-205
```

## Tasks

1. **Two-way lookup panel.** In `A17:B19`, build:

   ```
        A              B
   17   Rep          Priya
   18   Quarter       Q3
   19   Sales         =INDEX(B2:E6, MATCH(B17, A2:A6, 0), MATCH(B18, B1:E1, 0))
   ```

   Confirm `B19` returns `61000`. Change `B17` to `Sofia` and `B18` to `Q1` — confirm it updates to `37400`.

2. **Wrap it in `IFERROR`.** Change a rep name typed into `B17` to something that doesn't exist (`Jordan`). Confirm `B19` shows `#N/A`. Now wrap the whole formula in `IFERROR(..., "Rep or quarter not found")` and confirm the message replaces the error. Restore `B17` to a real rep afterward.

3. **Left-lookup by RepID.** In `A21:B22`, build a lookup that goes from `RepID` to `Region` — remember `Region` (column B) sits to the **left** of `RepID` (column C) in your directory table:

   ```
        A              B
   21   RepID to find    R-204
   22   Region         =INDEX(B10:B14, MATCH(A21, C10:C14, 0))
   ```

   Confirm `B22` returns `South`. Try typing `=VLOOKUP(A21, A10:C14, 2, FALSE)` in a scratch cell and observe that it returns the wrong thing entirely (it can't search column C at all with this table shape unless you rearrange columns — that's the point).

4. **Left-lookup for FullName too.** In `B23`, add a second `INDEX`/`MATCH` that returns `FullName` (column A) from the same `RepID` in `A21`. Confirm it returns `Malik Diallo` for `R-204`.

5. **Wrap both in `IFNA`.** Rewrite `B22` and `B23` wrapped in `IFNA(..., "Unknown RepID")`. Test with a fake ID (`R-999`) and confirm the message appears in both cells, then restore a real ID.

6. **Combine matrix + directory.** In `B25`, given the `RepID` in `A21` and a quarter typed into `A24`, write one formula that: (a) finds the rep's `FullName` via the directory left-lookup, then (b) uses that name to look up their sales figure in the matrix — two `INDEX`/`MATCH` calls, one feeding the other's lookup value. *(Hint: you can nest one full `INDEX`/`MATCH` formula as the `lookup_value` argument of `MATCH` inside the second.)*

## Expected result (spot checks)

- Task 1: `Priya`, `Q3` → `61000`.
- Task 3: `R-204` → `South`.
- Task 4: `R-204` → `Malik Diallo`.
- Task 6: `R-204` + `Q4` → `25900` (Malik's Q4 figure).

## Done when…

- [ ] Task 1's panel updates correctly for at least three different rep/quarter combinations you test yourself.
- [ ] You can explain out loud why `VLOOKUP` cannot do Task 3's lookup without rearranging the directory table's columns, and why `INDEX`/`MATCH` doesn't care.
- [ ] `B22`/`B23` show a clean message, not `#N/A`, for a nonexistent RepID.
- [ ] Task 6 correctly chains a directory lookup into a matrix lookup and returns the right sales figure for at least two RepIDs.

## Stretch

- Rebuild Task 1's panel using `XLOOKUP` nested inside `XLOOKUP` instead of `INDEX`/`MATCH`, and compare readability. Which do you prefer, and why?
- Add a `Q1–Q4 Total` column (`F`) to `SalesMatrix` using `SUM`, then extend the Task 1 panel with a `"Full Year"` option in `B18` that, when selected, returns the total instead of a single quarter — you'll need an `IF` around the `MATCH` for the column.

## Submission

Save your workbook. `INDEX`/`MATCH` and the error-trapping you practiced here carry straight into the mini-project's price-match component.
