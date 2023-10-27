import numpy as np

def create_modified_array(d, n, m):
    if m > n:
        raise ValueError(" m should be less than or equal to n")
    if d <= 0:
        raise ValueError(" d should be greater than 0")
    if n < 0:
        raise ValueError(" n should be greater than 0")
    if m < 0:
        raise ValueError(" m should be greater than 0")

    an_array = np.random.randint(0, 10 ** d, size=(n, n))
    print("Original Array:")
    print(an_array)

    start_idx = (n - m) // 2
    end_idx = start_idx + m

    an_array[start_idx:end_idx, start_idx:end_idx] = -1

    print("Modified Array:")
    print(an_array)
    return an_array

try:
    create_modified_array(3, 4, 2)
    # Test with m > n
except ValueError as e:
    print(f" {e}")
