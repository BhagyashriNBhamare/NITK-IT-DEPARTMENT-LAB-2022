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
		self.k=sorted(self.k, key=lambda x: x[2])
		print(self.k)	
	def operation(self):
		y=[]
		dsobj =DisjointSets()
		for x in range(len(self.graph)):
			z=dsobj.makeset(x)
			y.append(z)
		t=[]
		n=0
		z=len(self.graph)
		for x in self.k:
			if dsobj.findset(y[x[0]]).val!=dsobj.findset(y[x[1]]).val:
				t.append(x)
				n=n+1
				dsobj.union(y[x[0]],y[x[1]])
			if n==z-1:
				return t
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
	f=h.operation()
	print('minimum spanning tree is ')
	print(f)
main()