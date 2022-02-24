#Escreva um programa que recebe como entradas (utilize a função input) 
# dois números inteiros correspondentes à largura e à altura de um retângulo

def inicio():
    i = int(input("Insira a largura: "))
    j = int(input("Insira a altura: "))
    k = 0
    cont = 0
    while k < j:
        cont = 0
        while cont < i:
            print("#", end='' )
            cont += 1
        print("")
        k += 1

inicio()