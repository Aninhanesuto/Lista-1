n1 = float(input('Digite a nota do aluno:'))
n2 = float(input('Digite a nota do aluno:'))
n3 = float(input('Digite a nota do aluno:'))
media = (n1+n2+n3)/3
if media >=7:
	print('Aluno Aprovado!')
else:
	print('Ele infelizmente não passou, terá que fazer a prova final!')
	ProvaFinal = float(input('Digite a nota da prova final: '))
	mediafinal = (media + ProvaFinal)/2
	if mediafinal >=5:
		print('Aluno Aprovado') 
	else:
		print('Aluno reprovado!')