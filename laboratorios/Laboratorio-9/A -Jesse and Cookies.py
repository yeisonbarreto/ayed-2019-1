from sys import stdin
from collections import deque
def Jesse(arr,y):
    dequeue = deque(arr)
    
    cont = 0
    for i in range(len(arr)):
        if sweetness <= y:
            sweetness = 1 * dequeue[0] + 2 * dequeue[1]
            print('--',sweetness)
            print(dequeue.popleft())
            print(dequeue.popleft())
            dequeue.append(sweetness)
            print('***',sorted(dequeue))
            cont += 1
    print(cont)
    
def main():
    
    x,y = stdin.readline().strip().split()
    arr = [int(i) for i in stdin.readline().strip().split()]
    Jesse(sorted(arr),int(y))
    
main()
