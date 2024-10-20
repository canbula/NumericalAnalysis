import numpy as np


def replace_center_with_minus_one(d, n, m):
    error = m > n or d <= 0 or n < 0 or m < 0
    if error:
        raise ValueError("Problem with the parameters")
    arr = np.random.randint(10**(d-1), (10**d)-1, size=(n, n))
    start = int((n - m) / 2)
    end = start + m
    arr[start:end, start:end] = -1
    return arr
