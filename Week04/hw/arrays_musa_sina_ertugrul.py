""" Musa Sina ERTUGRUL 200316011 """

import numpy as np


def replace_center_with_minus_one(d, n, m):
    """This function replace center of a matris

    Arguments:
    d (int) : number of digits for the random integers
    n (int) : size of the main array
    m (int) : size of the central array that will be replaced with -1

    Return:
    np.array
    """

    if d <= 0 or n < 0 or m < 0 or m > n:
        raise ValueError("Erroneous data encountered")

    array = np.random.randint(0, 10 ** (d - 1), size=(n, n))

    start_index = (n - m) // 2
    end_index = start_index + m

    array[start_index:end_index, start_index:end_index] = -1

    return array
