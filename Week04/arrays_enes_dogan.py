import numpy as np
import random


def replace_center_with_minus_one(d: int, n: int, m: int):
    if d <= 0:
        raise ValueError("d can not be less than or equal to 0")
    if m > n:
        raise ValueError("m cannot be greater than n")
    if n < 0:
        raise ValueError("n can not be less than 0")
    if m < 0:
        raise ValueError("m can not be less than 0")

    arr = np.random.randint(0, (10**d), (n, n))
    start_index = (n - m) // 2
    end_index = start_index + m
    arr[start_index:end_index, start_index:end_index] = -1

    return arr
