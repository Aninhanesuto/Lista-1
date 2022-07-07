def Elevado(a,b):
	if b == 0:
		return 1
	elif b % 2 ==0:
		return ((a**(b/2)))**2
	elif b % 2 !=0:
		return (((a**((b-1)/2)))**2) * a
print(Elevado(7,3))