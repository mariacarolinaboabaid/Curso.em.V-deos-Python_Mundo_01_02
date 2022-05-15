#Verificando se o Usuário e o programa escolhem os mesmos números.

#Importando o módulo Random e Time:
from random import randint
from time import sleep

#Solicitando os dados do Usuário:
i = 0
while i == 0:
    max_number = input("Digite o número máximo inteiro e positivo que pode ser sorteado: ")
    try:
        max_number = int(max_number)
        i = i + 1
    except:
        print("Digite apenas dígitos numéricos.")

#Escolha do número do Usuário:
choice_user = int(input("Escolha o número entre O e {}: ".format(max_number)))
choice_program = randint(0, max_number)
print("O número sorteado pelo programa é: {}.".format(choice_program))

#Efeito visual:
print("Processando o resultado...")
sleep(3)

#Resultado:
if choice_user == choice_program:
    print("O programa e o Usuário escolheram o número {}.".format(choice_program))
else:
    print("Os números escolhidos pelo Usuário e programa são diferentes. Usuário: {}, Programa: {}.".format(choice_user, choice_program))

