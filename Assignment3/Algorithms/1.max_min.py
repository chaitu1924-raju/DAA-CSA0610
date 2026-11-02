def max_min_divide_conquer(arr, low, high, counter):
if low == high:
return arr[low], arr[low]

```
if high == low + 1:
    counter["comparisons"] += 1

    if arr[low] < arr[high]:
        return arr[high], arr[low]

    return arr[low], arr[high]

mid = (low + high) // 2

max1, min1 = max_min_divide_conquer(arr, low, mid, counter)
max2, min2 = max_min_divide_conquer(arr, mid + 1, high, counter)

counter["comparisons"] += 1
maximum = max1 if max1 > max2 else max2

counter["comparisons"] += 1
minimum = min1 if min1 < min2 else min2

return maximum, minimum
```

def find_max_min_divide_conquer(arr):
if not arr:
raise ValueError("Array must not be empty.")

```
counter = {"comparisons": 0}

maximum, minimum = max_min_divide_conquer(
    arr, 0, len(arr) - 1, counter
)

return maximum, minimum, counter["comparisons"]
```

def find_max_min_independently(arr):
if not arr:
raise ValueError("Array must not be empty.")

```
maximum = arr[0]
minimum = arr[0]
comparisons = 0

for i in range(1, len(arr)):
    comparisons += 1
    if arr[i] > maximum:
        maximum = arr[i]

    comparisons += 1
    if arr[i] < minimum:
        minimum = arr[i]

return maximum, minimum, comparisons
```

def main():
print("DIVIDE AND CONQUER: MAXIMUM AND MINIMUM")
print("-" * 50)

```
try:
    arr = list(map(
        int,
        input("Enter array elements separated by spaces: ").split()
    ))

    if not arr:
        print("Error: Please enter at least one element.")
        return

    maximum, minimum, dc_comparisons = find_max_min_divide_conquer(arr)

    max2, min2, independent_comparisons = (
        find_max_min_independently(arr)
    )

    print("\nInput array:", arr)

    print("\nDivide-and-Conquer Results")
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Element comparisons:", dc_comparisons)

    print("\nIndependent Scan Results")
    print("Maximum:", max2)
    print("Minimum:", min2)
    print("Element comparisons:", independent_comparisons)

    print("\nComparison Summary")
    print("Divide and Conquer:", dc_comparisons)
    print("Independent Scan:", independent_comparisons)

    if dc_comparisons < independent_comparisons:
        print("Divide and Conquer used fewer comparisons.")
    elif dc_comparisons > independent_comparisons:
        print("Independent scanning used fewer comparisons.")
    else:
        print("Both methods used the same number of comparisons.")

except ValueError as error:
    print("Error:", error)
```

if **name** == "**main**":
main()
