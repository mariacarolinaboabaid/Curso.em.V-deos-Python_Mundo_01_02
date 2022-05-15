#IMPORTANDO MÓDULO TIME:
from time import sleep

#OBJETIVO DO PROGRAMA:
print("\033[1;32mInsira a quantidade desejada de números inteiros, ao final, mostraremos a média e a soma dos valores, e o menor e o maior número inseridos.\033[m")
sleep(1.5)
print("\033[1;36mVamos lá!\033[m")

#DECLARANDO AS VARIÁVEIS:
condição = "S"
contagem = 0
soma = 0
menor = 0
maior = 0

#PEDINDO O NÚMERO PARA O USUÁRIO:
while condição == "S":
    número = input("\033[1mNúmero: \033[m")
    while (número.isalpha() == True):
        número = input("\033[1;31mInsira apenas dígitos numéricos. \033[m\033[1mNúmero: \033[m")
    número = float(número)
#FAZENDO A SOMA:
    soma = soma + número
#VERIFICANDO O MAIOR E MENOR NÚMERO:
    if número > maior:
        maior = número
    if contagem == 0:
        menor = número
    elif contagem > 0 and menor > número:
        menor == número
#CONTAGEM DOS NÚMEROS:
    contagem = contagem + 1
#PERGUNTANDO AO USUÁRIO SE ELE DESEJA CONTINUAR:
    condição = input("Você deseja inserir mais números?[S/N] ").strip().upper()[0]
    while condição not in "S N":
        condição = input("\033[1;31mVocê deve inserir apenas 'sim'ou 'não'. Deseja inserir mais números? [S/N] ").strip().upper()[0]

#RESULTADO:
print("""\033[1;36mA quantidade números inseridos foi {}.
A soma dos números inseridos é de {:.2f}.
A média dos números inseridos é de {:.2f}.
O menor número inserido foi: {:.2f}.
O maior número inserido foi: {:.2f}.\033[m""".format(contagem, soma, soma/contagem, menor, maior))