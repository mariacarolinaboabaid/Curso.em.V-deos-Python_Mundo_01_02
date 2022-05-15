#Objetivo do programa:
print("\033[1;33mEsse programa fará a conversão numérica desejada pelo Usuário do número por ele inserido.")

#Importando o módulo Time:
from time import sleep

#Solicitando o número para o Usuário:
x = 0
while x == 0:
    número = input("\033[1;32mInsira aqui o número que deseja converter: ")
    if número.isdecimal() == False:
        print("\033[1;31mO número inserido deve ser decimal.")
    else:
        número = int(número)
        x = x + 1

#Escolhendo a conversão:
i = 0
while i == 0: 
    conversão = input("""\033[1;36mEscolha a conversão desejada: 
[01] para Binário
[02] para Octal
[03] para Hexadecimal:\033[m """)
    if conversão in "01 02 03":
         i = i + 1
    else:
        print("\033[1;31mEssa opção não é válida, escolha novamente\033[m.")

#Efeito visual:
print("Calculando...")
sleep(2)

#Resultado:
if conversão == "01":
    print("O número \033[1;35m{}\033[m convertido para \033[1;35mbinário\033[m é \033[1;35m{}\033[m.".format(número, bin(número)[2:]))
elif conversão == "02":   
    print("O número \033[1;35m{}\033[m convertido para \033[1;35moctal\033[m é \033[1;35m{}\033[m.".format(número, oct(número)[2:]))
else:
    print("O número \033[1;35m{}\033[m convertido para \033[1;35mhexadecimal\033[m é \033[1;35m{}\033[m.".format(número, hex(número)[2:]))