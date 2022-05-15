#OBJETIVO DO PROGRAMA:
print("\033[1;35mÉ um palíndromo?\033[m")

#PEDINDO OS DADOS PARA O USUÁRIO:
phrase = input("\033[1;36mFrase: \033[m")

#TRANSFORMANDO A FRASE EM UMA LISTA:
phrase_upper = phrase.upper()
list_phrase = list(phrase_upper)
end = len(list_phrase) + 1

#RETIRANDO OS BLANK SPACES:
for i in range(0, end):
    if " " in list_phrase:
     list_phrase.remove(" ")
     
#FAZENDO UMA CÓPIA PARA REVERTER A LISTA:
list_phrase_copy = list_phrase[ : ]
list_phrase_copy.reverse()

#RESULTADO:
if (list_phrase == list_phrase_copy):
    print("\033[1;32m'{}'é um palíndromo.\033[m".format(phrase))
else:
    print("\033[1;31m'{}' não é um palíndromo.\033[m".format(phrase))