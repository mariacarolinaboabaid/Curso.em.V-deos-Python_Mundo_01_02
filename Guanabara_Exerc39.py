#Objetivo do programa:
print("""\033[1;32mEsse programa solicitará o nascimento do Usuário e informará se está na sua hora de se alistar ao serviço militar.
Caso não esteja, indicará o tempo faltante ou o tempo que já se passou para o alistamento.\033[m""")

#Importando módulos:
from time import sleep
from datetime import date

#Perguntando o sexo:
sexo = input("SEXO (Masculino / Feminino): ")
if sexo == "Feminino":
    print("Você não precisa se alistar.")
    quit
elif sexo == "Masculino":
#Solicitando a data de nascimento para o Usuário:
    i  = 0
    while i == 0:
        ano_nascimento = input("ANO DE NASCIMENTO:  ")
        try:
            ano_nascimento = int(ano_nascimento)
            i = i + 1
        except:
            print("Digite apenas dígitos numéricos.")

#Efeitos visuais:
    print("Fazendo os cálculos......")
    sleep(1.5)

#Verificando o alistamento:
    ano_corrente = date.today().year
    alistamento = ano_corrente - ano_nascimento

    #Resultado:
    if alistamento == 18:
        print("Você tem {} anos, e precisa se alistar esse ano!".format(alistamento))
    elif alistamento < 18:
        saldo = 18 - alistamento
        print("Você tem {} anos, e em {} anos você precisará se alistar. Seu alistamento será no ano {}.".format(alistamento, saldo, ano_corrente + saldo))
    else:
        saldo = alistamento - 18
        print("Você tem {} anos, e já passou {} anos do seu alistamento. Seu alistamento foi no ano {}.".format(alistamento, saldo, ano_corrente - saldo))
