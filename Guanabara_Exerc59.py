#OBJETIVO DO PROGRAMA:
print("\033[1mCALCULADORA\033[m")

#PEDINDO OS PRIMEIROS NÚMEROS PARA O USUÁRIO:
número_01 = input("Primeiro número: ")
while (número_01.isalpha() == True):
    número_01 = input("Insira apenas dígitos numéricos. Primeiro número: ")
número_01 = float(número_01)

número_02 = input("Segundo número: ")
while número_02.isalpha() == True:
    número_02 = input("Insira apenas dígitos numéricos. Segundo número: ")
número_02 = float(número_02)

#OPERAÇÕES:
operação = input("""Qual operação você deseja fazer?
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
Operação: """)
while operação not in "1 2 3 4" or operação.isalpha() == True:
    operação = input("Insira apenas '1', '2', '3' ou '4': ")

#RESULTADO:
if operação == "1":
    operador = "soma"
    resultado = número_01 + número_02
elif operação == "2":
    operador = "subtração"
    resultado = número_01 - número_02
elif operação == "3":
    operador = "multiplicação"
    resultado = número_01 * número_02
elif operação == "4":
    operador = "divisão"
    resultado = número_01 / número_02
print("O resultado da operação de {} entre os números {} e {} é {:.2f}.".format(operador, número_01, número_02, resultado))

condição = "S"
condição = input("Você deseja fazer mais operações[S/N]: ").strip().upper()[0]
while condição not in "S N":
    condição = input("Digite apenas 'Sim' ou 'Não': ").strip().upper()[0]
if condição == "N":
    print("Fim!")
while condição == "S":
    número = input("Digite o novo número aqui: ")
    while (número.isalpha() == True):
        número = input("Insira apenas dígitos numéricos. Primeiro número: ")
    número = float(número)
    operação = input("""Qual operação você deseja fazer?
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
Operação: """)
    while operação not in "1 2 3 4" or operação.isalpha() == True:
        operação = input("Insira apenas '1', '2', '3' ou '4': ")
    if operação == "1":
        operador = "soma"
        resultado = resultado + número
    elif operação == "2":
        operador = "subtração"
        resultado = resultado - número
    elif operação == "3":
        operador = "multiplicação"
        resultado = resultado * número
    elif operação == "4":
        operador = "divisão"
        resultado = resultado / número
    print("O resultado da operação de {} é {:.2f}.".format(operador,resultado))
    condição = input("Você deseja fazer mais operações[S/N]: ").strip().upper()[0]
    


    
