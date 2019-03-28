from collections import deque
from sys import stdin
def Rotation(numbers,d):
    queue = deque(numbers)
    for i in range(d):
        if d == 0:
            return queue
        else:
            queue.append(queue.popleft())
        d -= 1
    return queue

def main():
    
    numbers = [int(i) for i in stdin.readline().strip().split()]
    d = int(stdin.readline().strip())
    print(*Rotation(numbers,d))
    
main()
