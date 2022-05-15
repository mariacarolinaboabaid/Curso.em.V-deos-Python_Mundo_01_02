#Objetivo do programa:
print("""Esse programa classificará os atletas de acordo com a sua idade. As categorias são: 
[a] Mirim = 0 a 9 anos
[b] Infantil = 10 a 14 anos
[c] Júnior = 15 a 19 anos
[d] Sênior = 20 a 25 anos
[e] Master = A partir de 26 anos.""")

#Importando o módulo Time:
from datetime import date

#Pedindo os dados do atleta:
i = 0
while i == 0:
    nome_atleta = input("NOME: ")
    ano_nascimento = input("ANO DE NASCIMENTO: ")
    try:
        ano_nascimento = int(ano_nascimento)
        i = i + 1
    except:
        print("Somente dígitos numéricos são aceitos. Tente novamente!")

#Calculando a idade:
idade = date.today().year - ano_nascimento

#Resultado:
if 9 >= idade >= 0:
    print("\033[1;31;42mO atleta {} está na categoria Mirim.\033[m".format(nome_atleta))
elif 14 >= idade >= 10:
    print("\033[1;31;43mO atleta {} está na categoria Infantil.\033[m".format(nome_atleta))
elif 19 >= idade >= 15:
    print("\033[1;31;44mO atleta {} está na categoria Júnior.\033[m".format(nome_atleta))
elif 25 >= idade >= 20:
    print("\033[1;31;45mO atleta {} está na categoria Sênior.\033[m".format(nome_atleta))
elif 26 >= idade:
    print("\033[1;31;46mO atleta {} está na categoria Master.\033[m".format(nome_atleta))