from sys import stdin
def mergesort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        izq = mergesort(a[:mid])
        der = mergesort(a[mid:])
        a = merge(izq,der)
    return a
def merge(izq,der):
    i = 0
    d = 0
    n = len(izq)
    m = len(der)
    nueva = []
    while i < n and d < m:
        if izq[i] < der[d]:
            nueva += [izq[i]]
            i +=1
        else:
            nueva += [der[d]]
            d += 1
    if i < n:
        while i < n:
            nueva += [izq[i]]
            i += 1
    if d < m:
        while d < m:
            nueva += [der[d]]
            d += 1
    return nueva
def main():
    print('Secuencia de números separados por estacio!')
    x = list(map(int,stdin.readline().strip().split(' ')))
    if len(x) <= 10:
        print(*x)
    else:
        res = mergesort(x)
        res.reverse()
        print(*res[:10])
main()
    
