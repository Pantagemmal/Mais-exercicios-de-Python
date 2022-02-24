#Dados um número inteiro n, n > 0, e uma sequência com n números inteiros maiores do que zero, 
# determinar o fatorial de cada número da sequência.

def main():
    num = int(input("Qual o tamanho da sequência? "))
    k = 1
    while num >= k:
        fat1 = 1
        n = int(input("Insira o próximo valor:"))
        fatorial(n)
        print("Fatorial igual à:", fatorial(n))
        k += 1



def fatorial(n):
    i = 2
    fat1 = 1
    while i <= n:
        fat1 = fat1 * i 
        i += 1
    return fat1
main()