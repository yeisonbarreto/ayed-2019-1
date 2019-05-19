class Node:
        
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

def traversal(root):
    
	if root is None: 
		return
	    
	currentLevel = [] 
	nextLevel = [] 

	condi = True
 
	currentLevel.append(root) 

	while len(currentLevel) > 0: 

		temp = currentLevel.pop(-1) 

		print(temp.data, "", end="") 

		if condi:
			if temp.left: 
				nextLevel.append(temp.right) 
			if temp.right: 
				nextLevel.append(temp.left) 
		else: 
			if temp.right: 
				nextLevel.append(temp.left) 
			if temp.left: 
				nextLevel.append(temp.right) 

		if len(currentLevel) == 0: 
			condi = not condi  
			currentLevel, nextLevel = nextLevel, currentLevel 


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
traversal(root) 
