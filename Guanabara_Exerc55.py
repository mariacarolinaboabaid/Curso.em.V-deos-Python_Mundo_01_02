#OBJETIVO DO PROGRAMA:
print("\033[1;35mVamos analisar quem possui o maior peso?\033[m")

#PERGUNTANDO OS DADOS PARA O USUÁRIO:
i = 0
while i == 0:
    quantity = input("\033[1;36mQual a quantidade de pessoas que você deseja analisar? \033[m")
    try:
        quantity = int(quantity)
        i = i + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

x = 1
names = list()
weight_list = list()
while x != quantity + 1:
    name = input("Qual o nome da pessoa {}? ".format(x))
    weigth = input("Qual é o peso do(a) {}? ".format(name))
    try:
        weigth = float(weigth)
        weight_list.append(weigth)
        names.append(name)
        x = x + 1
    except:
        print("\033[1;31mInsira apenas dígitos numéricos. Tente novamente!\033[m")

#RESULTADO:
print("""\033[1;34mA pessoa mais leve é o(a) {}, com {}kg.
A pessoa mais pesado é o(a) {}, com {}kg.""".format(names[weight_list.index(min(weight_list))], min(weight_list), names[weight_list.index(max(weight_list))], max(weight_list)))

