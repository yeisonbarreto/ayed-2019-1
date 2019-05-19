def fastPow(N, K):
    if (K == 0):
        return 1
    temp = fastPow(N, int(K / 2))
    if (K % 2 == 0):
        return temp * temp
    else:
        return N * temp * temp

def countWays(N, K): 
    return K * fastPow(K - 1, N - 1)

N = 6
K = 5
print(countWays(N, K))

