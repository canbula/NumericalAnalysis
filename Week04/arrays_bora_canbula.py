import numpy as np

def replace_center_with_minus_one(d, n, m):
    """
    Creates an n-by-n numpy array with d digits random integers and 
    replaces its m-by-m center with a numpy array filled with -1.
    
    Parameters:
    - d: number of digits for the random integers
    - n: size of the main array
    - m: size of the central array to be replaced with -1
    
    Returns:
    - A modified numpy array with its center replaced with -1

    Raises:
    - ValueError: if m > n, d <= 0, n < 0, or m < 0
    """
    
    # Check for invalid parameters and raise ValueError
    if m > n:
        raise ValueError("The center array size 'm' should not be larger than the main array size 'n'.")
    if d <= 0:
        raise ValueError("The number of digits 'd' should be positive.")
    if n < 0 or m < 0:
        raise ValueError("Both 'n' and 'm' should be non-negative.")

    # Create an n-by-n matrix with random integers between 0 and 10^d - 1
    a = np.random.randint(0, 10**d, (n, n))

    # Calculate starting index to place the m-by-m center
    k = (n - m) // 2

    # Replace the center of 'a' with -1
    a[k:k+m, k:k+m] = -1
    
    return a


if __name__ == "__main__":
    # print(replace_center_with_minus_one(2, 5, 3))
    # print(replace_center_with_minus_one(2, 4, 2))
    # print(replace_center_with_minus_one(2, 6, 4))
    # print(replace_center_with_minus_one(3, 7, 3))
    # print(replace_center_with_minus_one(3, 9, 5))
    # print(replace_center_with_minus_one(3, 11, 9))
    print(replace_center_with_minus_one(3, 13, 11))