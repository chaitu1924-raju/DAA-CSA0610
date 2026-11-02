# Assessment 3 – CO3
## Case Study: Divide-and-Conquer Engine of the KartIQ Retail Data Analytics Platform

**Course:** CSA06 – Design and Analysis of Algorithms  
**Department:** Computer Science and Engineering  
**Student Name:** ______________________________  
**Register Number:** ___________________________  
**Duration:** 1 Week | **Mode:** Individual

---

## (a) Understand the Case

KartIQ processes about 10,000,000 orders per day and ranks 100,000 sellers. Its current performance problems are late nightly reports, a freezing seller leaderboard, slow order lookups, and infrequent recommendation updates. Divide-and-conquer algorithms are selected according to each module's input characteristics and correctness requirements.

| Module | Computational requirement | Key issues | Consequence of a poor choice |
|---|---|---|---|
| 1. Nightly order consolidation | Sort 10 million orders by timestamp | Stability is essential; large input; Merge Sort needs extra memory | An unstable sort can change the arrival order of equal-timestamp orders; a slow sort can miss the reporting deadline |
| 2. Live seller leaderboard | Re-sort 100,000 seller scores repeatedly | Scores are nearly sorted; first-element pivot can create unbalanced partitions; duplicates may occur | First-pivot Quick Sort can degrade to quadratic time and freeze the leaderboard |
| 3. Order lookup | Find an order by timestamp in the sorted order list | Input must be sorted; duplicate timestamps require the first match | Linear search is slow at this scale; ordinary binary search may return a later duplicate |
| 4. Recommendation scores | Multiply two 1,024 × 1,024 matrices | Matrix size; recursion overhead; memory allocation and padding | Conventional multiplication performs many scalar multiplications; an unpractical recursive implementation can lose its theoretical advantage |

## (b) Module 1 – Merge Sort for Nightly Order Consolidation

### Divide, conquer and combine

1. **Divide:** Split the order list into two halves repeatedly until each sublist contains one order.
2. **Conquer:** A one-element list is already sorted.
3. **Combine:** Merge two sorted sublists by repeatedly selecting the smaller timestamp. When timestamps are equal, select the item from the left sublist first. This preserves the original order and makes the algorithm stable.

### Trace using the supplied orders

Input:

`(105,O1), (102,O2), (105,O3), (101,O4), (102,O5), (103,O6)`

Initial single-element lists:

`[105 O1] [102 O2] [105 O3] [101 O4] [102 O5] [103 O6]`

First merge level:

- `[105 O1] + [102 O2]` → `[102 O2, 105 O1]`
- `[105 O3] + [101 O4]` → `[101 O4, 105 O3]`
- `[102 O5] + [103 O6]` → `[102 O5, 103 O6]`

Second merge level:

- `[102 O2, 105 O1] + [101 O4, 105 O3]`  
  → `[101 O4, 102 O2, 105 O1, 105 O3]`
- `[102 O5, 103 O6]` remains unchanged at this level.

Final merge:

`[101 O4, 102 O2, 105 O1, 105 O3] + [102 O5, 103 O6]`

Result:

`(101,O4), (102,O2), (102,O5), (103,O6), (105,O1), (105,O3)`

The two timestamp-102 orders remain O2 before O5, and the two timestamp-105 orders remain O1 before O3. Thus, equal timestamps retain their original arrival order.

### Recurrence and complexity

For an input of size n:

`T(n) = 2T(n/2) + Θ(n)`, with `T(1) = Θ(1)`.

By the Master Theorem:

`T(n) = Θ(n log₂ n)`.

For 10,000,000 orders, `log₂(10,000,000) ≈ 23.2535`. A useful comparison-scale estimate is approximately `n log₂ n`, or about **232.5 million** comparison-scale operations. The exact number depends on the input and merge pattern; the standard worst-case upper estimate is below roughly `n × ceil(log₂ n)` (about 240 million).

### Memory requirement and external sorting

Array-based Merge Sort needs `Θ(n)` auxiliary memory, in addition to the stored input. For 10 million records, memory use depends on the size and representation of each record. If the data does not fit in RAM, use **external Merge Sort**:

1. Read a RAM-sized chunk of orders.
2. Sort each chunk with stable Merge Sort.
3. Write each sorted chunk as a temporary file (sorted run).
4. Merge the runs using a k-way merge and a small priority queue.
5. Write the final sorted stream to storage.

This limits RAM use while retaining sorted order and stability.

## (c) Module 2 – Quick Sort for the Live Leaderboard

### One first-pivot partition trace

Sample scores: `[42, 17, 63, 8, 55, 29]`

Use the first element, 42, as the pivot. Move values smaller than the pivot to its left and larger values to its right.

- Start: `[42, 17, 63, 8, 55, 29]`, pivot = 42.
- 63 is on the wrong side and 29 is on the wrong side; swap them: `[42, 17, 29, 8, 55, 63]`.
- The pivot is placed between the smaller and larger values: `[8, 17, 29, 42, 55, 63]`.

This is one valid partition trace; subsequent recursive calls sort the two partitions.

### Why the first-element pivot is poor

If scores are already sorted or nearly sorted, choosing the first element repeatedly can produce partitions of sizes 0 and n−1. The recursion becomes highly unbalanced. This can make Quick Sort take quadratic time and can cause deep recursion, which explains the leaderboard freeze.

### Best-case and worst-case recurrences

Best case (approximately equal partitions):

`T(n) = 2T(n/2) + Θ(n) = Θ(n log n)`.

Worst case (one empty partition and one partition of size n−1):

`T(n) = T(n−1) + Θ(n) = Θ(n²)`.

For 100,000 already ordered scores, the first-pivot worst-case comparison count is:

`n(n−1)/2 = 100,000 × 99,999 / 2 = 4,999,950,000` comparisons.

A balanced comparison-scale estimate is `n log₂ n ≈ 100,000 × 16.61`, or about **1.66 million** comparison-scale operations. This is an estimate, not an exact count.

### Improved pivot strategy

Use **median-of-three pivot selection** (the median of the first, middle and last values), together with three-way partitioning for duplicate scores. This is less vulnerable to already sorted input than a fixed first-element pivot. Randomized pivot selection is another practical option. The implementation in this repository uses median-of-three selection and three-way partitioning.

Quick Sort has expected `Θ(n log n)` time with good pivot behaviour, but its worst case remains `Θ(n²)`. A production implementation can use introspective sorting (switching to Heap Sort after a recursion-depth limit) for a guaranteed `O(n log n)` worst-case bound.

## (d) Module 3 – Binary Search for Order Lookup

### Why sorted order is essential

Binary Search works only when the searched data is sorted by the same key used for lookup. Module 1 produces the timestamp-sorted list, so each comparison can eliminate approximately half of the remaining search range.

### Recurrence and maximum comparisons

`T(n) = T(n/2) + Θ(1)`, with `T(1) = Θ(1)`.

Therefore:

`T(n) = Θ(log₂ n)`.

For 10,000,000 orders, `ceil(log₂(10,000,000 + 1)) = 24`. Thus, a lower-bound binary search needs at most **24 timestamp comparisons** under the usual halving model.

### Return the first matching timestamp

Use **lower-bound Binary Search**:

- Set `low = 0`, `high = n`.
- While `low < high`, calculate `mid = low + (high-low)//2`.
- If `orders[mid].timestamp < target`, set `low = mid + 1`.
- Otherwise, set `high = mid`.
- At the end, `low` is the first possible matching position.
- If `low < n` and its timestamp equals the target, return that order; otherwise report not found.

This finds the first occurrence even when several orders share the timestamp. Its time complexity is `O(log n)` and its extra space is `O(1)`.

## (e) Module 4 – Strassen’s Method for Recommendation Scores

Given:

`A = [[1, 7], [3, 5]]` and `B = [[1, 3], [7, 5]]`.

For two 2 × 2 matrices:

`A = [[a, b], [c, d]]` and `B = [[e, f], [g, h]]`.

### Seven Strassen products

- `M1 = (a+d)(e+h)`
- `M2 = (c+d)e`
- `M3 = a(f-h)`
- `M4 = d(g-e)`
- `M5 = (a+b)h`
- `M6 = (c-a)(e+f)`
- `M7 = (b-d)(g+h)`

### Reconstruction formulas

- `C11 = M1 + M4 - M5 + M7`
- `C12 = M3 + M5`
- `C21 = M2 + M4`
- `C22 = M1 - M2 + M3 + M6`

### Verification on the sample matrices

Here `a=1, b=7, c=3, d=5, e=1, f=3, g=7, h=5`.

- `M1 = (1+5)(1+5) = 36`
- `M2 = (3+5)(1) = 8`
- `M3 = 1(3−5) = −2`
- `M4 = 5(7−1) = 30`
- `M5 = (1+7)(5) = 40`
- `M6 = (3−1)(1+3) = 8`
- `M7 = (7−5)(7+5) = 24`

Reconstruction:

- `C11 = 36 + 30 − 40 + 24 = 50`
- `C12 = −2 + 40 = 38`
- `C21 = 8 + 30 = 38`
- `C22 = 36 − 8 − 2 + 8 = 34`

Therefore:

`C = [[50, 38], [38, 34]]`.

### Recurrence and scalar multiplication comparison

Strassen performs seven multiplications of matrices of half the dimension, plus `Θ(n²)` additions:

`T(n) = 7T(n/2) + Θ(n²)`.

By the Master Theorem:

`T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.8074)`.

For `n = 1,024 = 2^10`:

- Strassen scalar multiplications: `7^10 = 282,475,249`.
- Conventional matrix multiplication: `n³ = 1,024³ = 1,073,741,824`.
- Strassen uses about 26.3% as many scalar multiplications, a theoretical reduction of about 73.7%.

### Why it may not be faster in practice

Strassen also performs matrix additions/subtractions, allocates temporary matrices, uses recursive calls, and can increase memory traffic. For small matrices, these overheads can outweigh the saved multiplications. Padding dimensions that are not powers of two can add further work.

### Practical hybrid

Use conventional multiplication below a measured cutoff (for example, 64 × 64), and Strassen above it. Pad non-power-of-two dimensions to a suitable size or split the matrix into blocks. Benchmark the cutoff on the target hardware and memory environment rather than assuming one threshold is best.

## (f) Final Algorithmic Design and Justification

| Module | Final choice | Time complexity | Extra memory | Main reason | Trade-off / when to change |
|---|---|---|---|---|---|
| 1. Order consolidation | Stable Merge Sort; external multiway merge if needed | `O(n log n)` | `O(n)` in-memory; bounded buffers for external merge | Guarantees stability and predictable performance | Uses extra memory; consider external sorting when data exceeds RAM |
| 2. Seller leaderboard | Median-of-three, three-way Quick Sort (or production introsort) | Expected `O(n log n)`; worst `O(n²)` for plain Quick Sort | `O(log n)` expected recursion stack | Better pivot behaviour for nearly sorted scores; handles duplicates | Use introsort if a strict worst-case guarantee is required |
| 3. Order lookup | Lower-bound Binary Search | `O(log n)` | `O(1)` | Finds the first matching timestamp quickly | Requires data to remain sorted; use an index if data updates frequently |
| 4. Recommendation scores | Hybrid Strassen + conventional multiplication cutoff | `O(n^2.8074)` above cutoff | Additional temporary matrix storage | Reduces asymptotic multiplication count for large dense matrices | Overhead and memory; use conventional/block multiplication for small or sparse matrices |

### Overall design

1. Sort each day's orders with stable Merge Sort. If the data is too large for RAM, create sorted runs and perform an external k-way merge.
2. Refresh the seller leaderboard using a robust pivot strategy. For production, use introsort or a trusted library sort to guard against pathological worst cases.
3. Keep the consolidated orders sorted by timestamp and use lower-bound Binary Search for support lookups.
4. Calculate dense recommendation matrices with a benchmarked Strassen/conventional hybrid.

The design balances correctness, performance, stability, and memory use. The main trade-off is that faster divide-and-conquer methods can require additional memory or implementation overhead. The algorithm should be changed when the input size, data distribution, memory limit, or update frequency changes.

---

## Python implementation

The accompanying `src/` directory contains runnable implementations of the four modules. Run `python src/main.py` to see the sample results and `python -m unittest discover -s tests -v` to execute the tests.

## Code of Conduct

I ______________________________ (Name / Register Number) certify that this submission is my original work and that I have adhered to the guidelines specified for this assessment. I understand that any violation of academic integrity rules will result in disciplinary action.

**Signature of the Student:** ____________________  
**Date:** ____________________
