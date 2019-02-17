from sys import stdin
def toy(x,n,t):
    if t == 0 or n == 0:
        return 0
    elif x[t-1] > n:
        return toy(x[:],n,t-1)
    else:
        return max(toy(x[:],n,t-1),1+toy(x[:],n-x[t-1],t-1))
def main():
    print('Lista de precio de los jugetes')
    x = [int(i) for i in stdin.readline().strip().split()]
    print('Presupuesto disponible para comprar los jugetes')
    n = stdin.readline().strip()
    print(toy(x,int(n),len(x)))
main()
