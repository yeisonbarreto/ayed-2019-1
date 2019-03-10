from sys import stdin
def memorization(Coins, N):
    array = [[0 for _ in range(N + 1)] for _ in range(len(Coins) + 1)]

    for i in range(N + 1):
        array[0][i] = i

    return array

def Coins_Change(Coins, N):
    array = memorization(Coins, N)

    for i in range(1, len(Coins) + 1):

        for j in range(1, N + 1):
            
            if Coins[i - 1] == j:
                array[i][j] = 1
                
            elif Coins[i - 1] > j:
                array[i][j] = array[i - 1][j]
                
            else:
                array[i][j] = min(array[i - 1][j], 1 + array[i][j - Coins[i - 1]])

    return array[1][-1]
def main():
    N = int(stdin.readline().strip())
    Coins = eval(stdin.readline().strip())
    print(Coins_Change(Coins, N))
main()
            
