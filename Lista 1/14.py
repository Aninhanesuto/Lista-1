print('Digite a sua data de nascimento:')

dia1 = int(input('Dia:'))
mes1 = int(input('Mês:'))
ano1 = int(input('Ano:'))
print('Digite a data atual:')
dia2 = int(input('Dia:'))
mes2 = int(input('Mês:'))
ano2 = int(input('Ano:'))
idade = ano2 - ano1
if ((mes2 - mes1)< 0) or ((dia2 - dia1)<0):
	idade -= 1
print (f'Idade: {idade}')
