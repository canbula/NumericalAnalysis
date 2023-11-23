import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input parameters")

    # Create an n-by-n array with random integers up to d digits
    random_array = np.random.randint(10**d, size=(n, n))

    # Find the starting and ending indices for the center region
    start_index = (n - m) // 2
    end_index = start_index + m

    # Create a copy of the random array and replace the center with -1
    modified_array = random_array.copy()
    modified_array[start_index:end_index, start_index:end_index] = -1

    return modified_array
