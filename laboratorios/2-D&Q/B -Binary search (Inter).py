from sys import stdin
def bbin(a,num,index):
    global n 
    if len(a) == 1:
        return 0
    else:
        for i in a:
            if i == num:
                index.append(n)
            n+=1
            if n == len(a) and index == []:
                return -1
        return index  
def main():
    global n
    n = 0
    x = int(input('Número que deseas buscar: '))
    num = input('Lista ordenada de números enteros separados por comas: ')
    num = list(map(int,num.split(',')))
    index = []
    res = bbin(num,x,index)
    print(*res)
main()
