def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas"))
    col = int(input("Digite o número de colunas"))
    print(cria_matriz(lin, col))

a = [[1, 2, 3], [4, 5, 6]]

print(len(a))