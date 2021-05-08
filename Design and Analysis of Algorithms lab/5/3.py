import collections
def solve(A):
    A=sorted(A, key=lambda x: x[1])
    i=1
    j=0
    c=1
    m=1
    w=collections.defaultdict(list)
    w[1].append(A[0])
    while i<len(A):
        while j<i and A[j][1]<=A[i][0]:
            c=c-1
            j=j+1
        c=c+1
        m=max(c,m)
        for y in range(1,m+1):
            if y in w:
                if w[y][-1][1]<A[i][0]:
                    w[y].append(A[i])
                    break
            else:
                w[y].append(A[i])
        i=i+1
    for x in w:
        print("region",x)
        for y in w[x]:
            print(y),
        print("\n")
def main():
    r=int(raw_input("Enter the number of intervals"))
    A=[]
    for x in range(r):
        s=raw_input()
        a=list(map(int,s.split(" ")))
        A.append(a)
    A= sorted(A, key=lambda x: x[1])
    solve(A)

main()


            