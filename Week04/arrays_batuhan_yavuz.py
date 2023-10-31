import numpy as np

def replace_center_with_minus_one(d:int, n:int, m:int) -> np.ndarray:
    if d <= 0 or m > n or n < 0 or m < 0:
        raise ValueError("Value Error: Invalid value")

    nn_array = np.random.randint(0, (10**d), size=(n,n))
    center = (n - m) // 2
    nn_array[center:center+m, center:center+m] = -1
    
    return nn_array
