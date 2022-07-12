def delta(a,b,c):
	calc = (b**2) - 4 * a * c
	return calc
def raizes(a,b,c):
	import math
	calc = delta(a,b,c)
	if calc<0:
		print("Essa equação não possui raízes reais")
	elif calc == 0:
			raiz = math.sqrt(calc)
			raizes1 = (-b +raiz)/( 2*a)
			raizes2 = (-b -raiz)/ (2*a)
			print(f"Essa equação possui uma raiz real {raizes1}")
	elif calc>0:
			raiz = math.sqrt(calc)
			raizes1 = (-b +raiz)/( 2*a)
			raizes2 = (-b -raiz)/ (2*a)
			print(f"Essa equação possui duas raizes reais: x1: {raizes1} e x2: {raizes2}")

raizes(4,0,-16)
