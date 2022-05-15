#Objetivo do programa:
print("Esse programa calculará a conversão de Real para Dólar conforme cotação dada pelo Usuário.")

#Solicitando para o Usuário os dados da moeda a ser convertida:
valor_converter = float(input("Qual o valor que o Usuário deseja converter?: R$ "))
valor_cotação = float(input("Qual o valor do Dólar para R$ 1,00?:$ "))

#Cálculo da conversão:
conversão = valor_converter / valor_cotação

#Resultado:
print("O valor de R${:.2f} corresponde a ${:.2f}, considerando a cotação de R$1,00 = ${:.2f}.".format(valor_converter, conversão, valor_cotação))
