import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input parameters")

    # Generate an n-by-n numpy array with random integers up to 10^d - 1
    random_array = np.random.randint(10**d, size=(n, n))

    # Calculate the indices for the center part to be replaced with -1
    start_row = (n - m) // 2
    end_row = start_row + m
    start_col = (n - m) // 2
    end_col = start_col + m

    # Create a copy of the random array and replace the center with -1
    modified_array = np.copy(random_array)
    modified_array[start_row:end_row, start_col:end_col] = -1

    return modified_array
