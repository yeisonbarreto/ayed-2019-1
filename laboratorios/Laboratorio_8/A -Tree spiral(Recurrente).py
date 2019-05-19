class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def printSpiral(root):
    h = height(root)
    condi = False
    for i in range(1, h + 1):
        printGivenLevel(root, i, condi)
        condi = not condi

def printGivenLevel(root, level, condi):
    
    if root == None:
        return
    
    if level == 1:
        print(root.data, end = " ")
        
    elif level > 1:
        
        if condi:
            printGivenLevel(root.left, level - 1, condi)
            printGivenLevel(root.right, level - 1, condi)
        else:
            printGivenLevel(root.right, level - 1, condi)
            printGivenLevel(root.left, level - 1, condi)
def height(node):
    if node == None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return(lheight + 1)
        else:
            return(rheight + 1)
if __name__ == '__main__': 
	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(7) 
	root.left.right = Node(6) 
	root.right.left = Node(5) 
	root.right.right = Node(4) 
	printSpiral(root) 

