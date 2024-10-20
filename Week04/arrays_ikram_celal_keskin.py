import numpy as np


def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:
    """This function creates a n x n array of random integers with d digits.
    Then it replaces the centr m x m size of the array with -1.

    Args:
    d (int): number of digits of the random integers
    n (int): size of the array
    m (int): size of the center to be want to replaced with -1

    Returns:
        np.ndarray: n x n array with the m x m center replaced with -1
    """
    if n < 0 or m > n or d <= 0 or m < 0 or m > n:
        raise ValueError("Something went wrong")

    numpy_nxn_array = np.random.randint(10 ** (d - 1), 10**d, (n, n))

    shape_x, shape_y = numpy_nxn_array.shape
    operational_x = (shape_x - m) // 2
    operational_y = (shape_y - m) // 2

    numpy_nxn_array[
        operational_x : operational_x + m, operational_y : operational_y + m
    ] = -1

    return numpy_nxn_array
