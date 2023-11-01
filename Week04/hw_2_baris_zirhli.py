def replace_center_with_minus_one(n: int, m: int, d: int) -> np.ndarray:
    
    if ( d <= 0 or n < 0 or m < 0 or m > n ):
        raise ValueError("Invalid parameter detection")
    
    base_array = np.random.randint(0, 10**d-1, size=(n, n))
    # We assume dimensions are always odd numbers
    subArray_start = (n - m) // 2
    subArray_end = subArray_start + m
    base_array[subArray_start:subArray_end, subArray_start:subArray_end] = -1
    return base_array


print(replace_center_with_minus_one(7, 5, 3))
