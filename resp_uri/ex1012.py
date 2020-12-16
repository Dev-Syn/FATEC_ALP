A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

a = (A*C)/2     #área do triângulo
b = 3.14159 * (C **2)   #área de um círculo
c = (C * ( A + B)) / 2 #área de um trapézio
d = B * B   #área de um quadrado
e = A * B   #área de um retângulo

print("TRIANGULO: %.3f" % a)
print("CIRCULO: %.3f" % b)
print("TRAPEZIO: %.3f" % c)
print("QUADRADO: %.3f" % d)
print("RETANGULO: %.3f" % e)
