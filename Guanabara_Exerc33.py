#Objetivo do programa:
print("""O programa lerá a quantidade de números desejada pelo Usuário.
Após o Usuário inserir todos os números desejados, o programa os sorteará em ordem crescente, mostrando o menor e maior números.""")

#Declarando a variável:
numbers = []

#Pedindo os dados para o Usuário:
i = 0
while i == 0:
    amount_numbers = input("Qual a quantidade de números a serem lidos? ")
    try:
        amount_numbers = int(amount_numbers)
        i = i + 1
    except:
        print("Digite apenas dígitos numéricos e inteiros.")

#Montando a lista de números:
for x in range(1, amount_numbers + 1):
    number = input("Digite o número {} aqui: ".format(x))
    try:
        number = int(number)
        numbers.append(number)
        x = x + 1
    except:
        print("Digite apenas dígitos numéricos e inteiros.")

#Sorteando a lista:
numbers.sort()

#Resultado:
print("O menor número da lista é {}, ao passo que o maior número é {}.".format(numbers[0], numbers[len(numbers) - 1]))