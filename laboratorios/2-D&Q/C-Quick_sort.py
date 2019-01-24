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
lista = [-6,2,-12,8,5,3,-98,55]
    
