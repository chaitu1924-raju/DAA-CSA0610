"""Run all four KartIQ assessment demonstrations."""

from merge_sort_orders import merge_sort_orders
from quick_sort_leaderboard import quick_sort_scores
from binary_search_orders import first_order_with_timestamp
from strassen_matrix import strassen_multiply


def main():
    orders = [(105, "O1"), (102, "O2"), (105, "O3"),
              (101, "O4"), (102, "O5"), (103, "O6")]
    sorted_orders = merge_sort_orders(orders)
    print("MODULE 1 - Stable Merge Sort")
    print("Sorted orders:", sorted_orders)

    scores = [42, 17, 63, 8, 55, 29]
    print("\nMODULE 2 - Quick Sort")
    print("Sorted seller scores:", quick_sort_scores(scores))

    print("\nMODULE 3 - First-match Binary Search")
    print("First order at timestamp 102:",
          first_order_with_timestamp(sorted_orders, 102))
    print("Timestamp 999:", first_order_with_timestamp(sorted_orders, 999))

    print("\nMODULE 4 - Strassen Matrix Multiplication")
    A = [[1, 7], [3, 5]]
    B = [[1, 3], [7, 5]]
    print("A x B =", strassen_multiply(A, B, cutoff=1))


if __name__ == "__main__":
    main()
