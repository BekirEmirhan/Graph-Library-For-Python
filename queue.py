class Queue:
	def __init__(self,queue):
		self.queue = queue
	def enqueue(self,s):
		self.queue.insert(0,s)
	def dequeue(self):
		temp = self.queue.pop()
		return temp
	def getQueue(self):
		return self.queue
	def isEmpty(self):
		return bool(self.queue)



if __name__ == "__main__":
	q = Queue([])
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(2)
	q.dequeue()
	print(q.getQueue())
