def Dominoes(n): 
  
    arr = [0 for i in range(n+1)]
    arr1 = [0 for j in range(n+1)]
    arr[0],arr[1] = 1,0
    arr1[0],arr1[1] = 0,1

    if n%2 == 1:
        return 0
    
    else:
        
        for i in range(2, n+1):
            
            arr[i] = arr[i - 2] + 2 * arr1[i - 1]
            arr1[i] = arr[i - 1] + arr1[i - 2]
            
        return arr[n]

if __name__ == '__main__':
    
    n = 10
##    n = 3
##    n = 4
##    n = 6
##    n = 8
##    n = 10
    print(Dominoes(n)) 
