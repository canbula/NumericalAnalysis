import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m should be less than or equal to n")
    if d <= 0:
        raise ValueError("d should be greater than 0")
    if n < 0:
        raise ValueError("n should be a positive integer")
    if m < 0:
        raise ValueError("m should be a positive integer")

    rand_array = np.random.randint(10**d, size=(n, n))
    center_start = (n - m) // 2
    center_end = center_start + m

    rand_array[center_start:center_end, center_start:center_end] = -1

    return rand_array








