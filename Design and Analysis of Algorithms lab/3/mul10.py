def karatsuba(x,y):
	if len(x) == 1 or len(y) == 1:
		return int(x,2)*int(y,2)
	else:
		n = max(len(str(x)),len(str(y)))
		if n%2==0:
			nby2 = n / 2
		else:
			nby2 = (n // 2)+1
		a = x[:nby2]
		b = x[nby2:]
		c = y[:nby2]
		d = y[nby2:]
		print(a,b,c,d)
		ac = karatsuba(a,c)
		print("ac",ac,a,c)
		bd = karatsuba(b,d)
		print("bd",bd,b,d)
		gh =  karatsuba(a,d)
		print("gh",gh,a,d)
		hy =  karatsuba(b,c)
		print("hy",hy,b,c)
		print(ac,bd,gh,hy)
		if n%2==1:
			prod = ac * (2**(n-1)) + (gh+hy)*(2**((n-1)//2)) + bd
		else:
			prod = ac * (2**(n)) + (gh+hy)*(2**(nby2//2)) + bd

		return prod
s=raw_input("Entre the two numbers")
a=list(map(str,s.split(" ")))
print("Multiplication of two number is "+str(karatsuba(a[0],a[1])))