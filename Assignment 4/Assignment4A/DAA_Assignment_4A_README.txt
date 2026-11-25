README — DAA ASSIGNMENT 4A (CO4)
SIMATS ENGINEERING — DESIGN AND ANALYSIS OF ALGORITHMS
Algorithmic Design Through Pseudocode | Individual Assignment | 50 Marks

STUDENT
Name: J. Lokesh
Registration Number: Please fill in your registration number as required on the cover.

IMPORTANT ASSIGNMENT REQUIREMENT
The source assignment (page 1 and page 17) explicitly says this is not a programming
assignment. It requires language-independent pseudocode following the SIMATS
Engineering Handbook for Algorithmic Pseudocode. Programming code in Python, C,
C++ or Java will not be accepted as pseudocode. Therefore, this package provides
pseudocode, reasoning, traces and design analysis—not executable program code.

FILES
1. DAA_Assignment_4A_All_Pseudocodes.txt — complete task-wise pseudocode and answers.
2. DAA_Assignment_4A_README.txt — this guide.
3. DAA_Assignment_4A_Trace_and_Answers.pdf — consolidated desk-checks, traces,
   complexity notes and final results.

TASK COVERAGE
Task 1 (6 marks): Diagnose vague fractional-knapsack pseudocode, repair it using
value-per-weight greedy selection and fractional loading, and provide a design defence.
Task 2 (8 marks): Model job sequencing with deadlines; formulate profit-descending
greedy rule; provide pseudocode, slot trace and a modified-profit challenge.
Task 3 (9 marks): Define 0/1 knapsack DP state and recurrence, fill states, reconstruct
selected items, and trace the capacity-7 instance.
Task 4 (7 marks): Find the missing DP-prefix condition in Word Break, construct a
counterexample, minimally repair the condition, and run a regression example.
Task 5 (7 marks): Write Dijkstra pseudocode and trace; explain why negative edges
invalidate its greedy finalisation; provide Bellman-Ford and Floyd-Warshall logic.
Task 6 (13 marks): Formulate weighted interval scheduling, define predecessor p(i)
and OPT(i), write complete DP/reconstruction pseudocode, trace the eight jobs and
construct an adversarial greedy counterexample.

KEY RESULTS
Task 2 given jobs: schedule slot 1=C, slot 2=A, slot 3=D; profit 180.
Task 2 challenge after changing D profit to 90: same schedule; profit 230.
Task 3 capacity 7: select P and Q; total weight 5; maximum value 32.
Task 4 counterexample: Text="ab", Dictionary={"b"}; faulty logic can set DP[2]=TRUE.
Correct logic also requires DP[j]=TRUE.
Task 5 shortest distances from A: A=0, B=4, C=6, D=7, E=10.
Task 6 provided jobs: select J2, J5, J7, J8; total energy-saving value 200.
Task 6 adversarial case: highest-value-first takes X1 for 100, while DP selects
X2+X3+X4+X5 for 160.

COMPLEXITY SUMMARY
- Fractional Knapsack: O(n log n) for sorting, then O(n) scan.
- Job Sequencing: O(n log n + nD) with the simple latest-free-slot scan,
  where D is maximum deadline; can be improved with a disjoint-set structure.
- 0/1 Knapsack: O(nW) time and O(nW) space for the full reconstruction table.
- Word Break: O(n^2) substring checks, plus dictionary lookup costs.
- Dijkstra: O(V^2) with array-based minimum selection; O((V+E) log V) with
  an appropriate priority queue.
- Bellman-Ford: O(VE) time, O(V) distance/predecessor storage.
- Floyd-Warshall: O(V^3) time, O(V^2) space.
- Weighted Interval Scheduling: O(n^2) to find predecessors by backward scan
  plus O(n) DP; predecessor computation can be O(n log n) by binary search.

HOW TO USE
Read each task's problem interpretation first, then the decision/state definition,
pseudocode, trace and design explanation. Preserve the handbook's formatting rules
when transferring the answers to your final assignment document. The source asks
for reasoning and manual traces; do not submit only final numerical answers.

NOTE ON TASK 4
The counterexample is Text="ab", Dictionary={"b"}. The faulty algorithm may set
DP[2] using the dictionary word "b" despite DP[1] being FALSE. The minimal repair
adds DP[j]=TRUE to the decision condition.

NOTE ON TASK 6
The finish-time-equals-start-time assumption is treated as compatibility:
finish[j] <= start[i]. The eight-job optimum is J2, J5, J7, J8 with value 200.

END OF README
