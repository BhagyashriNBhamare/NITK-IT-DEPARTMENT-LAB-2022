class short(object):
    """docstring for short"""
    def __init__(self,graph):
        super(short, self).__init__()
        self.graph = graph
        self.n=len(self.graph)
        self.arr=[]*len(self.graph)
        self.alarm=[-1]*len(self.graph)
        self.alarm[0]=0
        self.vertex=len(self.graph)
        self.dist=[0]*len(self.graph)
        stack=[0,0]
        self.arr.append(stack)
        for x in range(1,self.vertex):
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
            swap = arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = swap
            self.heapify(n, largest)
    def min(self):
        popped =self.arr[0] 
        self.n=self.n-1
        self.arr[0] = self.arr[self.n] 
        self.n=self.n-1
        self.heapify(self.n,0)
        # print(popped)
        return popped
    def func(self):
            s=self.min()
            v=s[0]
            # print(v)
            visited=[False]*5
            visited[v]=True
            for x in self.graph[v]:
                e=x[0]
                print(e)
def main():
    ''' Adjacency List representation. G is a list of lists. '''
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

    # print(G)
    # print(G[0][0][0])
    # s=[[0,1]]
    # print(s[0][0])
    # print(G[s[0][0]][0][0])
    # stack=[0,0]
    # arr=[]
    # arr.append(stack)
    # for x in range(1,4):
    #     stack=[x,50000]
    #     arr.append(stack)
    # print(arr[1][0])
    print(G)
    h=short(G)
    h.buildheap()
     # h.pointer()
    # # h.min()
    h.func()
    # h.func()
    print(type(G[0][1][0]))
    visited=[False]*5
    print(type(visited[G[0][1][0]]))

if __name__ == '__main__':
    main()