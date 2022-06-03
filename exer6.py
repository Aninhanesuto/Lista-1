n1 = int(input('Digite um número de 4 algarismos: Obs: Não funciona pra números maiores de 4 dígitos: '))
unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10
print('Esse número é um palíndromo:',unidade == milhar and dezena == centena)
## OBS: Pega uma unidade = n1 // 1 % 10
## OBS: Pega dois números = n1// 10 % 100
##Usando Conversão de String:
'''
n2 = str(n1)
inverter = (n2[::-1])
print('Esse número é um palíndromo:',n1 >=1000 and n1<=9999 and n2 == inverter)'''
##Usando o IF pra fazer:
"""if (n1 >=1000 and n1<=9999 ):
	if n2 == inverter:
		print('Esse número é um palíndromo')
	else:
		print('Esse número não é um palíndromo')
else:
	print("Esse número não tem 4 dígitos, tente rodar o código novamente e digitar corretamente")"""
