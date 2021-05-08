class solution(object):
	def call(self,X,u):
		file = open("output.txt","w") 
		print("P(x; u) = (e^-u) (u^x) / x!")
		file.write("P(x; u) = (e^-u) (u^x) / x!")
		file.write("\n")
		A=[[0 for x in range(u+X+1)] for y in range(X+1)]

		for x in range(1,X+1):
			for y in range(u,u+X+1):
				a=pow(2.71828,-1*y)
				b=pow(y,x)
				c=self.c(x)
				ans=a*b
				ans=ans*1.0
				ans=ans/c
				print("P("+str(x)+"; "+str(y)+") = e^-"+str(y)+"*"+str(y)+"^"+str(x)+" / "+str(x)+"!  ="+str(a)+"*"+str(b)+"/"+str(c)+" = "+str(ans))
				file.write("P("+str(x)+"; "+str(y)+") = e^-"+str(y)+"*"+str(y)+"^"+str(x)+" / "+str(x)+"!  ="+str(a)+"*"+str(b)+"/"+str(c)+" = "+str(ans))
				file.write("\n")


		print("\n")
		print("\n")
		print("\n")
		print("\n")
		file.write("\n")
		file.write("\n")
		file.write("\n")
		file.write("\n")
		print(" Poison Probability Distribution Table")
		file.write(" Poison Probability Distribution Table")
		file.write("\n")
		print("----------------------------------------------------------------------")
		file.write("----------------------------------------------------------------------")
		s='|       X            '+" | "+'        U            '+'  |  '+'     P(X,U)        |'
		file.write("\n")
		print(s)
		file.write(s)
		file.write("\n")
		print("----------------------------------------------------------------------")
		file.write("----------------------------------------------------------------------")
		file.write("\n")
		# print("\n")
		
		for y in range(u,u+X+1):
			s=0
			for x in range(0,X+1):
				a=pow(2.71828,-1*y)
				b=pow(y,x)
				c=self.c(x)
				ans=a*b
				ans=ans*1.0
				ans=ans/c
				q="|"+'{0:.17f}'.format(x)+"  |  "+'{0:.17f}'.format(y)+"  |  "+'{0:.17f}'.format(ans)+"|"

				w="----------------------------------------------------------------------"
				file.write(q)
				file.write("\n")
				file.write(w)
				file.write("\n")
				s=s+ans
				A[x][y]=s
				print(q)
				print(w)
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		file.write("\n")
		file.write("\n")
		file.write("\n")
		file.write("\n")
		print("Poison Probability sum Distribution Table")
		file.write("Poison Probability sum Distribution Table")
		file.write("\n")
		print("----------------------------------------------------------------------")
		file.write("----------------------------------------------------------------------")
		s='|       X            '+" | "+'        U            '+'  |  '+'     P(X,U)        |'
		file.write("\n")
		print(s)
		file.write(s)
		file.write("\n")
		# file.write("\n")
		print("----------------------------------------------------------------------")
		file.write("----------------------------------------------------------------------")
		file.write("\n")
		for y in range(u,u+X+1):
			for x in range(0,X+1):
			
				q="|"+'{0:.17f}'.format(x)+"  |  "+'{0:.17f}'.format(y)+"  |  "+'{0:.17f}'.format(A[x][y])+"|"
				w="----------------------------------------------------------------------"
				file.write(q)
				file.write("\n")
				file.write(w)
				file.write("\n")
				print(q)
				print(w)







	def c(self,n):
		if n==0:
			return 1
		elif n==1:
			return 1
		else:
			return self.c(n-1)*n
		
def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			a=line.split(" ")
			g.append(a)
	if g[0][0].isdigit() and g[0][1].isdigit():
		x=int(g[0][0])
		u=int(g[0][1])
		if x<0 or u<0:
			file = open("output.txt","w")
			file.write("invalid input")
			print("invalid input")
		else:
			h=solution()
			h.call(x,u)
	else:
		file = open("output.txt","w")
		file.write("invalid input")
		print("invalid input")
main()
