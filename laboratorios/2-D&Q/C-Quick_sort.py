def quick_sort(lista):
    if len(lista) == 0:
        return []
    else:
        pivote = lista[0]
        menor = quick_sort([k for k in lista[1:] if k < lista[0]])
        mayor = quick_sort([k for k in lista[1:] if k >= pivote])
        return menor + [pivote] + mayor
lista = [-6,2,-12,8,3]
    
