a, b = input().split(" ")

a = int(a)
b = int(b)

if a > b :
    ma = a
    me = b
else:
    ma = b
    me = a
t = ma / me

if ma % me == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
