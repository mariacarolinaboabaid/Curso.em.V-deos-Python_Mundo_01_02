#OBJETIVO DO PROGRAMA:
print("\033[1;35mVamos analisar quem é maoridade?\033[m")

#IMPORTANDO MÓDULOS:
from datetime import date

#PERGUNTANDO OS DADOS PARA O USUÁRIO:
i = 0
while i == 0:
    quantity = input("\033[1;36mQual a quantidade de pessoas que você deseja analisar? \033[m")
    try:
        quantity = int(quantity)
        i = i + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

x = 0
maioridade = 0
menoridade = 0
while x != quantity:
    name = input("Qual o nome da pessoa? ")
    year = input("Qual o ano de nascimento dela? ")
    try:
        year = int(year)
        age = date.today().year - year
        if age >= 18:
            print("\033[1;32m{} já é maior de idade e tem {} anos.\033[m".format(name.title(), age))
            maioridade = maioridade + 1
        else:
            print("\033[1;33m{} não é maior de idade e tem {} anos.\033[m".format(name.title(), age))
            menoridade = maioridade + 1
        x = x + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

#RESULTADO:
print("\033[1;34mNo total, {} eram de maioridade e {} de menoridade.".format(maioridade, menoridade))