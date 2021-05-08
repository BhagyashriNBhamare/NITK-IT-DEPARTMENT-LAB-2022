from disjoint import *
from numpy.random import randint
class mst(object):
	"""docstring for mst"""
	def __init__(self,graph):
		super(mst, self).__init__()
		self.graph = graph
		self.k=[]
		self.n=len(self.graph)
		for x in range(len(self.graph)):
			for y in self.graph[x]:
				d=[]
				d.append(x+1)
				d.append(y)
				if [y,x+1] not in self.k:
					self.k.append(d)	
	def operation(self):
		y=[]
		dsobj =DisjointSets()
		for x in range(len(self.graph)+1):
			z=dsobj.makeset(x)
			y.append(z)
		n=self.n
		w=len(self.k)
		ans=0
		l={}
		while n>2 and self.k!=[]: 
			v=randint(0,len(self.k)-1)
			# print(v,self.k[v])
			if dsobj.findset(y[self.k[v][0]]).val!=dsobj.findset(y[self.k[v][1]]).val:
				dsobj.union(y[self.k[v][0]],y[self.k[v][1]])
				dsobj.findset(y[self.k[v][0]])
				dsobj.findset(y[self.k[v][1]])
				n=n-1
		for v in range(len(self.k)):
			if dsobj.findset(y[self.k[v][1]]).val!=dsobj.findset(y[self.k[v][0]]).val:
				ans=ans+1
		return ans			
def main():
	G = [] 
	file=open('input1.txt','r')
	for line in file:
		line=line.strip()
		adjacentVertices = []
		first=True
		for edge in line.split(' '):
			if first:
				first=False
				continue
			adjacentVertices.append(int(edge))
		if adjacentVertices!=[]:
			G.append(adjacentVertices)
	file.close()
	# print(G)
	h=mst(G)
	f=float("inf")
	for x in range(1000):
		f=min(f,h.operation())
	print(f)
main()