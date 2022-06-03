def divisivel(x1):
	return True if (x1%5)==0 else False
def main():
	x = float(input())
	v = divisivel(x)
	print(v)
main()