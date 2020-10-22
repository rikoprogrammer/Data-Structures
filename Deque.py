"""
Deque - this is a collection of items where items can be added from either side, does not conform,
to LIFO nor FIFO rules.

"""

#Python Implementation

class Deque(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self, item):
		return self.items.pop()

	def removeRear(self, item):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

#Create an an instance and test some methods

d = Deque()
d.addFront(1)
d.addRear(2)
d.addFront('car')
d.removeRear(0)
print(d.size())

