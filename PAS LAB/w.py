s=raw_input()
M,N=[int(val) for val in s.split()]
w=raw_input()
f=raw_input()
a=list(map(int,w.split()))
b=list(map(float,f.split()))
print(M,N,a,b)
print(b[0]+b[1])