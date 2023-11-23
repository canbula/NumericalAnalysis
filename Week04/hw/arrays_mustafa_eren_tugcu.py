import numpy as np 
import random 

def replace_center_with_minus_one(d,n,m):
    """
    This function creates an n-by-n numpy array
    populated with random integers that have 
    up to d digits. It then replaces the central
    m-by-m part of this array with -1.


    :param d : Number of digits for the random integers. 
    :param n: Size of the main array. 
    :param m : Size of the central array that will be replaced with -1
    :return: A modified numpy array with its center replaced with -1 
    
    """
    
    if (m > n or d<=0 or n<0 or m<0):
        raise ValueError("Value Error has been ocurred")
    
    
    arr = np.random.randint(0,(10 ** d)-1,size=(n,n))

    for i in range((n-m)//2,((n-m)//2) + m ):
        for j in range((n-m)//2,((n-m)//2) + m ):
            arr[i,j] = -1 
        ## (n-m)//2 --> which is the starting index that centers the central region within the main array 
    return arr

