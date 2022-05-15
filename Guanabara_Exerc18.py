#Objetivo do programa é calcular o seno, cosseno e a tangente de um ângulo

#Importando o módulo math:
from math import radians, sin, cos, tan

#Pedindo o ângulo para o Usuário:
angulo = float(input("Insira o valor do ângulo: "))

#Convertendo o ângulo para radianos:
radiano = radians(angulo)

#Calculando o seno, o cosseno e a tangente:
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

#Resultado:
print("Do ângulo {}, temos o seno de {:.2f}, o cosseno de {:.2f} e a tangente {:.2f}.". format(angulo, seno, cosseno, tangente))
