import math as m

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

d = (b**2) - (4 * a * c)

if d < 0 or a==0:
    print("Impossivel calcular")
else:
    rd = m.sqrt(d)
    x1 = (-b + rd ) / (2 * a)
    x2 = (-b - rd ) / (2 * a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
