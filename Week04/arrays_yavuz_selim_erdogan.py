import numpy as np


def replace_center_with_minus_one(d: int, n: int, m: int):
    if m > n:
        raise ValueError("m can't be greater than n")
    elif d <= 0:
        raise ValueError("d must be greater than 0")
    elif m < 0 or n < 0:
        raise ValueError("m or n can't be lesser than 0")

    random_array = np.random.randint(0, 10**d, size=(n, n))

    start_row = (n - m) // 2
    end_row = start_row + m
    start_col = (n - m) // 2
    end_col = start_col + m

    random_array[start_row:end_row, start_col:end_col] = -1

    return random_array
