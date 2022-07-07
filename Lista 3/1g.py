def Soma(n):
	if n == 0:
		return 0
	else:
		return (n%10 + Soma(int(n/10)))

print(Soma(896))