```python
import math


def squared_distance(p1, p2):
    return (
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def closest_pair_recursive(points_x, points_y):
    n = len(points_x)

    if n <= 3:
        minimum = float("inf")
        closest = None
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                d = squared_distance(points_x[i], points_x[j])
                count += 1

                if d < minimum:
                    minimum = d
                    closest = (points_x[i], points_x[j])

        return minimum, closest, count

    mid = n // 2
    mid_point = points_x[mid]

    left_x = points_x[:mid]
    right_x = points_x[mid:]

    left_set = set(left_x)

    left_y = []
    right_y = []

    for point in points_y:
        if point in left_set:
            left_y.append(point)
        else:
            right_y.append(point)

    left_distance, left_pair, left_count = closest_pair_recursive(
        left_x, left_y
    )

    right_distance, right_pair, right_count = closest_pair_recursive(
        right_x, right_y
    )

    if left_distance <= right_distance:
        minimum = left_distance
        closest = left_pair
    else:
        minimum = right_distance
        closest = right_pair

    count = left_count + right_count

    strip = []

    for point in points_y:
        if (point[0] - mid_point[0]) ** 2 < minimum:
            strip.append(point)

    for i in range(len(strip)):
        j = i + 1

        while j < len(strip):
            if (strip[j][1] - strip[i][1]) ** 2 >= minimum:
                break

            d = squared_distance(strip[i], strip[j])
            count += 1

            if d < minimum:
                minimum = d
                closest = (strip[i], strip[j])

            j += 1

    return minimum, closest, count


def divide_conquer_closest_pair(points):
    if len(points) < 2:
        raise ValueError("At least two points are required")

    points_x = sorted(points, key=lambda p: (p[0], p[1]))
    points_y = sorted(points, key=lambda p: (p[1], p[0]))

    minimum, pair, count = closest_pair_recursive(
        points_x, points_y
    )

    return pair, math.sqrt(minimum), count


if __name__ == "__main__":
    n = int(input("Enter number of points: "))

    points = []

    print("Enter x and y coordinates:")

    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    pair, minimum_distance, count = divide_conquer_closest_pair(points)

    print("Closest Pair:", pair)
    print("Minimum Distance:", minimum_distance)
    print("Distance Calculations:", count)
```
