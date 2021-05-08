class adancylist:
	"""docstring for adancylist"""
	def __init__(self, data):
		super(adancylist, self).__init__()
		self.next=None
		self.data=data
class graph:
	"""docstring for graph"""
	def __init__(self,vertex):
		super(graph, self).__init__()
		self.vertex = vertex
		self.abc=[None]*self.vertex
		self.matrix=[]
		for i in range(vertex):
			self.matrix.append([0 for i in range(vertex)])
		for x in range(self.vertex):
			self.abc[x]=adancylist(x)
	def add_edge(self,src,des):
		x=adancylist(des)
		x.next=self.abc[src]
		self.abc[src]=x

		y=adancylist(src)
		y.next=self.abc[des]
		self.abc[des]=y

		self.matrix[src][des]=1
		self.matrix[des][src]=1

	def print(self):
		print('adjency list')
		for x in range(self.vertex):
			print(x,"adjcent vertex",end="")
			while self.abc[x].next:
				print(self.abc[x].data,end = " ")    
				self.abc[x]=self.abc[x].next
			print('\n')
		print("adjency matrix")
		for x in range (self.vertex):
			print(x,'',end="")
			for y in range(self.vertex):
				print(self.matrix[x][y],"",end="")
			print('\n')
def main():
		f=graph(5)
		f.add_edge(0, 1) 
		f.add_edge(0, 4) 
		f.add_edge(1, 2) 
		f.add_edge(1, 3) 
		f.add_edge(1, 4) 
		f.add_edge(2, 3) 
		f.add_edge(3, 4)
		f.print() 
main()




		
			


			
		
		

		



