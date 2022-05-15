#Esse programa irá checar se a cidade inserida pelo Usuário inicia com "Santo":

#Pedindo o nome da cidade para o Usuário:
city = input("Insira aqui a cidade de sua residência: ")

#Analisando o nome da cidade:
if city.upper().strip().startswith("SANTO"):
    print("O nome da sua cidade começa com Santo!")
else:
    print("O nome da sua cidade não começa com Santo.")