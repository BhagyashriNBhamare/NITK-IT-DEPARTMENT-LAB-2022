class dfs:
    def __init__(self,graph):
        super(dfs, self).__init__()
        self.graph= graph
        self.path = []
        self.start=[None]*len(self.graph)
        self.finish=[None]*len(self.graph)
        self.time=0
        self.stack=[]
    def pro(self,s):
        self.stack.append(s)
        visited=[False]*len(self.graph)
        visited[s]=True
        while self.stack!=[]:
            k=0
            v=self.stack.pop()
            self.start[v]=self.time
            self.time=self.time+1
            print(self.start[v],'start at',v)
            if v not in self.path:
                self.path.append(v)
            for w in self.graph[v]:
                if visited[w]==False:
                    self.stack.append(w)
                    visited[w]=True
                else:
                    if self.start[w]<self.start[v]:
                        k=k+1 
            if k==len(self.graph[v]):
                self.finish[v]=self.time
                self.time=self.time+1
                print(v)
                self.call()
        print(self.path)
    def call(self):
        self.path.pop()
        while self.path!=[]:
            v=self.path.pop()
            for x in self.graph[v]:
                if x in self.stack:
                    self.path.append(v)
                    print(x)
                    return
            self.finish[v]=self.time
            self.time=self.time+1
            
    def print(self):
        for x in range(len(self.graph)):
            print(x,':start time ',self.start[x],'finish time',self.finish[x])
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
    f.pro(0)
    f.print()
main()
