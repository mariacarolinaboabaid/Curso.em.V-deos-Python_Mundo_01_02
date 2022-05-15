#Objetivo do programa:
print("""Esse programa aprovará ou não o empréstimo solicitado pelo Usuário.
A condição de aprovação do empréstimo que o valor da parcela mensal não ultrapasse 30% do salário do Usuário.""")

#Importando o módulo Time:
from time import sleep

#Pedindo os dados para o Usuário:
i = 0
while i == 0: 
    valor_emprestimo = input("Qual o valor desejado do empréstimo: R$ ")
    salario = input("Qual o valor do salário do(a) Sr(a): R$ ")
    anos = input("Em quantos anos o(a) Sr(a) deseja pagar o empréstimo: ")
    try: 
        valor_emprestimo = float(valor_emprestimo)
        salario = float(salario)
        anos = int(anos) * 12
        i = i + 1
    except:
        print("Digite apenas dígitos numéricos.")

#Fórmulas de cálculo da condição de aprovação:
prestação_mensal = valor_emprestimo / anos
limite_prestação = salario * 0.3

#Efeito visual:
print("Processando...")
sleep(2)

#Resultado:
if prestação_mensal > limite_prestação:
    print("O valor da prestação mensal excede 30% do salário do(a) Sr(a). \033[1;31mSeu pedido de empréstimo foi NEGADO.")
else:
    print("\033[1;32mO pedido de empréstimo do(a) Sr(a) foi APROVADO!")