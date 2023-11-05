import numpy as np


# n: n x n matrix
# d: number of digits
# m: m x m matrix in the center

def replace_center_with_minus_one(d: int, n: int, m: int):
    if n < 0 or m > n or d <= 0 or m < 0 or m > n:
        raise ValueError("Invalid parameter(s)")

    # random_matrix = np.random.randint(min_val,max_val,(<num_rows>,<num_cols>))
    generated_random_matrix = np.random.randint(10 ** (d - 1), 10 ** d - 1, (n, n))
    # print(generated_random_matrix)
    y, x, *_ = generated_random_matrix.shape
    start_x = (x - m) // 2
    start_y = (y - m) // 2
    # minus_one_matrix = np.full((m, m), -1)
    generated_random_matrix[start_y:start_y + m, start_x:start_x + m, ...] = -1
    return generated_random_matrix