a , b , c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

if(a + b > c and b + c  > a and a + c > b ):
    p = a + b + c
    print("Perimetro = %.1f" % p)
else:
    a = ((a +b) / 2) * c
    print("Area = %.1f" % a)
