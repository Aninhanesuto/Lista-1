import math
def esfera(r):
	pi = math.pi
	area = 4 * pi * (r**2)
	volume = (4/3) * pi * (r**3)
	print(f"A área da esfera é {area:.4f} e o volume é {volume:.4f}")
	return area, volume
def main():
	r = int(input())
	esfera(r)
main()