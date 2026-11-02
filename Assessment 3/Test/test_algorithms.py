import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from merge_sort_orders import merge_sort_orders
from quick_sort_leaderboard import quick_sort_scores
from binary_search_orders import first_order_with_timestamp
from strassen_matrix import strassen_multiply, standard_multiply


class TestKartIQAlgorithms(unittest.TestCase):
    def test_merge_sort_and_stability(self):
        orders = [(105, "O1"), (102, "O2"), (105, "O3"),
                  (101, "O4"), (102, "O5"), (103, "O6")]
        expected = [(101, "O4"), (102, "O2"), (102, "O5"),
                    (103, "O6"), (105, "O1"), (105, "O3")]
        self.assertEqual(merge_sort_orders(orders), expected)

    def test_quick_sort_sample_and_duplicates(self):
        self.assertEqual(quick_sort_scores([42, 17, 63, 8, 55, 29]),
                         [8, 17, 29, 42, 55, 63])
        self.assertEqual(quick_sort_scores([3, 1, 3, 2, 3, 1]),
                         [1, 1, 2, 3, 3, 3])

    def test_binary_search_first_duplicate(self):
        orders = [(101, "O4"), (102, "O2"), (102, "O5"),
                  (103, "O6"), (105, "O1"), (105, "O3")]
        self.assertEqual(first_order_with_timestamp(orders, 102), (102, "O2"))
        self.assertIsNone(first_order_with_timestamp(orders, 999))

    def test_strassen_sample(self):
        a = [[1, 7], [3, 5]]
        b = [[1, 3], [7, 5]]
        self.assertEqual(strassen_multiply(a, b, cutoff=1),
                         [[50, 38], [38, 34]])

    def test_strassen_non_power_of_two(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        self.assertEqual(strassen_multiply(a, b, cutoff=1),
                         standard_multiply(a, b))


if __name__ == "__main__":
    unittest.main()
