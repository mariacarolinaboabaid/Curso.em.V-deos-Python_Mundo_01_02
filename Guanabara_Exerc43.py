#OBJETIVO DO PROGRAMA:
print("""Calcularemos o IMC do Usuário, solicitando seu peso e altura.
As classificações do IMC são:
[1] Menor que 18,5 = Abaixo do peso
[2] Entre 18,5 até 24,9 = Ideal
[3] Entre 25 até 29,9 = Sobrepeso
[4] Entre 30 a 39,9 = Obesidade
[5] Acima de 40 = Obesidade mórbida.
\033[1mVamos lá\033[m""")

#PEDINDO OS DADOS PARA O USUÁRIO:
i = 0
while i == 0:
    peso = input("Peso Kg: ")
    altura = input("Altura: ")
    try:
        peso = float(peso)
        altura = float(altura)
        i = i + 1
    except:
        print("Apenas aceitamos dígitos numéricos. Insira novamente seu peso e altura!")

#FÓRMULA:
imc = peso / (altura ** 2)

#RESULTADO:
if 18.5 > imc:
    print("\033[1;31mSeu IMC é {:.1f}. Você está abaixo do peso!\033[m".format(imc))
elif 24.9 >= imc >= 18.5:
    print("\033[1;32mSeu IMC é {:.1f}. Você está no peso ideal. Parabéns!\033[m".format(imc))
elif 29.9 >= imc >= 25:
    print("\033[1;31mSeu IMC é {:.1f}. Você está com sobrepeso!\033[m".format(imc))
elif 39.9 >= imc >= 30:
    print("\033[1;31mSeu IMC é {:.1f}. Você está com obesidade!\033[m".format(imc))
elif imc >= 40:
    print("\033[1;31mSeu IMC é {:.1f}. Você está com obesidade mórbida!\033[m".format(imc))