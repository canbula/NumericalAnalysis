import numpy as np
def replace_center_with_minus_one(d, n, m):
    if(m > n):
        raise ValueError("Value Error -> Parameter m can not be greater than the parameter n")
    if(d <= 0):
        raise ValueError("Value Error -> Parameter d can not be less then or equal 0")
    if(n < 0):
        raise ValueError("Value Error -> Parameter n can not be less then 0")
    if(m < 0): 
        raise ValueError("Value Error -> Parameter m can not be less then 0")
    
    np_array = np.random.randint(0, (10**d) - 1, size=(n,n))
    center_array_start_index = (n - m) // 2

    for i in range(center_array_start_index, center_array_start_index + m):
        for j in range(center_array_start_index, center_array_start_index + m):
            np_array[i, j] = -1
    return np_array
