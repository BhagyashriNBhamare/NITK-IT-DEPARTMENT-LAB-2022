class dfsrecursion(object):
        """docstring for dfsrecursion"""
        def __init__(self,graph):
            super(dfsrecursion, self).__init__()
            self.graph = graph
            self.visited=[False]*len(self.graph)
            self.time=0
            self.start=[None]*len(self.graph)
            self.final=[None]*len(self.graph)
            self.path=[]
        def dfs(self,u):
            self.path.append(u)
            self.visited[u]=True
            self.start[u]=self.time
            self.time=self.time+1
            for x in self.graph[u]:
                if self.visited[x]==False:
                    self.dfs(x)
            self.final[u]=self.time
            self.time=self.time+1
        def printdfs(self):
            print(self.path)
            for x in range(len(self.graph)):
                print(x,"start time=",self.start[x],"final time=",self.final[x]) 
   

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
    f=dfsrecursion(G)
    f.dfs(0)
    f.printdfs  ()
main()