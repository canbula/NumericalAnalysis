import numpy as np


def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m can't be greater than n")
    elif d <= 0:
        raise ValueError("d must be greater than 0")
    elif m < 0 or n < 0:
        raise ValueError("m or n can't be lesser than 0")

    numpy_array = np.random.randint(0, 10 ** d, size=(n, n))

    start_corner = (n-m) // 2
    end_row_or_col = start_corner + m-1

    for r in range(start_corner,end_row_or_col+1):
        for c in range(start_corner, end_row_or_col+1):
            numpy_array[r,c] = -1

    return numpy_array
