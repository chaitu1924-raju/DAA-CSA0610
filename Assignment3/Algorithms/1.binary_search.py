def binary_search(arr, target):
low = 0
high = len(arr) - 1
comparisons = 0

```
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
```

def main():
print("BINARY SEARCH")
print("-" * 40)

```
try:
    arr = list(map(
        int,
        input("Enter sorted array elements: ").split()
    ))

    if not arr:
        print("Error: Please enter at least one element.")
        return

    if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        print("Error: The array must be sorted in ascending order.")
        return

    target = int(input("Enter the target element: "))

    index, comparisons = binary_search(arr, target)

    print("\nArray:", arr)
    print("Target:", target)

    if index != -1:
        print("Target found at index:", index)
    else:
        print("Target not found.")

    print("Element comparisons:", comparisons)

except ValueError:
    print("Error: Please enter valid integers.")
```

if **name** == "**main**":
main()
