import numpy as np
def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError
    
    if d == 1:
        array = np.random.randint(0, 10, size=(n, n))
    else:
        array = np.random.randint(10**(d-1), 10**d, size=(n, n))

    border_start = (n - m) // 2
    border_end = border_start + m
    
    array[border_start:border_end, border_start:border_end] = -1
    
    return array