#OBJETIVO DO PROGRAMA:
print("\033[1;35mVamos analisar quem é possui o maior peso?\033[m")

#IMPORTANDO MÓDULOS:
from time import sleep

#PERGUNTANDO OS DADOS PARA O USUÁRIO:
i = 0
while i == 0:
    quantity = input("\033[1;36mQual a quantidade de pessoas que você deseja analisar? \033[m")
    try:
        quantity = int(quantity)
        i = i + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

x = 1
heaviest = 0
lightest = 0
while x <= quantity:
    weigth = input("Qual é o peso {}? ".format(x))
    try:
        weigth = float(weigth)
        if x ==1:
            heaviest = weigth
            lightest = weigth
        elif weigth > heaviest:
            heaviest = weigth
        elif weigth < lightest:
            lightest = weigth
        x = x + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

#RESULTADO:
print("\033[1;34mO menor peso é {:.2f}kg e o maior peso é de {:.2f}kg.".format(lightest, heaviest))