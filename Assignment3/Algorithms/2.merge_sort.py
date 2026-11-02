def merge(arr, left, mid, right):
left_array = arr[left:mid + 1]
right_array = arr[mid + 1:right + 1]

```
i = 0
j = 0
k = left

while i < len(left_array) and j < len(right_array):
    if left_array[i] <= right_array[j]:
        arr[k] = left_array[i]
        i += 1
    else:
        arr[k] = right_array[j]
        j += 1

    k += 1

while i < len(left_array):
    arr[k] = left_array[i]
    i += 1
    k += 1

while j < len(right_array):
    arr[k] = right_array[j]
    j += 1
    k += 1
```

def merge_sort(arr, left, right):
if left < right:
mid = (left + right) // 2

```
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, mid, right)
```

def main():
print("MERGE SORT")
print("-" * 40)

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

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted Array:", arr)

except ValueError:
    print("Please enter valid integers.")
```

if **name** == "**main**":
main()
