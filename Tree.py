"""Binary tree - represents the nodes connected by edges. Its a non linear data structure. 
It has the following properties:
-one node is marked as Root node.
-every node other than the root is associated with one parent node.
-each node can have an arbitary number of child node.
"""

#Python Implementation

#Create a root node
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

#insert into a tree
	def insert(self, data):

#compare the new value with the parent node
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)

		else:
			self.data = data

#print the tree
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data),
		if self.right:
			self.right.PrintTree()

    	

 #create an instance of the tree and test the insert method
root = Node(12)
root.insert(16)
root.insert(15)
root.insert(20)

print(root.PrintTree())


