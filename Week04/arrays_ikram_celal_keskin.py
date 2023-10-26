import numpy as np

def replace_center_with_minus_one(n, d, m):
    if (m < 0 or n < 0 or m > n or d <= 0) :
        raise ValueError("m should be less than or equal to n")

    rarr = np.random.randint(10 ** (d - 1), 10 ** d, (n, n))

    start_idx = (n - m) // 2
    end_idx = start_idx + m

    rarr[start_idx:end_idx, start_idx:end_idx] = -1

    return rarr

