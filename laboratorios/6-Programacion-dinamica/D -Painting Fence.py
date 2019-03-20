def ways(n, k) : 
  
    if n == 1:
        return k
    
    elif n == 2:
        return k*k
    
    elif n == 3:
        return k * (k-1 +(k-1)*k)
    
    else:
        return k * ways(n-1,k)- ways(n-3,k)*(k-1)
  

if __name__ == "__main__" : 
  
##    n, k = 2,4
##    n, k = 3,2
##    n, k = 6,3
    n, k = 5,2
    print(ways(n, k))  
  

