import time


def brute_force_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)

    comparisons = 0
    matches = []

    if m == 0:
        return [0], comparisons

    if m > n:
        return matches, comparisons

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def run_test(name, text, pattern):
    start = time.perf_counter()
    matches, comparisons = brute_force_string_matching(text, pattern)
    elapsed = time.perf_counter() - start

    print("\nTest:", name)
    print("Text Length:", len(text))
    print("Pattern Length:", len(pattern))
    print("Match Positions:", matches)
    print("Character Comparisons:", comparisons)
    print("Execution Time:", round(elapsed, 8), "seconds")


if __name__ == "__main__":
    tests = [
        (
            "Early Mismatch",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "XYZ"
        ),
        (
            "Repeated Prefix",
            "A" * 100 + "B",
            "A" * 10 + "C"
        ),
        (
            "Multiple Matches",
            "ABABABABAB",
            "AB"
        )
    ]

    for name, text, pattern in tests:
        run_test(name, text, pattern)
