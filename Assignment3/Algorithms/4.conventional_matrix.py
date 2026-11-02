```python
def conventional_multiply(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])

    if cols_a != rows_b:
        raise ValueError("Matrix multiplication not possible")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    multiplication_count = 0

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]
                multiplication_count += 1

    return result, multiplication_count


def read_matrix(rows, cols, name):
    print("Enter elements of matrix", name)

    matrix = []

    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != cols:
            raise ValueError("Incorrect number of elements")

        matrix.append(row)

    return matrix


if __name__ == "__main__":
    rows_a = int(input("Enter rows of A: "))
    cols_a = int(input("Enter columns of A: "))

    A = read_matrix(rows_a, cols_a, "A")

    rows_b = int(input("Enter rows of B: "))
    cols_b = int(input("Enter columns of B: "))

    B = read_matrix(rows_b, cols_b, "B")

    result, count = conventional_multiply(A, B)

    print("Result Matrix:")

    for row in result:
        print(row)

    print("Scalar Multiplications:", count)
```
