#Objetivo do programa:
print("O Usuário deve inserir o texto e indicar a palavra que deseja procurar.")

#Definindo a função: 
def finding_the_word(script, expression):
    if  (script.upper().find(expression.upper())) == -1:
        print("Essa palavra não está contida no texto.")
    else:
        print("A palavra aparece {} vezes, a partir do index {}.".format(script.upper().count(expression.upper()), script.upper().find(expression.upper())))

#Pedindo os dados para o Usuário:
text = input("Insira aqui o texto: ")
word = input("Insira aqui a palavra que deseja procurar no texto: ")

#Resultado:
finding_the_word(text, word)
