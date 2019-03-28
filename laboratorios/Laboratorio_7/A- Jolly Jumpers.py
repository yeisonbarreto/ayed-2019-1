def IsJolly(seq,n):
    new = [int(j) for j in range(1,n)]

    jolly = []
    for i in range(n-1):
        j = abs(seq[i] - seq[i+1])

        if 0 <= j <= n-1:
            jolly.append(j)

    jolly.sort()
    if new == jolly:
        return True
    else:
        return False
    
if __name__ == '__main__':
    
##    seq = [1,4,2,3]
##    seq = [1,4,2,-1,6]
##    seq = [11,7,4,2,1,6]
##    seq = [3,5,2,1]
    seq = [7,2,5,4,-2,1,3]
    print(IsJolly(seq,len(seq)))

