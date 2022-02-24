def é_primo(num):
    i = 2
    primo = True
    while primo and i < (num) :
        if num % i == 0:
            primo = False
        i = i + 1
    return primo

def main():
    num = int(input("Digite um numero (0 para terminar): "))
    contador =0
    
    while num != 0:
        if é_primo(num):
            contador += 1
        num = int(input("Digite um numero (0 para terminar): "))

    print ("Achei ", contador," primos na sequencia")
main()

