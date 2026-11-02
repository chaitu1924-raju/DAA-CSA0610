"""Median-of-three, three-way Quick Sort for seller scores."""

def median_of_three(values, low, high):
    middle = (low + high) // 2
    trio = [values[low], values[middle], values[high]]
    trio.sort()
    return trio[1]


def quick_sort_scores(scores):
    """Return a sorted copy. Uses median-of-three pivot and 3-way partitioning."""
    values = list(scores)

    def sort(low, high):
        while low < high:
            pivot = median_of_three(values, low, high)
            lt, i, gt = low, low, high

            # Dutch-national-flag partition: < pivot | == pivot | > pivot
            while i <= gt:
                if values[i] < pivot:
                    values[lt], values[i] = values[i], values[lt]
                    lt += 1
                    i += 1
                elif values[i] > pivot:
                    values[i], values[gt] = values[gt], values[i]
                    gt -= 1
                else:
                    i += 1

            # Recurse on the smaller side; loop over the larger side to
            # limit recursion depth on unbalanced partitions.
            if (lt - low) < (high - gt):
                sort(low, lt - 1)
                low = gt + 1
            else:
                sort(gt + 1, high)
                high = lt - 1

    if values:
        sort(0, len(values) - 1)
    return values


if __name__ == "__main__":
    sample = [42, 17, 63, 8, 55, 29]
    print("Sorted seller scores:", quick_sort_scores(sample))
