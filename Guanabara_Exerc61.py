#OBJETIVO DO PROGRAMA:
print("Calcularemos a \033[1;35mprogressão aritmética\033[m conforme \033[1;36mprimeiro termo, razão\033[m e \033[1;36mintervalo\033[m dados pelo Usuário!")

#IMPORTANDO O MÓDULO TIME:
from time import sleep

#PRIMEIRO TERMO:
primeiro_termo = input("Insira aqui o primeiro termo: ")
while primeiro_termo.isalpha() == True:
    primeiro_termo = input("\033[1;31mAceitamos apenas dígitos numéricos. Insira novamente o primeiro termo: \033[m")
primeiro_termo= int(primeiro_termo)

#RAZÃO:
razão = input("Insira aqui a razão: ")
while razão.isalpha() == True:
    razão = input("\033[1;31mAceitamos apenas dígitos numéricos. Insira novamente a razão: \033[m")
razão = int(razão)

#INTERVALO: 
limite = input("Insira aqui o limite da progressão aritmetica: ")
while limite.isalpha() == True:
    limite = input("\033[1;31mAceitamos apenas dígitos numéricos. Insira novamente o intervalo: \033[m")
limite = int(limite)

#EFEITO VISUAL:
print("\033[1;33mFazendo os cálculos....\033[m")
sleep(2)

#CALCULANDO A PROGRESSÃO ARITMÉTICA:
print("\033[1;32mA progressão aritmética do primeiro termo {} com razão {}, até o intervalo de {}, é: {}".format(primeiro_termo, razão, limite, primeiro_termo), end= " ")
while primeiro_termo < limite:
    primeiro_termo = primeiro_termo + razão
    if primeiro_termo > limite:
        quit()
    print("\033[1;32m", primeiro_termo, end= " ""\033[m")
