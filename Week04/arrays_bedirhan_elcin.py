#Bedirhan elçin 190316054
import numpy as np

def replace_center_with_minus_one(n, d, m):
    if m > n:
        raise ValueError("m can't be greater than n")
    elif d != 2:
        raise ValueError("d must be 2 for two-digit numbers")
    elif m < 0 or n < 0:
        raise ValueError("m or n can't be lesser than 0")

    matrix = np.random.randint(10, 100, (n, n))

    if m >= 3:

        center_start = (n - 3) // 2
        center_end = center_start + 3
        matrix[center_start:center_end, center_start:center_end] = -1

    return matrix
