def crescente(x1,x2,x3):
	if x1<x2<x3:
		print(f"{x1}\n{x2}\n{x3}") 
	elif x1<x3<x2:
		print(f"{x1}\n{x3}\n{x2}") 
	elif x2<x1<x3:
		print(f"{x2}\n{x1}\n{x3}")
	elif x2<x3<x1:
		print(f"{x2}\n{x3}\n{x1}")
	elif x3<x1<x2:
		print(f"{x3}\n{x1}\n{x2}")
	elif x3<x2<x1:
		print(f"{x3}\n{x2}\n{x1}")
x1 = int(input())
x2 = int(input())
x3 = int(input())
crescente(x1,x2,x3)

