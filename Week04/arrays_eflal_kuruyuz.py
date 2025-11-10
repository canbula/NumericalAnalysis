import numpy as np

def replace_center_with_minus_one(n, d, m):
    
    
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Value Error has been ocurred")
       
    
    max_value = 10**d - 1
    random_array = np.random.randint(0, max_value+1, size=(n, n))
    
    center_start = (n - m) // 2
    center_end = center_start + m
    
    random_array[center_start:center_end, center_start:center_end] = -1
    
    return random_array






