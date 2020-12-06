import math as m

n = input().split(" ")
num = [float (i) for i in n]
num.sort(reverse=True)

a = num[0]
b = num[1]
c = num[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif m.pow(a,2) == m.pow(b,2) + m.pow(c,2):
    print("TRIANGULO RETANGULO")
elif m.pow(a,2) > m.pow(b,2) + m.pow(c,2):
    print("TRIANGULO OBTUSANGULO")
elif m.pow(a,2) < m.pow(b,2) + m.pow(c,2):
    print("TRIANGULO ACUTANGULO")


if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif a == b != c or b == c != a or a == c != b:
    print("TRIANGULO ISOSCELES") 
