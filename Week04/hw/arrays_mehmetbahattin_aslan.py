import numpy as np

"""
    This function creates an n-by-n numpy array
    populated with random integers that have 
    up to d digits. It then replaces the central
    m-by-m part of this array with -1.


    :param d : Number of digits for the random integers. 
    :param n: Size of the main array. 
    :param m : Size of the central array that will be replaced with -1
    :return ar1: A modified numpy array with its center replaced with -1 
    
    """

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input values")
    
    ar1 = np.random.randint(0, 10 ** d - 1, size=(n, n))
    m_1 = (n - m) // 2
    m_2 = m_1 + m

    ar1[m_1:m_2, m_1:m_2] = -1
    
    return ar1
