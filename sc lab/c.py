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
		print(g)
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
		st=(st*1.0)/(n-1)
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
		x=int(input("entre x"))
		print(self.normal(x,mean,st))

def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		if line!="":
			a=line.split(" ")
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
	h=solution()
	h.call(g)


main()
