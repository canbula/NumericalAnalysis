import numpy as np

def replace_center_with_minus_one(n, d, m):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if d <= 0:
        raise ValueError("num_digits must be a positive integer")
    if m <= 0:
        raise ValueError("m must be a positive integer")
    if m > n:
        raise ValueError("m cannot be greater than n")
    
    arr1 = np.random.randint(10 ** (d - 1), 10 ** d, size=(n, n))
    arr1[1:n-1, 1:n-1] = -1
    return arr1

if __name__ == "__main__":
    try:
        n = int(input("Enter a dimension number (n): "))
        d = int(input("Enter the number of digits for random integers: "))
        m = int(input("Enter the size of the central array (m): "))
        
        result_array = replace_center_with_minus_one(n, d, m)
        
        print("Modified Array:")
        print(result_array)
    except ValueError as e:
        print(f"Error: {e}")










