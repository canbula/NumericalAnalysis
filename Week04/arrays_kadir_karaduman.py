import numpy as np

def replace_center_with_minus_one(d, n, m):

    if(m > n or d<= 0 or n < 0 or m < 0):
        raise ValueError("Value Error has been ocurred")


    end = (10**d) - 1

    array = np.random.randint(0, end, size=(n, n))

    start_index = (n - m) // 2

    for i in range(start_index, start_index+m):
        for j in range(start_index, start_index+m):
            array[i, j] = -1


    return array
