def fibonum(n): # Give the nth fibonacci number 
    x=[0,1] 
    for i in range(2,n):
        x.append(x[i-2]+x[i-1]) 
    print(x[n-1])
n = 281621358815590
