import numpy  as np

def replace_center_with_minus_one(d,n,m):
    if(m>n):
        raise Exception("m cannot be greater than n")
    if(d<=0):
        raise Exception("d cannot be less than  or equal to 0")
    if(n<0):
        raise Exception("n cannot be less than 0")
    if(m<0):
        raise Exception("m cannot be less than 0")
    a = 10**d
    b = a / 10 -1
    my_arr = np.random.randint(b,a,size=(n,n))
    for i in range(m,0,-1):
        for j in  range(m,0,-1):
            my_arr[i][j]=-1
    
    return my_arr


print(replace_center_with_minus_one(2,6,4))

    
