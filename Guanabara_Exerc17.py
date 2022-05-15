#Objetivo do programa: Calcular a hipotenusa a partir dos catetos

#Importando o módulo math:
from math import hypot

#Pedindo os valores dos catetos:
cateto_oposto = float(input("Qual a medida do cateto oposto? "))
cateto_adjacente= float(input("Qual a medida do cateto adjacente? "))

#Fórmula da hipotenusa:
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

#Resultado:
print("O valor da hipotenusa é {}.".format(hipotenusa))