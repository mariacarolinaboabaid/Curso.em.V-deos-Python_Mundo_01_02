#Objetivo do programa:
print("Esse programa calculará a média aritmética das notas dos alunos.")

#Perguntando o nome do aluno:
nome_aluno = input("Digite o nome do(a) aluno(a): ")

#Solicitando a quantidade de notas do aluno que serão informadas:
n = 0
while n == 0:
    quantidade_notas = input("Digite aqui a quantidade de notas do(a) aluno(a) {} a serem calculadas: ".format(nome_aluno))
    if (quantidade_notas.isnumeric() == False):
        print("Digite apenas números!")
    else:
        quantidade_notas = float(quantidade_notas)
        n = n + 1

#Solicitando as notas do aluno individualmente:
i = 0
notas = list()
while i < quantidade_notas:
    nota = input("Digite a aqui a nota {} do(a) aluno(a) {}: ".format(i +1, nome_aluno))
    if (nota.isnumeric() == False):
        print("Digite apenas números!")
    else:
        notas.append(float(nota))
        i = i + 1

#Demonstrando a média aritmética do aluno:
print("A média aritmética do(a) aluno(a) {} é {:.3f}.".format(nome_aluno, sum(notas) / quantidade_notas))