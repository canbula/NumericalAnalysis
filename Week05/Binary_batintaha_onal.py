import numpy as np
def detArrLen(x):
    a = 1
    count = 0
    while x > a:
        a *= 2
        count+=1
    return count
def detArrLen2(x):
    a = 0.5
    count = 1
    while x != 0:
        if (x >= a):
            x -= a
            continue
        count += 1
        a/=2
    return count
def setArr(a):
    arr = np.zeros(a)
    b = a - 1
    for i in range(0,len(arr)):
        arr[i]=2**b
        b-=1
    return arr
def setArr2(a):
    b = (-a)
    arr=np.zeros(a)
    for i in range((len(arr)-1),-1,-1):
        arr[i]=2**b
        b+=1
    return arr
def convertBinary(b):
    arr=np.zeros(detArrLen(b))
    arr=setArr(detArrLen(b))
    arr2=np.zeros(len(arr))
    i = 0
    while i != len(arr):
        if (b >= arr[i]):
            b %= arr[i]
            arr2[i] = 1
        i+=1
    return arr2
def convertBinary2(x):
    arr=np.array(setArr2(detArrLen2(x)))
    arr2=np.zeros(len(arr))
    i = 0
    a = 0.5
    while x != 0:
        if x >= a:
            x -= a
            arr2[i]=1
            continue
        i+=1
        a/=2
    return arr2
def displayWholeNumber (arr,arr2):
    for i in range(0,len(arr)):
        print(int(arr[i]),end="")
    print(".",end="")
    for i in range(0,len(arr2)):
        print(int(arr2[i]),end="")
displayWholeNumber(convertBinary(54),convertBinary2(0.375));
