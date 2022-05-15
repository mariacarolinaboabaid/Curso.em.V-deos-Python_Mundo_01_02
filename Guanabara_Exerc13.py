#Objetivo do programa:
print("Esse programa calculará o reajuste salarial conforme porcentagem dada pelo Usuário.")

#Definindo a função:
def reajuste_salarial (salário, reajuste):
    salário_reajustado = salário + salário * (reajuste / 100)
    print("O valor do salário reajustado é de R${:.2f}.".format(salário_reajustado))

#Pedindo os dados para o Usuário:
salário = float(input("Digite aqui o valor do salário a ser reajustado: R$ "))
reajuste = float(input("Digite aqui a porcentagem do reajuste: "))

#Resultado:
reajuste_salarial(salário, reajuste)