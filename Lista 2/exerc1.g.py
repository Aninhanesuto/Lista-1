def soma(x1,x2,x3):
	if x1>x2 and x2>x3:
		return ((x1 ** 2) + (x2**2))
	elif x1>x3 and x3>x2:
		return ((x1 ** 2) + (x3**2))
	elif x2>x3 and x3>x1:
		return ((x2 ** 2) + (x3**2))
	elif x2>x1 and x1>x3:
		return ((x2 ** 2) + (x1**2))
	elif x3>x2 and x2>x1:
		return ((x3 ** 2) + (x2**2))
	elif x3>x1 and x1>x2:
		return ((x3 ** 2) + (x1**2))

def main():
	x1 = int(input())
	x2 = int(input())
	x3 = int(input())
	print(soma(x1,x2,x3))
main()