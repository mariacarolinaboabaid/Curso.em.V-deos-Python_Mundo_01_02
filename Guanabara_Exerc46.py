#OBJETIVO DO PROGRAMA:
print("Lá vem o Ano Novo! Contagem regressiva de:")

#IMPORTANDO O MÓDULO TIME:
from time import sleep
from datetime import date

#CONTAGEM REGRESSIVA:
for x in range(10, -1, -1):
    print(x)
    sleep(1)
print("FELIZ ANO NOVO!")