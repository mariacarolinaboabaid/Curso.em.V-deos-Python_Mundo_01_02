#OBJETIVO DO PROGRAMA:
print("""\033[1mIremos ler todos os números inteiros e positivos.
Escolha uma palavra-chave para que o programa pare e mostre a quantidade dos números digitados e a sua soma.\033[m""")

#PALAVRA CHAVE:
palavra = input("\033[1;34mPalavra Chave: \033[m")

#SOLICITANDO OS NÚMEROS:
números = list()
número = ' '
while número != palavra:
    número = input("\033[36mNúmero: \033[m")
    if número == palavra:
        break
    else:
        while (número.isalpha() == True):
            número = input("\033[31mInsira apenas digitos numéricos. Número: \033[m")
        números.append(float(número))
    
#RESULTADO:
print("\033[1;32mA quantidade de números inserido é {} e a soma importa o total de {:.2f}\033[m.".format(len(números), sum(números)))