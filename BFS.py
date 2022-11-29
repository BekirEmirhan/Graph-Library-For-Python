import queue


def BFS(graph):
	g = graph[0]
	g.setColor(1)
	q = queue.Queue([])
	q.enqueue(g)
	while((q.isEmpty())):
		u = q.dequeue()
		print(u.getID())
		adj = u.getAdj()
		for a in adj:
			if a.getColor() == 0:
				a.setColor(1)
				q.enqueue(a)
		u.setColor(2)
