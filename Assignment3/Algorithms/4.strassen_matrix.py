```python
def add_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]


def subtract_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]


def conventional_small(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                count += 1

    return result, count


def strassen(A, B):
    n = len(A)

    if n <= 2:
        return conventional_small(A, B)

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1, c1 = strassen(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2, c2 = strassen(
        add_matrix(A21, A22),
        B11
    )

    M3, c3 = strassen(
        A11,
        subtract_matrix(B12, B22)
    )

    M4, c4 = strassen(
        A22,
        subtract_matrix(B21, B11)
    )

    M5, c5 = strassen(
        add_matrix(A11, A12),
        B22
    )

    M6, c6 = strassen(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7, c7 = strassen(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    C11 = add_matrix(
        subtract_matrix(add_matrix(M1, M4), M5),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        add_matrix(subtract_matrix(M1, M2), M3),
        M6
    )

    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    total_count = c1 + c2 + c3 + c4 + c5 + c6 + c7

    return C, total_count


def pad_matrix(A, size):
    padded = [[0] * size for _ in range(size)]

    for i in range(len(A)):
        for j in range(len(A[0])):
            padded[i][j] = A[i][j]

    return padded


def strassen_multiply(A, B):
    if not A or not B:
        raise ValueError("Matrices cannot be empty")

    if len(A[0]) != len(B):
        raise ValueError("Matrix multiplication not possible")

    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])

    size = 1

    while size < max(rows_a, cols_a, rows_b, cols_b):
        size *= 2

    padded_a = pad_matrix(A, size)
    padded_b = pad_matrix(B, size)

    padded_result, count = strassen(padded_a, padded_b)

    result = [
        row[:cols_b]
        for row in padded_result[:rows_a]
    ]

    return result, count


if __name__ == "__main__":
    rows_a = int(input("Enter rows of A: "))
    cols_a = int(input("Enter columns of A: "))

    A = []

    print("Enter matrix A:")
    for i in range(rows_a):
        row = list(map(int, input().split()))

        if len(row) != cols_a:
            raise ValueError("Incorrect number of elements")

        A.append(row)

    rows_b = int(input("Enter rows of B: "))
    cols_b = int(input("Enter columns of B: "))

    B = []

    print("Enter matrix B:")
    for i in range(rows_b):
        row = list(map(int, input().split()))

        if len(row) != cols_b:
            raise ValueError("Incorrect number of elements")

        B.append(row)

    result, count = strassen_multiply(A, B)

    print("Result Matrix:")

    for row in result:
        print(row)

    print("Scalar Multiplications:", count)
```
