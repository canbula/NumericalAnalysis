def replace_center_with_minus_one(d,n,m):
   if d <= 0 or n <= 0 or m <= 0 or m > n:
       raise ValueError("the requiring conditions was didn't ensure")
    else:
        a=np.array(range(0,n*n)).reshape(n,n)
        for i in range(0,n):
            for j in range(0,n):
                a[i][j]=int(random.random()*(10**d))
        for i in range(0,m):
            for j in range(0,m):
                a[i][j]=-1
        return a
