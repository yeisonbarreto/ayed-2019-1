from sys import stdin
def main(lista):
    if len(lista) == 1:
        return False
    else:
        acum = 0
        for i in range(len(lista)):
            if lista[0] == lista[i]:
                acum += 1
    if acum > len(lista)/2:
        return True
    else:
        return False
lista = [1,2,3]
