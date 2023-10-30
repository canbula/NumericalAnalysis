import numpy as np

'''
d:Number of digits for the random integers.
n:size of the main array.
m:Size of the central array that will be replaced with -1.
'''
def replace_center_with_minus_one(d:int ,n:int ,m:int):


    if ( m>n or d<=0 or n<0 or m<0  ):
        raise ValueError("! Value Error has been ocurred !")

    max_value = 10 ** d - 1
    arr = np.random.randint(max_value, size=(n, n))

    firstPoint =(n-m) //2
    lastPoint = (n-m) //2 +m



    for j in range(firstPoint,lastPoint) :
        for i in range(firstPoint,lastPoint) :
            arr[j,i] = -1

    return arr


print(replace_center_with_minus_one(1,5,2))
