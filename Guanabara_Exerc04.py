#Esse programa dissecará uma variável dada pelo Usuário

#Pedindo a variável para o Usuário:
variável_usuário = input("Digite algo:  ")

#Dissecando:
print("O tipo primitivo desse valor é: ", type(variável_usuário)) 
print("Só tem espaços?", variável_usuário.isspace())
print("É um número?", variável_usuário.isnumeric())
print("É alfabético?", variável_usuário.isalpha())
print("É alfanumérico?", variável_usuário.isalnum())
print("Está em maiúsculo?", variável_usuário.isupper())
print("Está em minúsculo?", variável_usuário.islower())
print("Está capitalizada?", variável_usuário.istitle())