import numpy as np
import random

def replace_center_with_minus_one(d, n, m):
    if n < 0 or m < 0 or d <= 0 or m > n:
        raise ValueError("Error: Invalid values!!")
    
    array = np.random.randint(10**(d - 1), 10**d, size=(n, n))
    x = (n - m) // 2
    y = x + m
    
    for i in range(x, y):
        for j in range(x, y):
            array[i, j] = -1

    return array
