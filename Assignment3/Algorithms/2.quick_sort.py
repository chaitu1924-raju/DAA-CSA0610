def quick_sort(arr, low, high, depth, stats):
stats["max_depth"] = max(stats["max_depth"], depth)

```
if low < high:
    pivot_index = partition(arr, low, high)

    left_size = pivot_index - low
    right_size = high - pivot_index

    stats["partitions"].append({
        "pivot": arr[pivot_index],
        "left_size": left_size,
        "right_size": right_size,
        "depth": depth
    })

    quick_sort(
        arr, low, pivot_index - 1,
        depth + 1, stats
    )

    quick_sort(
        arr, pivot_index + 1, high,
        depth + 1, stats
    )
```

def partition(arr, low, high):
pivot = arr[high]
i = low - 1

```
for j in range(low, high):
    if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

arr[i + 1], arr[high] = arr[high], arr[i + 1]

return i + 1
```

def run_quick_sort(arr):
stats = {
"partitions": [],
"max_depth": 0
}

```
quick_sort(arr, 0, len(arr) - 1, 1, stats)

return arr, stats
```

def main():
print("QUICK SORT - PARTITION ANALYSIS")
print("-" * 50)

```
try:
    arr = list(map(
        int,
        input("Enter array elements: ").split()
    ))

    if not arr:
        print("Please enter at least one element.")
        return

    print("\nOriginal Array:", arr)

    sorted_arr, stats = run_quick_sort(arr)

    print("Sorted Array:", sorted_arr)

    print("\nPARTITION DETAILS")
    print("-" * 50)

    for i, partition_info in enumerate(
        stats["partitions"], start=1
    ):
        print(
            "Partition", i,
            "| Pivot:", partition_info["pivot"],
            "| Left:", partition_info["left_size"],
            "| Right:", partition_info["right_size"],
            "| Depth:", partition_info["depth"]
        )

    print("\nMaximum Recursion Depth:",
          stats["max_depth"])

    print("Total Partitions:",
          len(stats["partitions"]))

except ValueError:
    print("Please enter valid integers.")
```

if **name** == "**main**":
main()
