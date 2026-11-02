import csv
import os
import random
import time
import statistics

# --------------------------------------------------
# Configuration
# --------------------------------------------------

RESULTS_DIR = "../results"
os.makedirs(RESULTS_DIR, exist_ok=True)

CSV_FILE = os.path.join(RESULTS_DIR, "benchmark_results.csv")

INPUT_SIZES = [100, 500, 1000, 2000, 5000]
REPETITIONS = 5

random.seed(42)


# --------------------------------------------------
# Reference Sorting Algorithms
# Replace these with your submitted implementations
# when we verify their function names.
# --------------------------------------------------

def bubble_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --------------------------------------------------
# Reference Sequential Search
# --------------------------------------------------

def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1


# --------------------------------------------------
# Timing Function
# --------------------------------------------------

def measure_time(function, *args):
    start = time.perf_counter()
    function(*args)
    end = time.perf_counter()

    return end - start


# --------------------------------------------------
# Benchmark Sorting Algorithms
# --------------------------------------------------

def benchmark_sorting():

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort
    }

    rows = []

    for size in INPUT_SIZES:

        original_data = [
            random.randint(0, 100000)
            for _ in range(size)
        ]

        for name, algorithm in algorithms.items():

            timings = []

            for _ in range(REPETITIONS):
                elapsed = measure_time(
                    algorithm,
                    original_data
                )

                timings.append(elapsed)

            average_time = statistics.mean(timings)

            rows.append({
                "Experiment": "Sorting",
                "Algorithm": name,
                "Input_Size": size,
                "Average_Time_Seconds": average_time
            })

            print(
                "Sorting |",
                name,
                "| Size:",
                size,
                "| Average:",
                round(average_time, 6),
                "seconds"
            )

    return rows


# --------------------------------------------------
# Benchmark Sequential Search
# --------------------------------------------------

def benchmark_search():

    rows = []

    for size in INPUT_SIZES:

        data = list(range(size))

        # Search for the last element to measure
        # the worst-case successful search.
        target = size - 1

        timings = []

        for _ in range(REPETITIONS):

            elapsed = measure_time(
                sequential_search,
                data,
                target
            )

            timings.append(elapsed)

        average_time = statistics.mean(timings)

        rows.append({
            "Experiment": "Searching",
            "Algorithm": "Sequential Search",
            "Input_Size": size,
            "Average_Time_Seconds": average_time
        })

        print(
            "Searching | Sequential Search",
            "| Size:",
            size,
            "| Average:",
            round(average_time, 6),
            "seconds"
        )

    return rows


# --------------------------------------------------
# Save Results to CSV
# --------------------------------------------------

def save_results(rows):

    fieldnames = [
        "Experiment",
        "Algorithm",
        "Input_Size",
        "Average_Time_Seconds"
    ]

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)

    print("\nResults saved to:", CSV_FILE)


# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main():

    print("DAA Assignment 2 - Benchmark Experiments")
    print("-----------------------------------------")

    all_results = []

    all_results.extend(benchmark_sorting())
    all_results.extend(benchmark_search())

    save_results(all_results)

    print("\nAll experiments completed successfully.")


if __name__ == "__main__":
    main()

