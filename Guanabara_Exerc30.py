#Objetivo do programa:
print("O programa solicitará um número para Usuário e informará se é par ou ímpar.")

#Pedindo o número para o Usuário:
i = 0
while i == 0:
    number = input("Digite aqui um número inteiro: ")
    if number.isdecimal() == False:
        print("Digite apenas dígitos numéricos, devendo o número ser inteiro e positivo.")
    else:
        number = int(number)
        i = i + 1

#Verificando se o número é par ou ímpar:
if (number % 2 == 0):
    print("O número {} é par.".format(number))
else:
    print("O número {} é ímpar.".format(number))