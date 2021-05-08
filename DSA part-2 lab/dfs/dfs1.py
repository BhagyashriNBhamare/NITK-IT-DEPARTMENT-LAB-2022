class dfs:
    def __init__(self,graph):
        super(dfs, self).__init__()
        self.graph= graph
    def pro(self,s):
        path = []
        stack = []
        stack.append(s)
        while stack != []:
            v = stack.pop()
            if v not in path:
                path.append(v)
            for w in self.graph[v]:
                if w not in path:
                    stack.append(w)
        return path
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
    f=dfs(G)
    s=f.pro(0)
    print(s)
main()