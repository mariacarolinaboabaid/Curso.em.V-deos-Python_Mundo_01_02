#OBJETIVO DO PROGRAMA:
print("Calcularemos o preço final do produto conforme a forma de pagamento escolhida pelo Consumidor.")

#PERGUNTANDO O PREÇO DO PRODUTO:
i = 0 
while i == 0:
    preço_produto = input("Insira aqui o preço do produto: R$ ")
    try:
        preço_produto = float(preço_produto)
        i = i + 1
    except:
        print("\033[31mAceitamos apenas números. Insira novamente o preço do produto.\033[m")

#FORMAS DE PAGAMENTO DISPONÍVEIS:
print("""As formas de pagamento são:
[1] \033[32mÀ VISTA NO DINHEIRO OU CHEQUE = Desconto de 10%\033[m
[2] \033[35mÀ VISTA NO CARTÃO = Desconto de 5%\033[m
[3] \033[33mPARCELADO 2x NO CARTÃO DE CRÉDITO = Preço normal\033[m
[4] \033[36mPARCELADO 3 OU MAIS VEZES NO CARTÃO DE CRÉDITO = Juros de 20%\033[m""")

#PERGUNTANDO AO CONSUMIDOR A FORMA DE PAGAMENTO:
x = 0
while x == 0:
    forma_pagamento = input("Agora, insira aqui a sua escolha da forma de pagamento. Digite: 1, 2, 3 ou 4: ")
#FAZENDO O CÁLCULO DO PREÇO FINAL DO PRODUTO:
    if forma_pagamento in "1 2 3 4":
#À VISTA NO DINHEIRO OU CHEQUE
        if forma_pagamento == "1":
            desconto = preço_produto * 0.1
            print("O desconto é de R$ {:.2f} e o preço final do produto é de R$ {:.2f}.".format(desconto, preço_produto - desconto))
#À VISTA NO CARTÃO:
        elif forma_pagamento == "2":
            desconto = preço_produto * 0.05
            print("O desconto é de R$ {:.2f} e o preço final do produto fica em R$ {:.2f}.".format(desconto, preço_produto - desconto))
#PARCELADO 2x NO CARTÃO DE CRÉDITO:
        elif forma_pagamento == "3":
            print("O preço final do produto fica em R$ {:.2f}, com duas parcelas de R$ {:.2f}.".format(preço_produto, preço_produto / 2))
#PARCELADO 3 OU MAIS VEZES NO CARTÃO DE CRÉDITO:
        elif forma_pagamento == "4":
            juros = preço_produto * 0.2
            preço_juros = preço_produto + juros
#PEDINDO O NÚMERO DE PARCELAS AO CONSUMIDOR:
            j = 0
            while j == 0:
                parcela = input("Insira a quantidade de parcelas: ")
                try: 
                    parcela = int(parcela)
                    j = j + 1
#CASO O CONSUMIDOR NÃO INSIRA A QUANTIDADE DE PARCELAS EM DÍGITOS NUMÉRICOS:
                except:
                    print("\033[31mAceitamos apenas números. Insira novamente o número de parcelas.\033[m")
            print("Os juros totalizam R$ {:.2f}, o preço final do produto fica R$ {:.2f}, parcelado em {}x de R$ {:.2f}.".format(juros, preço_juros, parcela, preço_juros / parcela))
        x = x + 1
#CASO O CONSUMIDOR NÃO ESCOLHA UMA DAS FORMAS DE PAGAMENTO DISPONÍVEIS:
    else:
        print("\033[31mErro na escolha, tente novamente. Lembre-se, digite 1, 2, 3 ou 4.\033[m")