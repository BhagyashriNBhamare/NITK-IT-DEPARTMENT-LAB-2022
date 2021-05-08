class heap(object):
	"""docstring for heap"""
	def __init__(self):
		super(heap, self).__init__()
		self.arr = [5,4,8,12,3,0,11,43,23,6]
		self.n=len(self.arr)
	def buildheap(self):
		startIdx = int((self.n / 2)) - 1
		for i in range(startIdx, -1, -1): 
			self.heapify(self.n, i) 
	def heapify(self,n,i):
		largest = i
		l = 2 * i + 1 
		r = 2 * i + 2
		if (l < n and self.arr[l] < self.arr[largest]): 
			largest = l
		if (r < n and self.arr[r]< self.arr[largest]): 
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
	def insert(self):
		k=input('entre the number')
		y=int(k)
		self.arr.append(y)
		self.n=self.n+1
		k=int(self.n/2-1)
		self.buildheap()

	def printheap(self):
		for x in range (0,self.n):
			print(self.arr[x])


def main():
	h=heap()
	h.buildheap()
	h.printheap()
	# h.min()
	h.insert()
	print('\n')
	h.printheap()
main()	