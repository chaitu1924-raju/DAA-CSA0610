import math
import random
import time


def brute_force_closest_pair(points):
    n = len(points)

    if n < 2:
        return None, None, 0, 0

    min_distance = float("inf")
    closest_pair = None

    pairs_examined = 0
    distance_calculations = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            pairs_examined += 1

            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = math.sqrt(
                (x2 - x1) ** 2 + (y2 - y1) ** 2
            )

            distance_calculations += 1

            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return (
        closest_pair,
        min_distance,
        pairs_examined,
        distance_calculations
    )


def run_test(size):
    points = [
        (random.randint(0, 100000), random.randint(0, 100000))
        for _ in range(size)
    ]

    start = time.perf_counter()

    pair, distance, pairs, calculations = (
        brute_force_closest_pair(points)
    )

    elapsed = time.perf_counter() - start

    print("\nNumber of Points:", size)
    print("Closest Pair:", pair)
    print("Minimum Distance:", distance)
    print("Pairs Examined:", pairs)
    print("Distance Calculations:", calculations)
    print("Expected Unique Pairs:", size * (size - 1) // 2)
    print("Execution Time:", round(elapsed, 8), "seconds")


if __name__ == "__main__":
    random.seed(42)

    for size in [10, 100, 500, 1000]:
        run_test(size)
