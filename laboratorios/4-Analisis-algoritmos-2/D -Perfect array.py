from sys import stdin
def ord_ins(arr):
    cont = 0
    for i in range (len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos -1
        arr[pos] = cursor
        cont = cont +1
    return cont // 2
def main():
    print('Arreglo de enteros')
    x = [int(i) for i in stdin.readline().strip().split()]
    print(ord_ins(x))
main()
