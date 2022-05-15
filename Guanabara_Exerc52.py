#OBJETIVO DO PROGRAMA:
print("\033[1;36mVamos verificar se um número é primo?\033[m")

#IMPORTANDO O MÓDULO TIME:
from time import sleep

#PEDINDO UM NÚMERO PARA O USUÁRIO:
i = 0
while i == 0:
    number = input("\033[1;34mInsira um número qualquer: \033[m")
    try:
        number = int(number)
        i = i + 1
    except:
        print("\033[1;31mAceitamos apenas dígitos numéricos. Tente novamente!\033[m")

#EFEITO VISUAL:
print("\033[1;37mAguarde, estamos verificando...\033[m")
sleep(3)

#PRIMO OU NÃO?
lista_divisores = list ()
for número in range(1, number + 1):
    if number % número == 0:
        lista_divisores.append(número)

#RESULTADO:
if lista_divisores == [1, number]:
    print("\033[1;35mEsse número é primo!\033[m")
else:
    print("\033[1;33mEsse número não é primo! Ele é divisível por {}, sendo eles: {}.\033[m".format(len(lista_divisores), lista_divisores))
    
 