CSA06 CO5 – UNIVERSITY EXAMINATION TIMETABLING
Prepared for: J. Lokesh
Registration Number: __________________

FILES
1. CSA06_CO5_Timetable.py
   Complete Python implementation: backtracking feasibility search, room-capacity
   checks, trace instrumentation, timetable printing, and branch-and-bound
   optimisation of the same-day clash penalty.
2. CSA06_CO5_All_Pseudocodes_and_Answers.txt
   Part (a)–(f): problem definition, constraints, complete pseudocode, trace
   explanation, complexity, branch and bound, and 300-course scaling.
3. CSA06_CO5_README.txt
   This guide.
4. CSA06_CO5_All_Outputs.pdf
   Actual output produced by running the Python implementation.

HOW THE MODEL IS REPRESENTED
- Each course is a vertex.
- Each clash pair is an undirected edge.
- Each of the four time slots is a colour.
- Two halls mean at most two exams can occupy one slot.
- Hall A has capacity 160; Hall B has capacity 120.
- C5 has 150 students and must therefore use Hall A.
- Every other course fits either hall, subject to one exam per hall per slot.

IMPORTANT FEASIBILITY RESULT
Three slots are impossible: two halls per slot provide only six exam positions,
while eight courses must be scheduled. Four slots are therefore necessary.
The clash graph also contains the clique C1-C2-C3, requiring at least three
different slots, but the hall-count bound is stronger for this particular
three-slot question.

RUN IN GOOGLE COLAB
1. Open https://colab.research.google.com/
2. Upload CSA06_CO5_Timetable.py using the Files panel, or upload it from your PC.
3. Run this cell:
   !python CSA06_CO5_Timetable.py
4. To save the complete terminal output as a text file:
   !python CSA06_CO5_Timetable.py > CSA06_CO5_All_Outputs.txt
5. Download the text output:
   from google.colab import files
   files.download('CSA06_CO5_All_Outputs.txt')

RUN IN VS CODE
1. Install Python 3 if it is not already installed.
2. Open the folder containing CSA06_CO5_Timetable.py in VS Code.
3. Open Terminal > New Terminal.
4. Run:
   python CSA06_CO5_Timetable.py
   On some Windows installations use:
   py CSA06_CO5_Timetable.py
5. To save output:
   python CSA06_CO5_Timetable.py > CSA06_CO5_All_Outputs.txt

DOWNLOAD THE PROVIDED OUTPUT PDF IN COLAB
Upload CSA06_CO5_All_Outputs.pdf to the Colab session, then run:
   from google.colab import files
   files.download('CSA06_CO5_All_Outputs.pdf')

GITHUB COMMANDS
   git init
   git add CSA06_CO5_Timetable.py CSA06_CO5_All_Pseudocodes_and_Answers.txt CSA06_CO5_README.txt
   git commit -m "Add CSA06 CO5 examination timetabling solution"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPOSITORY_URL
   git push -u origin main
Replace YOUR_GITHUB_REPOSITORY_URL with your own repository URL.

ALGORITHM NOTES
- Search order: descending clash degree, then descending enrolment.
- Feasibility search checks clashes first, then hall count and room capacity.
- Branch and bound minimises the number of clash edges whose courses are on
  the same day. The lower bound counts such edges whose endpoints are already
  assigned; these penalties cannot be undone by future assignments.
- Complexity is exponential in the worst case. Verification of a proposed
  timetable is polynomial.
- The generalised decision problem is NP-complete by reduction from graph
  k-colouring; the optimisation problem is NP-hard.

ACADEMIC NOTE
The output is generated for the exact course sizes, clash list, slot names and
hall capacities in the uploaded CSA06 CO5 question. Registration number is left
blank because it was not supplied. Review the final work and follow your
institution's submission and academic-integrity requirements.
