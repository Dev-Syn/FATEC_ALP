a=int(input("Digite o valora para A "))
b=int(input("Digite o valora para B "))
c=int(input("Digite o valora para C "))

delta = (b ** 2) - 4 * a * c

if delta <  0:
    print("Não existem raízes reais")
else:
    if delta == 0:
        print("As raízes são iguais")
    else:
        x1 =  (-b  + (delta) ** 0.5 ) / (2 * a)
        x2 =  (-b  - (delta) ** 0.5 ) / (2 * a)
        print("\nExistem duas raízes diferentes reais\n")
        print("x1 = %.1f" % x1)
        print("x2 = %.1f" % x2)
