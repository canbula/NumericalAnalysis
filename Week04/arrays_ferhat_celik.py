import random
import numpy as np
def replace_center_with_minus_one(d, n, m):
    # d: Number of digits for the random integers.
    # n: Size of the square like main array.
    # m: Size of the central array that will be replaced by -1.
    if m > n:
        raise ValueError("m must be smaller than n")
    if d <= 0:
        raise ValueError("d must be greater than 0")
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if m <= 0:
        raise ValueError("m must be greater than 0")
    min_value = 10**(d-1)
    max_value = 10**d - 1
    array = np.array([[random.randint(min_value, max_value) for i in range(n)] for j in range(n)])
    array[(n-m)//2:(n-m)//2+m, (n-m)//2:(n-m)//2+m] = -1
    return array

if __name__ == '__main__':
    d = input("Enter the number of digits for the random integers: ")
    n = input("Enter the size of the square like main array: ")
    m = input("Enter the size of the central array that will be replaced by -1: ")
    print(replace_center_with_minus_one(int(d), int(n), int(m)))