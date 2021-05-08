class adancylist(object):
	"""docstring for adancylist"""
	def __init__(self, data):
		super(adancylist, self).__init__()
		self.next=None
		self.data=data
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
		for x in range(self.vertex):
			self.abc[x]=adancylist(x)
	def reverse(self):
		for y in range(self.vertex):
			for x in self.graph[y]:
				z=adancylist(y)
				z.next=self.abc[x].next
				self.abc[x].next=z
	def dfs1(self,u):
		# self.path.append(u)
		self.visited[u]=True
		self.visited[self.abc[u].data]=True
		while self.abc[u]:
			if self.visited[self.abc[u].data]==False:
				self.dfs1(self.abc[u].data)
			self.abc[u]=self.abc[u].next
		self.path.append(u)
	def dfs(self):
		for u in range(self.vertex):
			if self.visited[u]==False:
				self.dfs1(u)
		print(self.path)		
	def pro(self):
		# print(self.path)
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
	h.reverse()
	h.dfs()
	h.pro()
main()						

