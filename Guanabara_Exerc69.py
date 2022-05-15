"""OBJETIVO DO PROGRAMA:
Solicitaremos o nome o sexo, idade e peso.
Informaremos quem é o mais velho e o mais novo de cada sexo e geral.
Informaremos também quem é o mais pesado e mais leve de cada sexo e geral.
Por fim, informaremos a média da idade de cada sexo e geral."""

#VARÍAVEIS MULHERES:
women_name = list()
women_age = list()
women_weight = list()
#VARÍAVEIS MULHERES:
men_name = list()
men_age = list()
men_weight = list()

#PERGUNTANDO O SEXO:
condição = "S"
while condição == "S":
    sex = input("Sexo (Feminino / Masculino): ").lower()[0]
    while sex not in "f m":
        sex = input("\033[31mOpção inválida. Insira 'feminino'ou 'masculino': \033[m")
#PERGUNTANDO NOME, IDADE E PESO:
    name = input("Primeiro nome: ")
    age = input("Idade: ")
    while age.isalpha() == True:
        age = input("\033[31mInsira apenas dígitos numéricos.\033[m Idade: ")
    age = int(age) 
    weigth = input("Peso: ")
    while weigth.isalpha() == True:
        weigth = input("\033[31mInsira apenas dígitos numéricos.\033[m Peso: ")
    weigth = float(weigth)
#SE O SEXO FOR FEMININO:
    if sex == "f":
        women_name.append(name)
        women_age.append(age)
        women_weight.append(weigth)
#SE O SEXO FOR MASCULINO:
    elif sex == "m":
        men_name.append(name)
        men_age.append(age)
        men_weight.append(weigth)
    condição = input("\033[1;34mDesejar continuar? [S/N] \033[m").strip().upper()[0]
    while condição not in "S N":
        condição = input("\033[1;31mInserir apenas 'sim' ou 'não'. \033[1;34m Deseja continuar? [S/N] \033[m").strip().upper()[0]
#GERAL:
general_name = women_name + men_name
general_age = women_age + men_age
general_weigth = women_weight + men_weight

#RESULTADO:
print("\033[1;31mR\033[m \033[1;32mE\033[m \033[1;33mS\033[m \033[1;34mU\033[m \033[1;35mL\033[m \033[1;36mT\033[m \033[1;31mA\033[m \033[1;32mD\033[m \033[1;33mO\033[m")
#RESULTADO FEMININO:
print("A mulher mais nova é a {} e tem {} anos.".format(women_name[women_age.index(min(women_age))].title(), min(women_age)))
print("A mulher mais velha é a {} e tem {} anos.".format(women_name[women_age.index(max(women_age))].title(), max(women_age)))
print("A mulher mais leve é a {} e tem {} kg.".format(women_name[women_weight.index(min(women_weight))].title(), min(women_weight)))
print("A mulher mais pesada é a {} e tem {} kg.\n".format(women_name[women_weight.index(max(women_weight))].title(), max(women_weight)))
#RESULTADO MASCULINO:
print("O homem mais novo é o {} e tem {} anos.".format(men_name[men_age.index(min(men_age))].title(), min(men_age)))
print("O homem mais velho é o {} e tem {} anos.".format(men_name[men_age.index(max(men_age))].title(), max(men_age)))
print("O homem mais leve é o {} e tem {} kg.".format(men_name[men_weight.index(min(men_weight))].title(), min(men_weight)))
print("O home mais pesado é o {} e tem {} kg.\n".format(men_name[men_weight.index(max(men_weight))].title(), max(men_weight)))
#RESULTADO GERAL:
print("A pessoa mais novo(a) é o(a) {} e tem {} anos.".format(general_name[general_age.index(min(general_age))].title(), min(general_age)))
print("A pessoa mais velho(a) é o(a) {} e tem {} anos.".format(general_name[general_age.index(max(general_age))].title(), max(general_age)))
print("A pessoa mais leve é o(a) {} e tem {} kg.".format(general_name[general_weigth.index(min(general_weigth))].title(), min(general_weigth)))
print("A pessoa mais pesada é o(a) {} e tem {} kg.\n".format(general_name[general_weigth.index(max(general_weigth))].title(), max(general_weigth)))