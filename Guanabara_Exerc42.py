#Objetivo do programa:
print("""Diga o cumprimento dos lados de um triângulo e diremos se e possível de compor a forma geométrica.
Também diremos se com os cumprimentos dados o triângulo será: 
[1] Equilátero 
[2] Isósceles
[3] Escaleno.
\033[1;35mVamos lá!\033[m""")

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
    print("\033[1;32mEsse triângulo é possível de ser criado!\033[m")
    if (lados[0] == lados[1] == lados[2]):
        print("\033[1;33mO triângulo será equilátero!\033[m")
    elif (lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]):
        print("\033[1;36mO triângulo será isósceles!\033[m")
    elif lados[0] != lados[1] != lados[2]:
        print("\033[1;34mO triângulo será escaleno!\033[m")
else:
    print("\033[1;31mEsse triângulo não é possível de ser criado!\033[m")