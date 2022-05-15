#IMPORTANDO O MÓDULO TIME:
from time import sleep

#OBJETIVO DO PROGRAMA:
print("\033[1;35mVamos ler os nomes e os preços dos produtos?\033[m")
sleep(1)
print("""\033[1mNo final, mostraremos:\033[m
[1]\033[1;36m O nome do produto mais caro e seu preço\033[m
[2]\033[1;36m O nome do produto mais barato e seu preço\033[m
[3]\033[1;36m Quantos produtos foram inseridos\033[m
[4]\033[1;36m O preço total dos produtos.\033[m""")
sleep(1)
print("\033[1;32mVamos lá!\033[m")

#VARIÁVEIS:
produtos = list()
preços = list()
condição = "S"
while condição == "S":
    produtos.append(input("\033[1mNOME DO PRODUTO: "))
    valor = input("PREÇO DO PRODUTO: R$ ")
    while valor.isalpha() == True:
        valor = input("\033[31mInsira apenas dígitos numéricos.\033[m \033[1mPreço: ")
    valor = float(valor)
    preços.append(valor)
    condição = input("\033[1;34mDesejar continuar? [S/N] \033[m").strip().upper()[0]
    while condição not in "S N":
        condição = input("\033[1;31mInserir apenas 'sim' ou 'não'. \033[1;34m Deseja continuar? [S/N] \033[m").strip().upper()[0]

#EFEITO:
print("-" * 30)
print("Preparando os dados....")
print("-" * 30)
sleep(1)

#RESULTADO:
print(f"""\033[1;33mO nome do produto mais caro é {produtos[preços.index(max(preços))].title()} e o seu preço é R$ {max(preços):.2f}.
O nome do produto mais barato é {produtos[preços.index(min(preços))].title()} e o seu preço é R$ {min(preços):.2f}.
A quantidade produtos inseridos é {len(produtos)}.
E a soma total dos preços dos produtos inseridos é de R$ {sum(preços):.2f}.\033[m""")