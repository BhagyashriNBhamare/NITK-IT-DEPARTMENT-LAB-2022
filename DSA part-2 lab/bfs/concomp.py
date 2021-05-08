class bfs1:
    """docstring for dfs"""
    def __init__(self,graph):
        super(bfs1, self).__init__()
        self.graph = graph
    def bfs(self):    
        visited=[False]*(len(self.graph))
        k=len(self.graph)
        s=0
        w=[]
        while s!=len(self.graph) :
            if(visited[s]!=True):
                queue=[]
                temp=[s]
                queue.append(s)
                visited[s]=True
                while queue:
                    s=queue.pop(0)
                    for i in (self.graph[s]):
                        if visited[i] == False:
                            temp.append(i) 
                            queue.append(i)
                            visited[i] = True
                w.append(temp)


            s=s+1
        print(w)        
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
    h.bfs()
main()