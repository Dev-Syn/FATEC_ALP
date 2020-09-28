dias  = int(input())
ano = 0
meses = 0
qdias = 0


while dias != 0 :
    if dias >= 365 :
        ano += 1
        dias -= 365
    elif dias >= 30 :
        meses += 1
        dias -= 30
    elif dias <= 29 :
        qdias += + 1
        dias -=1

print("%i ano (s)\n%i mes (ses)\n%i dia (s)" % (ano, meses, qdias))
