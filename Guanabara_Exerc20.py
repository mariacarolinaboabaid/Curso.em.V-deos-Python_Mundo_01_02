#O programa apresentará a ordem sorteada de seus alunos:

#Importando o módulo Random:
from random import shuffle

#Declarando as variáveis:
alunos = []

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
    aluno_nome = input("Digite o nome do aluno {}: ".format(x))
    alunos.append(aluno_nome)

#Sorteando:
shuffle(alunos)

#Resultado:
print("A lista dos alunos sorteada é: {}.". format(alunos))
