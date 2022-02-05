from math import sqrt, floor

def squared_divisors(n):
    arr = set()
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            arr.add(i ** 2)
            arr.add(int(n / i) ** 2)
    return list(arr)


def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisor = squared_divisors(num)
        sum_of_squares = sum(divisor)
        if (sqrt(sum_of_squares) * 10) % 10 == 0:
            result.append([num, sum_of_squares])

    return result

print(list_squared(1, 250))


