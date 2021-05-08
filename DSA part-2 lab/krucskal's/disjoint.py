class Node:
	def __init__(self,x):
		self.val = x
		self.parent = self
		self.rank = 0
class DisjointSets(object):
	def __init__(self):
		self=self

	def makeset(self,i):
		z=Node(i)
		return z

	def findset(self,x):
		if x!=x.parent:
			y=self.findset(x.parent)
			x.parent=y
			return y
		else:
			return x

			
	def union(self,x,y):
		r1=self.findset(x)
		r2=self.findset(y)
		if r1==r2:
			return
		if r1.rank>r2.rank:
			r2.parent=r1
		else:
			r1.parent=r2
			if r1.rank==r2.rank:
				r2.rank=r2.rank+1



		