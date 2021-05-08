def solve(A):
    c=1
    k=A[0][1]
    w=[0]
    for x in range(1,len(A)):

        if A[w[-1]][1]>=A[x][0]:
            k=min(k,A[x][1])
            if A[w[-1]][1]>A[x][1]:
                print(A[w[-1]][1],A[x][1])
                w[-1]=x
            else:
                if A[w[-1]][1]==A[x][1]:
                    if A[w[-1]][0]>A[x][0]:
                        w[-1]=x
        else:
            c=c+1
            w.append(x)
            k=A[x][1]
        print(w,"hi")
    for x in w:
        print(A[x]),
    return c
def main():
    r=int(raw_input("Enter the number of intervals"))
    A=[]
    for x in range(r):
        s=raw_input()
        a=list(map(int,s.split(" ")))
        A.append(a)
    A= sorted(A, key=lambda x: x[1])
    for x in A:
        print(x)
    solve(A)

main()
