import numpy as np

def replace_center_with_minus_one(d, n, m):

    main_array = np.random.randint(10 ** (d - 1), 10 ** d, size=(n, n))
    start_index = (n - m) // 2
    end_index = start_index + m
    main_array[start_index:end_index, start_index:end_index] = -1
  
    return main_array
