#Objetivo do programa:
print("Esse programa calculará a média do aluno para verificar se ele foi aprovado, reprovado ou está em recuperação.")

#Dicionário das cores:
cores = {"verde_negrito" : "\033[1;32m", "amarelo_negrito" : "\033[1;33m", "vermelho_negrito" : "\033[1;31m", "fim" : "\033[m" }

#Importando o módulo time:
from time import sleep

#Pedindo a quantidade de notas a serem computadas para o Professor:
x = 0
while x == 0:
    quantidade_notas = input("Quantas notas serão computadas? ")
    try:
        quantidade_notas = int(quantidade_notas)
        x = x + 1
    except:
        print("Insira apenas dígitos numéricos. Tente novamente!")

#Pedindo as notas para o Professor:
notas = list ()
i = 1
while i <= quantidade_notas:
    nota = input("Insira a nota {} aqui: ".format(i))
    try:
        nota = float(nota)
        notas.append(nota)
        i = i + 1
    except:
        print("Insira apenas dígitos numéricos. Tente novamente!")

#Calculando a média:
print("Calculando a média....Aguarde....")
sleep(1.5)
média = sum(notas) / quantidade_notas

#Resultado:
if média < 5:
    print(cores["vermelho_negrito"],"Sua média é {:.2f}. Você foi REPROVADO".format(média))
elif 6.9 >= média >= 5:
    print(cores["amarelo_negrito"],"Sua média é {:.2f}. Você está em RECUPERAÇÃO".format(média))
elif média >= 7:
    print(cores["verde_negrito"],"Sua média é {:.2f}. Você foi APROVADO".format(média))