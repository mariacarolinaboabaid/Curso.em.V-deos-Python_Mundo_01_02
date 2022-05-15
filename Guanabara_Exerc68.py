#IMPORTANDO OS MÓDULOS:
from time import sleep
from random import randint

#OBJETIVO DO PROGRAMA:
print("\033[1;31;43mPAR\033[m \033[1;31;44mOU\033[m \033[1;31;45mÍMPAR\033[m\033[1m?\033[m")
sleep(1)


condição = "S"
while condição == "S":
#PERGUNTANDO O TIPO DE JOGO:
    tipo_jogo = input("""\033[1;33mSelecione:
[1] Jogar com o computador
[2] Dois jogadores
Opção: \033[m""")
#CASO O USUÁRIO DIGITE UMA OPÇÃO DE JOGO INVÁLIDA:
    while tipo_jogo not in "1 2":
        tipo_jogo = input("""\033[1;31mInsira apenas '1' ou '2' .\033[m \033[1;33mSelecione:
[1] Jogar com o computador
[2] Dois jogadores
Opção: \033[m""")
    print("\033[1;35mAs opções de jogada são os números entre 0 a 10.\033[m")
#JOGO = HUMANO VS. COMPUTADOR
    if tipo_jogo == "1":
#PERGUNTANDO AO HUMANO A SUA JOGADA:
        escolha_humano = input("\033[1;31;46mEscolha entre 'PAR' ou 'ÍMPAR': \033[m").upper()
        while escolha_humano not in "PAR ÍMPAR IMPAR":
            escolha_humano = input("\033[1;31mInsira apenas PAR' ou 'ÍMPAR'.\033[m \033[1;31;46mEscolha novamente entre 'PAR' ou 'ÍMPAR': \033[m").upper()
        player_humano = input("\033[1;31;46mInsira a sua jogada: \033[m")
        while player_humano.isalpha() == True: 
            player_humano = ("\033[1;31mInsira apenas dígitos númericos entre 0 a 10. \033[m \033[1;31;46mInsira novamente a sua jogada: \033[m")
        player_humano = int(player_humano)
#SORTEANDO O NÚMERO DO COMPUTADOR:
        computador = randint(0, 10)
        print(f"\033[1mA jogada do computador foi {computador}.\033[m")
#CALCULANDO A SOMA:
        soma = computador + player_humano
        print("Somando as jogadas...Calculando o resultado!")
        sleep(1)
        print("-" * 30)
#PRINTANDO O RESULTADO:
        if (escolha_humano == "PAR" and soma % 2 == 0) or ((escolha_humano == "IMPAR" or escolha_humano == "ÍMPAR") and (soma % 2 != 0)):
            print(f"""\033[1mA soma dos números jogados deu {soma}.
\033[1;32mParabéns, você venceu!\033[m""")
        elif (escolha_humano == "PAR" and soma % 2 != 0) or ((escolha_humano == "IMPAR" or escolha_humano == "ÍMPAR") and (soma % 2 == 0)):
            print(f"""\033[1mA soma dos números jogados deu {soma}.
\033[1;32mQue pena, você perdeu!\033[m""")
#JOGO = HUMANO VS. HUMANO
    if tipo_jogo == "2":
#JOGADA PLAYER 01:
        escolha_player1 = input("\033[1;31;46mPlayer 01, escolha entre 'PAR' ou 'ÍMPAR': \033[m").upper()
        while escolha_player1 not in "PAR ÍMPAR IMPAR":
            escolha_player1 = input("\033[1;31mPlayer 01, insira apenas PAR' ou 'ÍMPAR'.\033[m 033[1;31;46mEscolha novamente entre 'PAR' ou 'ÍMPAR': \033[m").upper()
        player01 = input("\033[1;31;46mPlayer 01, insira a sua jogada: \033[m")
        while player01.isalpha() == True: 
            player01 = input("\033[1;31mPlayer 01, insira apenas dígitos númericos entre 0 a 10. \033[m \033[1;31;46mInsira novamente a sua jogada: \033[m")
        player01 = int(player01)
#JOGADA PLAYER 02:
        player02 = input("\033[1;31;46mPlayer 02, insira a sua jogada: \033[m")
        while player02.isalpha() == True: 
            player02 = input("\033[1;31mPlayer 02, insira apenas dígitos númericos entre 0 a 10. \033[m \033[1;31;46mInsira novamente a sua jogada: \033[m")
        player02 = int(player02)
#CALCULANDO A SOMA:
        soma = player01 + player02
        print("Somando as jogadas...Calculando o resultado!")
        sleep(1)
        print("-" * 30)
#PRINTANDO O RESULTADO:
        if (escolha_player1 == "PAR" and soma % 2 == 0) or ((escolha_player1 == "IMPAR" or escolha_player1 == "ÍMPAR") and (soma % 2 != 0)):
            print(f"""\033[1mA soma dos números jogados deu {soma}.
\033[1;32mParabéns PLAYER 01, você venceu!\033[m""")
        elif (escolha_player1 == "PAR" and soma % 2 != 0) or ((escolha_player1 == "IMPAR" or escolha_player1 == "ÍMPAR") and (soma % 2 == 0)):
            print(f"""\033[1mA soma dos números jogados deu {soma}.
\033[1;32mParabéns PLAYER 02, você venceu!\033[m""")   
#PERGUNTANDO SE QUEREM JOGAR NOVAMENTE:
    print("-" * 30)
    sleep(1.5)
    condição = input("\033[1;34mJogar novamente? [S/N] \033[m").strip().upper()[0]
    while condição not in "S N":
        condição = input("\033[1;31mInserir apenas 'sim' ou 'não'. \033[1;34mJogar novamente? [S/N] \033[m").strip().upper()[0]

#FIM:
sleep(1)
print("-" * 30)
print("\033[1mFIM DO JOGO! VOLTE SEMPRE :)\033[m")       