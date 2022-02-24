import re

def le_assinatura():
    '''A funcao lê os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    s_ab = []
    aux_a = 0
    aux_b = 0
    while i < 6:
        aux_a = as_a[i]
        aux_b = as_b[i]
        #print(aux_a, aux_b)
        aux = abs(aux_a - aux_b)
        s_ab.append(aux)
        i += 1
    s_ab_aux = 0
    for n in s_ab:
        s_ab_aux += n

    return (s_ab_aux / 6)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #Receber um texto, chamar as outras funções para segmenta-lo em novas listas 
    # e usar essas listas para calcular os 6 traços linguisticos
    lista_palavras = []
    lista_frases = []
    lista_sentencas = separa_sentencas(texto)
    
    for sent in lista_sentencas:  
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)

    for fr in lista_frases:
        novas_palavras = separa_palavras(fr)
        lista_palavras.extend(novas_palavras)
    
    #Calcular média de letras por palavra
    i = 0
    letras = 0

    while i < (len(lista_palavras)):

        letras += len(lista_palavras[i])
        i += 1

    wal_texto = letras / len(lista_palavras)

    # Calcular porcentagem (entre 1 e 0) de palavras únicas. Relação Type-Token
   
    ttr_texto = n_palavras_diferentes(lista_palavras) / len(lista_palavras)

    ## Calcular o total de palavras que aparecem uma única vez contra o total de palavras

    hlr_texto = n_palavras_unicas(lista_palavras) / len(lista_palavras)

    #Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças

    i = 0
    tam_sent = 0
    while i < len(lista_sentencas):
        tam_aux = lista_sentencas[i]
        tam_sent += len(tam_aux)
        i += 1

    sal_texto = tam_sent / len(lista_sentencas)

    #Complexidade de sentença é o número total de frases divido pelo número de sentenças.

    sac_texto = len(lista_frases) / len(lista_sentencas)

    #Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto 

    i = 0 
    frases_car = 0

    while i < len(lista_frases):

        tam_fr = lista_frases[i]
        frases_car += len(tam_fr)
        i += 1

    pal_texto = frases_car / len(lista_frases)

    #print(wal_texto,ttr_texto, hlr_texto, sal_texto, sac_texto , pal_texto)
    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

    

def avalia_textos(textos, ass_cp):
    #'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    #deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    ass_texto = calcula_assinatura(textos[i]) 
    grau_similaridade = compara_assinatura(ass_texto, ass_cp) 
    
    menor_grau = grau_similaridade  
    texto_infectado = i 

    while i <(len (textos)): 
        ass_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(ass_texto, ass_cp) 

        if grau_similaridade < menor_grau:  

            menor_grau = grau_similaridade  
            texto_infectado = i    

        i = i+1


    return (texto_infectado +1) #necessário adcionar 1 para ajustar a lógica do python à vida real


def main():
    #Primeiro chama a Função le_assinatura, para receber os parametros que definem o texto infectado
    ass_cp = le_assinatura()

    textos = le_textos()

    menor = avalia_textos(textos, ass_cp)

    print("O autor do texto", menor ,"está infectado com COH-PIAH")




texto1 = "Aba daba duuuuu aba daba duuu Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma."
texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres. "
texto3 = "Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens."
textos = [texto1, texto2, texto3]
ass_cp = [4.51, 0.693 , 0.55, 70.82, 1.82, 38.5]

print(avalia_textos(textos , ass_cp))


