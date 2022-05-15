#Objetivo do programa:
print("""Esse valor calculará o custa das passagens por Km/h.
Até 200 Km, o Km rodado terá o custo de R$ 0,50.
Acima de 200 Km, o Km rodado terá o custo de R$ 0,45.""")

#Importando o módulo Time:
from time import sleep

#Pedindo a quantidade de Km:
i = 0
while i == 0:
    quilometers = input("Insira a quantidade de quilômetros a serem percorridos: ")
    try:
        quilometers = float(quilometers)
        i = i + 1
    except:
        print("Digite apenas dígitos númericos.")

#Efeito visual:
print("Calculando...")
sleep(2)

#Calculando o valor da passagem:
if 0 < quilometers <= 200:
    price = quilometers * 0.5
    print("O valor passagem para {} Km é R$ {}.".format(quilometers, price))
else:
    price = quilometers * 0.45
    print("O valor passagem para {} Km é R$ {}.".format(quilometers, price))