import math
x = float(input("Digite um numero: "))
raiz = math.sqrt(x)
if x<=1:
	print(math.log(x))
elif 1<x<=2:	
	raiz = math.sqrt(x)
	print(math.log10(x) + raiz)
elif 2<x<=5:
	euler = math.e
	print(x**2 + euler ** x)
elif x> 5:
	print(math.pow(x,x/2) + math.log2(x))


