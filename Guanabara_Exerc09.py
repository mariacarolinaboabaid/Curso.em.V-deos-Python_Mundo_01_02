#Objetivo do programa:
print("Esse programa calculará a tabuada do número inserido pelo Usuário.\nO limite do cálculo da tabuada será inserido também pelo Usuário.")

#Definindo a função para checar se o número é Float:
def is_float(número):
    try:
        float(número)
        return True
    except:
        return False

#Pedindo os dados para o Usuário:
n = 0
while n == 0:
   número_usuário = input("Digite o número inteiro que você deseja realizar a tabuada: ")
   limite_cálculo = input("Digite até que número você deseja fazer a multiplicação da tabuada: ")
#Caso os dados inseridos pelo Usuário estejam corretos:
   if (número_usuário.isnumeric() == True) or (is_float(número_usuário)== True) and (limite_cálculo.isnumeric() == True):
       número_usuário = float(número_usuário)
       limite_cálculo = int(limite_cálculo)
       n = n + 1 
#Se o Usuário não digitar números:
   else:
        print("Apenas números devem ser digitados!")

#Imprimindo os valores da tabuada:
for i in range(1, limite_cálculo + 1):
    print("O número {} multiplicado por {} equivale a {:.2f}.".format(número_usuário, i, número_usuário * i))
    i = i + 1