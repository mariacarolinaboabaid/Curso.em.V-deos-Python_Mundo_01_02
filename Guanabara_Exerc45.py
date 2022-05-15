#OBJETIVO DO PROGRAMA:
print("\033[1;31mJ\033[m \033[1;32mO\033[m \033[1;33mK\033[m \033[1;34mE\033[m \033[1;35mN\033[m \033[1;36mP\033[m \033[1;31mÔ\033[m")

#IMPORTANDO OS MÓDULOS:
from random import randint
from time import sleep

#APRESENTAÇÃO DO JOGO:
print("""\033[1;37mPedra, Papel ou Tesoura?\033[m
Escolha a pedra, o papel ou a tesoura.\n
Jogue sozinho ou com o seu amigo.\n
Lembre o papel ganha da pedra, mas perde da tesoura.\n
A tesoura perde da pedra, mas ganha do papel.\n
A pedra ganha da tesoura, mas perde pro papel.\n
Vamos lá!!!""")
print("----" * 20)
sleep(1.5)

#PERGUNTANDO A OPÇÃO DE JOGO:
j = 0
while j == 0:
    print("""Opções de Jogo:
[1] 02 Players
[2] Jogar com o computador""")
    game = input("Selecione a opção de jogo: ")
    if game not in "1 2":
        print("\033[1;31mOpção inválide. Selecione 1 ou 2. Tente novamente!\033[m")
    else:
        j = j + 1

#INDICANDO AS JOGADAS DISPONÍVEIS:
sleep(1)
print("\033[1;37mJOGADAS DISPONÍVEIS: Pedra, Papel ou Tesoura.\033[m")
        
#JOGADA COM DOIS PLAYERS:
if game == "1": 
    i = 0
    while i == 0:
        player_01 = input("\033[1;31;45mJogada Player 01: \033[m")
        player_02 = input("\033[1;31;46mJogada Player 02: \033[m")
        player_01 = player_01.lower()
        player_02 = player_02.lower()
#SE OS JOGADORES INSERIREM OPÇÕES DE JOGADAS VÁLIDAS:
        if player_01 and player_02 in "pedra papel tesoura":
#EFEITO VISUAL:
            print("\033[1;31mJ\033[m \033[1;32mO\033[m")
            sleep(1)
            print("\033[1;33mK\033[m \033[1;34mE\033[m \033[1;35mN\033[m")
            sleep(1)
            print("\033[1;36mP\033[m \033[1;31mÔ\033[m")
            sleep(1)
#SE OS JOGADORES INSERIREM A MESMA OPÇÃO:
            if (player_01 == player_02 == "pedra") or (player_01 == player_02 == "tesoura" ) or (player_01 == player_02 == "papel"):
                print("O Player 1 jogou {}. O Player 2 jogou {}. Empate entre os players.".format(player_01, player_02))
#HIPÓTESES QUE O PLAYER_1 VENCE:
            elif (player_01 == "pedra" and player_02 == "tesoura") or (player_01 == "tesoura" and player_02 == "papel") or (player_01 == "papel" and player_02 == "pedra"): 
                print("O Player 1 jogou {}. O Player 2 jogou {}. Player 01 ganhou!".formatformat(player_01, player_02))
#HIPÓTESES QUE O PLAYER_2 VENCE:
            elif (player_02 == "pedra" and player_01 == "tesoura") or (player_02 == "tesoura" and player_01 == "papel") or (player_02 == "papel" and player_01 == "pedra"): 
                print("O Player 1 jogou {}. O Player 2 jogou {}. Player 02 ganhou!".format(player_01, player_02))
            i = i + 1
#SE OS JOGADORES INSERIREM OPÇÕES DE JOGADAS INVÁLIDAS:
        else:
            print("\033[1;31mAs opções inseridas pelos players não são válidas. Joguem novamente!\033[m")

#JOGADA COM UM PLAYER VS COMPUTADOR:
elif game == "2":
    jogadas_computador = {1: "pedra", 2: "tesoura", 3: "papel"}
    computador = jogadas_computador[randint(1, 3)]
    x = 0
    print("O computador está escolhendo a sua jogada...Espere.")
    sleep(2)
    while x == 0:
        player_humano = input("\033[1;31;45mSua vez: \033[m")
        player_humano = player_humano.lower()
#SE O JOGADOR HUMANO INSERIR UMA OPÇÃO DE JOGADA VÁLIDA:
        if player_humano in "pedra papel tesoura":
#EFEITO VISUAL:
            print("\033[1;31mJ\033[m \033[1;32mO\033[m")
            sleep(1)
            print("\033[1;33mK\033[m \033[1;34mE\033[m \033[1;35mN\033[m")
            sleep(1)
            print("\033[1;36mP\033[m \033[1;31mÔ\033[m")
            sleep(1)
#SE O JOGADOR HUMANO E O COMPUTADOR ESCOLHEREM A MESMA OPÇÃO:
            if (player_humano == computador == "pedra") or (player_humano == computador == "tesoura") or (player_humano == computador == "papel"):
                print("O computador jogou {}. Você jogou {}. Deu empate!".format(computador, player_humano))
#HIPÓTESES QUE O JOGADOR HUMANO VENCE:
            elif (player_humano == "pedra" and computador == "tesoura") or (player_humano == "tesoura" and computador == "papel") or (player_humano == "papel" and computador == "pedra"): 
                print("O computador jogou {}. Você jogou {}. Você venceu!".format(computador, player_humano))
#HIPÓTESES QUE O COMPUTADOR VENCE:
            elif (computador == "pedra" and player_humano == "tesoura") or (computador == "tesoura" and player_humano == "papel") or (computador == "papel" and player_humano == "pedra"): 
                print("O computador jogou {}. Você jogou {}. O computador venceu!".format(computador, player_humano))
            x = x + 1
#SE O JOGADOR HUMANO NÃO INSERIR UMA OPÇÃO DE JOGADA VÁLIDA:
        else:
            print("\033[1;31mA opção inserida pelo player não é válidas. Jogue novamente!\033[m")

#FIM DO JOGO:
sleep(1)
print("----" * 20)
print("Fim do Jogo!")