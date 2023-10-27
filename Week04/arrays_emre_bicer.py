import numpy as np

def replace_center_with_minus_one(d, n, m):
    if(d <= 0):
        raise ValueError("d can not be less than or equal to 0")
    elif(m > n):
        raise ValueError("n can not be less than m")
    elif(n < 0):
        raise ValueError("n can not be less than 0")
    elif(m < 0):
        raise ValueError("m can not be less than 0")

    highest_rand_num = int('9' * d)

    np_array = np.random.randint(0, highest_rand_num+1, size=(n, n))

    start_index = int((n - m) / 2)
    end_index = int(start_index + m)

    np_array[start_index:end_index, start_index:end_index] = -1

    return np_array
