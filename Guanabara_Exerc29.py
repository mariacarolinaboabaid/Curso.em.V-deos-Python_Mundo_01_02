#Objetivo do programa:
print("""Esse programa solicitará a velocidade do carro, e caso ultrapasse o limite de velocidade mostrará o valor da multa.
O limite de velocidade é 80 Km/h.
O valor da multa é de R$ 7,00 para cada Km/h acima do limite.""")

#Importando o módulo time:
from time import sleep
#Solicitando a velocidade do Usuário:
i = 0
while i == 0:
    velocity = input("Digite a velocidade por Km/h: ")
    try:
        velocity = int(velocity)
        i = i + 1
    except:
        print("Digite apenas dígitos numéricos.")

#Efeito visual:
print("Processando...")
sleep(3)

#Resultado:
if velocity > 80:
    traffic_ticket = (velocity - 80) * 7
    print("O motorista ultrapassou o limite de velocidade por {} Km/h, e deverá pagar R$ {},00 a título de multa.".format((velocity - 80), traffic_ticket))
else:
    print("O motorista está dentro do limite de velocidade.")

print("Lembrete: Dirija sempre com segurança!")