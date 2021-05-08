def karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return int(x)*int(y)
	else:
		n = max(len(x),len(y))
		nby2 = n / 2
		a = x / 2**(nby2)
		b = x % 2**(nby2)
		c = y / 2**(nby2)
		d = y % 2**(nby2)
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
		prod = ac * 2**(2*nby2) + (ad_plus_bc * 2**nby2) + bd

		return prod
s=raw_input("Entre the two numbers")
a=list(map(str,s.split(" ")))
print("Multiplication of two numbre is "+str(karatsuba(a[0],a[1])))