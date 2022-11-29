import DFS
import BFS
class Graph:
	def __init__(self,adj,id,color=0):
		self.adj = adj # this is the list of neighbor
		self.id = id
		self.color = 0
	def getAdj(self):
		return self.adj
	def getColor(self):
		return self.color
	def setColor(self,new_color):
		self.color = new_color
	def getID(self):
		return self.id

def clearGraph(graph):
	for g in graph:
		g.setColor(0)

if __name__ == "__main__":
	size=6
	graphs = [[2,6],[3],[4],[5],[3,6],[]]
	mainG = []
	for i in range(size): # O(V) putting vertices into list
		mainG.append(Graph([],i+1))


	for i in range(len(graphs)): # O(V^2) setting all adjacents 
		t = mainG[i]
		t2 = t.getAdj()
		for j in range(len(graphs[i])):
			t2.append(mainG[graphs[i][j]-1])
	BFS.BFS(mainG)
	clearGraph(mainG)
	print("-------")
	DFS.DFSVisit(mainG)
