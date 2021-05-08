class solution(object):
	def circle(self,g):
		file = open("output.txt","w") 
		for r in g:
			if r[0]=='+' or r[0]=='-':
				if r[0]=='-':
					file.write("output for radius"+" "+r+" "+" "+"invalid input"+ '\n'+'\n') 
				else:
					if r[1:].isdigit():
						w=float(r)
						if w<0:
							file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n') 	
						elif w>=100 and w<=999:
							s=[]
							d=int(w)
							if w>=2:
								for x in range(1,d):
									for y in range(1,d):
										if x*x+y*y<d*d:
											s.append([x,y])
								file.write("output for radius"+" "+r+" "+str(s)+ '\n'+'\n')
						else:
							file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n') 


					else:
						file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n') 
			else:
				if r.isdigit():
						w=float(r)
						if w<0:
							file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n') 
						else:
							s=[]
							if w>=100 and w<=999:
								s=[]
								d=int(w)
								y=1
								if w>=2:
									for x in range(0,d):
										for y in range(0,d):
											if x*x+y*y<d*d:
												s.append([x,y])
								file.write("output for radius"+" "+r+" "+str(s)+ '\n'+'\n')
							else:
								file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n')
				else:
					file.write("output for radius"+" "+r+" "+"invalid input"+ '\n'+'\n')
		file.close() 

def main():
	g=[]
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		g.append(line)
	h=solution()
	h.circle(g)
main()