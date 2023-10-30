import numpy as np

def create_array(d, n, m):
    if m > n:
        raise ValueError("m should be less than or equal to n")
    if d <= 0:
        raise ValueError("d should be greater than 0")
    if n < 0:
        raise ValueError("n should be non-negative")
    if m < 0:
        raise ValueError("m should be non-negative")
    
    arr = np.random.randint(10**(d-1), 10**d, (n, n))

    start = (n - m) // 2
    end = start + m
    arr[start:end, start:end] = -1
    
    return arr

try:
    d = int(input("Enter the number of digits for the random integers (d): "))
    n = int(input("Enter the size of the main array (n): "))
    m = int(input("Enter the size of the central array that will be replaced with -1 (m): "))
    
    print(create_array(d, n, m))

except ValueError as e:
    print(f"Error: {e}")

