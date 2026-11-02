import time


def exhaustive_package_selection(packages, capacity):
    n = len(packages)

    best_value = 0
    best_weight = 0
    best_selection = []

    candidates_examined = 0
    feasible_candidates = 0

    for mask in range(1 << len(packages)):
        candidates_examined += 1

        total_weight = 0
        total_value = 0
        selected = []

        for i in range(n):
            if mask & (1 << i):
                package_id, weight, value = packages[i]

                total_weight += weight
                total_value += value
                selected.append(package_id)

        if total_weight <= capacity:
            feasible_candidates += 1

            if total_value > best_value:
                best_value = total_value
                best_weight = total_weight
                best_selection = selected

    return (
        best_selection,
        best_weight,
        best_value,
        candidates_examined,
        feasible_candidates
    )


def run_test(packages, capacity):
    start = time.perf_counter()

    result = exhaustive_package_selection(
        packages,
        capacity
    )

    elapsed = time.perf_counter() - start

    selected, weight, value, candidates, feasible = result

    print("\nNumber of Packages:", len(packages))
    print("Payload Capacity:", capacity)
    print("Selected Packages:", selected)
    print("Total Weight:", weight)
    print("Total Value:", value)
    print("Candidate Combinations:", candidates)
    print("Feasible Combinations:", feasible)
    print("Expected Combinations:", 2 ** len(packages))
    print("Execution Time:", round(elapsed, 8), "seconds")


if __name__ == "__main__":
    packages = [
        ("P1", 2, 30),
        ("P2", 3, 40),
        ("P3", 4, 50),
        ("P4", 5, 60),
        ("P5", 1, 15),
        ("P6", 6, 70),
        ("P7", 2, 25),
        ("P8", 3, 35)
    ]

    for size in [4, 6, 8]:
        run_test(packages[:size], capacity=10)
