num = int(input('Digite um número entre 1000 e 9999: '))
print('OBS: O programa não irá funcionar se você escrever um número maior que 4 dígitos')
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('O número é ascendente: ', milhar<centena<dezena<unidade)

