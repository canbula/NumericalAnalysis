## Mahmut Sacit Meydanal, 200316057

import numpy as np

def replace_center_with_minus_one(d: int, n: int, m: int):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input parameters")

    random_array = np.random.randint(10 ** (d - 1), 10 ** d, size=(n, n))

    start = (n - m) // 2
    end = start + m

    random_array[start:end, start:end] = -1

    return random_array
