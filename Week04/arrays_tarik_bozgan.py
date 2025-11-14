import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m cannot be greater than n")
    if d <= 0:
        raise ValueError("d must be greater than 0")
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
    if m < 0:
        raise ValueError("m must be greater than or equal to 0")
    
    arr = np.random.randint(10**d, size=n)
    
    start_index = (n - m) // 2
    end_index = start_index + m
    
    for i in range(start_index, end_index):
        arr[i] = -1
    
    return arr