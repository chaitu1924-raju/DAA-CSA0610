import matplotlib.pyplot as plt


def cross_product(a, b, c):
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


def brute_force_convex_hull(points):
    n = len(points)

    if n <= 1:
        return list(points), 0

    # Duplicate coordinates are not needed for the hull.
    points = sorted(set(points))
    n = len(points)

    if n <= 1:
        return points, 0

    hull_edges = set()
    geometric_tests = 0

    for i in range(n):
        for j in range(i + 1, n):
            positive = False
            negative = False

            for k in range(n):
                if k == i or k == j:
                    continue

                geometric_tests += 1

                value = cross_product(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

                if positive and negative:
                    break

            if not (positive and negative):
                hull_edges.add((points[i], points[j]))

    # Collect vertices belonging to accepted hull edges.
    hull_points = set()

    for a, b in hull_edges:
        hull_points.add(a)
        hull_points.add(b)

    # Sort boundary vertices around their centroid.
    hull_points = list(hull_points)

    if len(hull_points) < 3:
        return sorted(hull_points), geometric_tests

    center_x = sum(p[0] for p in hull_points) / len(hull_points)
    center_y = sum(p[1] for p in hull_points) / len(hull_points)

    hull_points.sort(
        key=lambda p: __import__("math").atan2(
            p[1] - center_y,
            p[0] - center_x,
        )
    )

    return hull_points, geometric_tests


def visualize_hull(points, hull):
    plt.figure()

    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]

    plt.scatter(x_values, y_values, label="Input Points")

    if hull:
        closed_hull = hull + [hull[0]]

        hull_x = [p[0] for p in closed_hull]
        hull_y = [p[1] for p in closed_hull]

        plt.plot(hull_x, hull_y, marker="o", label="Convex Hull")

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Brute-Force Convex Hull")
    plt.legend()
    plt.grid(True)
    plt.savefig("convex_hull_visualization.png")
    plt.show()


if __name__ == "__main__":
    points = [
        (0, 0),
        (4, 0),
        (5, 3),
        (2, 5),
        (-1, 3),
        (2, 2),
        (1, 1),
        (3, 2),
    ]

    hull, tests = brute_force_convex_hull(points)

    print("Input Points:", points)
    print("Hull Vertices:", hull)
    print("Geometric Tests:", tests)

    visualize_hull(points, hull)
