import numpy as np

def replace_center_with_minus_one(n, d, m):
    max_value = 10**d - 1
    random_array = np.random.randint(0, max_value+1, size=(n, n))
    
    if m > n or d <= 0 or n < 0 or m < 0:
        print("please follow the value rules and try again.")
       
    else:
        max_value = 10**d - 1
        random_array = np.random.randint(0, max_value+1, size=(n, n))
    
        center_start = (n - m) // 2
        center_end = center_start + m
    
        random_array[center_start:center_end, center_start:center_end] = -1
        print(random_array)
    
        return random_array

replace_center_with_minus_one(5, 9, 3)




