class bfs1:
    """docstring for dfs"""
    def __init__(self,graph):
        super(bfs1, self).__init__()
        self.graph = graph
    def bfs(self,s):
        color=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        color[s]='red'
        while queue:
            s=queue.pop()
            for i in (self.graph[s]):
                if color[i] == False:
                    if color[s]=='red':
                        color[i]='blue'
                    else:
                        if color[s]=='blue':
                            color[i]='red'
                    queue.append(i)
                if color[i]==color[s]:
                    return False
        return True                        
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

    # print(G)
    a=bfs1(G)
    h=a.bfs(0)
    if(h==True):
        print('its bipartite graph')
    else:
        print('its not a bipartite graph')
main()