import math

def sort_alerts(alerts):
    """Sort alerts in descending order by their second field."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1

        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1

        alerts[j + 1] = key

    return alerts

def is_blocked(blocklist, ip):
    """Return whether the IP is present in the blocklist."""
    for i in range(len(blocklist)):
        if blocklist[i] == ip:
            return True
    return False

def find_signature(log, pattern):
    """Return all starting indices where pattern occurs in log."""
    n, m = len(log), len(pattern)
    hits = []

    if m == 0:
        return list(range(n + 1))

    for i in range(n - m + 1):
        for j in range(m):
            if log[i + j] != pattern[j]:
                break
        else:
            hits.append(i)

    return hits


def closest_logins(events):
    """Return the indices and distance of the closest pair of events."""
    min_dist = math.inf
    pair = None

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            d = math.sqrt(
                (events[i][0] - events[j][0]) ** 2
                + (events[i][1] - events[j][1]) ** 2
            )

            if d < min_dist:
                min_dist = d
                pair = (i, j)

    return pair, min_dist

