from disjoint import *
import disjointnotcom as e
from disjointnotcom import *
import time
class mst(object):
	"""docstring for mst"""
	def __init__(self,graph):
		super(mst, self).__init__()
		self.graph = graph
		self.k=[]
		for x in range(len(self.graph)):
			for y in self.graph[x]:
				d=[]
				d.append(x)
				d.append(y[0])
				d.append(y[1])
				self.k.append(d)
		self.k= sorted(self.k, key=lambda x: x[2])
		print(self.k)	
	def operation(self):
		y=[]
		dsobj =DisjointSets()
		for x in range(len(self.graph)):
			z=dsobj.makeset(x)
			y.append(z)
		t=[]
		n=0
		k=0
		z=len(self.graph)
		for x in self.k:
			k=k+1
			if dsobj.findset(y[x[0]]).val!=dsobj.findset(y[x[1]]).val:
				t.append(x)
				n=n+1
				dsobj.union(y[x[0]],y[x[1]])
			if n==z-1:
				return t
class mst1(object):
	"""docstring for mst"""
	def __init__(self,graph):
		super(mst1, self).__init__()
		self.graph = graph
		self.k=[]
		for x in range(len(self.graph)):
			for y in self.graph[x]:
				d=[]
				d.append(x)
				d.append(y[0])
				d.append(y[1])
				self.k.append(d)
		self.k= sorted(self.k, key=lambda x: x[2])
		print(self.k)	
	def operation(self):
		y=[]
		dsobj =e.DisjointSets()
		for x in range(len(self.graph)):
			z=dsobj.makeset(x)
			y.append(z)
		t=[]
		n=0
		k=0
		z=len(self.graph)
		for x in self.k:
			k=k+1
			if dsobj.findset(y[x[0]]).val!=dsobj.findset(y[x[1]]).val:
				t.append(x)
				n=n+1
				dsobj.union(y[x[0]],y[x[1]])
			if n==z-1:
				return t
class short(object):
	"""docstring for short"""

	def __init__(self,graph):
		super(short, self).__init__()
		self.graph = graph
		self.source=int(input('entre the source vertex'))
		self.n=len(self.graph)
		self.arr=[]*len(self.graph)
		self.vertex=len(self.graph)
		self.dist=[0]*len(self.graph)
		self.pre=[None]*len(self.graph)
		self.k=[]
		stack=[self.source,0]
		self.arr.append(stack)
		for x in range(0,self.vertex):
			if x!=self.source:
				stack=[x,50000]
				self.arr.append(stack)
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
		# self.heapify(self.n,0) 
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
			v=s[0]
			# print('extracted element',v)
			if self.pre[v] is not None:
				stack=[self.pre[v],v,s[1]]
				self.k.append(stack)
			visited[v]=True
			for x in self.graph[v]:
				e=x[0]
				# print('adjacent vertex',e,visited[e])
				if visited[e]==False:
					w=self.dist[e]
					# print('position of it heap',w)
					t=self.arr[w][1]
					# print('distance in heap',t)
					if t>x[1]:
						self.arr[w][1]=x[1]
						self.pre[e]=v
						# print(self.arr[w][1])
			self.buildheap()
			self.pointer()
			# self.printheap()
			# print('\n')
			k=k-1
		return self.k
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

	start=time.time()
	h=mst(G)
	f=h.operation()
	print('minimum spanning tree is ')
	print(f)
	total=time.time()-start
	print(total)


	start=time.time()
	h=mst1(G)
	f=h.operation()
	print('minimum spanning tree is ')
	print(f)
	total=time.time()-start
	print(total)

	start=time.time()
	h=short(G)
	h.buildheap()
	h.pointer()
	z=h.func()
	print(z)
	total=time.time()-start
	print(total)
main()