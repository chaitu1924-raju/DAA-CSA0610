import time


def sequential_search(data, target):
    comparisons = 0

    for index, value in enumerate(data):
        comparisons += 1

        if value == target:
            return index, comparisons

    return -1, comparisons


def run_experiment(size):
    tools = ["T-" + str(i) for i in range(size)]

    test_cases = [
        ("First Position", "T-0"),
        ("Middle Position", "T-" + str(size // 2)),
        ("Last Position", "T-" + str(size - 1)),
        ("Unsuccessful Search", "T-MISSING")
    ]

    print("\nDataset Size:", size)

    for name, target in test_cases:
        start = time.perf_counter()
        index, comparisons = sequential_search(tools, target)
        elapsed = time.perf_counter() - start

        print("\nTest:", name)
        print("Target:", target)
        print("Result Index:", index)
        print("Comparisons:", comparisons)
        print("Execution Time:", round(elapsed, 8), "seconds")


if __name__ == "__main__":
    for size in [10, 100, 1000, 10000]:
        run_experiment(size)

