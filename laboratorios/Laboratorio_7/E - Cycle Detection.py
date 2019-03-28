class Node:
    def __init__(self, value):
       self.value = value
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        if self.head is None:
            return None
        else:
            pop = self.head.value
            self.head = self.head.next
            return pop
##        
##    def CycleDetection(self):
##        s = set()
##        temp = self.head
##        while temp:
##            if temp in s:
##                return False
##            s.add(temp)
##            temp = temp.next
##        return True
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
 


L = Stack()
L.push(50)
L.push(20)
L.push(15)
L.push(4)
L.push(10)
L.push(15)
##if L.CycleDetection():
##    print(False)
##else:
##    print(True)
##    L.pop()

##print(L.pop())
##print(L.peek())
L.pop()

L.display()
