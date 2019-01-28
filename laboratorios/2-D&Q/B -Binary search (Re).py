def bbin(a,num,index):
    if len(a) == 1:
        if a[0] == num:
            return index
        else:
            return -1
    else:
        mid = len(a)//2
        if a[mid] > num:
            return bbin(a[:mid],num,index)
        else:
            index += mid
            return bbin(a[mid:],num,index)

def main():
    x = int(input('Número que deseas buscar: '))
    num = input('Lista ordenada de números enteros separados por comas: ')
    num = list(map(int,num.split(',')))
    index = 0
    print(bbin(num,x,index))
main()

