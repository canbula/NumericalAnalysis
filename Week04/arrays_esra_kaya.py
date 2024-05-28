import numpy as np

def create_array(d, n, m):

    # create a random n by n array with random integers
    rand_array = np.random.randint(0, 10 ** d, size=(n, n))
    print(rand_array)

    # The he starting and ending indices for the central array
    start_index = (n - m) // 2
    end_index = start_index + m

    # Replace the central m by m array with -1
    rand_array[start_index:end_index, start_index:end_index] = -1

    if m > n:
        raise ValueError("Error: m should be less than or equal to n")
    if d <= 0:
        raise ValueError("Error: d should be greater than 0")
    if n < 0:
        raise ValueError("Error: n should be non-negative")
    if m < 0:
        raise ValueError("Error: m should be non-negative")

    print(rand_array) 

try:
    d = 4
    n = 7
    m = 3
    new_array = create_array(d, n, m)
    
    print("New Array:")
    print(new_array)
    
except ValueError as e:
    print(f"Error: {e}")
