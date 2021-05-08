import math
import scipy.stats as stu
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import math as m
from scipy.stats import norm
class solution(object):
	def normal(self,x,mean,s) :
		power = (m.exp(0.5*((x-mean)/s)*((x-mean)/s)))
		return 1/(s*m.sqrt(2*(np.pi))*power)
	def call(self,g):
		file = open("output.txt","w") 
		print(" ")
		n=len(g)
		print("The Normal curve distribution Distribution \n ")
		file.write("The Normal curve distribution Distribution \n  \n \n")
		s=""
		sum=0
		for x in g:
			s=s+" + "+str(x)
			sum=sum+x

		mean=(sum*1.0)/n
		st=0
		p=""
		for x in g:
			st=st+pow((x-mean),2)
			p=p+" + ("+str(x)+" - "+str(mean)+")^2"
		st=(st*1.0)/n
		st=math.sqrt(st)
		print("mean = sum of all numbers/total nmeanmbers = "+s[3:]+" / "+str(n)+" = "+str(mean))
		file.write("mean = sum of all numbers/total nmeanmbers = "+s[3:]+" / "+str(n)+" = "+str(mean))
		file.write("\n")
		print("Standard deviation = sqrt(sum(x-mean)^2)/total nmeanmbers) = sqrt("+p[3:]+") / "+str(n)+") = "+str(st)+"\n \n ")
		file.write("Standard deviation = sqrt(sum(x-mean)^2)/total nmeanmbers) = sqrt("+p[3:]+") / "+str(n)+") = "+str(st)+"\n \n ")
		file.write("\n")
		file.write("\n")
		file.write("mean = "+str(mean)+"\n")
		print("mean = "+str(mean)+"\n")
		print("Standard deviation = "+str(st))
		file.write("Standard deviation = "+str(st)+"\n \n \n ")
		print("\n")
		print("\n")
		print("f(x) = (1/(standred deviation * sqrt(2*pi)) * e ^((-1/2)*((x-mean)/Standard deviation))^2" )
		file.write("f(x) = (1/(standred deviation * sqrt(2*pi)) * e ^((-1/2)*((x-mean)/Standard deviation))^2 \n \n")
		file.write("-----------------------------------------------------\n")
		A=[]
		i=mean-st
		k=mean+st
		B=[i,k]
		d=[]
		con=0.39886201761
		con=con/st
		for Z in g:
			print("for x = "+str(Z))
			file.write("for x = "+str(Z)+"\n")
			ans2=self.normal(Z,mean,st)
			print("f("+str(Z)+") = "+"{:.17f}".format(float(ans2))+"\n")
			file.write("f("+str(Z)+") = "+"{:.17f}".format(float(ans2))+"\n")
			file.write("\n")
			print("--------------------------------------------------------")
			file.write("-----------------------------------------------------\n")
			A.append(ans2)
		C=[]
		for x in B:
			a=self.normal(x,mean,st)
			d.append(a)
			z=self.normal(x,mean,st)
		print("--------------------------------------------------------")
		file.write("-----------------------------------------------------\n")
		print("Inflection points")
		file.write("Inflection points \n \n")

		print("mean-standard deviation = "+str(mean)+" - "+str(st)+" = "+str(B[0]))
		file.write("mean-standard deviation = "+str(mean)+" - "+str(st)+" = "+str(B[0])+"\n")
		# print("mean = "+str(mean)+" = "+str(B[1]))
		# file.write("mean = "+str(mean)+" = "+str(B[1])+"\n")
		print("mean+standard deviation = "+str(mean)+" + "+str(st)+" = "+str(B[1]))
		file.write("mean+standard deviation = "+str(mean)+" + "+str(st)+" = "+str(B[1])+"\n \n")
		print("f("+str(B[0])+") = "+"{:.17f}".format(float(d[0]))+"\n")
		file.write("f("+str(B[0])+") = "+"{:.17f}".format(float(d[0]))+"\n")
		file.write("\n")
		print("f("+str(B[1])+") = "+"{:.17f}".format(float(d[1]))+"\n")
		file.write("f("+str(B[1])+") = "+"{:.17f}".format(float(d[1]))+"\n")
		file.write("\n")
		print("Inflection points are ("+str(B[0])+" , "+str(d[0])+")"+" and ("+str(B[1])+" , "+str(d[1])+") \n \n")
		file.write("Inflection points are ("+str(B[0])+" , "+str(d[0])+")"+" and ("+str(B[1])+" , "+str(d[1])+") \n \n")
		print("--------------------------------------------------------")
		file.write("-----------------------------------------------------\n")
		
		print("Ploting a Graph  with given points\n")
		file.write("Ploting a Graph  with given points\n\n")
		for x in range(len(g)):
			print("f("+str(g[x])+") = "+str(A[x]))
			file.write("f("+str(g[x])+") = "+str(A[x])+"\n")
		fig = plt.figure()
		ax = fig.add_subplot(111) 
		
		red_patch = mpatches.Patch(color='red', label='Input points')
		black = mpatches.Patch(color='black', label='Normal distribution curve')
		red_patc = mpatches.Patch(color='blue', label='Inflection points')
		plt.legend(handles=[red_patc,red_patch,black])
		# plt.plot(g,A)
		plt.xlabel(' x ') 
		plt.ylabel(' Normal Distribution Value ') 
		plt.title(' Normal Distribution Curve ') 
		# xt = np.linspace(min(g)-5,max(g)+5,1000)
		xt = np.linspace(mean-3*st,mean+3*st,1000)
		y = norm.pdf(xt, mean, st)
		plt.plot(xt,y,'k',g,A,'ro',B,d,'bo')
		for xy in zip(B,d):                                       
			ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 
		plt.scatter(B[0], d[0], color="red")
		plt.scatter(B[1], d[1], color="red")
		plt.savefig('plot.png', dpi=300, bbox_inches='tight')
		plt.show() 
def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			a=line.split(", ")
	k=False
	# print(a)
	g=[]
	for x in a:
		if x.isdigit():
			g.append(int(x))

		else:
			k=True
			break
	# print(g)
	if k==True:
		plt.title('Invalid input')
		# plt.plot()
		plt.savefig('plot.png')
		plt.show() 
		file = open("output.txt","w")
		file.write("invalid input")
		print("invalid input")
	else:
		h=solution()
		h.call(g)

main()
