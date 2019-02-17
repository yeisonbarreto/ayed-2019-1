from sys import stdin
def main():
    print('Número de enteros a procesar')
    n = stdin.readline().strip()
    f = []
    print('Secuencia de consultas')
    cont = 1
    for i in range(int(n)):
        x = stdin.readline().strip().split(' ')
        if x in f:
            print('2')
        elif x[0] in f:
            cont += 1
            f += (x[1])
        elif x[1] in f:
            cont += 1
            f += (x[0])
        else:
            cont += 1
            f += (x)
            print('2')
    print(cont)
main()
