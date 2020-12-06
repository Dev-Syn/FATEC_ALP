n1, n2, n3, n4 = input().split(" ")

ex = False
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

mp = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print("Media: %.1f" % mp)

if mp >= 7.0:
    print("Aluno aprovado.")
elif mp >= 5.0 and mp <= 6.9:
    print("Aluno em exame.")
    ex = True
else:
    print("Aluno reprovado.")

if ex == True:
    e = float(input())
    print("Nota do exame: %.1f" % e)
    m = (mp + e) / 2
    if m >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print("Media final: %.1f" % m)
else:
    exit()
