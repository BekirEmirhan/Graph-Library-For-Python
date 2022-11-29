
def visit(g): ## Its definition and analysis made in DFS function
	"""
		g: Graph
		it traverse the graph given DFS rule.

	"""
	g.setColor(1)
	t = g.getAdj()
	for g2 in t:
		print(g2.getID())
		if(g2.getColor() == 0):
			visit(g2)
	g.setColor(2)




gl = 0 #check condition for if there is cycle condition
def detectCycle(g,trace): 
	"""
		It can detects if there is cycle in given graph
		g : Graph
		trace: empty list to append cycled nodes

	"""
	global gl
	trace.append(g.getID())
	g.setColor(1)
	t = g.getAdj()
	for g2 in t:
		if g2.getColor() == 1:
			a = g2.getID()
			flag = 0
			num = 0
			lists = []
			for i in trace:
				if(a==i):
					flag =1
				if(flag==1):
					num+=1
					lists.append(i)
			return True
		elif(g2.getColor() == 0):
			visit(g2,trace)
	g.setColor(2)
	return False

def DFSVisit(graph):
	"""
		graph : list of Graph object
		This is the Depth First Algorithm:
		Also we are searching for directed graph where V: number of vertices, E: number of edges
		Thus:
			Time complexity: O(V+E) we must traverse all edges and vertices
			Space complexity: O(V^2) for each vertex there is maximum number of edges for each vertex A we have maximum V-1 edges
			so V*(V-1) => O(V^2)
		There is 3 colors black:2, gray:1, white: 0
		The algoritm only visit white nodes for each visiting, Visit function turns the vertex color into gray each white vertex.
		If the vertex hasn't got any white adjacent vertex, its color turned into black
		If the vertex has any gray adjacent vertex then there is cycle.However, In visit function, we have trace list which is hold
		visited vertices in the road so if there is cycle, we count number of elements in trace list. Number of elements is odd then
		print true, else false.

	"""
	for g in graph:
		if g.getColor() == 0:
			print(g.getID())
			visit(g)






def DFSDetectCycle(graph):
	"""
		graph : list of Graph object

	"""
	for g in graph:
		if g.getColor() == 0:
			detectCycle(g,[])


