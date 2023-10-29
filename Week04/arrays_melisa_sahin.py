import numpy as np
import random


def replace_center_with_minus_one(d,n,m):
    if ( m>n or d<=0 or n<0 or m<0):
        raise ValueError("Value Error has been ocurred")
    
    max_value = 10**d - 1
    arr = np.random.randint(0,max_value+1,size=(n,n))
    start_index = (n-m) // 2
    
    for i in range(start_index, start_index+m):
        for j in range(start_index, start_index+m):
            arr[i,j] = -1

    return arr
