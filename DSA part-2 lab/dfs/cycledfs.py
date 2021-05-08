class cycledfs(object):
    """docstring for cycledfs"""
    def __init__(self, graph):
        super(cycledfs, self).__init__()
        self.graph = graph
    def check(self):
        st=[]
        visited=[False]*len(self.graph)
        on_stack=[False]*len(self.graph)
        for w in range(len(self.graph)):
            if visited[w]:
                continue  
            st.append(w)
            while st!=[]:
                s = st.pop()
                st.append(s)
                if visited[s]==False:
                    visited[s] = True
                    on_stack[s] = True
                else:
                    on_stack[s] = False
                    st.pop()
                for v in self.graph[s]:
                    if visited[v]==False:
                        st.append(v)
                    elif on_stack[v]:
                        return True
 
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
    h=cycledfs(G)
    print(h.check())
main()