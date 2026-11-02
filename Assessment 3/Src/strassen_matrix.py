"""Hybrid Strassen matrix multiplication using standard multiplication at a cutoff."""

def add_matrix(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def subtract_matrix(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]


def standard_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def next_power_of_two(number):
    return 1 if number <= 1 else 2 ** (number - 1).bit_length()


def strassen_multiply(a, b, cutoff=64):
    """
    Multiply square matrices a and b.
    Matrices with non-power-of-two dimensions are zero-padded and trimmed.
    Small matrices use conventional multiplication.
    """
    if not a or not b or len(a) != len(a[0]) or len(b) != len(b[0]):
        raise ValueError("Inputs must be non-empty square matrices of equal size.")
    if len(a) != len(b):
        raise ValueError("Matrices must have the same dimensions.")

    original_n = len(a)
    padded_n = next_power_of_two(original_n)

    def pad(matrix):
        return [row + [0] * (padded_n - original_n) for row in matrix] + [
            [0] * padded_n for _ in range(padded_n - original_n)
        ]

    A, B = pad(a), pad(b)

    def recurse(x, y):
        n = len(x)
        if n <= cutoff:
            return standard_multiply(x, y)

        half = n // 2
        a11 = [row[:half] for row in x[:half]]
        a12 = [row[half:] for row in x[:half]]
        a21 = [row[:half] for row in x[half:]]
        a22 = [row[half:] for row in x[half:]]
        b11 = [row[:half] for row in y[:half]]
        b12 = [row[half:] for row in y[:half]]
        b21 = [row[:half] for row in y[half:]]
        b22 = [row[half:] for row in y[half:]]

        m1 = recurse(add_matrix(a11, a22), add_matrix(b11, b22))
        m2 = recurse(add_matrix(a21, a22), b11)
        m3 = recurse(a11, subtract_matrix(b12, b22))
        m4 = recurse(a22, subtract_matrix(b21, b11))
        m5 = recurse(add_matrix(a11, a12), b22)
        m6 = recurse(subtract_matrix(a21, a11), add_matrix(b11, b12))
        m7 = recurse(subtract_matrix(a12, a22), add_matrix(b21, b22))

        c11 = add_matrix(subtract_matrix(add_matrix(m1, m4), m5), m7)
        c12 = add_matrix(m3, m5)
        c21 = add_matrix(m2, m4)
        c22 = add_matrix(add_matrix(subtract_matrix(m1, m2), m3), m6)

        top = [c11[i] + c12[i] for i in range(half)]
        bottom = [c21[i] + c22[i] for i in range(half)]
        return top + bottom

    product = recurse(A, B)
    return [row[:original_n] for row in product[:original_n]]


if __name__ == "__main__":
    A = [[1, 7], [3, 5]]
    B = [[1, 3], [7, 5]]
    print("Product:", strassen_multiply(A, B, cutoff=1))
