#Objetivo do programa:
print("Esse programa solicitará um ano para o Usuário e informará se ele é bissexto.")

#Importando os módulos:
from time import sleep
from datetime import date

#Pedindo o ano para o Usuário:
i = 0
while i == 0:
    year = input("Insira o ano desejado aqui, caso queira analisar o ano atual, insira '0': ")
    try: 
        if year == "0":
            year = date.today().year
        else:
            year = int(year)
        i = i + 1
    except:
        print("Digite apenas dígitos numéricos decimais.")

#Efeito visual:
print("Processando...")
sleep(2)

#Verificando se o ano é bissexto:
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("O ano {} é bissexto.".format(year))
else:
    print("O ano {} não é bissexto.".format(year))