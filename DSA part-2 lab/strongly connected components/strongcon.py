class edgeconnectedtwo(object):
    """docstring for dfsrecursion"""

    def __init__(self, graph):
        super(edgeconnectedtwo, self).__init__()
        self.graph = graph
        self.visited = [False]*len(self.graph)
        self.time = 0
        self.start = [None]*len(self.graph)
        # self.parent = [None]*len(self.graph)
        self.source = 0

    def edgecon(self, u):
        self.visited[u] = True
        self.start[u] = self.time
        self.time = self.time+1
        des = self.start[u]
        for x in self.graph[u]:
            if self.visited[x] == False:
                des = min(self.edgecon(x), des)
            else:
                des = min(self.start[x], des)
        if(self.start[u] == des and self.source != u):
            print("strongly connected")
            exit()
        else:
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
    print('start time of deepest edge in 2 way edge connected graph ', s)

main()