```python
import math


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def brute_force_closest_pair(points):
    n = len(points)

    if n < 2:
        raise ValueError("At least two points are required")

    minimum_distance = float("inf")
    closest_pair = None
    distance_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            current_distance = distance(points[i], points[j])
            distance_count += 1

            if current_distance < minimum_distance:
                minimum_distance = current_distance
                closest_pair = (points[i], points[j])

    return closest_pair, minimum_distance, distance_count


if __name__ == "__main__":
    n = int(input("Enter number of points: "))

    points = []

    print("Enter x and y coordinates:")

    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    pair, minimum_distance, count = brute_force_closest_pair(points)

    print("Closest Pair:", pair)
    print("Minimum Distance:", minimum_distance)
    print("Distance Calculations:", count)
```
