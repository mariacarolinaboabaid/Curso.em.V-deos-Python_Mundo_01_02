#Objetivo do programa:
print("Esse programa solicitará ao Usuário um número e mostrará o seu dobro, triplo e raiz quadrada.")

#Importando o módulo Math:
import math

#Solicitando o número para o Usuário:
n = 0
while n == 0:
    número_usuário = input("Digite um número: ")
#Se o Uusário não digitar um número:
    if (número_usuário.isnumeric() == False):
        print("Digite apenas números!")
    else:
        número_usuário = int(número_usuário)
        n = n + 1

#Mostrando o resultado:
print("O dobro do número {} é {}, o seu triplo é {}, e a sua raiz quadrada é {:.3f}.".format(número_usuário, número_usuário * 2, número_usuário * 3, math.sqrt(número_usuário)))