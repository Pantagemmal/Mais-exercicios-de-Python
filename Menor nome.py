# Deve receber uma lista de strings e devolver o menor nome/string da lista
#a função deve ignorar espaços e o retorno deve ser capitalizado
#caso dê empate deve retornar o primeiro na lista

listanomes = ['maria', 'josé', 'PAULO', 'Catarina']

def arrumar(nomes):
    

    return novos_nomes


def menor_nome(nomes):
    
    novos_nomes = []
    for i in nomes:
        palavra = ""
        palavra += i
        palavra = palavra.capitalize()
        palavra = palavra.strip()
        novos_nomes.append(palavra)
    x = 0
    
    menor_palavra = ""

    for i in novos_nomes:
        palavra =""
        palavra += i
        letras = len(palavra)

        if x == 0:
            x = letras
            menor_palavra = palavra
        elif letras < x:
            x = letras
            menor_palavra = palavra

    return menor_palavra
