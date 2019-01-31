from datetime import datetime
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
    instanteini = datetime.now()
    x = [1,5,3,8,10,22,48,2,1,0,3,6,9]
    if len(x) <= 10:
        print(x)
    else:
        res = mergesort(x)
        res.reverse()
        print(res[:10])
    instantefin = datetime.now()
    time = instantefin - instanteini
    segundos = time.seconds
    print(segundos)
main()
    
