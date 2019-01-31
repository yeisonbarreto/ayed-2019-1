from sys import stdin
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
         
    return merged
def main():
    print('Número de elementos en la secuencia!')
    num = int(input())
    print('Secuencia de números separados por estacio!')
    x = list(map(int,stdin.readline().strip().split(' ')))
    if len(x) <= 1:
        print(x)
    else:
        res = merge_sort(x)
        r = res[0] , res[-1]
        print(*r)
main()
    
