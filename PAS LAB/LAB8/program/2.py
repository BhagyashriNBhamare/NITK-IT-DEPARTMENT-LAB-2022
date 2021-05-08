 def solve(self, A):
        A= sorted(A, key=lambda x: x[1])
        c=1
        k=A[0][1]
        w=[0]
        for x in range(1,len(A)):
            if A[w[-1]][1]>=A[x][0]:
                k=min(k,A[x][1])
                if A[w[-1]][1]>A[x][1]:
                    w[-1]=x
                else:
                    if A[-1][1]==A[x][1]:
                        if A[w[-1]][0]>A[x][0]:
                            w[-1]=x
            else:
                c=c+1
                w.append(x)
                k=A[x][1]
        for x in w:
            print(A[x]),
        return c
def main():
    r=raw_input()
    a=list(map(int,r.split(" ")))
    r=raw_input()
    b=list(map(int,r.split(" ")))
    A=[]
    for x in range(len(a)):
        A.append([a[x],b[x]])
    solve(a)
