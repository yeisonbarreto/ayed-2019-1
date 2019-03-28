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
    def peek(self):
        if self.head is None:
            return None
        else:
            peek = self.head.value
            return peek
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
 


L = Stack()
L.push(3)
L.push(5)
print(L.pop())
print(L.peek())
L.display()
