import numpy as np
def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError()
    if d <= 0:
        raise ValueError()
    if n <= 0 or m <= 0:
        raise ValueError()

    max_value = 10 ** d - 1
    main_array = np.random.randint(low=0, high=max_value + 1, size=(n, n))

    start_index = (n - m) // 2
    end_index = start_index + m
    main_array[start_index:end_index, start_index:end_index] = -1

    return main_array
