def main():
    n = int(input("Quantos múltiplos voce quer?"))
    cont = 1
    i = int(input("Qual o valor do primeiro número"))
    j = int(input("Qual o valor do segundo número"))
    num = 1
    while cont <= n:
        
        if i % num==0 and j % num ==0:
            print(num) 
            cont += 1
        num += 1   
main()
