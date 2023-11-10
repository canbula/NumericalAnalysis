import numpy as np

def create_array(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input parameters")

    random_array = np.random.randint(10 ** (d-1), 10 ** d, size=(n, n))


    center_start = (n - m) // 2
    center_end = center_start + m


    random_array[center_start:center_end, center_start:center_end] = -1

    return random_array
