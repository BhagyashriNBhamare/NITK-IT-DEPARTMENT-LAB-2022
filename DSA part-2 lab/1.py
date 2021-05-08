class short(object):
        def __init__(self,graph):
            super(short, self).__init__()
            self.graph = graph
            self.source=int(input('entre the source vertex'))
        def call(self):
            for i in range(len(self.graph)):
                if i!=self.source:
                    h=self.all(i)
                    print(h)
        def all(self,N):
            paths = [[self.source]]
            ans = []
            while paths:
                path = paths.pop()
                for n in graph[path[-1]]:
                    if n == N:
                        ans.append(path + [n])
                    else:
                        paths.append(path + [n])
            return ans
def main():
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
    h=short(G)


main()