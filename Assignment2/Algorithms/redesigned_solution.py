import math
import random
import time

def brute_force(points):
    if len(points) < 2:
        return float("inf"), 0

    best = float("inf")
    comparisons = 0

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            comparisons += 1

            distance = math.dist(points[i], points[j])
            best = min(best, distance)

    return best, comparisons

def closest_pair_divide_conquer(points):
    if len(points) < 2:
        return float("inf"), 0

    comparisons = [0]

    def distance(a, b):
        return math.dist(a, b)

    def solve(px, py):
        n = len(px)

        if n <= 3:
            best = float("inf")

            for i in range(n - 1):
                for j in range(i + 1, n):
                    comparisons[0] += 1
                    best = min(best, distance(px[i], px[j]))

            return best

        mid = n // 2
        left_x = px[:mid]
        right_x = px[mid:]

        split_x = px[mid][0]

        left_set = set(left_x)

        left_y = []
        right_y = []

        for point in py:
            if point in left_set:
                left_y.append(point)
            else:
                right_y.append(point)

        delta = min(
            solve(left_x, left_y),
            solve(right_x, right_y)
        )

        strip = [
            point for point in py
            if abs(point[0] - split_x) < delta
        ]

        for i in range(len(strip)):
            j = i + 1

            while (
                j < len(strip)
                and strip[j][1] - strip[i][1] < delta
            ):
                comparisons[0] += 1

                delta = min(
                    delta,
                    distance(strip[i], strip[j])
                )

                j += 1

        return delta

    px = sorted(points)
    py = sorted(points, key=lambda p: (p[1], p[0]))

    result = solve(px, py)

    return result, comparisons[0]

def run_comparison(size):
    random.seed(100 + size)

    points = [
        (random.random() * 10000, random.random() * 10000)
        for _ in range(size)
    ]

    start = time.perf_counter()
    original_distance, original_operations = brute_force(points)
    original_time = time.perf_counter() - start

    start = time.perf_counter()
    revised_distance, revised_operations = (
        closest_pair_divide_conquer(points)
    )
    revised_time = time.perf_counter() - start

    print("\nInput Size:", size)

    print("\nOriginal Brute-Force Solution")
    print("Minimum Distance:", original_distance)
    print("Distance Calculations:", original_operations)
    print("Execution Time:", round(original_time, 8), "seconds")

    print("\nRedesigned Divide-and-Conquer Solution")
    print("Minimum Distance:", revised_distance)
    print("Distance Calculations:", revised_operations)
    print("Execution Time:", round(revised_time, 8), "seconds")

    print(
        "Results Match:",
        math.isclose(
            original_distance,
            revised_distance,
            rel_tol=1e-9,
            abs_tol=1e-9
        )
    )

if __name__ == "__main__":
    for size in [10, 100, 500, 1000]:
        run_comparison(size)

