#O que o progtama faz:
print("Esse programa pedirá ao Usuário dois números e mostrará a sua soma")

#Criando as variáveis:
n = 0
número = list()

#Perguntando ao Usuário os números a serem adicionados:
while n < 2:
    usuário_número = (input("Digite um número aqui: "))
    if (usuário_número.isnumeric()):
        usuário_número = float(usuário_número)
        número.append(usuário_número)
        n = n + 1
    elif (usuário_número.isalpha()):
        print("Digite apenas números!")

#Mostrando o resultado:
print("A soma dos números é:", sum(número))