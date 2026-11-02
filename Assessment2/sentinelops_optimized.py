import math


def sort_alerts(alerts):
    """Sort alerts by descending severity using Python's stable sort.

    Alerts with equal severity retain their original order.
    """
    return sorted(alerts, key=lambda alert: alert[1], reverse=True)


def prepare_blocklist(blocklist):
    """Build a set for repeated blocklist membership queries."""
    return set(blocklist)


def is_blocked(blocklist_set, ip):
    """Check blocklist membership using a set (average O(1) lookup)."""
    return ip in blocklist_set


def find_signature(log, pattern):
    """Find all pattern occurrences with brute-force matching.

    Overlapping matches are included. An empty pattern matches every
    boundary position.
    """
    n = len(log)
    m = len(pattern)
    hits = []

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return hits

    for i in range(n - m + 1):
        j = 0
        while j < m and log[i + j] == pattern[j]:
            j += 1
        if j == m:
            hits.append(i)

    return hits


def closest_logins(events):
    """Find the closest event pair using divide and conquer.

    Events are (x, y) coordinates. Returns ((i, j), distance), preserving
    original indices and resolving equal-distance ties deterministically.
    Returns (None, None) when fewer than two events are supplied.
    """
    points = [(x, y, index) for index, (x, y) in enumerate(events)]
    if len(points) < 2:
        return None, None

    points_x = sorted(points, key=lambda point: (point[0], point[1], point[2]))
    points_y = sorted(points, key=lambda point: (point[1], point[0], point[2]))

    def squared_distance(p, q):
        dx = p[0] - q[0]
        dy = p[1] - q[1]
        return dx * dx + dy * dy

    def brute_force(points_subset):
        """Solve small subsets directly."""
        best_distance = math.inf
        best_pair = None

        for i in range(len(points_subset) - 1):
            for j in range(i + 1, len(points_subset)):
                p = points_subset[i]
                q = points_subset[j]
                distance = squared_distance(p, q)
                pair = tuple(sorted((p[2], q[2])))

                if (distance < best_distance or
                        (distance == best_distance and
                         (best_pair is None or pair < best_pair))):
                    best_distance = distance
                    best_pair = pair

        return best_distance, best_pair

    def closest_recursive(px, py):
        """Return the closest squared distance and original indices."""
        n = len(px)
        if n <= 3:
            return brute_force(px)

        mid = n // 2
        left_x = px[:mid]
        right_x = px[mid:]
        dividing_x = right_x[0][0]
        left_ids = {point[2] for point in left_x}

        left_y = [point for point in py if point[2] in left_ids]
        right_y = [point for point in py if point[2] not in left_ids]

        left_distance, left_pair = closest_recursive(left_x, left_y)
        right_distance, right_pair = closest_recursive(right_x, right_y)

        if (left_distance < right_distance or
                (left_distance == right_distance and left_pair is not None and
                 (right_pair is None or left_pair < right_pair))):
            best_distance = left_distance
            best_pair = left_pair
        else:
            best_distance = right_distance
            best_pair = right_pair

        strip = [point for point in py
                 if (point[0] - dividing_x) ** 2 <= best_distance]

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip):
                dy = strip[j][1] - strip[i][1]
                if dy * dy > best_distance:
                    break

                p = strip[i]
                q = strip[j]
                distance = squared_distance(p, q)
                pair = tuple(sorted((p[2], q[2])))

                if (distance < best_distance or
                        (distance == best_distance and
                         (best_pair is None or pair < best_pair))):
                    best_distance = distance
                    best_pair = pair
                j += 1

        return best_distance, best_pair

    best_squared, best_pair = closest_recursive(points_x, points_y)
    return best_pair, math.sqrt(best_squared)
