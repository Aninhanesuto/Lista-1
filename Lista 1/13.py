print('Tempo do corredor 1:')
h = int(input('Quantas horas?')) * 3600
m = int(input('Quantos minutos?')) * 60
s = int(input('Quantos segundos?'))
print('Tempo do corredor 2:')
h2 = int(input('Quantas horas?'))  * 3600
m2 = int(input('Quantos minutos?')) * 60
s2 = int(input('Quantos segundos?'))
soma = (h + m + s)
soma2 = (h2 + m2 + s2)


if soma > soma2:
	print('Vencedor: corredor 1')
	dif = soma - soma2
	h4 = dif // 3600
	res = dif % 3600
	m4 = res // 60
	seg = res % 60
	print(f'Diferença: {h4} horas {m4} minutos {seg} segundos')

if soma2 > soma:
	print('Vencedor: corredor 2')
	dif2 = soma2 - soma
	h3 = dif2 // 3600
	res = dif2 % 3600
	m3 = res // 60
	seg2 = res % 60
	print(f'Diferença: {h3} horas {m3} minutos {seg2} segundos')
# print(f'{} horas {min} minutos {segun} segundos ')
