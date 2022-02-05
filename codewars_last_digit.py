def last_digit(arr):
    n = 1
    for i in reversed(arr):
        n = i ** (n if n < 4 else n % 4)
    return n % 10

print(last_digit([2, 2, 2, 4]))