from sys import stdin
def quick_sort(lista):
    menor = []
    mayor = []
    if len(lista) == 0:
        return []
    else:
        pivote = lista[0]
        for i in range(1,len(lista)):
            if lista[i] < pivote:
                menor.append(lista[i])
            else:
                mayor.append(lista[i])
    return quick_sort(mayor) + [pivote] + quick_sort(menor)
def main():
    print('Secuencia de números separados por estacio!')
    x = list(map(int,stdin.readline().strip().split(' ')))
    res = quick_sort(x)
    if len(x) <= 10:
        print(x)
    else:
        print(res[:10])
main()
    
