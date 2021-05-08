import xlrd
def main(): 
	wb = xlrd.open_workbook("input.xlsx", "rb") 
	j=0
	for x in range(6):
		sheet = wb.sheet_by_index(x+j) 
		s="output"+str(x+1)+".txt"
		file = open(s,"w") 
		G=False
		j=sheet.nrows
		n=sheet.ncols
		m=sheet.nrows
		d=[[0 for x in range(n)]for y in range(m)]
		for x in range(m):
			for y in range(n):
				d[x][y]=sheet.cell_value(x,y)
				if d[x][y]>1:
					G=True
		if G==True:
			file.write("invalid input")
		else:
			f=[]
			for x in d:
				f.append(x)
			for x in range(1,len(d)):
				sum=0
				for y in range(1,len(d[x])):
					sum=sum+d[x][y]
				f[x].append(sum)
			k=[]
			for y in range(1,len(f[0])):
				sum=0
				for x in range(1,len(f)):
					sum=sum+f[x][y]
				k.append(sum)
			f.append(k)
			file.write("---------------------------------------------------------------------------------------------\n")
			file.write("Joint Probability Distribution Table with row wise sum and columan wise sum\n \n")
			print("---------------------------------------------------------------------------------------------\n")
			print("Joint Probability Distribution Table with row wise sum and columan wise sum\n \n")
			for x in range(n):
				if x==0:
					q="y/x"
				else:
					q=q+"    "+'{0:.2f}'.format(f[0][x])
			q=q+"    "+"SUM"
			file.write(str(q)+"\n")
			print(str(q)+"\n")
			for x in range(1,m):
				s=str(d[x][0])
				for y in range(1,len(d[x])):
					s=s+"    "+'{0:.2f}'.format(d[x][y])
				file.write(s+"\n \n")
				print(s+"\n \n")
			s="Sum    "
			for x in range(len(f[-1])):
				if x==0:
					s=s+'{0:.2f}'.format(f[-1][x])
				else:
					s=s+"    "+'{0:.2f}'.format(f[-1][x])

			file.write(s+"\n \n")
			print(s+"\n \n")
			file.write("---------------------------------------------------------------------------------------------\n")
			print("---------------------------------------------------------------------------------------------\n")
			file.write("The Marginal Distributions table of X \n \n")
			print("The Marginal Distributions table of X \n \n")
			q="x"
			e=[]
			for x in range(1,n):
				if x==0:
					e.append([d[0][x],f[-1][x-1]])
					q=q+"     "+str(d[0][x])
				else:
					e.append([d[0][x],f[-1][x-1]])
					q=q+"     "+str(d[0][x])
			print(str(q)+"\n")
			file.write(str(q)+"\n")
			# print(f)
			s="g(x)  "
			for y in range(len(f[-1])):
				if y==0:
					s=s+'{0:.2f}'.format(f[-1][y])
				else:
					s=s+"    "+'{0:.2f}'.format(f[-1][y])
			print(s+"\n")
			file.write(s+"\n")
			s=""
			t=0
			for x in e:
				s=s+"+"+str(x[0])+"*"+str(x[1])
				t=t+x[0]*x[1]

			file.write("Value of Ux is "+s[1:]+" = "+str(t)+"\n \n")		
			print("Value of Ux is "+s[1:]+" = "+str(t)+"\n \n")
			file.write("---------------------------------------------------------------------------------------------\n")
			print("---------------------------------------------------------------------------------------------\n")
			file.write("The Marginal Distributions table of Y \n \n")
			print("The Marginal Distributions table of Y \n \n")
			q="y"
			e=[]
			for x in range(1,m):
				if x==0:
					e.append([d[x][0],f[x][-1]])
					q=q+"     "+str(d[x][0])
				else:
					e.append([d[x][0],f[x][-1]])
					q=q+"     "+str(d[x][0])

			file.write(str(q)+"\n")
			print(str(q)+"\n")
			# print(f)
			s="g(y)  "
			for y in range(1,len(f)-1):
				if y==1:
					s=s+'{0:.2f}'.format(f[y][-1])
				else:
					s=s+"    "+'{0:.2f}'.format(f[y][-1])
			file.write(s+"\n")
			print(s+"\n")
			s=""
			t=0
			for x in e:
				s=s+"+"+str(x[0])+"*"+str(x[1])
				t=t+x[0]*x[1]

			file.write("Value of Uy is "+s[1:]+" = "+str(t)+"\n \n")		
			print("Value of Uy is "+s[1:]+" = "+str(t)+"\n \n")
			print("---------------------------------------------------------------------------------------------\n")

			s=""
			t=0
			for x in range(1,m):
				for y in range(1,n):
					t=t+d[x][y]*d[0][y]*d[x][0]*2
					s=s+"+ "+str(d[x][y])+" * "+str(d[0][y])+" * "+str(d[x][0])+" * "+"2 "

			file.write("expected value of g (X, Y) = 2XY is "+s[1:]+" = "+str(t))
			print("expected value of g (X, Y) = 2XY is "+s[1:]+" = "+str(t))


