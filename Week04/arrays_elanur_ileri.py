import numpy as np

def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:

    if (m > n or d <= 0 or n < 0 or m < 0):
        raise ValueError("Unexpected Value")

    arr = np.random.randint(0,(10**d), size=(n,n))

    center = (n - m) // 2
    arr[center:center + m, center:center + m] = -1

    return arr
