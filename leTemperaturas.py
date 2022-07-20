def leTemperaturas(n, i = 1, soma = 0):
    t = float(input(f"Digite a temperatura {i}: "))
    if t < -5 or t > 45:
        return leTemperaturas(n, i, soma)
    elif n <= i :
        return soma + t
    else:
        return leTemperaturas(n, i + 1, soma + t)

def main():
    n = int(input("Digite a quantidade de temperaturas:  "))
    soma = leTemperaturas(n)
    soma = round(soma,2)
    media = soma/n
    media = round(media, 3)
    #maior = leTemperaturas(maior)
    #menor = leTemperaturas(menor)
    print(f"A soma das temperaturas é: {soma}")
    print(f"A média das temperaturas é: {media}")
    #print(f"A maior temperatura é: {maior}")
    #print(f"A maior temperatura é: {menor}")

main()