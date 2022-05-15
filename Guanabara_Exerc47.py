#OBJETIVO DO PROGRAMA:
print("Escolha o número inteiro par máximo e mostraremos todos os números pares entre ele e 0!")

#DEFININDO O NÚMERO PAR MÁXIMO:
i = 0
while i == 0:
    par_máximo = input("Digite o número inteiro par máximo desejado: ")
    if par_máximo.endswith(('1', '3', '5', '7', '9')):
        print("Insira apenas números pares. Tente novamente!")
    elif par_máximo.isdecimal() == False:
        print("Aceitamos apenas dígitos numéricos. Tente novamente!")
    else:
        par_máximo = int(par_máximo)
        i = i + 1

#PRINTANDO OS NÚMEROS PARES:
for par in range(0, par_máximo + 1, 2):
    print(par)
print("Fim!")