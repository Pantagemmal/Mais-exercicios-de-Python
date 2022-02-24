
def inicio():
    i = int(input("Insira a largura: "))
    j = int(input("Insira a altura: "))
    k = 0
    linha_vazia = "#" + (" " * (i-2)) + "#" 
    linha_cheia = "#" * i 

    while k < j:
        if k == 0 or k == j-1:
            print(linha_cheia)
        else:
            print(linha_vazia)
        k += 1


inicio()