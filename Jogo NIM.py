def usuario_escolhe_jogada(n,m):
    p = int(input("Quantas peças você vai tirar?"))
    if p > m or p < 0:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)
    else:
        return p

def computador_escolhe_jogada(n,m):

    return n

    


def partida(n,m):
    p = 0
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    if m > n or n <= 0 or m <= 0: 
        print("O valor inserido não é válido")
    if n // m + 1 == 0:
        print("O computador terá pena de sua alma. Você começa!")
        while n >= m:
            usuario_escolhe_jogada()
    else:
        print("Computador começa!")
        while n > 0:
            computador_escolhe_jogada()
            n = n - p
            
            usuario_escolhe_jogada()
            n = n - p
            print("\nVocê tirou", p, "peças.")
            print("Agora restam", n,"peças no tabuleiro.")
            if n == 0 and torneio == False:
                print("Parabéns! Você perdeu!")

def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    par = int(input("1 - para jogar uma partida isolada  2 - para jogar um campeonato:"))
    torneio = 0
    contador = 0
    n= 0 
    m= 0
    if par == 1:
        torneio == False
        print("Você escolheu jogar uma partida!")
    if par == 2:
        torneio == True
        contador = 1
        print("Voce escolheu um campeonato!")
    else:
        print("comando inválido")
    while par == 2 :
        print("**** Rodada", contador, "****")
        partida(n,m)

inicio()