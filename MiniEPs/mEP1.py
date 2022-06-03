x = float(input())
op = input()
y = float(input())
if op == '+':
	print(f'{x} {op} {y} = {x+y}')
elif op == '-':
	print(f'{x} {op} {y} = {x-y}')
elif op == '*':
	print(f'{x} {op} {y} = {x*y}')
elif op == '**':
	print(f'{x} {op} {y} = {x**y}')
elif op == '//':
	if y == 0:
		print('Divisao por 0!')
	else:
		print(f'{x} {op} {y} = {x//y}')
elif op == '%':
	if y == 0:
		print('Divisao por 0!')
	else:
		print(f'{x} {op} {y} = {x%y}')
else:
	print('Operacao nao reconhecida!')