#O programa sorteará um aluno para os professores:

#Importando o módulo Random:
from random import choice, randint

#Declarando as variáveis:
alunos = {}

#Solicitando a quantidade de alunos para o Usuário:
i = 0
while i == 0:
    quantidade_alunos = input("Insira aqui a quantidade de alunos que participarão do sorteio: ")
    if quantidade_alunos.isnumeric()== True:
        quantidade_alunos = int(quantidade_alunos)
        i = i + 1
    else:
        print("Digite apenas números inteiros.")

#Solicitando os nomes dos alunos:
for x in range(1, quantidade_alunos + 1):
    alunos[x] = input("Digite o nome do aluno {}: ".format(x))

#Sorteando:
sorteio = choice(alunos)

#Resultado:
print("O aluno sorteado foi {}.". format(sorteio))
