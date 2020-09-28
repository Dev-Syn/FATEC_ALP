n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 == n2 :
    print("Os números são iguais")
else:
    if n1 > n2 :
        print("O maior é %.2f e o menor é %.2f" % (n1, n2))
    else:
        print("O maior é %.2f e o menor é %.2f" % (n2, n1))