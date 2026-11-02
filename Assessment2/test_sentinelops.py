import math
import random
import unittest

import sentinelops_debugged as debugged
import sentinelops_optimized as optimized


class SentinelOpsTests(unittest.TestCase):
    def test_sort_alerts(self):
        alerts = [
            ("A1", 3),
            ("A2", 9),
            ("A3", 5),
            ("A4", 9),
            ("A5", 1),
        ]
        expected = [
            ("A2", 9),
            ("A4", 9),
            ("A3", 5),
            ("A1", 3),
            ("A5", 1),
        ]

        self.assertEqual(debugged.sort_alerts(alerts), expected)
        self.assertEqual(optimized.sort_alerts(alerts), expected)

    def test_sort_empty_and_single_alert(self):
        self.assertEqual(debugged.sort_alerts([]), [])
        self.assertEqual(optimized.sort_alerts([]), [])

        alert = [("A1", 7)]
        self.assertEqual(debugged.sort_alerts(alert), alert)
        self.assertEqual(optimized.sort_alerts(alert), alert)

    def test_blocklist(self):
        blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]

        for ip in blocklist:
            self.assertTrue(debugged.is_blocked(blocklist, ip))

        self.assertFalse(debugged.is_blocked(blocklist, "8.8.8.8"))
        self.assertFalse(debugged.is_blocked([], "8.8.8.8"))

        blocked_set = optimized.prepare_blocklist(blocklist)
        for ip in blocklist:
            self.assertTrue(optimized.is_blocked(blocked_set, ip))

        self.assertFalse(optimized.is_blocked(blocked_set, "8.8.8.8"))
        empty_set = optimized.prepare_blocklist([])
        self.assertFalse(optimized.is_blocked(empty_set, "8.8.8.8"))

    def test_find_signature(self):
        log = "FAILFAIXFAIL"
        pattern = "FAIL"
        expected = [0, 8]

        self.assertEqual(debugged.find_signature(log, pattern), expected)
        self.assertEqual(optimized.find_signature(log, pattern), expected)

    def test_signature_at_final_position(self):
        self.assertEqual(debugged.find_signature("ABCD", "BCD"), [1])
        self.assertEqual(optimized.find_signature("ABCD", "BCD"), [1])

    def test_signature_overlapping_matches(self):
        expected = [0, 1, 2]
        self.assertEqual(debugged.find_signature("AAAAA", "AAA"), expected)
        self.assertEqual(optimized.find_signature("AAAAA", "AAA"), expected)

    def test_signature_boundary_cases(self):
        for implementation in (debugged.find_signature, optimized.find_signature):
            self.assertEqual(implementation("", "A"), [])
            self.assertEqual(implementation("ABC", "ABCDE"), [])
            self.assertEqual(implementation("", ""), [0])
            self.assertEqual(implementation("ABC", ""), [0, 1, 2, 3])

    def test_closest_pair_example(self):
        events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        expected_pair = (0, 5)
        expected_distance = math.sqrt(2)

        for implementation in (debugged.closest_logins, optimized.closest_logins):
            pair, distance = implementation(events)
            self.assertEqual(pair, expected_pair)
            self.assertAlmostEqual(distance, expected_distance)

    def test_closest_pair_small_inputs(self):
        for implementation in (debugged.closest_logins, optimized.closest_logins):
            self.assertEqual(implementation([]), (None, None))
            self.assertEqual(implementation([(1, 2)]), (None, None))

            pair, distance = implementation([(0, 0), (3, 4)])
            self.assertEqual(pair, (0, 1))
            self.assertAlmostEqual(distance, 5.0)

    def test_closest_pair_duplicate_coordinates(self):
        events = [(0, 0), (5, 5), (0, 0)]

        for implementation in (debugged.closest_logins, optimized.closest_logins):
            pair, distance = implementation(events)
            self.assertEqual(pair, (0, 2))
            self.assertEqual(distance, 0.0)

    def test_closest_pair_randomized(self):
        rng = random.Random(42)

        for size in range(2, 35):
            events = [
                (rng.randint(-100, 100), rng.randint(-100, 100))
                for _ in range(size)
            ]
            baseline_pair, baseline_distance = debugged.closest_logins(events)
            optimized_pair, optimized_distance = optimized.closest_logins(events)

            self.assertEqual(optimized_pair, baseline_pair)
            self.assertAlmostEqual(optimized_distance, baseline_distance)


if __name__ == "__main__":
    unittest.main()
