#stacks - a collection of objects based on LIFO criteria i.e last in object 
#is the first object to come out

#Implementation
class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) -1]

	def size(self):
		return len(self.items)

#create an instance of the stack and test few methods
s = Stack()
s.push(2)
s.push(44)
s.push('cars')
s.push('tree')
s.pop()
print(s.size())
print(s.peek())
print(s.isEmpty())
print(s.size())