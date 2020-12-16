a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) / 2

if maiorAB > c:
    print("%d eh o maior" % maiorAB)
else:
    print("%d eh o maior" % c)
