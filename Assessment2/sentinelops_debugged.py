import math


def sort_alerts(alerts):
    """Sort alerts by descending severity using stable insertion sort.

    Each alert is represented as (alert_id, severity). Equal-severity alerts
    retain their original order.
    """
    alerts = alerts.copy()

    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1

        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1

        alerts[j + 1] = key

    return alerts


def is_blocked(blocklist, ip):
    """Return True if an IP address is in the blocklist using sequential search."""
    for blocked_ip in blocklist:
        if blocked_ip == ip:
            return True

    return False


def find_signature(log, pattern):
    """Return all starting indexes where pattern occurs in log.

    Overlapping matches are included. An empty pattern matches every boundary.
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
    """Find the closest pair of distinct login events using brute force.

    Returns ((i, j), distance), or (None, None) for fewer than two events.
    """
    n = len(events)

    if n < 2:
        return None, None

    best_squared = float("inf")
    best_pair = None

    for i in range(n - 1):
        for j in range(i + 1, n):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            squared_distance = dx * dx + dy * dy

            if squared_distance < best_squared:
                best_squared = squared_distance
                best_pair = (i, j)

    return best_pair, math.sqrt(best_squared)
