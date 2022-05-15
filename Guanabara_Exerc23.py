#Criando função para checar se o número é negativo:
def number_negativo(número):
    if número < 0:
       return True
    else:
        return False

#Solicitando o número para o Usuário:
i = 0 
while i == 0:
    number = input("Digite aqui um número de 0 a 9.999: ")
    if number.isalpha() == True:
        print("Digite apenas dígitos numéricos.")
    else:
        number = int(number)
        if number >= 10000:
            print("O número deve ser entre 0 a 9.999.")
        elif number_negativo(number) == True:
            print("Digite apenas números positivos.")
        else:
            number = str(number)
            i = i + 1

#Imprimindo o número:
if len(number) == 4:
    unidade = number[3]
    dezena = number[2]
    centena = number [1]
    milhar = number [0]
    print("Unidade: {}, Dezena: {}, Centena: {}, Milhar: {}.".format(unidade, dezena, centena, milhar))
elif len(number) == 3:
    unidade = number[2]
    dezena = number[1]
    centena = number [0]
    milhar = 0
    print("Unidade: {}, Dezena: {}, Centena: {}, Milhar: {}.".format(unidade, dezena, centena, milhar))   
elif len(number) == 2:
    unidade = number [1]
    dezena = number [0]
    centena = 0
    milhar = 0
    print("Unidade: {}, Dezena: {}, Centena: {}, Milhar: {}.".format(unidade, dezena, centena, milhar))
elif len(number) == 1:
    unidade = number [0]
    dezena = 0
    centena = 0
    milhar = 0
    print("Unidade: {}, Dezena: {}, Centena: {}, Milhar: {}.".format(unidade, dezena, centena, milhar))                 