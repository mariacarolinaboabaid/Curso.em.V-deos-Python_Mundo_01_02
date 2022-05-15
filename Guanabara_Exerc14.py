#Objetivo do programa:
print("Esse programa converterá a temperatura em Celsius para Fahrenheit e vice versa.")

#Definindo as funções:
def conversor_fahrenheit():
    celsius = float(input("Qual a temperatura em Celsius? "))
    fahreneit = celsius * 1.8 + 32
    print("A temperatura de {} em Celsius equivale a {:.2f} em Fahrenheit.".format(celsius, fahreneit))

def conversor_celsius():
    fahrenheit = float(input("Qual a temperatura em Fahrenheit? "))
    celsius= (fahrenheit - 32) / 1.8
    print("A temperatura de {} em Fahrenheit equivale a {:.2f} em Celsius.".format(fahrenheit, celsius))

#Perguntando ao Usuário para qual escala termométrica ele deseja converter:
escolha = input("Digite '1': para converter Celsius para Fahrenheit / '2': para converter Fahrenheit para Celsius: ")

#Resultado:
if escolha == "1":
    conversor_fahrenheit()
elif escolha == "2":
    conversor_celsius()