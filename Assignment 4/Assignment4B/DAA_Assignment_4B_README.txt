README — DAA ASSIGNMENT 4B (CO4)
SIMATS ENGINEERING — DESIGN AND ANALYSIS OF ALGORITHMS
Algorithm Engineering: Implement, Test, Debug & Optimise
Individual assignment | 50 marks

STUDENT
Name: J. Lokesh
Registration number: Fill in your correct registration number.

FILES
1. DAA_Assignment_4B_All_Codes.py — complete Python demonstrations for Tasks 1–6.
2. DAA_Assignment_4B_All_Pseudocodes.txt — algorithm pseudocode for every task.
3. DAA_Assignment_4B_README.txt — this guide.
4. DAA_Assignment_4B_All_Outputs.pdf — consolidated execution output and traces.

TASK COVERAGE
Task 1 — Word Wrap DP:
Computes minimum squared-slack penalty (final line penalty is zero), reconstructs
line contents, unused spaces and each line penalty, prints suffix DP states, and
tests three widths plus a word-too-long boundary case.

Task 2 — Greedy vs DP Knapsack:
Implements fractional knapsack and 0/1 knapsack. Reports selected fractions/items,
DP state count and memory cells. Demonstrates why value/weight greedy selection
is not generally optimal for indivisible 0/1 items. The sample with weights
10,20,30; values 60,100,120; capacity 50 gives a 0/1 optimum of 220 (items B+C),
while a whole-item ratio greedy choice A+B gives 160. Fractional knapsack is a
different problem formulation and can take part of an item.

Task 3 — Routing:
Uses an eight-vertex, twelve-edge directed network. Displays Dijkstra distances,
paths, predecessors and finalisation order. Adds a negative edge and compares
Bellman-Ford. Adds a reachable negative cycle and reports it. Prints Floyd
all-pairs distances and Warshall reachability.

Task 4 — Assembly Line:
Implements the two-line DP, prints stay-versus-transfer costs at each station,
reconstructs the optimal line sequence, and runs transfer-time and station-delay
experiments. Explains the F[line][station] extension for three lines.

Task 5 — MST:
Implements Kruskal (disjoint sets), Prim (cut-minimum edge) and Boruvka
(cheapest outgoing edge per component). Prints edge construction traces and
compares costs. A tie-weight graph demonstrates that valid MSTs may differ
in edge set while retaining equal total cost.

Task 6 — TSP:
Implements Held-Karp subset DP for a hub plus six delivery locations, reconstructs
the full cycle, validates a smaller instance against exhaustive permutation
enumeration, and prints the subset-state growth. It does not attempt 200 locations.

HOW TO RUN IN GOOGLE COLAB
1. Upload DAA_Assignment_4B_All_Codes.py to Colab.
2. Run:
   %run /content/DAA_Assignment_4B_All_Codes.py
3. The program prints the demonstrations and validation checks.
4. To download the consolidated PDF after uploading it:
   from google.colab import files
   files.download('/content/DAA_Assignment_4B_All_Outputs.pdf')

HOW TO RUN IN VS CODE
Install Python 3.10 or later. Open the folder and run:
   python DAA_Assignment_4B_All_Codes.py
Only Python standard-library modules are used.

COMPLEXITY SUMMARY
- Word Wrap: O(n^2) time, O(n) DP/reconstruction storage.
- Fractional Knapsack: O(n log n) time due to sorting.
- 0/1 Knapsack: O(nW) time and O(nW) space.
- Dijkstra: O(V^2) in this array-based implementation.
- Bellman-Ford: O(VE).
- Floyd-Warshall and Warshall: O(V^3), O(V^2) storage.
- Two-line assembly scheduling: O(n) time and O(n) reconstruction storage.
- Kruskal: O(E log E); Prim here uses simple edge scans; Boruvka has
  O(E log V) phases with suitable component handling.
- Held-Karp TSP: O(m^2 2^m) time and O(m 2^m) space.

IMPORTANT ENGINEERING NOTES
The graph is directed for routing tasks and undirected for MST tasks.
Dijkstra is only valid for non-negative edge weights. Bellman-Ford detects
reachable negative-weight cycles. Floyd computes costs; Warshall computes
reachability. The TSP cost matrix is symmetric and complete in this demonstration.
Measured execution time and memory vary by machine. DP state counts and theoretical
growth are more useful than timing alone. For 200 delivery locations, exact
Held-Karp is impractical; a heuristic can return a good route but cannot guarantee
the mathematical optimum.

GITHUB
git add DAA_Assignment_4B_All_Codes.py
git add DAA_Assignment_4B_All_Pseudocodes.txt
git add DAA_Assignment_4B_README.txt
git commit -m "Add DAA Assignment 4B CO4 algorithms"
git push

END OF README
