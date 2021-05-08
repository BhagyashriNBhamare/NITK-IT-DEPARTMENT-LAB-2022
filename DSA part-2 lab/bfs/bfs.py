class bfs1:
    """docstring for dfs"""
    def __init__(self,graph):
        super(bfs1, self).__init__()
        self.graph = graph
    def bfs(self,s):
        visited=[False]*(len(self.graph))
        queue=[]
        k=0
        queue.append(s)
        visited[s]=True
        while len(self.graph)!=0:
            while queue:
                s=queue.pop(0)
                print(s)
                for i in (self.graph[s]):
                    if visited[i] == False: 
                        queue.append(i) 
                        visited[i] = True
                        
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
    h=bfs1(G)
    print(h.bfs())
main()