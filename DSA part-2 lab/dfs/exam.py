class edge(object):
    """docstring for dfsrecursion"""

    def __init__(self, graph):
        super(edge, self).__init__()
        self.graph = graph
        self.visited = [False]*len(self.graph)
        self.time = 0
        self.start = [None]*len(self.graph)
        self.parent = [None]*len(self.graph)
        self.source = 0
    def edgecon(self, u):
        self.visited[u] = True
        self.start[u] = self.time
        self.time = self.time+1
        des = self.start[u]
        for x in self.graph[u]:
            if self.visited[x] == False:
                self.parent[x] = u
                des = min(self.edgecon(x), des)
            else:
                if self.parent[u] != x:
                    des=min(self.start[x], des)
        if u!=self.source:
            if(des>self.start[self.parent[u]]):
                print(u,"and",self.parent[u])
        return des
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
    h=edge(G)
    h.edgecon(0)


main()