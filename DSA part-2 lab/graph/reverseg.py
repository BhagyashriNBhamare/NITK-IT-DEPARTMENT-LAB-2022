class adancylist:
	"""docstring for adancylist"""
	def __init__(self, data):
		super(adancylist, self).__init__()
		self.next=None
		self.data=data
class rev:
	"""docstring for graph"""
	def __init__(self,graph):
		super(rev, self).__init__()
		self.graph=graph
		self.vertex =len(self.graph)
		self.abc=[None]*self.vertex
		for x in range(self.vertex):
			self.abc[x]=adancylist(x)
	def reverse(self):
		for y in range(self.vertex):
			for x in self.graph[y]:
				z=adancylist(y)
				z.next=self.abc[x]
				self.abc[x]=z
	def print(self):
		print('adjency list')
		for x in range(self.vertex):
			print(x,"adjcent vertex",end="")
			while self.abc[x].next:
				print(self.abc[x].data,end = " ")    
				self.abc[x]=self.abc[x].next
			print('\n')
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
    h.print()
main()						

