from sys import stdin
def main(lista,acum):
    if len(lista) == 1:
        return False
    else:
        if lista[0] == lista[1]:
            acum += 1
    if acum > len(lista)/2:
        return True
    else:
        return False

    return main(lista[1:],acum+1)
lista = [2,2,2,2]
acum = 0
