def cria_matriz(num_lin, num_col, valor):
    matriz = []  #lista vazia
    for i in range(num_lin):
        linha = []
        for j in range(num_col):
            
            linha.append(valor)
        matriz.append(linha)
    return matriz

