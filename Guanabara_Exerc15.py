#Objetivo do programa:
print("Cálculo do valor do aluguel do carro conforme diária e Km rodados.")

#Pedindo os dados para o Usuário:
valor_quilometragem = float(input("Qual o valor pago por Km rodado? R$"))
quilometragem = float(input("Qual foi a quilometragem rodada? "))
diária = float(input("Qual o valor da diária do aluguel? R$"))
dias = int(input("Por quantos dias o carro foi alugado? "))

#Definindo o cálculo do aluguel:
aluguel = (valor_quilometragem * quilometragem) + (diária * dias)

#Resultado:
print("O valor do aluguel é de R${:.2f}.".format(aluguel))


