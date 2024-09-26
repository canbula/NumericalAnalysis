import numpy as np 

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid values entered. Check m, d, n!")
        
    random_array = np.random.randint(10**d, size=(n, n))
    
    start_index = (n - m) // 2
    end_index = start_index + m
    
    modified_array = random_array.copy()
    
    modified_array[start_index:end_index, start_index:end_index] = -1
    
    return modified_array

d = int(input("Number of digits for random integers (d): "))
n = int(input("Size of the main array (n): "))
m = int(input("Size of the central array to be replaced with -1 (m): "))

result = replace_center_with_minus_one(d, n, m)
print(result)
