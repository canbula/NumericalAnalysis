import numpy as np

def replace_center_with_minus_one(d, n, m):
    if ( d <= 0 or n < 0 or m < 0 or m > n ):
        raise ValueError("Erroneous data encountered")

    rarr = np.random.randint(0, 10 ** (d - 1), size=(n, n))

    start_idx = (n - m) // 2
    end_idx = start_idx + m

    rarr[start_idx:end_idx, start_idx:end_idx] = -1

    return rarr

