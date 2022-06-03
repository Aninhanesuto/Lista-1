Flag = True
peso = float(input())
idade = int(input())
if (16 <= idade < 18):
    doc = input()
saude = input()
droga = input()
primeira = input()
if (primeira == "N"):
    meses = int(input())
    intervalo = int(input())
sexo = input()
if (sexo == "F"):
    gravida = input()
    amamentando = input()
    if (amamentando == "S"):
       idadebebe = int(input())

print(f"Peso: {peso}")
print(f"Idade: {idade}")
if (16 <= idade < 18): 
    print(f"Documento de autorizacao: {doc}")
print(f"Boa saude: {saude}")
print(f"Uso drogas injetaveis: {droga}")
print(f"Primeira doacao: {primeira}")
if (primeira == "N"):
    print(f"Meses desde ultima doacao: {meses}")
    print(f"Doacoes nos ultimos 12 meses: {intervalo}")
print(f"Sexo biologico: {sexo}")
if (sexo == "F"):
    print(f"Gravidez: {gravida}")
    print(f"Amamentando: {amamentando}")
    if (amamentando == "S"):
        print(f"Meses bebe: {idadebebe}")

if (peso < 50):
    print("Impedimento: abaixo do peso minimo.")
    Flag = False
if (16 > idade):
    print("Impedimento: menor de 16 anos.")
    Flag = False
elif (idade > 60 and primeira == "S"):
    print("Impedimento: maior de 60 anos, primeira doacao.")
    Flag = False
elif ((16 <= idade < 18) and (doc == "N")):
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    Flag = False
elif (idade > 69):
    print("Impedimento: maior de 69 anos.")
    Flag = False
if (saude == "N"):
    print("Impedimento: nao esta em boa saude.")
    Flag = False
if (droga == "S"):
    print("Impedimento: uso de drogas injetaveis.")
    Flag = False
if ((primeira == "N") and ((sexo == "M" and meses < 2) or (sexo == "F" and meses < 3))):
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    Flag = False
if ((primeira == "N") and ((sexo == "M" and intervalo >= 2) or (sexo == "F" and intervalo >= 3))):
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    Flag = False
if ((sexo == "F") and (gravida == "S")):
    print("Impedimento: gravidez.")
    Flag = False
if ((sexo == "F") and (amamentando == "S") and (idadebebe < 12)):
    print("Impedimento: amamentacao.")
    Flag = False

if (Flag):
    print("Procure um hemocentro.")