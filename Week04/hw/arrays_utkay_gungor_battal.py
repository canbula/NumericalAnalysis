import numpy as np 

def replace_center_with_minus_one(d, n, m):
  
  if (m > n or d <= 0 or n < 0 or m < 0):
      raise ValueError("Value Error has been ocurred")

  max_val = 10**d -1
  arr = np.random.randint(0, max_val + 1, (n, n))

  start_index = (n - m) // 2
  end_index = start_index + m

  arr[start_index:end_index, start_index:end_index] = -1
  return arr

