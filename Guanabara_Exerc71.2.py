#IMPORTANDO O MÓDULO TIME:
from time import sleep

#OBJETIVO DO PROGRAMA:
print("""\033[1mCAIXA ELETRÔNICO
Iremos calcular quantas notas de R$ 50, R$ 20, R$ 10 e R$ 1 são necessárias para o seu saque.\033[m""")

sleep(0.5)

#PEDINDO O VALOR DO SAQUE AO USUÁRIO:
saque = input("Valor do Saque: R$ ")
while saque.isalpha() == True:
    saque = input("\033[31mInsira apenas dígitos numéricos.\033[m Valor do Saque: R$ ")
saque = int(saque)

#DECLARANDO AS VARIÁVEIS:
total = saque 
cédula = 50
total_cédula = 0

#CALCULANDO AS CÉDULAS:
while True:
    if total >= cédula:
        total = total - cédula
        total_cédula = total_cédula + 1
    else:
        if total_cédula > 0:
            print(f"Total de {total_cédula} cédulas de R$ {cédula}.")
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break