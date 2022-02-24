#Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos, 
# indicando também a mutiplicidade de cada fator.

10 % 2 

def main():
    n = int(input("Digite um numero (>1): "))
    mult = 0
    fator = 2
    while n != 1:
        mult = 0
        while n % fator == 0:
            n = n/fator
            mult += 1
        if mult >= 1:    
            print("fator ",fator, "multiplicidade", mult)
        fator += 1

main()

