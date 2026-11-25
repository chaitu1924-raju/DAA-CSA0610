"""
CSA06 CO5 – University Examination Timetabling
J. Lokesh | Registration Number: __________________

Run: python CSA06_CO5_Timetable.py
The script uses only Python's standard library.
It prints the backtracking trace, a feasible four-slot timetable,
the three-slot feasibility proof, and an exact branch-and-bound result.
"""
from collections import defaultdict

COURSES = {
    "C1": ("Design and Analysis of Algorithms", 120),
    "C2": ("Operating Systems", 90),
    "C3": ("Database Management Systems", 110),
    "C4": ("Computer Networks", 60),
    "C5": ("Java Programming", 150),
    "C6": ("Discrete Mathematics", 80),
    "C7": ("Artificial Intelligence", 40),
    "C8": ("Cloud Computing", 70),
}
EDGES = [
    ("C1","C2"), ("C1","C3"), ("C2","C3"), ("C1","C5"),
    ("C3","C5"), ("C2","C4"), ("C4","C6"), ("C5","C6"),
    ("C6","C7"), ("C7","C8"), ("C3","C8"), ("C5","C8"), ("C1","C6")
]
SLOTS = ["S1 (Day 1 FN)", "S2 (Day 1 AN)", "S3 (Day 2 FN)", "S4 (Day 2 AN)"]
ROOMS = {"A": 160, "B": 120}
ADJ = {c: set() for c in COURSES}
for a, b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)

def room_pair_possible(courses):
    """At most two exams per slot; assign distinct halls by capacity."""
    if len(courses) > 2:
        return False
    if len(courses) == 0:
        return True
    if len(courses) == 1:
        return any(ROOMS[r] >= COURSES[courses[0]][1] for r in ROOMS)
    # Try both room permutations.
    a, b = courses
    return ((COURSES[a][1] <= ROOMS["A"] and COURSES[b][1] <= ROOMS["B"]) or
            (COURSES[b][1] <= ROOMS["A"] and COURSES[a][1] <= ROOMS["B"]))

def assign_rooms(courses):
    if len(courses) == 1:
        c = courses[0]
        return {c: "A" if COURSES[c][1] > ROOMS["B"] else "B"}
    if len(courses) == 2:
        a, b = courses
        if COURSES[a][1] <= ROOMS["A"] and COURSES[b][1] <= ROOMS["B"]:
            return {a: "A", b: "B"}
        if COURSES[b][1] <= ROOMS["A"] and COURSES[a][1] <= ROOMS["B"]:
            return {b: "A", a: "B"}
    return {}

def ordered_courses():
    # DSATUR-inspired static order: degree descending, then registration count.
    return sorted(COURSES, key=lambda c: (-len(ADJ[c]), -COURSES[c][1], c))

def backtracking_four_slots(show_trace=True):
    order = ordered_courses()
    slot_courses = [[] for _ in SLOTS]
    assignment = {}
    metrics = {"nodes": 0, "attempts": 0, "clash_rejects": 0,
               "room_rejects": 0, "backtracks": 0}
    trace = []

    def search(i):
        metrics["nodes"] += 1
        if i == len(order):
            return True
        c = order[i]
        for s in range(4):
            metrics["attempts"] += 1
            clash_with = [x for x in slot_courses[s] if x in ADJ[c]]
            if clash_with:
                metrics["clash_rejects"] += 1
                trace.append(f"Reject {c} in {SLOTS[s]}: clashes with {', '.join(clash_with)}")
                continue
            if len(slot_courses[s]) >= 2:
                metrics["room_rejects"] += 1
                trace.append(f"Reject {c} in {SLOTS[s]}: both halls already occupied")
                continue
            if not room_pair_possible(slot_courses[s] + [c]):
                metrics["room_rejects"] += 1
                trace.append(f"Reject {c} in {SLOTS[s]}: no distinct room assignment meets capacity")
                continue
            trace.append(f"Choose {c} -> {SLOTS[s]}")
            assignment[c] = s
            slot_courses[s].append(c)
            if search(i + 1):
                return True
            slot_courses[s].pop()
            del assignment[c]
            metrics["backtracks"] += 1
            trace.append(f"Backtrack: undo {c} from {SLOTS[s]}")
        return False

    found = search(0)
    if show_trace:
        print("\n=== BACKTRACKING SEARCH TRACE ===")
        for line in trace:
            print(line)
        print("Search metrics:", metrics)
    return found, assignment, slot_courses, metrics

def print_timetable(slot_courses, heading):
    print("\n" + heading)
    for i, courses in enumerate(slot_courses):
        print(SLOTS[i] + ":")
        if not courses:
            print("  (empty)")
            continue
        rooms = assign_rooms(courses)
        for c in courses:
            print(f"  Hall {rooms[c]} | {c} | {COURSES[c][0]} | {COURSES[c][1]} students")

def same_day_penalty(assignment):
    return sum(1 for a, b in EDGES if assignment[a] // 2 == assignment[b] // 2)

def exact_branch_and_bound():
    """Enumerate feasible 4-slot assignments and minimise same-day clash edges."""
    order = ordered_courses()
    current = {}
    groups = [[] for _ in SLOTS]
    best_cost = float("inf")
    best_assignment = None
    nodes = 0
    prunes = 0

    def lower_bound():
        # Count already determined clash edges whose endpoints share a day.
        return sum(1 for a, b in EDGES
                   if a in current and b in current
                   and current[a] // 2 == current[b] // 2)

    def recurse(i):
        nonlocal best_cost, best_assignment, nodes, prunes
        nodes += 1
        if lower_bound() >= best_cost:
            prunes += 1
            return
        if i == len(order):
            cost = same_day_penalty(current)
            if cost < best_cost:
                best_cost = cost
                best_assignment = dict(current)
            return
        c = order[i]
        # Slot order is deterministic; try all feasible slots.
        for s in range(4):
            if len(groups[s]) >= 2:
                continue
            if any(x in ADJ[c] for x in groups[s]):
                continue
            if not room_pair_possible(groups[s] + [c]):
                continue
            current[c] = s
            groups[s].append(c)
            recurse(i + 1)
            groups[s].pop()
            del current[c]

    recurse(0)
    result_groups = [[] for _ in SLOTS]
    for c, s in best_assignment.items():
        result_groups[s].append(c)
    return best_cost, best_assignment, result_groups, nodes, prunes

def main():
    print("CSA06 CO5 – Examination Timetabling")
    print("Courses:", len(COURSES), "| slots:", len(SLOTS), "| halls per slot:", len(ROOMS))
    print("Clash edges:", len(EDGES), "| search order:", ordered_courses())
    print("\nNecessary checks:")
    print("- Maximum hall capacity is 160; all courses fit Hall A.")
    print("- C5 has 150 students, so it cannot use Hall B (capacity 120).")
    print("- At most 2 exams can run in one slot because there are 2 halls.")
    print("- Three slots can host at most 3 x 2 = 6 exams, fewer than 8: impossible.")
    print("- C1, C2, C3 form a 3-course clique, so at least 3 distinct slots are needed by clashes.")
    found, assignment, groups, metrics = backtracking_four_slots()
    print("\nFour-slot feasible:", found)
    if found:
        print_timetable(groups, "=== FEASIBLE FOUR-SLOT TIMETABLE ===")
        print("Every course scheduled exactly once:", len(assignment) == len(COURSES))
    cost, best, best_groups, nodes, prunes = exact_branch_and_bound()
    print_timetable(best_groups, "=== BRANCH-AND-BOUND BEST TIMETABLE ===")
    print("Same-day clash penalty (number of clash edges on the same day):", cost)
    print("Exact search nodes:", nodes, "| bound prunes:", prunes)
    print("Day 1 courses:", [c for c in COURSES if best[c] // 2 == 0])
    print("Day 2 courses:", [c for c in COURSES if best[c] // 2 == 1])
    print("\nFull unconstrained slot-domain assignments: 4^8 =", 4**8)
    print("Room choices before constraints (2 halls per course): 2^8 =", 2**8)
    print("Naive combined assignment upper bound: 8^8 =", 8**8)
    print("Actual search is much smaller due to early clash, hall-count, capacity and bound pruning.")
    print("\nVerification:")
    ok = all(best[a] != best[b] for a, b in EDGES)
    ok &= all(len(g) <= 2 and room_pair_possible(g) for g in best_groups)
    ok &= len([c for g in best_groups for c in g]) == len(COURSES)
    print("No same-slot clash:", ok)
    print("Room capacity and one-exam-per-hall constraints:", all(
        room_pair_possible(g) for g in best_groups))
    print("Exactly-once scheduling:", sum(map(len, best_groups)) == len(COURSES))

if __name__ == "__main__":
    main()
