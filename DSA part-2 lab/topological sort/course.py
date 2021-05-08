class Solution:
    def findOrder(self,s):
        num =int(input('entre the number of courses'))
        # s=[]
        # x=int(input('if any dependent courses r there then press 1 or more than 1'))
        # while x!=0:
        #     y=[]
        #     x=int(input('entre the dependent of course'))
        #     z=int(input('entre the course on which it depend'))
        #     y.append(x)
        #     y.append(z)
        #     s.append(y)
        #     x=int(input('press 0 to exit'))
        # print(s)
        w= [list() for i in range(num)]
        if s==[]:
            return 1 
        indegree=[0]*len(w)
        for x in s:
            k=x[0]
            t=x[1]
            w[t].append(k)
            indegree[k]=indegree[k]+1
        e=[]
        parent=[None]*len(w)
        for x in range(len(w)):
            if indegree[x]==0:
                e.append(x)
        if e ==[]:
            print('we cant complete any course all couses are dependent on each other')
            exit()
        print(e)
        z=1
        path=[]
        height=[0]*len(w) 
        while e!=[]: 
            x=e.pop()
            print(x,'extracted element')
            height[x]=1
            f=[]
            f.append(x)
            while f!=[]:
                k=0
                y=f.pop()
                if y not in path:
                    path.append(y)
                print(y,'extracted element from middle stack')
                for v in w[y]:
                    indegree[v]=indegree[v]-1
                    parent[v]=y
                    if height[v] is None:
                        height[v]=height[y]+1
                    else:
                        if height[y]+1>height[v]:
                            height[v]=height[y]+1
                    if indegree[v]==0:
                        f.append(v)
                if height[y]>z:
                    z=height[y]
                    print(z)
        if len(path)==num:
            print(path)
            return z
        else:
            print('u cant complete the course because detected a cycle')
            exit()
def main():
    # s=[[1,0],[2,1],[3,2],[5,4],[7,6],[8,6],[8,9],[3,4]]
    s=[[1,0],[2,0],[3,1],[4,1],[5,2],[6,3]]
    # s=[[1,0],[2,0],[3,1],[4,1],[5,2],[6,2]]
    h=Solution()
    print('min number of semester',h.findOrder(s))
main()

        
        
        