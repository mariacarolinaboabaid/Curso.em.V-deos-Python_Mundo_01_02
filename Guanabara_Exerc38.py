#Objetivo do programa:
print("Esse programa analisará os dois números dados pelo Usuário e dirá qual é o maior ou se são equivalentes.")

#Importando o módulo time:
from time import sleep

#Pedindo os números para o Usuário:
i = 0
while i == 0:
    number_01 = input("Insira aqui o primeiro número: ")
    number_02 = input("Insira aqui o segundo número: ")
    try:
        number_01 = float(number_01)
        number_02 = float(number_02)
        i = i + 1
    except:
        print("\033[31mInsira apenas dígitos numéricos.Tente novamente.\033[m")

#Analisando os números:
print("Analisando os números...")
sleep(2)

#Resultado:
if number_01 > number_02:
    print("O primeiro número de valor {:.2f} é maior que o segundo número de valor {:.2f}.".format(number_01, number_02))
elif number_02 > number_01:
    print("O segundo número de valor {:.2f} é maior que o primeiro número de valor {:.2f}.".format(number_02, number_01))
else:
    print("O primeiro número de valor {:.2f} e o segundo número de valor {:.2f} são iguais.".format(number_01, number_02))