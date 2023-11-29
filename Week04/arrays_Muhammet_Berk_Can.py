import numpy as np

def replace_center_with_minus_one(d, n, m):
    """
    :param d: Number of digit for the random integers.
    :param n: Size of the main array.
    :param m: Size of the center array that will be replaced with '-1'.
    :return: A modified numpy array with its center replaced by '-1'.
    """

    if(m > n or d <= 0 or n < 0 or m < 0):
        raise ValueError

    min_val = 10 ** (d -1)   #Minimum value for 'd' digit number
    max_val = 10 ** d - 1    #Maximum value for 'd' digit number
    array = np.random.randint(min_val, max_val, size=(n, n)) #Creating n-by-n array with random 'd' digit numbers

    first_point = (n - m) // 2      # m-by-m array's start index to be replaced by -1
    last_point = (n - m) // 2 + m   # m-by-m array's end index to be replaced by -1


    for i in range(first_point, last_point):    # Replacing the center of the n-by-n matrix with m-by-m '-1' matrix
        for j in range(first_point, last_point):
            array[i,j] = -1

    return array

print(replace_center_with_minus_one(3, 9, 3))
