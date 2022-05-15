#Objetivo do programa:
print("Esse programa mostra se um caráter aparece no texto inserido pelo Usuário, se sim, quantas vezes, o index de sua primeira e última ocorrência.")

#Pedindo os dados para o Usuário:
def finding_the_word(script, character):
    if  (script.upper().find(character.upper())) == -1:
        print("Essa palavra não está contida no texto.")
    else:
        print("A palavra aparece {} vezes, a partir do index {} e por último no index {}.".format(script.upper().count(character.upper()), script.upper().find(character.upper()), script.upper().rfind(character.upper())))

#Pedindo os dados para o Usuário:
text = input("Insira aqui o texto: ")
letter = input("Insira aqui a palavra que deseja procurar no texto: ")

#Resultado:
finding_the_word(text, letter)