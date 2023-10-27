import numpy as np

#200315048 AYŞEGÜL EZBER

import numpy as np

def generate_arr(d, n, m):
    if m > n:
        raise ValueError("m should be less than or equal to n")
    if d <= 0:
        raise ValueError("d should be positive")
    if n < 0:
        raise ValueError("n should be non-negative ")
    if m < 0:
        raise ValueError("m should be non-negative")

    rand_arr = np.random.randint(10**(d-1), 10**d, size=(n, n)) #random array
    print("Random array")
    print(rand_arr)
    
    start_idx = (n - m) // 2
    end_idx = start_idx + m
    start_idx = (n - m) // 2
    end_idx = start_idx + m

    
    rand_arr[start_idx:end_idx, start_idx:end_idx] = -1

    return rand_arr

#Example
d = 2  
n = 9
m = 5 

generated_arr = generate_arr(d, n, m)
print("New generated array")
print(generated_arr)
