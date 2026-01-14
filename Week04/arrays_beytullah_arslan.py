import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid parameters")
    arr = np.random.randint(0, 10**d, (n, n))
    if n == m:
        arr[:] = -1
    else:
        start = (n - m) // 2
        end = start + m
        arr[start:end, start:end] = -1
    return arr


