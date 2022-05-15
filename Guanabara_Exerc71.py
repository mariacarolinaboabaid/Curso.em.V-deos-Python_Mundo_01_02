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

#CALCULANDO AS CÉDULAS:
if saque >= 50:
    cinquenta = saque // 50
    saque = saque % 50
    print(f"{cinquenta:.0f} nota(s) de R$ 50,00 será(ão) necessária(s) para o saque.")
    if saque == 0:
        quit
if saque >= 20:
    vinte = saque // 20
    saque = saque % 20
    print(f"{vinte:.0f} nota(s) de R$ 20,00 será(ão) necessária(s) para o saque.")
    if saque == 0:
        quit
if saque >= 10:
    dez = saque // 10
    saque = saque % 10
    print(f"{dez:.0f} nota(s) de R$ 10,00 será(ão) necessária(s) para o saque.")
    if saque == 0:
        quit
if saque >= 1:
    um = saque // 1
    saque = saque % 1
    print(f"{um:.0f} nota(s) de R$ 1,00 será(ão) necessária(s) para o saque.")
    if saque == 0:
        quit



