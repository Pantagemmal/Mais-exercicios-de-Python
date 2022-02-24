

def n_harmonico(n):
    num = 1
    i = 0
    while num < n:
        i += 1/num
        num += 1

    return i

def n_harmonico2(n):
    num = n
    i = 0
    while num > 0:
        i += 1/num
        num -= 1

    return i

print(n_harmonico(10000))
print(n_harmonico2(10000))