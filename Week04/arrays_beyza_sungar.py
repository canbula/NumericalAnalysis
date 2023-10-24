import numpy as np

try:
    n = int(input("Enter a dimension number (n): "))
    if n <= 0:
        raise ValueError("n must be a positive integer")

    num_digits = int(input("Enter the number of digits for random integers: "))
    if num_digits <= 0:
        raise ValueError("num_digits must be a positive integer")

    m = int(input("Enter the size of the central array (m): "))
    if m <= 0:
        raise ValueError("m must be a positive integer")
    if m > n:
        raise ValueError("m cannot be greater than n")
except ValueError as e:
    print(f"Error: {e}")
    exit()


arr1 = np.random.randint(10 ** (num_digits - 1), 10 ** num_digits, size=(n, n))

#print(arr1)

def change_edge_elements(arr):
    n, m = arr.shape
    arr[1:n-1, 1:m-1] = -1
    return arr

result_array = change_edge_elements(arr1)
print(result_array)
