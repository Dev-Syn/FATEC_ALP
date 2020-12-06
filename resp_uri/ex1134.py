a = 0
g = 0
d = 0
c = 0
while c != 4:
    c = int(input())

    if c == 1:
        a += 1
    elif c == 2:
        g += 1
    elif c == 3:
        d += 1

print("MUITO OBRIGADO")
print("Alcool: %d" % a)
print("Gasolina: %d" % g)
print("Diesel: %d" % d)
