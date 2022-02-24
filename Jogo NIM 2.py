def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato ")
    par= int(input("Qual será sua escolha?"))
    contador = 0
    
    if par == 1:
        print("Você escolheu jogar uma partida!")
        partida()
        print("Fim do jogo! O computador ganhou!")

    elif par == 2:
        contador = 1
        print("Voce escolheu um campeonato!")
    else:

        print("**** comando inválido! ***")
        print("")
        inicio()
    while contador > 0 and contador < 4 :

        print("**** Rodada", contador, "****")
        partida()
        print("Fim do jogo! O computador ganhou!")
        contador = contador + 1

        if contador == 4:
            print("")
            print("**** Final do campeonato! ****")
            print("")
            print("Placar: Você 0 X 3 Computador")

def partida():
    print("")
    n = int(input("Quantas peças?"))
    print("")
    m = int(input("Limite de peças por jogada?"))
    is_computer_turn = True

    if n % (m+1) == 0: 
        is_computer_turn = False
        print("Você começa!")
    else:
        is_computer_turn = True
        print("Computador começa!")

    

    if n < m or n < 0 or m <=0:
        print("*** comando inválido ***") 
        partida()
    
    while n > 0:

        if is_computer_turn == True:
            p = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou", p ,"peças")
        
        else:
            p = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou", p ,"peças")
            
        
        n = n - p
        print("Agora restam", n ,"peças no tabuleiro.")

def usuario_escolhe_jogada(n,m):

    p = 0
    while p == 0:
        p = int(input("Quantas peças você quer retirar?"))
        if p > m or p <= 0 or p > n:
            p = 0

    return p

def computador_escolhe_jogada(n,m):
    if n <= m:
        return n

    else:
        p = n % (m+1)

        if p > 0:
            return p
        return m


inicio()