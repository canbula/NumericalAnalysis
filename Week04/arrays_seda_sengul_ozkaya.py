import numpy as np

def replace_center_with_minus_one(d, n, m):

    if m > n:
        raise ValueError("m cannot be greater than n.")
    if d <= 0:
        raise ValueError("d must be positive.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if m < 0:
        raise ValueError("m cannot be negative.")

    low = 10 ** (d - 1)
    high = 10 ** d
    arr = np.random.randint(low, high, size=(n, n))

   
    start = (n - m) // 2
    end = start + m

    if n % 2 == 0 and m % 2 == 1:
        start -= 1
        end -= 1

    arr[start:end, start:end] = -1

    return arr
