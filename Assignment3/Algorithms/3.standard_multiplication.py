```python
def standard_multiply(x, y):
    sign = -1 if (x < 0) != (y < 0) else 1

    x = abs(x)
    y = abs(y)

    if x == 0 or y == 0:
        return 0, 0

    a = [int(digit) for digit in str(x)][::-1]
    b = [int(digit) for digit in str(y)][::-1]

    result = [0] * (len(a) + len(b))
    multiplication_count = 0

    for i in range(len(a)):
        carry = 0

        for j in range(len(b)):
            product = a[i] * b[j]
            multiplication_count += 1

            total = result[i + j] + product + carry
            result[i + j] = total % 10
            carry = total // 10

        k = i + len(b)

        while carry > 0:
            total = result[k] + carry
            result[k] = total % 10
            carry = total // 10
            k += 1

    answer = int("".join(map(str, result[::-1])))

    return sign * answer, multiplication_count


if __name__ == "__main__":
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))

    answer, count = standard_multiply(x, y)

    print("Product:", answer)
    print("Digit multiplications:", count)
```
