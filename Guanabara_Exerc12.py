#Objetivo do programa:
print("Esse programa calculará o preço do produto com o desconto indicado pelo Usuário.")

#Coletando os dados do Usuário:
valor_original = float(input("Insira o preço do produto: R$ "))
desconto = int(input("Qual a porcentagem do desconto?: ")) 

#Calculando o desconto:
valor_com_desconto = valor_original - (valor_original * desconto / 100)

#Resultado:
print("O valor do produto é R${:.2f}, com o desconto de {}% o valor do produto passa a ser de R${:.2f}.".format(valor_original, desconto, valor_com_desconto))

