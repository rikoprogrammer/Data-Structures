"""A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to a nother data element in form of a pointer.
"""

#Python Implementation 

class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class LinkedList:
	def __init__(self):
		self.headval = None
    
    #printing the linked list
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print (printval.dataval)
			printval = printval.nextval

	#Inserting at the beginning of the list

	def AtBegin(self, newdata):
		newNode = Node(newdata)

		#update the new nodes next  val to existing node
		newNode.nextval = self.headval
		self.headval = newNode

	#Insert at the end of the list

	def AtEnd(self, newdata):
		newNode = Node(newdata)
		if self.headval is None:
			self.headval = newNode
			return

		laste = self.headval
		while(laste.nextval):
			laste = laste.nextval
		laste.nextval = newNode
 
 #Insert in between two data nodes
	def InBetween(self, middle_node, newdata):
		if middle_node is None:
			print("The node is absent")
			return

		newNode = Node(newdata)
		newNode.nextval = middle_node.nextval
		middle_node.nextval = newNode



#Instantiate the linked list class

List1 = LinkedList()
List1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second node
List1.headval.nextval = e2

#Link second node to third node
e2.nextval = e3

print(List1.listprint())
List1.AtBegin("Sun")
print(List1.listprint())
List1.AtEnd("Thur")
print(List1.listprint())
List1.InBetween(List1.headval.nextval, "Fri")
print(List1.listprint())





