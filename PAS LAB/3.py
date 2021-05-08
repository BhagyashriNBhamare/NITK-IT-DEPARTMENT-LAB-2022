class solution(object):
	"""docstring for ClassName"""
	def cal(self,m,a,n):
		ans=0
		for x in range(0,n+1):
			ans=ans+pow(x,m)+a
		print("summation of f(x)=x^m+a is for m="+str(m)+" a="+str(a)+" n="+str(n)+" is "+str(ans))
		return 1.0/ans
def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			g.append(line)
	# print(g)
	file = open("output.txt","w") 
	k=1
	for x in range(0,len(g),4):
		m=int(g[x+1])
		a=int(g[x+2])
		n=int(g[x+3])
		if a<0 or n<0:
			file.write("invalid output for test case"+str(k)+"\n")
		else:
			h=solution()
			d=h.cal(m,a,n)
			print("value of c is "+str(d)+"\n")
			file.write("output for test case "+str(k)+" is "+str(d)+"\n")
		k=k+1
main()
