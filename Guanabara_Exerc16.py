#Objetivo do programa: Truncar um número com o módulo math

#Importando o módulo math:
from math import trunc

#Pedindo um número para o Usuário:
number = float(input("Insira aqui um número: "))

#Resultado:
print("A porção inteira do número {} é {}.".format(number, trunc(number)))