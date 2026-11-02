```python
def karatsuba_multiply(x, y):
    sign = -1 if (x < 0) != (y < 0) else 1

    result, count = karatsuba(abs(x), abs(y))

    return sign * result, count


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y, 1

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    power = 10 ** m

    high1 = x // power
    low1 = x % power

    high2 = y // power
    low2 = y % power

    z0, count0 = karatsuba(low1, low2)
    z2, count2 = karatsuba(high1, high2)

    z1, count1 = karatsuba(
        high1 + low1,
        high2 + low2
    )

    z1 = z1 - z2 - z0

    result = (z2 * (10 ** (2 * m))) + (z1 * power) + z0

    total_count = count0 + count1 + count2

    return result, total_count


if __name__ == "__main__":
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))

    answer, count = karatsuba_multiply(x, y)

    print("Product:", answer)
    print("Recursive single-digit multiplications:", count)
```
