def Sum(n):
	if n <=1:
		return n
	else:
		return n + Sum(n - 1)

print(Sum(int(input("Write a number: "))))

def sum(n):
	return n * (n  + 1) /2

print(sum(10))