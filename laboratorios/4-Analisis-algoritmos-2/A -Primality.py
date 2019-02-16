from sys import stdin
def prime(numero):
    for i in range(2,numero):
        if (numero%i) == 0:
            return "No"
    return "Si"
def val(x):
    if len(x) == 1:
        return prime(int(x[0]))
    else:
        return prime(int(x[0]))+" "+val(x[1:])
def main():
    print('Número de enteros a procesar')
    a = stdin.readline().strip()
    print('Secuencia de enteros')
    x = stdin.readline().strip().split(' ')
    print(val(x)) 
main()
