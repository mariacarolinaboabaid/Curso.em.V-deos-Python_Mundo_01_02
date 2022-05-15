#Objetivo do programa:
print("Esse programa dirá se os cumprimentos dados pelo Usuário são capazes de formar um triângulo.")

#Pedindo os lados para o Usuário:
lados = []
i = 1
while i < 4:
    lado = input("Digite o cumprimento do lado {}: ".format(i))
    try:
        lado = float(lado)
        lados.append(lado)
        i = i + 1
    except:
        print("Insira apenas dígitos numéricos.")

#Resultado:
if (lados[0] < lados[1] + lados[2]) and (lados[1] < lados[0] + lados[2]) and (lados[2] < lados[0] + lados[1]):
    print("Esse triângulo é possível de ser criado!")
else:
    print("Esse triângulo não é possível de ser criado!")