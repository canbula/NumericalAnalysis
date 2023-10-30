import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Value Error: Invalid values")
      
    random_array = np.random.randint(10 ** (d - 1), 10 ** d, size=(n, n))
    
    start_row = (n - m) // 2
    end_row = start_row + m
    start_col = (n - m) // 2
    end_col = start_col + m
  
    random_array[start_row:end_row, start_col:end_col] = -1
    
    return random_array
