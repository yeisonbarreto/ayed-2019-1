class Node:

        def __init__(self, data):
                self.data = data
                self.left = self.right = None
def printPaths(root):
        path = []
        printPathsRec(root, path, 0)
def printPathsRec(root, path, pathLen):
        if root is None:
                return
        if(len(path) > pathLen):
                path[pathLen] = root.data
        else:
                path.append(root.data)
        pathLen = pathLen + 1

        if root.left is None and root.right is None:
                printArray(path, pathLen)
        else:
                printPathsRec(root.left, path, pathLen)
                printPathsRec(root.right, path, pathLen)
def printArray(ints, len):
        res = []
        for j in ints:
                res.append(str(j))
                res.append('->')
        for i in range(1):
                print(*res[0:-1])

root = Node(6) 
root.left = Node(3) 
root.right = Node(5) 
root.left.left = Node(2) 
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(4)
printPaths(root)
