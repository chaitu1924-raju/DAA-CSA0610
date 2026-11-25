README — DAA ASSIGNMENT 5 (CO5)
SIMATS ENGINEERING — DESIGN AND ANALYSIS OF ALGORITHMS
Search, Complexity and Approximation Engineering | 50 Marks

STUDENT
Name: J. Lokesh
Registration Number: Fill in your correct registration number.

PACKAGE FILES
1. DAA_Assignment_5_All_Codes.py — executable Python implementations for Part B.
2. DAA_Assignment_5_All_Pseudocodes.txt — Part A pseudocode and design answers.
3. DAA_Assignment_5_README.txt — this guide.
4. DAA_Assignment_5_All_Outputs.pdf — one PDF containing the full run output.

ASSIGNMENT STRUCTURE
Part A (25 marks): A1 Graph Colouring; A2 Subset Sum; A3 common backtracking pattern;
A4 P, NP, NP-Complete and NP-Hard; A5 Set Cover approximation design.
Part B (25 marks): B1 instrumented Graph Colouring; B2 adversarial graph inputs;
B3 exact versus greedy Set Cover; B4 Bin Packing heuristic and decision note.

IMPLEMENTED TASKS
B1 — Graph Colouring:
Backtracking tests feasibility against already-coloured neighbours. Counters include
search nodes, candidate attempts, rejected branches, backtracks and maximum depth.
Two orderings are compared: input order and descending vertex degree. Test cases
include a colourable 8-cycle with 3 colours, an uncolourable K3 with 2 colours,
and an empty graph boundary case.

B2 — Adversarial Search:
Compares an 8-cycle and complete graph K8, both with 8 vertices and 3 colours.
The complete graph is not 3-colourable and causes unsuccessful branches as colours
are exhausted. Search statistics are printed for both.

B3 — Set Cover:
Exact search enumerates centre combinations in increasing size and returns a
minimum-cardinality cover. Greedy repeatedly selects the centre covering the most
currently uncovered zones. Four instances are included, including a greedy
counterexample candidate. The program also prints operation counts for larger
families. If a set of centres cannot cover the universe, the method reports failure.

B4 — Bin Packing:
First Fit Decreasing (FFD) sorts workloads in descending order and places each
workload in the first server with enough remaining capacity. It reports workloads,
server usage, remaining capacity, server count and a volume lower bound.

RUN IN GOOGLE COLAB
1. Upload DAA_Assignment_5_All_Codes.py to Colab.
2. Execute:
   %run /content/DAA_Assignment_5_All_Codes.py
3. The output PDF is a separate file in this package. Upload it to Colab if you
   want to download it through Colab:
   from google.colab import files
   files.download('/content/DAA_Assignment_5_All_Outputs.pdf')

RUN IN VS CODE
Use Python 3.9 or later. Open a terminal in the folder and run:
   python DAA_Assignment_5_All_Codes.py
The script uses only Python standard-library modules.

COMPLEXITY NOTES
- Graph Colouring: worst-case O(k^V * (V+E)) in a straightforward backtracking model;
  actual work depends heavily on graph structure and vertex ordering.
- Subset Sum backtracking: worst-case O(2^n), with pruning helping on some inputs.
- Exact Set Cover by subset enumeration: O(2^m * total-set-union work).
- Greedy Set Cover: polynomial; repeated scans over candidate centres and uncovered
  zones. It is not guaranteed to find the minimum cover.
- First Fit Decreasing: O(n log n + nB) in this simple implementation, where B is
  the number of bins opened; worst-case placement scans can be quadratic.

IMPORTANT NOTES
The uploaded assignment leaves some mathematical symbols blank in the PDF extraction
(e.g. the number of server groups in A1 and capacity symbol in B4). The code uses
explicit example values and documents them in output. Adjust these values if your
instructor specified different values elsewhere.
The Part A section is pseudocode and reasoning, not programming code, because the
assignment explicitly says programming-language code will not be accepted as
pseudocode. Part B contains executable Python.

GITHUB COMMANDS
git add DAA_Assignment_5_All_Codes.py
git add DAA_Assignment_5_All_Pseudocodes.txt
git add DAA_Assignment_5_README.txt
git commit -m "Add DAA Assignment 5 CO5 solutions"
git push

END OF README
