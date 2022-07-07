media = float(input("Digite a média do aluno: "))
if media >= 9.0:
    print("A")
elif media >= 8.0:
    print("B")
elif media >= 7.0:
    print("C")
elif media >= 6.0:
    print("D")
elif 0<=media<=5:
    print("R")
else:
    print('Esse valor não é aceito!')