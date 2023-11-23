import numpy as np


def replace_center_with_minus_one(d, n, m):
    """
    This function generates an n-by-n NumPy array populated with random integers having up to d digits.
    It replaces the central m-by-m part of this array with -1.

    """
    if m > n:
        raise ValueError(
            "Size of the center matrix cannot be bigger than the size of the main matrix")
    if d <= 0:
        raise ValueError(
            "The maximum number of digits for the random integers cannot be less than or equal to zero")
    if n < 0:
        raise ValueError(
            "The size of the n-by-n array cannot be less than zero")
    if m < 0:
        raise ValueError(
            "The size of the central m-by-m part to be replaced with -1 cannot be less than zero")

    array = np.random.randint(10 ** (d - 1), 10 ** d, (n, n))

    start_point = (n - m) // 2
    end_point = ((n - m) // 2) + m

    array[start_point:end_point, start_point:end_point] = -1

    return array
