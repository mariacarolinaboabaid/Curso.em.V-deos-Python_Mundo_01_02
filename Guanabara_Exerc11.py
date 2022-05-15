#Objetivo do programa:
print("Esse programa calculará a quantidade de tinta necessária para pintar uma parede, conforme sua área em metros quadros.\nA área será calculada de acordo com a largura e a altura dadas pelo Usuário.\nConsideramos que um litro de tinta pinte uma área de 2 metros quadrados.")

#Coletando os dados do Usuário:
largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))

#Calculando a área: 
área = (largura * altura) 
quantidade_tinta = área / 2

#Resultado:
print("A quantidade de tinta necessária para pintar a parede de {} metros quadradors é de {} litros.".format(área, quantidade_tinta))