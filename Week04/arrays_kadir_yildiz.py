import numpy as np
import random

def create_array(d, n, m):
    # n-by-n boyutunda bir numpy array oluştur
    main_array = np.random.randint(10 ** (d - 1), 10 ** d, size=(n, n))
    
    # Merkezdeki m-by-m kısmı -1 ile değiştir
    start_index = (n - m) // 2
    end_index = start_index + m
    main_array[start_index:end_index, start_index:end_index] = -1
  
    return main_array
d = 3  
n = 5  
m = 3
