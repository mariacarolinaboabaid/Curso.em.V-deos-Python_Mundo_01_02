#OBJETIVO DO PROGRAMA:
print("""\033[1;36mMostraremos todos os múltiplos do número inteiro escolhido pelo Usuário até o limite escolhido por ele também!\033[m]
\033[1;32mVamos lá!\033[m""")

#ESCOLHENDO O NÚMERO MÚLTIPLO:
i = 0
while i == 0:
    múltiplo = input("\033[1;35mInsira aqui número que você deseja encontrar os seus múltiplos: \033[m")
    if múltiplo.isdecimal() == False:
        print("Aceitamos apenas dígitos numéricos. Tente novamente!")
    else:
        múltiplo = int(múltiplo)
        i = i + 1

#ESCOLHENDO O LIMITE:
x = 0
while x == 0:
    limite = input("\033[1;33mAgora insira o limite para encontrarmos os múltiplos do número escolhido: \033[m")
    if limite.isdecimal() == False:
        print("Aceitamos apenas dígitos numéricos. Tente novamente!")
    else:
        limite = int(limite)
        x = x + 1

#VERIFICANDO OS NÚMEROS MÚLTIPLOS:
lista_resultado = list ()
for y in range(0, limite + 1):
    if y % múltiplo == 0:
        lista_resultado.append(y)

#RESULTADO:
print("\033[1;31mOs múltiplos do número {}, entre o intervalo de 0 a {}, são: {}.\033[m".format(múltiplo, limite, lista_resultado))
print("\033[1;34mA quantidade de números múltilpos do número {}, entre o intervalo de 0 a {}, é {}, e a sua é {}.\033[m".format(múltiplo, limite, len(lista_resultado), sum(lista_resultado)))

