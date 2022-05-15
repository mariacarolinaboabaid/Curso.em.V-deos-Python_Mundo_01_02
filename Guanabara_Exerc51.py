#OBJETIVO DO PROGRAMA:
print("Calcularemos a \033[1;35mprogressão aritmética\033[m conforme \033[1;36mprimeiro termo, razão\033[m e \033[1;36mintervalo\033[m dados pelo Usuário!")

#IMPORTANDO O MÓDULO TIME:
from time import sleep

#PEDINDO OS DADOS PARA O USUÁRIO:
i = 0
while i == 0:
    primeiro_termo = input("Insira aqui o primeiro termo: ")
    razão = input("Insira aqui a razão: ")
    intervalo = input("Insira aqui o limite da progressão aritmetica: ")
    try:
        primeiro_termo= int(primeiro_termo)
        razão = int(razão)
        intervalo = int(intervalo)
        i = i + 1
    except:
        print("\033[1;31mAceitamos apenas dígitos numéricos. Tente novamente!\033[m")

#EFEITO VISUAL:
print("\033[1;33mFazendo os cálculos....\033[m")
sleep(2)

#CALCULANDO A PROGRESSÃO ARITMÉTICA:
lista_progressão = list()
for x in range (primeiro_termo, intervalo + 1, razão):
    lista_progressão.append(x)

#RESULTADO
print("\033[1;32mA progressão aritmética do primeiro termo {} com razão {}, até o intervalo de {}, é {}\033[m.".format(primeiro_termo, razão, intervalo, lista_progressão))