#OBJETIVO DO PROGRAMA:
print("\033[1;35mEM QUAL NÚMERO EU PENSEI?\033[m")

#IMPORTANDO MÓDULOS:
from random import randint
from time import sleep

sleep(1.7)

#DEFININDO O LIMITE:
limite = input("\033[1;36mPosso pensar até que número?: \033[m")
while (limite.isdecimal() == False):
    limite = input("\033[1;31mO limite deve ser um dígito numérico e inteiro. Tente novamente: \033[m")
limite = int(limite)

#SORTEANDO O NÚMERO:
sorteio = randint(0, limite)
 
#ESCOLHA DO USUÁRIO:
tentativas = 0
escolha = int(input("\033[1;33mAdvinhe o número: \033[m"))
while escolha != sorteio:
    if escolha > sorteio:
        escolha = int(input("\033[41mO número escolhido é menor......Tente novamente: \033[m"))
    else:
        escolha = int(input("\033[41mO número escolhido é maior......Tente novamente: \033[m"))
    tentativas += 1

#RESULTADO:
print("\033[1;35;46mPARABÉNS VOCÊ ACERTOU!! SEU NÚMERO DE TENTATIVAS FOI: {}.\033[m".format(tentativas))