README — CSA06 CO4: CLOUD RELEASE BUDGET PLANNER
Student: J. Lokesh | Registration No.: 192311216
Course: CSA06 Design and Analysis of Algorithms | CO4
Topic: Dynamic Programming and Greedy Strategies

FILES
- CSA06_CO4_Cloud_Release_Budget_Planner.py: runnable Python solution.
- CSA06_CO4_All_Pseudocodes.txt: greedy, DP and reconstruction pseudocode.
- CSA06_CO4_README.txt: this guide.
- CSA06_CO4_All_Outputs.pdf: combined sample and edge-test output.

PROBLEM
Each feature has a name, cost and value. Select each feature at most once,
with total cost no greater than W, to maximise total value. Report both
the greedy value-per-cost result and the optimal DP result.

INPUT
First line: n W
Next n lines: name cost value

OUTPUT — EXACTLY FOUR LINES
Greedy Value = G
Maximum Value = V
Selected = names in input order, or NONE
Budget Used = B

GREEDY
Sort by decreasing value/cost ratio and take each feature if it fits.
This is a heuristic only. Sample 1 demonstrates that it can be suboptimal:
greedy chooses Auth and Search (value 160), while the optimum chooses
Search and Payments (value 220).

DYNAMIC PROGRAMMING
The implementation uses exact-cost DP. DP[i][w] stores the best value
using the first i features with exact total cost w; unreachable costs are
None. Each feature is either skipped or selected once. A take table stores
decisions for reconstruction. The final scan chooses maximum value and,
on a tie, the smallest used budget. Names are output in original input order.

TESTING
The script checks both assignment samples and these edge cases:
zero budget, no feature fits, all features fit, tied optimum with
different costs, a single feature, and maximum constraints n=200/W=10000.

COMPLEXITY
Greedy: O(n log n) time.
DP: O(nW) time and O(nW) space.
With n<=200 and W<=10000, at most about two million state transitions.
The algorithm is pseudo-polynomial because runtime depends on numeric W,
whose binary encoding takes O(log W) bits.

GOOGLE COLAB
Upload the .py file, then run:
%run /content/CSA06_CO4_Cloud_Release_Budget_Planner.py
To run a custom input file:
!python /content/CSA06_CO4_Cloud_Release_Budget_Planner.py < /content/input.txt
Download the PDF after uploading it:
from google.colab import files
files.download('/content/CSA06_CO4_All_Outputs.pdf')

GITHUB
git add CSA06_CO4_Cloud_Release_Budget_Planner.py
git add CSA06_CO4_All_Pseudocodes.txt
git add CSA06_CO4_README.txt
git commit -m "Add CSA06 CO4 Cloud Release Budget Planner"
git push

This is an individual in-class challenge. Practise explaining the greedy
limitation, DP recurrence, tie-breaking, reconstruction and complexity.
