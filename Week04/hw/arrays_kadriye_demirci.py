import numpy as np
def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Value Error!")
    np_array = np.random.randint(0, int("9" * d) + 1, size=(n, n))
    np_array[int((n-m)/2):int(((n-m)/2)+m),
             int((n-m)/2):int(((n-m)/2)+m)] = -1
    return np_array
