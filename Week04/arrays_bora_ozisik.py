import numpy as np

def replace_center_with_minus_one(d,n,m):

    if(m > n | d <= 0 | n < 0 | m < 0):
        raise ValueError("Value Error: Invalid value used.Check parameters.")


    numpy_array = np.random.randint(0, (10 ** d) - 1, size=(n, n))

    start_index = (n - m) // 2
    end_index = start_index + m

    numpy_array[start_index:end_index, start_index:end_index] = -1
