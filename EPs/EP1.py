from os import system, name  # Funções importadas para limpar a tela do terminal

def limpaTela():
    """
    Essa função é auto-explicativa, ela irá limpar a tela do terminal quando é executada.
    """
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux ou outro SO
        system('clear')
def Troco(vt):
    """
    Essa função recursiva calcula o troco e exibe o valor na tela
    Parâmetros: 
    * vt: O troco calculado na função maquina
    Return:
    - Essa função retorna o valor do troco(vt)
    """
    if vt <= 0: return
    if vt >= 100:
        print("R$ 100.00")
        Troco(vt - 100)
    elif vt >= 50:
        print("R$ 50.00")
        Troco(vt - 50)
    elif vt >= 20:
        print("R$ 20.00")
        Troco(vt - 20)
    elif vt >= 10:
        print("R$ 10.00")
        Troco(vt - 10)
    elif vt >= 5:
        print("R$ 5.00")
        Troco(vt - 5)
    elif vt >= 2:
        print("R$ 2.00")
        Troco(vt - 2)
    elif vt >= 1:
        print("R$ 1.00")
        Troco(vt - 1)
    elif vt >= 0.5:
        print("R$ 0.50")
        Troco(vt - 0.5)
    elif vt >= 0.25:
        print("R$ 0.25")
        Troco(vt - 0.25)
    elif vt >= 0.10:
        print("R$ 0.10")
        Troco(round(vt - 0.10,2))
    elif vt >= 0.05:
        print("R$ 0.05")
        Troco(round(vt - 0.05,2))
    else:
        print("R$ 0.01")
        Troco(round(vt - 0.01,2))

def verificar(valor, convert):
    """
    Essa função recursiva, tenta converter as variaveis opcao e dinheiro para respectivamente int e float, 
    caso ela não consiga ela chama novamente a funcao e pede pro usuário digitar novamente um valor até que dê 
    um valor válido.
    Parâmetros: 
    * valor: Essa será a variável que será convertida
    ** convert: Esse parâmetro será int ou float, para converter o parâmetro valor dependendo de cada caso.
    Return:
    - Essa função retorna o valor convertido, ou uma mensagem pedindo o usuário que digite novamente até que o usuário
    digite um valor válido.

    """
    try: #Tenta fazer a conversão do valor digitado para int ou float
        x = convert(valor)
        return x
    except : #Se não for possível fazer a conversão , uma exceção é lançada
        return verificar(input("Opção não reconhecida!, Digite Novamente: "), convert)

def maquina(valor, valorDepositado = 0):
    """
    Essa função irá pedir para o usuário inserir o dinheiro e mostrará na tela o valor pago, caso esse valor 
    seja menor que os valores dos produtos ou seja um valor negativo, a função realizará uma recursão até ter um valor que seja igual ao valor do produto. 
    No fim, se esse valor for igual ao valor do produto, não mostrará o troco, porém se ele for maior, a função chamará a função Troco, para calcular
    o troco.
    Parâmetros: 
    * valor = Valor do produto dado na função menu
    **  valorDepositado = valor depositado na maquina automático, esse parâmetro é opcional e começa com o valor zero.
    Return: Retorna o valor pago e o troco caso haja troco.

    """
    dinheiro = verificar(input("Coloque o seu dinheiro: "), float)
    if dinheiro <0:
        print("Operação Inválida!")
        return maquina(valor, valorDepositado)
    valorDepositado += dinheiro
    if valorDepositado < valor:
        return maquina(valor, valorDepositado)
  
    print(f"Valor pago:R${valorDepositado:.02f}")
    if(valor == valorDepositado):
        print("Obrigado pela compra!\nRetire seu produto.")
    else:
        troco = round(valorDepositado - valor, 2)
        print(f"Troco: R${troco:.02f}")
        print("Pegue seu troco:")
        Troco(troco)
    


def menu(vodka, cerveja, catuaba, semlimite, bafo, fat):
    """
    Essa função menu, mostra na tela as principais bebidas da maquina automática na loja e controla as outras opções da máquina.
    Parâmetros: 
    * vodka: se refere a quantidade de Shot de Vodka
    * cerveja: se refere a quantidade de bebida Cerveja
    *catuaba: se refere a quantidade de bebida Catuaba
    *sem limite: se refere a quantidade de bebida Sem Limite
    *bafo: se refere a quantidade de bebida Bafo de Tigre
    *fat: Esse parâmetro se refere ao faturamento total da loja
    """
    RED ="\033[0;31m" # Muda a cor do Terminal para vermelho
    print(RED) # Muda a cor do Terminal para vermelho
    print("+---------------BOTEQUINHO XFX-------------+")
    print("| 1 - SHOT DE VODKA ................R$2,50 |")
    print("| 2 - CERVEJA.......................R$4,00 |")
    print("| 3 - CATUABA.......................R$6,75 |")
    print("| 4 - 100 LIMITE....................R$12,00|")
    print("| 5 - BAFO DE TIGRE.................R$13,75|")
    print("+---------------OUTRAS OPÇÕES--------------+")
    print("| 6 - Informações Internas                 |")
    print("| 7 - Finalizar                            |")
    print("+------------------------------------------+")
    opcao = verificar(input("Escolha uma opção: "), int)
    
    if opcao == 1:
        if vodka <= 0:
            print("Desculpe, mas a bebida 'Shot de Vodka' está indisponível")
            input("--> Enter para continuar...")
            limpaTela()
            return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        else:
            vodka-= 1
            fat+=2.50
            print("Você escolheu 'Shot de Vodka'")
            print("Preço: R$2,50")
            maquina(2.50)
            decisao = input("Deseja comprar outro produto? (S/N): ")
            if decisao == "s" or decisao == "S":
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
            elif decisao == "n" or decisao == "N":
                limpaTela()
                print("Obrigada pela preferência! ^-^")
                print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
                input("--> Enter para continuar...")
                exit()
            else:
                limpaTela()
                print("Opção não reconhecida!")
                input("--> Enter para continuar...")
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        
        
    elif opcao == 2:
        if cerveja <= 0:
            print("Desculpe, mas a bebida 'Cerveja' está indisponível")
            input("--> Enter para continuar...")
            limpaTela()
            return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        else:
            cerveja-=1
            fat+=4.00
            print("Você escolheu 'Cerveja'")
            print("Preço: R$4,00")
            maquina(4.00)
            decisao = input("Deseja comprar outro produto? (S/N): ")
            if decisao == "s" or decisao == "S":
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
            elif decisao == "n" or decisao == "N":
                limpaTela()
                print("Obrigada pela preferência! ^-^")
                print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
                input("--> Enter para continuar...")
                exit()
            else: 
                limpaTela()
                print("Opção não reconhecida!")
                input("--> Enter para continuar...")
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        
    elif opcao == 3:
        if catuaba <= 0:
            print("Desculpe, mas a bebida 'Catuaba' está indisponível")
            input("--> Enter para continuar...")
            limpaTela()
            return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        else:
            catuaba-=1
            fat+=6.75
            print("Você escolheu 'Catuaba'")
            print("Preço: R$6,75")
            maquina(6.75)
            decisao = input("Deseja comprar outro produto? (S/N): ")
            if decisao == "s" or decisao == "S":
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
            elif decisao == "n" or decisao == "N":
                limpaTela()
                print("Obrigada pela preferência! ^-^")
                print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
                input("--> Enter para continuar...")
                exit()
            else:
                limpaTela()
                print("Opção não reconhecida!")
                input("--> Enter para continuar...")
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
    elif opcao == 4:
        if semlimite <= 0:
            print("Desculpe, mas a bebida '100 Limite' está indisponível")
            input("--> Enter para continuar...")
            limpaTela()
            return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        else:
            semlimite-=1
            fat+=12.00
            print("Você escolheu '100 Limite'")
            print("Preço: R$12,00")
            maquina(12.00)
            decisao = input("Deseja comprar outro produto? (S/N): ")
            if decisao == "s" or decisao == "S":
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
            elif decisao == "n" or decisao == "N":
                limpaTela()
                print("Obrigada pela preferência! ^-^")
                print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
                input("--> Enter para continuar...")
                exit()
            else:
                limpaTela()
                print("Opção não reconhecida!")
                input("--> Enter para continuar...")
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
    elif opcao == 5:
        if bafo <= 0:
            print("Desculpe, mas a bebida '100 Limite' está indisponível")
            input("--> Enter para continuar...")
            limpaTela()
            return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        else:
            bafo-=1
            fat+=13.75
            print("Você escolheu 'Bafo de Tigre'")
            print("Preço: R$13,75")
            maquina(13.75)
            decisao = input("Deseja comprar outro produto? (S/N): ")
            if decisao == "s" or decisao == "S":
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
            elif decisao == "n" or decisao == "N":
                limpaTela()
                print("Obrigada pela preferência! ^-^")
                print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
                input("--> Enter para continuar...")
                exit()
            else:
                limpaTela()
                print("Opção não reconhecida!")
                input("--> Enter para continuar...")
                limpaTela()
                return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
          
    elif opcao == 6:
        print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------""")
        input("--> Enter para continuar...")
        limpaTela()
        return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
        
    elif opcao == 7:

        print(f"""--------- Informações Internas ----------
-----------------------------------------
Shot de Vodka: {vodka}
Cerveja: {cerveja}
Catuaba: {catuaba}
Sem Limite: {semlimite}
Bafo de Tigre: {bafo}
Faturamento: R$:{fat:.02f}
-----------------------------------------
-----Obrigada pela preferência! ^-^ -----""")
        input("--> Enter para continuar...")
    else:
        print("Opção Inválida, escolha novamente")
        input("--> Enter para continuar...")
        limpaTela()
        return menu(vodka, cerveja, catuaba, semlimite, bafo, fat)
    
def main ():
    """
    A função main é a função principal, na qual eu chamarei a função menu e função limparTela
    """
    limpaTela()
    menu(5,5,5,5,5,0) # Os Estoques Iniciais das bebidas são 5 e o faturamento inicial é zero.

main ()