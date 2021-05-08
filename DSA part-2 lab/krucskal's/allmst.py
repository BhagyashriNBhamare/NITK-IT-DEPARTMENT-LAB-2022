from disjoint import *
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
		self.y=[]
		dsobj =DisjointSets()
		for x in range(len(self.graph)):
			z=dsobj.makeset(x)
			self.y.append(z)
		t=[]
		n=0
		k=0
		z=len(self.graph)
		for x in self.k:
			k=k+1
			if dsobj.findset(self.y[x[0]]).val!=dsobj.findset(self.y[x[1]]).val:
				t.append(x)
				n=n+1
				dsobj.union(self.y[x[0]],self.y[x[1]])
			if n==z-1:
				return t
	def call(self):
		dsobj =DisjointSets()
		h=self.operation()
		for x in h:
			self.k.remove(x) 
		s=[]
		self.all=[]
		self.all.append(h)
		for x in h:
			a=x[2]
			b=x[0]
			d=x[1]
			for c in self.k:
				if c[2]==a:
					s=[]
					if c[1]==d or c[1]==b or c[0]==d or c[0]==b:
						if dsobj.findset(self.y[x[0]]).val==dsobj.findset(self.y[x[1]]).val:
							s.append(c)
							for i in h:
								s.append(i)
							s.remove(x)
							self.all.append(s)
		for h in self.all:
			print(h)





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
	h=mst(G)
	h.call()
main()