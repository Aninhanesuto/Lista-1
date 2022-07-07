def calculo(x):
	import math
	y = 0
	if x<=1:
		a = abs(x)
		y = math.log(a)
	elif 1<x<=2:	
		raiz = math.sqrt(x)
		y = math.log10(x) + raiz
	elif 2<x<=5:
		euler = math.e
		y = (x**2 + euler ** x)
	elif x> 5:
		y = math.pow(x,x/2) + math.log2(x)
	return y