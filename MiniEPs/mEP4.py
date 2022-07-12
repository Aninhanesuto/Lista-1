######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Ana Clara Sesana Moreira
# Matrícula: 2022100199

def count(p1, p2, p3, p4, p5, p6, p7, p8, p9, v):
    conta = 0
    if p1==v: 
        conta+=1
    if p2==v: 
        conta+=1
    if p3==v: 
        conta+=1
    if p4==v:
        conta+=1
    if p5==v: 
        conta+=1
    if p6==v: 
        conta+=1
    if p7==v: 
        conta+=1
    if p8==v: 
        conta+=1
    if p9==v: 
        conta+=1
    return conta
    
def verifica(entrada):
    if entrada =="x" or entrada == "o" or entrada == " ": 
        return True
    else: 
        return False

def GanhadorO(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if p1==p2==p3=="o": 
        return True
    elif p1==p4==p7=="o": 
        return True
    elif p1==p5==p9=="o": 
        return True
    elif p2==p5==p8=="o": 
        return True
    elif p3==p6==p9=="o": 
        return True
    elif p3==p5==p7=="o": 
        return True
    elif p4==p5==p6=="o": 
        return True
    elif p7==p8==p9=="o": 
        return True
    else: 
        return False
def Ganhadorx(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if p1==p2==p3=="x": 
        return True
    elif p1==p4==p7=="x": 
        return True
    elif p1==p5==p9=="x": 
        return True
    elif p2==p5==p8=="x": 
        return True
    elif p3==p6==p9=="x": 
        return True
    elif p3==p5==p7=="x": 
        return True
    elif p4==p5==p6=="x": 
        return True
    elif p7==p8==p9=="x": 
        return True
    else: 
        return False

def verificaespaco(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if p1==" " or p2 == " " or p3 == " " or p4 == " " or p5 == " " or p6 == " " or p7 == " " or p8 == " " or p9 == " ":
        return True
    else:
        return False


def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    print(f""" {p7} | {p8} | {p9} \n---+---+---\n {p4} | {p5} | {p6} \n---+---+---\n {p1} | {p2} | {p3} """)

     
def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if verifica(p1) and verifica(p2) and verifica(p3) and verifica(p4) and verifica(p5) and verifica(p6) and verifica(p7) and verifica(p8) and verifica(p9):
        return True
    else:
        return False
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    #Complete o código da função

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    soma1 = count(p1, p2, p3, p4, p5, p6, p7, p8, p9, "x")
    soma2 = count(p1, p2, p3, p4, p5, p6, p7, p8, p9, "o")
    return False if (abs(soma1 - soma2) >= 2) else True
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    #Complete o código da função

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if Ganhadorx(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'x' venceu!")
    elif GanhadorO(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'o' venceu!")
    elif verificaespaco(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogo nao terminou!")
    else:
        print("Empate!")
        
        
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    #Complete o código da função

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
