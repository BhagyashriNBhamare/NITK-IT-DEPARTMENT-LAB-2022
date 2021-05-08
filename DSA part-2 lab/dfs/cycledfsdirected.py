class edgeconnectedtwo(object):
    """docstring for dfsrecursion"""

    def __init__(self, graph):
        super(edgeconnectedtwo, self).__init__()
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
                    des = min(self.start[x], des)
                else:
                    print('true')
                    exit()
        if self.source!=u  and des<self.start[self.parent[u]]:
            print('true')
            exit()
        return des


def main():
    G = []
    file = open('input.txt', 'r')
    for line in file:
        line = line.strip()
        adjacentVertices = []
        first = True
        for node in line.split(' '):
            if first:
                first = False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    print(G)
    f = edgeconnectedtwo(G)
    s = f.edgecon(0)
    if s >=0:
        print('False')

main()       

