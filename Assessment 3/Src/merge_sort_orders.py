"""Stable Merge Sort for orders represented as (timestamp, order_id) tuples."""

def merge_sort_orders(orders):
    """Return orders sorted by timestamp, preserving arrival order for equal timestamps."""
    if len(orders) <= 1:
        return list(orders)

    middle = len(orders) // 2
    left = merge_sort_orders(orders[:middle])
    right = merge_sort_orders(orders[middle:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        # <= is important: equal timestamps are taken from the left half first.
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    sample = [(105, "O1"), (102, "O2"), (105, "O3"),
              (101, "O4"), (102, "O5"), (103, "O6")]
    print("Sorted orders:", merge_sort_orders(sample))
