print("Esse programa pedirá ao Usuário um número inteiro e mostrará seu antecessor e sucessor")

#Pedindo o número para o Usuário:
n = 0
while n < 1:
    número_usuário = input("Digite um número inteiro: ")
#Verificando se é um número inteiro:
    if número_usuário.isalpha():    
        print("Digte apenas números!")
    else:
        número_usuário = int(número_usuário)
        n = n + 1

#Mostrando o resultado:
print("O número antecessor de {} é {}, e o seu número sucessor é {}.".format(número_usuário, número_usuário - 1, número_usuário + 1))