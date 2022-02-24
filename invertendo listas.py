def inversão():
    lista = []
    x = 1
    while x != 0:
        x = int(input("insira o próximo número da lista: "))
        if x!= 0:
            lista.append(x)
    cont = -1
    for i in lista:
        print(lista[cont])
        cont -= 1
        

inversão()