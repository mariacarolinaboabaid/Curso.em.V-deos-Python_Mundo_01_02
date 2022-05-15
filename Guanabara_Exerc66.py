#IMPORTANDO O MÓDULO TIME:
from time import sleep

#OBJETIVO DO PROGRAMA:
print("\033[1;36mEscolha uma palavra-chave e iremos fazer a soma dos números digitados até a palavra-chave ser chamada.\033[m")
sleep(1)

#PEDINDO A PALAVRA-CHAVE:
palavra_chave = input("\033[1;33mPALAVRA-CHAVE: \033[m")

#DECLARANDO AS VARIÁVEIS:
soma = 0
contagem = 0

#PEDINDO OS NÚMEROS:
while True:
    número = input("\033[1;35mNÚMERO: \033[m")
    if (número.isalpha() == True):
        if número == palavra_chave:
            break
        else:
            while (número.isalpha() == True):
                número = input("\033[1;31mInsira apenas dígitos numéricos.\033[m \033[1;35mNÚMERO: \033[m")
    número = float(número)
    soma = soma + número
    contagem = contagem + 1

#RESULTADO:
print(f"\033[1;32m{contagem} números foram inseridos, resultando a soma de {soma:.2f}.\033[m")