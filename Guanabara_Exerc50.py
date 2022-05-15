#OBJETIVO DO PROGRAMA:
print("Listaremos e somaremos todos os números pares ou ímpares existentes entre o intervalo escolhido por você!")

#SOLICITANDO O INTERVALO PARA O USUÁRIO:
i = 0
while i == 0:
    intervalo_inicial = input("Insira o início do intervalo aqui: ")
    intervalo_final = input("Insira o final do intervalo aqui: ")
    try:
        intervalo_inicial = int(intervalo_inicial)
        intervalo_final = int(intervalo_final)
        i = i + 1
    except:
        print("\033[1;31mAceitamos apenas dígitos numéricos. Tente novamente!\033[m")

#ESCOLHENDO PAR OU ÍMPAR:
x = 0
while x == 0:
    escolha = input("Escolha entre PAR ou ÍMPAR: ")
    if (escolha.lower() not in "par ímpar"):
        print("\033[1;31mDigite par ou ímpar Tente novamente!\033[m")
    else:
        x = x + 1

#SE A ESCOLHA POR PAR:
lista_pares = list()
lista_ímpares = list ()
if escolha.lower() == "par":
    for y in range(intervalo_inicial, intervalo_final + 1):
        if y % 2 == 0:
            lista_pares.append(y)
#RESULTADO:
    print("Entre {} e {}, a quantidade de números pares é {}, a sua soma é {}, e os números são:{}.". format(intervalo_inicial, intervalo_final, len(lista_pares), sum(lista_pares), lista_pares))
#SE A ESCOLHA POR ÍMPAR:
elif escolha.lower() == "ímpar":
    for z in range(intervalo_inicial, intervalo_final + 1):
        if z % 2 != 0:
            lista_ímpares.append(z)
#RESULTADO:
    print("Entre {} e {}, a quantidade de números pares é {}, a sua soma é {}, e os números são: {}.". format(intervalo_inicial, intervalo_final, len(lista_ímpares), sum(lista_ímpares), lista_ímpares))