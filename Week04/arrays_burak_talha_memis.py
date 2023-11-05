import numpy as np
import random

def replace_center_with_minus_one(d,n,m):
    if(m > n or d <= 0 or n < 0 or m < 0):
        raise ValueError("Value Error")
    
    a_array = np.random.randint(0 , 10**d ,(n,n))
         
    start_index = int((n - m) / 2)
    end_index = int(int((n - m) / 2) + m)

    a_array[start_index : end_index , start_index : end_index] = -1

    return a_array
