def sao_multiplicaveis(m1, m2):
    'Recebe duas matrizes e devolve True ou False dependendo delas serem multiplicaveis ou não. Para uma matriz ser multiplicável o número de linhas da primeira tem que ser igual ao numero de colunas da segunda'

    lin = len(m2)
    col = len(m1[0])

    if lin != col:
        return False
    else:
        return True

m1 = [[1],[1],[1]]
m2 = [[1, 2, 3],[1,2,3]]
print(sao_multiplicaveis(m1, m2))
