# this progran is for directed and undirected graph
class dfs:
    def __init__(self,graph):
        self.graph= graph
    def bfs(self,s):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        popout=[]
        while queue:
            s=queue.pop(0)
            popout.append(s)
            for i in (self.graph[s]):
                if visited[i]==True :
                    if i in queue:
                        return True
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True 
        return False
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
    s=f.bfs(0)
    if s==True:
        print('graph contains cycle') 
    else:
        print('graph not contains cycle')

main()