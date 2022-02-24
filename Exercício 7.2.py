#Dados um número inteiro n > 0 e 
# uma sequência com n números inteiros maiores do que zero, determinar o máximo divisor comum entre eles.

def main():
    n = int(input("Informe o tamanho da sequência: "))
    mdc_atual = int(input("Insira o 1° valor: "))
    i = 1
    while i<n:
        num = int(input("Insira o próximo valor: "))
        mdc_atual= mdc(mdc_atual,num)
        i += 1
    print(mdc_atual)



def mdc(a,b):
    mdc = a
    while a%mdc != 0 and b%mdc != 0:
        mdc -= 1
    
    return mdc

main()
