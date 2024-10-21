import random
import numpy as np
import math

def replace_center_with_minus_one(d, n, m):
    """
    This function creates an n-by-n numpy array populated 
    with random integers that have up to d digits. It then
    replaces the central m-by-m part of this array with -1.
    
    :param d: number of digits for the random integers
    :param n: size of main array
    :param m: size of central array that will replaced with -1 
    
    :return: modified numpy array with its center replaced with -1
    """
    if not (type(d) == int and type(n) == int and type(m) == int):
        raise TypeError
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError
    
    arr = np.full((n,n),-1,dtype=int)
    start_index = math.floor((n - m) / 2)
    end_index = start_index + m - 1
    
    print(start_index)
    print(end_index)


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i < start_index or i > end_index) or (j < start_index or j > end_index):
                arr[i][j] = random.randint(0,d + 1)
    return arr

