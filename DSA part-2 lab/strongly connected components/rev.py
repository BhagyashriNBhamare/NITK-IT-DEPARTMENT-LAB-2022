class rev(object):
	"""docstring for graph"""
	def __init__(self,graph):
		super(rev, self).__init__()
		self.graph=graph
		self.vertex =len(self.graph)
		self.abc=[None]*self.vertex
		self.visited=[False]*len(self.graph)
		self.delate=[False]*len(self.graph)
		self.path=[]
		self.w= [list() for i in range(self.vertex)]
		for y in range(self.vertex):
			for x in self.graph[y]:
				self.w[x].append(y)
		print(self.w)
		for u in range(self.vertex):
			if self.visited[u]==False:
				self.dfs1(u)
		print(self.path)
	def dfs1(self,u):
		self.visited[u]=True
		for v in self.w[u]:
			if self.visited[v]==False:
				self.dfs1(v)
		self.path.append(u)	
	def pro(self):
		self.visited=[False]*len(self.graph)
		while self.path!=[]:
			v=self.path.pop()
			if self.delate[v]==False:
				self.visited[v]=True
				self.delate[v]=True
				stack = []
				stack.append(v)
				renge=[]
				while stack != []:
					v = stack.pop()
					if v not in renge:
						renge.append(v)
					for w in self.graph[v]:
						if w not in renge and self.delate[w]==False:
							stack.append(w)
							self.visited[w]=True
							self.delate[w]=True
				print(renge)
def main():
	''' Adjacency List representation. G is a list of lists. '''
	G = [] 

	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		adjacentVertices = []
		first=True
		for node in line.split(' '):
			if first:
				first=False
				continue
			adjacentVertices.append(int(node))
		G.append(adjacentVertices)

	file.close()

	print(G)
	h=rev(G)


	h.pro()
main()						

