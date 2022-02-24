def maximo(x,y,z):
    if x >= y:
        if x >= z:
            return x
        if x < z:
            return z
    else:
        if y >= z:
            return y
        else:
            return z

print(maximo(31,-1,10))