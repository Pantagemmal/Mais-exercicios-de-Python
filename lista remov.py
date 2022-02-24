lista = [2, 2, 3,1,4,1,3,10]
def remove_repetidos(lista):
    lista.sort()
    x = "ba"
    lista1 = []
    for i in lista:
        if i != x:
            lista1.append(i)
        x = i
    return(lista1)

remove_repetidos(lista)
