import numpy as np


def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid parameters")

    min_val = 10 ** (d - 1)
    max_val = 10 ** d

    arr = np.random.randint(min_val, max_val, size=(n, n))

    start_index = (n - m) // 2
    end_index = start_index + m

    arr[start_index:end_index, start_index:end_index] = -1

    return arr

print(replace_center_with_minus_one(2, 5, 3))
