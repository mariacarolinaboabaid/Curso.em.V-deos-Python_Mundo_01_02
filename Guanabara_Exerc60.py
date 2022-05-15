#OBJETIVO DO PROGRAMA: Vamos calcular o fatorial de um número dado pelo Usuário

#PEDINDO O NÚMERO PARA O USUÁRIO:
number = input("Qual o número para calcularmos o fatorial? ")
while number.isalpha() == True:
    number = input("Insira apenas dígitos numéricos e inteiro: ")
number = int(number)

#IMPORTANDO O MÓDULO MATH:
from math import factorial
print("O fatorial do número {} é {}.".format(number, factorial(number)))