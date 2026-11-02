"""Lower-bound Binary Search: return the first order with a timestamp."""

def first_order_with_timestamp(orders, target):
    """
    orders must be sorted by timestamp.
    Each order is a (timestamp, order_id) tuple.
    Returns the first matching tuple, or None if no timestamp matches.
    """
    low, high = 0, len(orders)

    while low < high:
        middle = low + (high - low) // 2
        if orders[middle][0] < target:
            low = middle + 1
        else:
            high = middle

    if low < len(orders) and orders[low][0] == target:
        return orders[low]
    return None


if __name__ == "__main__":
    sorted_orders = [(101, "O4"), (102, "O2"), (102, "O5"),
                     (103, "O6"), (105, "O1"), (105, "O3")]
    print("First order at timestamp 102:",
          first_order_with_timestamp(sorted_orders, 102))
