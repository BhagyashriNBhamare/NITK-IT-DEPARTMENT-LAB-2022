from fractions import Fraction
def main():
	def factorial(n):
		if n==1:
			return 1
		else:
			return n*factorial(n-1)
	def pow(a,b):
		z=1
		for x in range(b):
			z=z*a
		return z
	n=raw_input("Entre the total number of plans ")
	U=0
	w={}
	F=0
	for x in range(1,4):
		w[x]=[]
	k=True
	if n.isdigit():
		n=int(n)
		for x in range(1,4):
			a=raw_input("Entre the number of plane in runway"+str(x)+" n"+str(x)+" = ")
			b=raw_input("Probability that  runway"+str(x)+" are accessed by a randomly arriving commercial jet p"+str(x)+" = ")
			c=b
			d=float(c)
			if (type(d) == float): 
				if a.isdigit():
					a=int(a)
					w[x].append(x)
					w[x].append(a)
					w[x].append(d)
					U=U+d
					F=F+a
				else:
					print("\n")
					print("invalid input")
					k=False

			else:
				print("\n")
				print("invalid input")
				k=False
		if U!=1 and F!=n:
			print("\n")
			print("invalid input")
			k=False

		if k==True:
			print('\n\n')
			print("------------------------------------------------------------------------------------------------------------------------------------")
			s=""
			z=n
			print("Multinomial = ((total no plane)!/(n1)!*(n2)!.....)*((p1)^n1)*((p2)^n2).....")
			print("------------------------------------------------------------------------------------------------------------------------------------")
			print('\n')
			f=""
			e=1
			total=factorial(z)
			print(str(z)+'! = '+str(total))
			for x in w:
				j=factorial(w[x][1])
				print(str('n'+str(w[x][0])+'! = '+str(w[x][1])+"! = "+str(j)))
				f=f+" * "+str(j)
				e=e*j
			m=1
			g=""
			for x in w:
				l=pow(w[x][2],w[x][1])
				g=g+" * "+str(l)
				print(str('p'+str(w[x][0])+"^ n"+str(w[x][0])+" = "+str(w[x][2])+'^'+str(w[x][1])+" = "+str(l)))
				m=m*l
			ans=(total)/e
			ans=ans*m
			print('\n\n')
			print("------------------------------------------------------------------------------------------------------------------------------------")
			print("Multinomial = ( ( "+str(total)+" ) / ( "+f[3:]+" ) ) * "+str(g[3:])+" = "+str(ans))
	else:
		print("\n")
		print("invalid input")
		k=False



main()













