class rev(object):
    """docstring for graph"""
    def __init__(self,graph):
        super(rev, self).__init__()
        self.graph=graph
        self.vertex =len(self.graph)
        self.abc=[None]*self.vertex
        self.visited=[False]*len(self.graph)
        self.delate=[False]*len(self.graph)
        self.path=[]
        self.rev=[list() for i in range(len(graph))]
        self.indegree=[0]*len(self.graph)
        self.height=[0]*len(self.graph) 
        for x in range(len(self.graph)):
            for y in self.graph[x]:
                self.indegree[y]=self.indegree[y]+1
        self.e=[]
        self.parent=[None]*len(self.graph)
        for x in range(len(self.graph)):
            if self.indegree[x]==0:
                self.e.append(x)
    def pro(self):
        z=0
        for u in self.e:
            self.height[u]=1
        self.visited=[False]*len(self.graph)
        for v in self.e:
            if self.delate[v]==False:
                self.visited[v]=True
                self.delate[v]=True
                stack = []
                stack.append(v)
                renge=[]
                while stack != []:
                    k = stack.pop()
                    if k not in renge:
                        renge.append(v)
                    for w in self.graph[k]:
                        if w not in renge and self.delate[w]==False:
                            self.height[w]=self.height[k]+1
                            stack.append(w)
                            self.visited[w]=True
                            self.delate[w]=True
                        if z<self.height[w]:
                            z=self.height[w]
        return z

                        
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
    print(h.pro())
main()                      

