#Objetivo do progarma:
print("Esse programa solicita o nome completo do Usuário, mostrando seu primeiro e último nome.")

#Pedindo os dados para o Usuário:
name = input("Insira aqui o seu nome completo: ")
splitted_name = name.split()


#Resultado:
print("O nome completo do Usuário é {}, seu primeiro nome é {}, e o seu último nome é {}.".format(name, splitted_name[0], splitted_name[len(splitted_name) - 1]))