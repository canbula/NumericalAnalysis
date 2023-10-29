import numpy as np
# n: n x n matrix
# d: number of digits
# m: m x m matrix in the center

def change_parts_of_array_with_minus_one(n, d ,m):
    if ( n < 0 or m > n or d <= 0 or m < 0 or m > n ):
        raise ValueError("There is a problem in the parameters")

    # random_matrix = np.random.randint(min_val,max_val,(<num_rows>,<num_cols>))
    generated_random_matrix = np.random.randint(10**(d-1), 10**d - 1, (n, n))
    # print(generated_random_matrix)
    y, x, *_ = generated_random_matrix.shape
    start_x = x // 2 - (m // 2)
    start_y = y // 2 - (m // 2)
    minus_one_matrix = np.full((m, m), -1)
    generated_random_matrix[start_y:start_y + m, start_x:start_x + m, ...] = minus_one_matrix[:]
    # print(generated_random_matrix)
    return generated_random_matrix
