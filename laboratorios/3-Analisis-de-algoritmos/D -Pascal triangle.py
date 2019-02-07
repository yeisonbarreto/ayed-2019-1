from sys import stdin
def trianPascal(x):
    lista = [[1],[1,1]]
    for i in range(1,x):
        linea = [1]
        for j in range(0,len(lista[i])-1):
            linea.extend([lista[i][j] +lista[i][j+1]])
        linea += [1]
        lista.append(linea)
    return lista
def main():
    print('Número entero!')
    x = int(stdin.readline().strip())
    res = trianPascal(x-1)
    cont = x
    for i in res:
        cont = cont -1
        print('  '* cont,'   '.join([str(c) for c in i]))
main()
