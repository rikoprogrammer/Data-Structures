""" Queues - just like normal queues, this work on a FIFO basis, i.e first in first out
or first come first serve.

"""

#Implementation

class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueu(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

#Create an instance of the class and test some of its methods

q = Queue()
q.enqueu(22)
q.enqueu(33)
q.enqueu('bus')
q.enqueu('boy')
q.dequeue()
print(q.isEmpty())
print(q.size())


