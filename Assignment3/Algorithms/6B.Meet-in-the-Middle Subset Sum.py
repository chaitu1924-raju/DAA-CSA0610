```python
def generate_subset_sums(arr):
    result = [(0, [])]

    for value in arr:
        new_sums = []

        for current_sum, subset in result:
            new_sums.append((
                current_sum + value,
                subset + [value]
            ))

        result.extend(new_sums)

    return result


def meet_in_middle(arr, target):
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left_sums = generate_subset_sums(left)
    right_sums = generate_subset_sums(right)

    right_lookup = {}

    for current_sum, subset in right_sums:
        if current_sum not in right_lookup:
            right_lookup[current_sum] = subset

    for current_sum, subset in left_sums:
        required = target - current_sum

        if required in right_lookup:
            result = subset + right_lookup[required]

            return True, result

    return False, []


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))

    target = int(input("Enter target sum: "))

    found, subset = meet_in_middle(arr, target)

    if found:
        print("Subset Found:", subset)
        print("Subset Sum:", sum(subset))
    else:
        print("No subset found")
```
