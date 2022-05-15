#OBJETIVO DO PROGRAMA: Validação de Dados: Ler o sexo da pessoa apenas aceitando "M" ou "F"

sexo = input("Sexo [M/F]: ").strip().upper()[0]
while sexo not in "F M":
    sexo = input("Aceitamos apenas 'M' ou 'F'. Tente novamente! Sexo: ").strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))