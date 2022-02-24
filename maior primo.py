def é_primo(x):
    i = 2
    resto = True
    while resto and i < (x-1) :
        if x % i == 0:
            resto = False
        i = i + 1
    return resto

def maior_primo(x):
    if x <= 2:
        print("insira um número maior que 2!")
    else:
        while x > 1 and é_primo(x) == False:
            x = x - 1
        return x
            


