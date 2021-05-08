import socket                
  
import sys
s = socket.socket()          
print("Socket successfully created")
  

port = 245            
  

s.bind(('', port))         
print("Socket binded to %s" %(port)) 
  

s.listen(5)      
print("Socket is listening") 
print()        
c, addr = s.accept() 
for i in range(2):     
   l=c.recv(1024)
   l=l.decode()
   l = int(l)
   if l==1:
      t= c.recv(1024)
      t=t.decode()
      c.send("Value of n is received ".encode())
      n = int(t)
      print("Value of n = "+str(n)+" received from client")
      print()
      v=c.recv(1024)
      v=v.decode()
      v = int(v)
      c.send("Value of v is received ".encode())
      print("Value of v = "+str(v)+" received from client")
      print()
      x=c.recv(1024)
      x=x.decode()
      x = int(x)
      print()
      print("Value of x = "+str(x)+" received  from client")
      c.send("Value of x is received ".encode())
      print()
      s1 = input("Enter challenge : ")
      challenge = int(s1)
      print()
      c.send(str(challenge).encode())
      y=c.recv(1024)
      y=y.decode()
      y = int(y)
      c.send("Value of y is received ".encode())
      print()
      print("Value of y= "+str(y)+" received  from client")
      print()
      lhs = (y*y)%n
      rhs = (x*(v**challenge))%n
      print("lhs = (y*y) %n = "+str(lhs))
      print("rhs = (x*(v**challenge))%n = "+str(rhs))
      print()
      if(lhs==rhs):
      	print("Authenticated user")
      	c.send("Authenticated user".encode())
      else:
      	print("Not Authenticated user")
      	c.send("Not Authenticated user".encode())
      print("---------------------------")
   else:
      print("Error in input from client")
      print("---------------------------")

c.close() 
s.close()