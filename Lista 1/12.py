l = int(input('Digite o número de lados de um polígono: '))
medida =  int(input('Digite a medida do lado: '))
if l == 3:
	print(f'A figura é um triângulo e o valor do perímetro é: {l*medida}')
elif l == 4:
	print(f'A figura é um quadrado e sua área é {medida*medida}')
elif l == 5:
	print('A figura é um Pentágono')
else:
	print('Polígono não identificado')
