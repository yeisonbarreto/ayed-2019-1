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
    return quick_sort(menor) + [pivote] + quick_sort(mayor)
def maxi(lista):
    lista = quick_sort(lista)
    num = lista[-1] *lista[-2]
    return num
def main():
    print('Secuencia de números separados por estacio!')
    x = list(map(int,stdin.readline().strip().split(' ')))
    print(maxi(x))
main()
    
