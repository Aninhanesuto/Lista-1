def min(a, b):
	if a < b:
		return a
	return b
def mystery(a, b, c, d):
	x = min(a, b)
	y = min(c, d)
	return min(x, y)
def main():
	a = 10
	b = 15
	c = 20
	d = 5
	print(mystery(a, b, c, d)) ##- A funcao mystery retorna os menores valores de a e b, c e d.
main()
