import random
import time


def selection_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps


def bubble_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps


def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                movements += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        movements += 1

    return arr, comparisons, movements


def run_test(name, data):
    print("\nDataset:", name)
    print("Input:", data)

    algorithms = [
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort)
    ]

    for algorithm_name, algorithm in algorithms:
        start = time.perf_counter()
        result, comparisons, operations = algorithm(data)
        elapsed = time.perf_counter() - start

        print("\nAlgorithm:", algorithm_name)
        print("Sorted Output:", result)
        print("Comparisons:", comparisons)
        print("Swaps/Movements:", operations)
        print("Execution Time:", round(elapsed, 8), "seconds")


if __name__ == "__main__":
    datasets = {
        "Already Sorted": [1, 2, 3, 4, 5, 6],
        "Reverse Sorted": [6, 5, 4, 3, 2, 1],
        "Nearly Sorted": [1, 2, 4, 3, 5, 6],
        "Random Order": random.sample(range(1, 101), 10),
        "Edge Case - Duplicates": [4, 2, 4, 1, 2, 1]
    }

    for name, data in datasets.items():
        run_test(name, data)
