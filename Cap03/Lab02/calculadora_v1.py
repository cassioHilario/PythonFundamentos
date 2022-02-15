# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def primeiroNumero():
    return int(input("Digite o primeiro número: "))

def segundoNumero():
    return int(input("Digite o segundo número: "))

def opcoes(opcao):
    print("\n\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - SAIR")
    opcao2 = int(input("\n\n Escolha a operação: \n"))

    if opcao2 == 1:
        p = primeiroNumero()
        s = segundoNumero()
        print(p + s)
        opcoes(opcao)
    elif opcao2 == 2:
        p = primeiroNumero()
        s = segundoNumero()
        print(p - s)
        opcoes(opcao)
    elif opcao2 == 3:
        p = primeiroNumero()
        s = segundoNumero()
        print(p * s)
        opcoes(opcao)
    elif opcao2 == 4:
        p = primeiroNumero()
        s = segundoNumero()
        print(p / s)
        opcoes(opcao)
    else:
        print("saindo...")
        exit()

opcao = 0

opcoes(opcao)
