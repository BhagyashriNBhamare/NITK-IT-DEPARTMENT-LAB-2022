def main():
	def fac(n):
		if n==1:
			return 1
		else:
			return n*fac(n-1)
	def pow(a,b):
		z=1
		for x in range(b):
			z=z*a
		return z
	n=raw_input("Entre the number of runways")
	if n.isdigit():
		n=int(n)
		w={}
		for x in range(1,n+1):
			w[x]=[]
		k=True
		for x in range(1,n+1):
			a=raw_input("Entre the number of plane in runway",x)
			b=raw_input("Probability that ",x,"runways are accessed by a randomly arriving commercial jet",x)
			if a.isdigit() and b.isdigit():
				w[x].append(x)
				w[x].append(a)
				w[x].append(b)
			else:
				print("invalid input")
				k=False
		if k==True:
			s=""
			z=0
			for x in w:
				s=s+"+"str(w[x][0])
				z=z+w[x][0]
			print("Total number of planes = ",s[1:]," ",str(z))
			print("Multinomial = ((total no plane)!/(n1)!*(n2)!.....)*((p1)^a)*((p2)^a).....")
			f=""
			e=1
			total=fac(z)
			print(z,'! = ',fac(z))
			for x in w:
				j=fac(x[1])
				print(x[1],"! = ",j)
				f=f+" * "+str(j)
				e=e*j
			m=1
			g=""
			for x in w:
				l=pow(x[2],x[1])
				g=g+" * "+str(j)
				print(x[2],'^',x[1]," = ",l)
				m=m*l
			ans=(total)/e
			ans=ans*m
			print("Multinomial = ( ( ",str(fac(z))," ) / ",f," ) * ",str(m)," = ",str(ans))
main()













