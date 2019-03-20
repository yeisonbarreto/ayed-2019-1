def friends(n): 
  
    arr = [0 for i in range(n + 1)]
    i = 0

    while n+1 != 0:
  
        if i <= 2: 
            arr[i] = i 
        else: 
            arr[i] = arr[i - 1] + (i - 1) * arr[i - 2]
            
        i += 1
        n -= 1
  
    return arr[n]

if __name__ == '__main__':
    
##    n = 1
##    n = 3
##    n = 4
##    n = 8
    n = 10
    print(friends(n)) 
