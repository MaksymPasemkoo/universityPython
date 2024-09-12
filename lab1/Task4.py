def calculate_function():
    a = 10
    b = 5
    n = 20

    x = (a ** 2) * n
    y = (n - b) ** 3
    res = 0
    if y % 2 == 0:
        res = y / x
    else:
        res = x // y
    return res
