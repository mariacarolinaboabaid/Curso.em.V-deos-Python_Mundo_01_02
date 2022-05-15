#IMPORTANDO O MÓDULO TIME:
from time import sleep

#OBJETIVO DO PROGRAMA:
print("\033[1;33mVamos mostrar a tabuada do número indicado até o número que também será indicado pelo Usuário.\033[m")
sleep(1)

#PEDINDO OS NÚMEROS PARA O USUÁRIO:
condição = "S"
while condição == "S":
    número = input("\033[1;36mQual o número que você deseja a tabuada? \033[m")
    while número.isalpha() == True: 
        número = input("\033[1;31mInsira apenas dígitos numéricos.\033[m \033[1;36mQual o número que você deseja a tabuada? \033[m")
    número = int(número)
    limite = input("\033[1;35mAté que número devemos calcular a tabuada? \033[m")
    while limite.isalpha() == True: 
        limite = input("\033[1;31mInsira apenas dígitos numéricos.\033[m \033[1;35mAté que número devemos calcular a tabuada? \033[m")
    limite = int(limite)
#CÁLCULO DA TABUADA:
    print("-" * 30)
    for tabuada in range(limite + 1):
        print(f"\033[1;32m{número} x {tabuada} = {número * tabuada:.0f}\033[m")
    print("-" * 30)
#PERGUNTANDO SE O USUÁRIO DESEJA CONTINUAR:
    sleep(1)
    condição = input("\033[1;34mVocê deseja inserir mais números? [S/N] \033[m").strip().upper()[0]
    while condição not in "S N":
        condição = input("\033[1;31mVocê deve inserir apenas 'sim'ou 'não'. \033[1;34mDeseja inserir mais números? [S/N] \033[m").strip().upper()[0]
    print("-" * 30)

sleep(1)
#FIM:
print("\033[1mVolte sempre!\033[m")