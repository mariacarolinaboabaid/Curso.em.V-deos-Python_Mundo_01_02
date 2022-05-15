#Objetivo do programa:
print("Esse programa transformará a medida em metros inserida pelo Usuário em centímeros e milímetros!")

#Pedindo a medida em metros do Usuário:
medida_metros = input("Digite aqui a medida em metros: ")
#Mostrando o resultado para o Usuário:
try: 
    medida_metros = float(medida_metros)
    print("{} metros equivale a {:.0f} centímetros e {:.0f} milímetros.".format(medida_metros, medida_metros * 100, medida_metros * 1000))
#Caso o Usuário não insira um número:
except:
    print("Você deve apenas digitar números.")
    

