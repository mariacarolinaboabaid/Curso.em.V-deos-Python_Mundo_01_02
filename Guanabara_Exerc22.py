#Perguntando o nome do Usuário:
nome = input("Insira aqui seu nome: ")

#Nome em letras maiúsculas:
print("Seu nome em letras maísculas: {}.".format(nome.upper())) 

#Nome em letras minúsculas:
print("Seu nome em letras maísculas: {}.".format(nome.lower())) 

#Quantidade de letras sem considerar espaço:
lista_nome = list(nome)
lista_nome.remove(" ")
print("O seu nome possui {} letras.".format(len(lista_nome)))

#Quantidade de letras que possui o primeiro nome:
print("O seu primeiro nome tem {} letras.".format(len(nome.split()[0])))



