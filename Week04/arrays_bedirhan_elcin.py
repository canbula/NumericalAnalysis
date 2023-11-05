#Bedirhan ELÇİN 190316054

import random
import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m can't be greater than n")
    if d <= 0 or m <= 0 or n <= 0:
        raise ValueError("m,n, and d can't be equal or less than 0")
    min_value = 10 ** (d - 1)
    max_value = 10 ** d - 1
    my_array = np.array([[random.randint(min_value, max_value) for i in range(n)] for j in range(n)])
    my_array[(n - m) // 2:(n - m) // 2 + m, (n - m) // 2:(n - m) // 2 + m] = -1
    return my_array




