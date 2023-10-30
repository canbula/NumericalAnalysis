import numpy as np

def replace_center_with_minus_one(d, n, m):
    """
    This function creates an n-by-n numpy array populated
    with random integers that have up to d digits. It then
    replaces the central m-by-m part of this array with -1.

    :param d: Number of digits for the random integers.
    :param n: Size of the main array.
    :param m: Size of the central array that will be replaced with -1.
    :return: A modified numpy array with its centre replaced with -1.
    """

    if (m > n) or (d <= 0) or (n<0) or (m<0):
        raise ValueError("ValueError exception thrown")
    
    arr = np.random.randint(10**(d-1) , 10**d , size=(n, n))
    start_point = (n-m) // 2
    end_point = start_point + m

    arr[start_point:end_point , start_point:end_point] = -1
    return arr
