import numpy as np

def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:
   
    if(m > n or d <= 0 or n < 0 or m < 0):
        raise ValueError("Unexpected value")

    max = 10 ** d
    array = np.random.randint(0, max, size=(n, n))

    start = (n - m) // 2
    end = ((n - m) // 2) + m

    array[start:end, start:end] = -1
    return array
