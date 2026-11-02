```python
def median_of_medians(arr):
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    medians = []

    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group) // 2])

    return deterministic_select(
        medians,
        (len(medians) + 1) // 2
    )


def deterministic_select(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("Invalid k value")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    pivot = median_of_medians(arr)

    smaller = []
    equal = []
    larger = []

    for value in arr:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    if k <= len(smaller):
        return deterministic_select(smaller, k)

    elif k <= len(smaller) + len(equal):
        return pivot

    else:
        new_k = k - len(smaller) - len(equal)

        return deterministic_select(larger, new_k)


def quickselect(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("Invalid k value")

    arr = arr.copy()

    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot = arr[high]

        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]

        position = i - low + 1

        if position == k:
            return arr[i]

        elif position > k:
            high = i - 1

        else:
            k -= position
            low = i + 1

    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))

    k = int(input("Enter k (1-based position): "))

    if not arr:
        print("Array cannot be empty")

    elif k < 1 or k > len(arr):
        print("Invalid k value")

    else:
        result1 = deterministic_select(arr, k)
        result2 = quickselect(arr, k)

        print("Median of Medians result:", result1)
        print("QuickSelect result:", result2)
```
