import numpy as np
import random

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m cannot be greater than n")
    elif d <= 0:
        raise ValueError("d cannot be equal to or smaller than 0")
    elif n < 0:
        raise ValueError("n cannot be negative")
    elif m < 0:
        raise ValueError("m cannot be negative")
    else:
        my_matrix = []
        for row in range(n):
            row = []
            for element in range(n):
                row.append(random.randint(10**(d-1), 10**d))
            my_matrix.append(row)

        for i in range(1, m+1):
            for j in range(1, m+1):
                my_matrix[i][j] = -1

        for row in my_matrix:
            print(row)

if __name__ == "__main__":
    replace_center_with_minus_one(1, 5, 3)
