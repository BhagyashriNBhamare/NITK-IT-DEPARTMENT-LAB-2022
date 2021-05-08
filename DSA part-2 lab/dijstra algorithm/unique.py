class short(object):
	"""docstring for short"""
	def __init__(self,graph):
		super(short, self).__init__()
		self.graph = graph
		self.source=int(input('entre the source vertex'))
		self.n=len(self.graph)
		self.arr=[]*len(self.graph)
		self.alarm=[0]*len(self.graph)
		self.alarm[self.source]=0
		self.vertex=len(self.graph)
		self.dist=[0]*len(self.graph)
		stack=[self.source,0]
		self.b=[True]*len(self.graph)
		self.arr.append(stack)
		for x in range(0,self.vertex):
			if x!=self.source:
				stack=[x,50000]
				self.arr.append(stack)
		self.path=[0]*len(self.graph)
		self.path[self.source]=1
	def buildheap(self):
		startIdx = int((self.n / 2)) - 1
		for i in range(startIdx, -1, -1): 
			self.heapify(self.n, i) 
	def heapify(self,n,i):
		largest = i
		l = 2 * i + 1 
		r = 2 * i + 2
		if (l < n and self.arr[l][1] < self.arr[largest][1]): 
			largest = l
		if (r < n and self.arr[r][1] < self.arr[largest][1]): 
			largest = r
		if (largest != i): 
			swap = self.arr[i]
			self.arr[i] = self.arr[largest]
			self.arr[largest] = swap
			self.heapify(n, largest)

	def min(self):
		popped =self.arr[0] 
		self.arr[0] = self.arr[self.n-1] 
		self.n=self.n-1
		self.heapify(self.n,0) 
		return popped
	def pointer(self):
		for i in range(self.vertex):
			self.dist[self.arr[i][0]]=i
	def func(self):
		k=self.vertex
		visited=[False]*len(self.graph)
		while k!=0:
			s=self.min()
			self.pointer()
			self.printheap()
			v=s[0]
			print('extracted element',v)
			visited[v]=True
			for x in self.graph[v]:
				e=x[0]
				print('adjacent vertex',e,visited[e])
				w=self.dist[e]
				print('position of it heap',w)
				t=self.arr[w][1]
				print('distance in heap',t)
				if visited[e]==False:
					if t>x[1]+self.alarm[v]:
						self.alarm[e]=x[1]+self.alarm[v]
						self.arr[w][1]=self.alarm[x[0]]
						print(v,'from distance of',x[0],'changed to',self.alarm[x[0]])
						if self.b[v]==True:
							self.b[e]=True
						else:
							self.b[e]=False
						self.path[e]=self.path[v]
					elif t==x[1]+self.alarm[v]:
							self.b[e]=False
							self.path[e]=self.path[e]+1	
				self.buildheap()
				self.pointer()
			self.printheap()
			print('\n')	
			k=k-1
		
	def printer(self):
	 	for x in range(self.vertex):
	 		print('shortest distance of',x,'from',self.source,'is',self.alarm[x],self.b[x],'num of path',self.path[x])
	def printheap(self):
		for x in range (0,self.n):
			print(self.arr[x])



def main():
	G = [] 

	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		adjacentVertices = []
		first=True
		for edge in line.split(' '):
			if first:
				first=False
				continue
			node,weight = edge.split(',')
			adjacentVertices.append((int(node),int(weight)))
		G.append(adjacentVertices)
	file.close()
	print(G)
	h=short(G)
	h.buildheap()
	h.printheap()
	h.pointer()
	h.func()
	print('FINAL ANSWER IS')
	h.printer()
	# h.check()


main()