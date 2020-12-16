n = int(input())

cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

print(n)
while n >= 100:
    n -= 100
    cont100 += 1
while n >= 50:
    n -= 50
    cont50 += 1
while n >= 20:
    n -= 20
    cont20 +=1
while n >= 10:
    n -= 10
    cont10 += 1
while n >= 5:
    n -= 5
    cont5 += 1
while n >= 2:
    n -= 2
    cont2 += 1
while n >= 1:
    n -= 1
    cont1 += 1

print("%d nota(s) de R$ 100,00" % cont100)
print("%d nota(s) de R$ 50,00" % cont50)
print("%d nota(s) de R$ 20,00" % cont20)
print("%d nota(s) de R$ 10,00" % cont10)
print("%d nota(s) de R$ 5,00" % cont5)
print("%d nota(s) de R$ 2,00" % cont2)
print("%d nota(s) de R$ 1,00" % cont1)
