import socket   
import sys 

def isprime(temp):
	if(temp==2):
		return True
	for i in range(2,temp):
		if(temp%i==0):
			return False
	return True

def check_s(temp,n):
	if(temp>=1 and temp<=n-1):
		return True
	else:
		return False


def check_r(temp,n):
	if(temp>=1 and temp<=n-1):
		return True
	else:
		return False



  
so = socket.socket()          
  
port = 245              
  
so.connect(('127.0.0.1', port)) 

for i in range(2):
	print()
	s1 = input("Enter p: ")
	p = int(s1)
	s2 = input("Enter q: ")
	q=int(s2)
	s3 = input("Enter r: ")
	r=int(s3)
	s4 = input("Enter s: ")
	s = int(s4)
	print()
	n=p*q
	if((not isprime(p)) or (not isprime(q)) ):
		print("p or q is not prime")
		b=0
		byt=str(b).encode()
		so.send(byt)
		print("--------------------------------------")
		continue
	if(check_r(r,n)==False):
		print("r is not valid")
		b=0
		byt=str(b).encode()
		so.send(byt)
		print("--------------------------------------")
		continue

	if(check_s(s,n)==False):
		print("s is not valid")
		b=0
		byt=str(b).encode()
		so.send(byt)
		print("--------------------------------------")
		continue

	else:
		b=1
		byt=str(b).encode()
		so.send(byt)

		print("Value of n :"+str(n))
		byt=str(n).encode()
		so.send(byt)

		print("Message from server: "+so.recv(1024).decode())
		print()


		v = (s*s)%n

		print("Value of v :"+str(v))
		byt=str(v).encode()
		so.send(byt)
		print("Message from server: "+so.recv(1024).decode())
		print()


		x = (r*r)%n
		print("Value of x :"+str(x))
		byt=str(x).encode()
		so.send(byt)
		print("Message from server: "+so.recv(1024).decode())
		print()

		c = int(so.recv(1024).decode())
		print("Challenge value recived from server....")
		print("Challenge : "+str(c))
		print()

		y  = r * (s**c)%n

		print("Value of y: "+str(y))
		byt=str(y).encode()
		so.send(byt)
		print("Message from server: "+so.recv(1024).decode())
		conf = so.recv(1024).decode()
		print()
		print(conf)
		print("--------------------------------------")
so.close()     