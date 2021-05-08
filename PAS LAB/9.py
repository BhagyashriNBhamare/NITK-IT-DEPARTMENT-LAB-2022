import math
import scipy.stats as st

class solution(object):
	def call(self,Y,X,Z):
		file = open("output.txt","w") 
		print(" ")
		print("The Binomial Distribution \n ")
		file.write("The Binomial Distribution \n \n ")
		y=(Y*1.0)/100
		t=1-y
		print("The probability that "+str(Z)+" of them will have at least one credit card  = "+"P("+str(Z)+") = "+str(X)+"C"+str(Z)+" * "+str(y)+"^"+str(Z)+" * "+str(t)+"^"+str(X-Z)+"\n")
		file.write("The probability that "+str(Z)+" of them will have at least one credit card = "+"P("+str(Z)+") = "+str(X)+"C"+str(Z)+" * "+str(y)+"^"+str(Z)+" * "+str(t)+" ^ "+str(X-Z)+"\n")
		file.write("\n")
		a=pow(y,Z)
		b=pow(t,X-Z)
		c=self.c(X,Z)
		ans=a*b*c
		# ans=round(ans,4)
		print("P("+str(Z)+") = "+str(a)+" * "+str(b)+" * "+str(c))
		file.write("P("+str(Z)+") = "+str(a)+" * "+str(b)+" * "+str(c))
		file.write("\n")
		print("P("+str(Z)+") = "+str(ans))
		file.write("P("+str(Z)+") = "+str(ans))
		file.write("\n")
		print("----------------------------------------------------------------------------------------------------------------------------------------------- \n")
		file.write("-----------------------------------------------------------------------------------------------------------------------------------")
		file.write("\n")
		print("The Normal Approximation of The Binomial Distribution \n ")
		file.write("The Normal Approximation of The Binomial Distribution \n ")
		file.write("\n")
		u=X*y
		print("mean = n*p = "+str(X)+" * "+str(y)+" = "+str(u))
		file.write("mean = n*p = "+str(X)+" * "+str(y)+" = "+str(u))
		file.write("\n")
		s=X*y*t
		s=math.sqrt(s)
		print("Standard deviation = sqrt(n*p*(1-p)) = sqrt("+str(X)+" * "+str(y)+" * "+str(t)+") = "+str(s))
		file.write("Standard deviation = sqrt(n*p*(1-p)) = sqrt("+str(X)+" * "+str(y)+" * "+str(t)+") = "+str(s))
		file.write("\n")
		file.write("\n")
		print("\n")
		print("\n")
		a1=Z-0.5
		a2=Z+0.5
		print("z = (x-mean)/Standard deviation")
		file.write("z = (x-mean)/Standard deviation \n")
		b1=a1-u
		b1=b1/s
		b1=round(b1, 2)
		b2=a2-u
		b2=b2/s
		b2=round(b2, 2)
		print("For x="+str(a1)+"   z = ("+str(a1)+" - "+str(u)+") /"+str(s)+" = "+str(b1))
		file.write("For x="+str(a1)+"   z = ("+str(a1)+" - "+str(u)+") /"+str(s)+" = "+str(b1)+"\n")
		print("For x="+str(a2)+"   z = ("+str(a2)+" - "+str(u)+") /"+str(s)+" = "+str(b2)+" \n \n ")
		file.write("For x="+str(a2)+"   z = ("+str(a2)+" - "+str(u)+") /"+str(s)+" = "+str(b2)+"\n \n")
		print("P("+str(a1)+" <= x <= "+str(a2)+") = "+"P("+str(b1)+"  <= x <=  "+str(b2)+") \n")
		file.write("P("+str(a1)+" <= x <= "+str(a2)+") = "+"P("+str(b1)+" <= x <= "+str(b2)+") \n \n")
		q1= st.norm.cdf(b1)
		q2= st.norm.cdf(b2)
		# q1=round(q1, 4)
		# q2=round(q2, 4)
		ans2=q2-q1
		print("Z("+str(b1)+") = "+str(q1))
		print("Z("+str(b2)+") = "+str(q2)+"\n")
		file.write("Z("+str(b1)+") = "+str(q1)+"\n")
		file.write("Z("+str(b2)+") = "+str(q2)+"\n \n")
		print("P("+str(b1)+"  <= x <=  "+str(b2)+") = "+str(q2)+" - "+str(q1)+" = "+str(ans2))
		file.write("P("+str(b1)+"  <= x <=  "+str(b2)+") = "+str(q2)+" - "+str(q1)+" = "+str(ans2)+"\n")
		print("P("+str(Z)+") = "+str(ans2)+"\n")
		file.write("P("+str(Z)+") = "+str(ans2))
		file.write("\n")
		print("Error = "+str(ans)+" - "+str(ans2)+" = "+str(ans-ans2)+"\n \n")
		file.write("Error = "+str(ans)+" - "+str(ans2)+" = "+str(ans-ans2)+"\n \n ")
		print("-----------------------------------------------------------------------------------------------------------------------------------------------\n")
		file.write("----------------------------------------------------------------------------------------------------------------------------------- \n")
		print("The error due to using the normal approximation is "+str(abs(ans-ans2)))
		file.write("The error due to using the normal approximation is "+str(abs(ans-ans2)))

	def normalProbabilityDensity(self,x):
		return(0.398862017609 * np.exp((-x**2) / 2.0) )


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
		# print(sum)
		sum1=1
		for y in range(1,b+1):
			sum1=sum1*y
		# print(sum1)
		return sum/sum1
		
def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			a=line.split(" ")
			g.append(a)
	if g[0][1].isdigit() and g[0][2].isdigit():
		s=g[0][0]
		s=s[:len(s)-1]
		X=int(s)
		print(X)
		Y=int(g[0][1])
		Z=int(g[0][2])
		if X<0 or Y<0 or Z<0:
			file = open("output.txt","w")
			file.write("invalid input")
			print("invalid input")
		else:
			h=solution()
			h.call(X,Y,Z)
	else:
		file = open("output.txt","w")
		file.write("invalid input")
		print("invalid input")
main()
