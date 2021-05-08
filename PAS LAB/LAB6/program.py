class solution(object):
	def call(self,n,oranges,apples,banana):
		file = open("output6.txt","w") 
		total=apples+banana+oranges
		file.write("Number of fruits to be selected "+str(n)+"\n")
		print("Number of fruits to be selected "+str(n)+"\n")
		file.write("Number of apples fruits "+str(apples)+"\n")
		print("Number of apples fruits "+str(apples)+"\n")
		file.write("Number of banana fruits "+str(banana)+"\n")
		print("Number of banana fruits "+str(banana)+"\n")
		file.write("Number of oranges fruits "+str(oranges)+"\n")
		print("Number of oranges fruits "+str(oranges)+"\n")
		file.write("Total number of fruits "+str(total)+"\n \n")
		print("Total number of fruits "+str(total)+"\n \n")
		w=[]
		for x in range(oranges+1):
			for y in range(apples+1):
				if x+y<=n:
					w.append([x,y])
		
		M=self.c(apples+banana+oranges,n)
		file.write("possible set of x,y is "+str(w)+"\n \n")
		print("possible set of x,y is "+str(w)+"\n \n")
		file.write("number  of ways to select "+str(n)+" fruits form "+str(total)+" is "+str(total)+"C"+str(n)+" = "+str(M)+"\n \n")
		print("number  of ways to select "+str(n)+" fruits form "+str(total)+" is "+str(total)+"C"+str(n)+" = "+str(M)+"\n \n")
		file.write("---------------------------------------------------------------------------------------------\n")
		file.write(" probability function f(x, y) = ("+str(oranges)+'C'+"x"+"*"+str(apples)+'C'+"y"+"*"+str(banana)+'C'+'('+str(n)+'-x-y)) /'+str(total)+"C"+str(n)+"\n \n" )
		print(" probability function f(x, y) = ("+str(oranges)+'C'+"x"+"*"+str(apples)+'C'+"y"+"*"+str(banana)+'C'+'('+str(n)+'-x-y)) /'+str(total)+"C"+str(n)+"\n \n" )
		print(" probability function f(x, y) = ("+str(oranges)+'C'+"x"+"*"+str(apples)+'C'+"y"+"*"+str(banana)+'C'+'('+str(n)+'-x-y)) /'+str(total)+"C"+str(n)+"\n \n" )

		file.write("---------------------------------------------------------------------------------------------\n")
		d=[[0 for x in range(n+1)]for x in range(n+1)]
		print(w)
		for x in w:
			e=self.c(oranges,x[0])*self.c(apples,x[1])*self.c(banana,n-(x[1]+x[0]))
			h=e/(1.0*M)
			c=n-(x[1]+x[0])
			file.write("Number  of ways to  select  "+str(x[0])+" oraanges fruits, "+str(x[1])+" apple fruits and "+str(c)+" banana fruits from  "+str(total)+" fruits is "+str(apples)+'C'+str(x[0])+"*"+str(banana)+'C'+str(x[1])+"*"+str(oranges)+'C'+str(c)+" = "+str(e)+"\n")
			file.write("Probability of  selecting "+str(x[0])+" orange fruits, "+str(x[1])+" apple fruits and "+str(c)+" banana fruits from  "+str(total)+" fruits is "+str(e)+"/"+str(M)+" = "+str(h)+"\n \n")
			d[x[0]][x[1]]=h

			print("Number  of ways to  select  "+str(x[0])+" apples fruits, "+str(x[1])+" banana fruits and "+str(c)+" oranges fruits from  "+str(total)+" fruits is "+str(apples)+'C'+str(x[0])+"*"+str(banana)+'C'+str(x[1])+"*"+str(oranges)+'C'+str(c)+" = "+str(e)+"\n")
			print("Probability of  selecting "+str(x[0])+" apples fruits, "+str(x[1])+" banana fruits and "+str(c)+" oranges fruits from  "+str(total)+" fruits is "+str(e)+"/"+str(M)+" = "+str(h)+"\n \n")
		file.write("\n\n\n")
		file.write("---------------------------------------------------------------------------------------------\n")

		file.write("Joint Probability Distribution Table \n \n")
		print("Joint Probability Distribution Table \n \n")
		print(d)
		q=""
		for x in range(n+1):
			if x==0:
				q=q+"     "+str(x)
			else:
				q=q+"\t\t\t\t\t\t "+str(x)

		file.write(str(q)+"\n")

		for x in range(n+1):
			s=str(x)
			for y in d[x]:
				s=s+"    "+'{0:.17f}'.format(y)
			file.write(s+"\n")
		file.write("\n")	
		f=[]
		for x in d:
			f.append(x)
		for x in range(len(d)):
			sum=0
			for y in d[x]:
				sum=sum+y
			f[x].append(sum)
		k=[]
		print(f)
		for y in range(len(f[0])):
			sum=0
			for x in range(len(f)):
				# print(str(x),str(y))
				sum=sum+f[x][y]
			# print(sum)
			k.append(sum)
		f.append(k)
		print(f[-1])
		file.write("---------------------------------------------------------------------------------------------\n")
		file.write("\n \n \n")
		file.write("---------------------------------------------------------------------------------------------\n")
		file.write("Joint Probability Distribution Table with row wise sum and columan wise sum\n \n")
		print("Joint Probability Distribution Table with row wise sum and columan wise sum\n \n")
		print(f)
		q=""
		for x in range(n+1):
			if x==0:
				q=q+"     "+str(x)
			else:
				q=q+"\t\t\t\t\t\t "+str(x)
		q=q+"\t\t\t\t\t\t "+"SUM"
		file.write(str(q)+"\n")
		for x in range(n+1):
			s=str(x)
			for y in d[x]:
				s=s+"    "+'{0:.17f}'.format(y)
			file.write(s+"\n \n")
		# file.write("---------------------------------------------------------------------------------------------\n")
		s="Sum  "
		for x in range(len(f[-1])):
			if x==0:
				s=s+'{0:.17f}'.format(f[-1][x])
			else:
				s=s+"    "+'{0:.17f}'.format(f[-1][x])
		file.write(s+"\n \n ")
		file.write("---------------------------------------------------------------------------------------------\n")
		file.write("\n \n \n ")
		file.write("---------------------------------------------------------------------------------------------\n")

		file.write("The Marginal Distributions table of X \n \n")
		print("The Marginal Distributions table of X \n \n")
		q="x"
		for x in range(n+1):
			if x==0:
				q=q+"     "+str(x)
			else:
				q=q+"\t\t\t\t\t\t "+str(x)

		file.write(str(q)+"\n")
		
		s="g(x)  "
		for y in range(len(f[-1])-1):
			if y==0:
				s=s+'{0:.17f}'.format(f[y][-1])
			else:
				s=s+"    "+'{0:.17f}'.format(f[y][-1])
		file.write(s+"\n\n")
		for y in range(len(f[-1])-1):
			file.write("f("+str(y)+")"+" = "'{0:.17f}'.format(f[y][-1])+"\n")
			print("f("+str(y)+")"+" = "'{0:.17f}'.format(f[y][-1])+"\n")
		H=""
		F=0
		for y in range(len(f[-1])-1):
			
			H=H+" + "+'{0:.17f}'.format(f[y][-1])+" * " +str(y)
			F=F+y*f[y][-1]
		file.write("Value of Ux is "+H[2:]+" = "+str(F)+"\n \n")		
		print("Value of Ux is "+H[2:]+" = "+str(F)+"\n \n")
		Ux=F

		file.write("---------------------------------------------------------------------------------------------\n")

		file.write("\n \n \n \n ")

		
		file.write("---------------------------------------------------------------------------------------------\n")
		file.write("The Marginal Distributions table of Y  \n \n")
		print("The Marginal Distributions table of Y  \n \n")
		q="y"
		for x in range(n+1):
			if x==0:
				q=q+"     "+str(x)
			else:
				q=q+"\t\t\t\t\t\t "+str(x)

		file.write(str(q)+"\n")

		s="h(y)  "
		for y in range(len(f)-1):
			if y==0:
				s=s+'{0:.17f}'.format(f[-1][y])
			else:
				s=s+"    "+'{0:.17f}'.format(f[-1][y])
		file.write(s+"\n \n \n \n")
		for y in range(len(f)-1):
			file.write("f("+str(y)+")"+" = "'{0:.17f}'.format(f[-1][y])+"\n")
			print("f("+str(y)+")"+" = "'{0:.17f}'.format(f[-1][y])+"\n")
		H=""
		F=0
		for y in range(len(f)-1):
			H=H+" + "+'{0:.17f}'.format(f[-1][y])+" * " +str(y)
			F=F+y*f[-1][y]
		Uy=F
		file.write("Value of Uy is "+H[2:]+" = "+str(F)+"\n \n")		
		print("Value of Uy is "+H[2:]+" = "+str(F)+"\n \n")
		file.write("--------------------------------------------------------------------------------------------------------------------\n")

		s=""
		t=0
		for x in range(n+1):
			for y in range(n+1):
				t=t+d[x][y]*x*y
				s=s+" + "+str(d[x][y])+" * "+str(x)+" * "+str(y)
		file.write("Value of E(XY) is "+s[2:]+" = "+str(t)+"\n \n")		
		print("Value of E(XY) is "+s[2:]+" = "+str(t)+"\n \n")
		file.write("---------------------------------------------------------------------------------------------------------------------\n")
		ans=t-Ux*Uy
		file.write("The covariance of the random variables X and Y is E(XY) - Ux * Uy = "+str(t)+" - "+str(Ux)+' * '+str(Uy)+" = "+str(ans))		
		print("The covariance of the random variables X and Y is E(XY)-Ux * Uy = "+str(ans))	





	def c(self,a,b):
		if a<b:
			return 0
		if b==0:
			return 1
		sum=1
		k=b
		w=a
		while k>0:
			sum=sum*w
			k=k-1
			w=w-1
		print(sum)
		sum1=1
		for y in range(1,b+1):
			sum1=sum1*y
		print(sum1)
		return sum/sum1





def main():
	g=[]
	file=open('input6.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			a=line.split(" ")
			g.append(a)
	if g[0][0].isdigit() and g[1][0].isdigit() and g[1][1].isdigit() and g[1][2].isdigit():
		N=int(g[0][0])
		B=int(g[1][0])
		R=int(g[1][1])
		G=int(g[1][2])
		if N<0 or B<0 or R <0 or G<0:
			file = open("output4.txt","w")
			file.write("invalid input")
			print("invalid input")
		else:
			h=solution()
			h.call(N,B,R,G)
	else:
		file = open("output5.txt","w")
		file.write("invalid input")
		print("invalid input")
main()
