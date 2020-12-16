n = float(input())

#Contador Notas.
cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0

#Contador Moedas.
m1 = 0
m50 = 0
m25 = 0
m10 = 0
m05 = 0
m01 = 0

#Separando as notas
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

#Separando as moedas
while n >= 1:
    n -= 1
    m1 += 1
while n >=0.50:
    n -= 0.50
    m50 += 1
while n >= 0.25:
    n -= 0.25
    m25 +=1
while n >= 0.10:
    n -= 0.10
    m10 += 1
while n >= 0.05:
    n -= 0.05
    m05 += 1
while n >= 0.01:
    n -= 0.01
    m01 += 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cont100)
print("%d nota(s) de R$ 50.00" % cont50)
print("%d nota(s) de R$ 20.00" % cont20)
print("%d nota(s) de R$ 10.00" % cont10)
print("%d nota(s) de R$ 5.00" % cont5)
print("%d nota(s) de R$ 2.00" % cont2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % m1)
print("%d moeda(s) de R$ 0.50" % m50)
print("%d moeda(s) de R$ 0.25" % m25)
print("%d moeda(s) de R$ 0.10" % m10)
print("%d moeda(s) de R$ 0.05" % m05)
print("%d moeda(s) de R$ 0.01" % m01)
