import random
import time
import csv

from max_min import (
    find_max_min_divide_conquer,
    find_max_min_independently
)


def binary_search_count(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = low + (high - low) // 2

        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons

        comparisons += 1

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def average_time(function, repetitions):
    total_time = 0

    for _ in range(repetitions):
        start = time.perf_counter()
        function()
        end = time.perf_counter()

        total_time += end - start

    return total_time / repetitions


def benchmark_max_min():
    sizes = [1000, 5000, 10000, 50000, 100000]
    repetitions = 5

    results = []

    print("\nMAX-MIN BENCHMARK")
    print("-" * 65)

    for n in sizes:
        data = [random.randint(1, 1000000) for _ in range(n)]

        dc_result = find_max_min_divide_conquer(data)
        independent_result = find_max_min_independently(data)

        dc_time = average_time(
            lambda: find_max_min_divide_conquer(data),
            repetitions
        )

        independent_time = average_time(
            lambda: find_max_min_independently(data),
            repetitions
        )

        if dc_result[:2] != independent_result[:2]:
            raise AssertionError("Max-Min results do not match")

        results.append([
            n,
            "Divide and Conquer",
            dc_result[2],
            dc_time
        ])

        results.append([
            n,
            "Independent Scan",
            independent_result[2],
            independent_time
        ])

        print("Input size:", n)
        print("D&C comparisons:", dc_result[2])
        print("Independent comparisons:", independent_result[2])
        print("D&C time:", dc_time)
        print("Independent time:", independent_time)
        print("-" * 65)

    with open("q1_max_min_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Input Size",
            "Algorithm",
            "Comparisons",
            "Average Time (seconds)"
        ])

        writer.writerows(results)


def benchmark_binary_search():
    sizes = [100, 1000, 5000, 10000, 50000, 100000]
    repetitions = 5

    results = []

    print("\nBINARY SEARCH BENCHMARK")
    print("-" * 65)

    for n in sizes:
        data = list(range(1, n + 1))

        successful_target = data[n // 2]
        unsuccessful_target = n + 1

        cases = [
            ("Successful", successful_target),
            ("Unsuccessful", unsuccessful_target)
        ]

        for case_name, target in cases:
            index, comparisons = binary_search_count(data, target)

            avg_time = average_time(
                lambda: binary_search_count(data, target),
                repetitions
            )

            if case_name == "Successful" and index == -1:
                raise AssertionError("Successful search failed")

            if case_name == "Unsuccessful" and index != -1:
                raise AssertionError("Unsuccessful search returned an index")

            results.append([
                n,
                case_name,
                comparisons,
                avg_time
            ])

            print("Input size:", n)
            print("Case:", case_name)
            print("Comparisons:", comparisons)
            print("Average time:", avg_time)
            print("-" * 65)

    with open("q1_binary_search_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Input Size",
            "Search Case",
            "Comparisons",
            "Average Time (seconds)"
        ])

        writer.writerows(results)


if __name__ == "__main__":
    benchmark_max_min()
    benchmark_binary_search()

    print("\nBenchmark completed successfully.")
    print("CSV files generated.")
