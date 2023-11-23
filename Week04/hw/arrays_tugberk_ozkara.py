import numpy as np


def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:
    """
    Replaces the center of a 2d array with -1.

    :param d: Maximum number of digits for the random integers
    :param n: Size of the main array: nxn
    :param m: Size of the central array will be replaced with -1: mxm
    :return: The array with the center replaced with -1.
    """
    if m > n:
        raise ValueError("Central array cannot be larger than the main array.")
    if d <= 0:
        raise ValueError("Maximum number of digits must be greater than 0.")
    if n < 0:
        raise ValueError("Size of the main array cannot be negative.")
    if m < 0:
        raise ValueError("Size of the central array cannot be negative.")

    arr = np.random.randint(0, 10**d, size=(n, n))
    arr[(n-m)//2: (n-m)//2 + m, (n-m)//2: (n-m)//2 + m] = -1
    return arr
