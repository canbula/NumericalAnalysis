import numpy as np
import random

def replace_center_with_minus_one(d:int ,n:int, m:int):

    if (m>n) or (d<=0) or (n<0) or (m<0):
        raise ValueError("Value Error")
    

    my_array = np.random.randint(0, 10**d , (n,n))

    start_point = (n-m)//2
    end_point = start_point + m
    
    my_array[start_point:end_point, start_point:end_point] = -1

    return my_array


if __name__ == "__main__" :

    myarr = replace_center_with_minus_one(1 , 3, 1)
    print(myarr)
