import numpy as np

def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:
    """
    This function generates an n-by-n NumPy array populated with random integers having up to d digits.
    It replaces the central m-by-m part of this array with -1.

    :param d: The maximum number of digits for the random integers type -> int
    :param n: The size of the n-by-n array. type -> int
    :param m: The size of the central m-by-m part to be replaced with -1. type ->int
    :return: A NumPy array with the specified properties. type -> numpy.ndarray
    """
  
    if(m > n or d <= 0 or n < 0 or m < 0):
        raise ValueError("Unexpected value")

    max_value = 10 ** d
    array = np.random.randint(0, max_value, size=(n, n))

    start_point = (n - m) // 2
    end_point = ((n - m) // 2) + m

    array[start_point:end_point, start_point:end_point] = -1
    return array
