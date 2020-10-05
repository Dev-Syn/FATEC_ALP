ladoA = int(input("Digite o comprimento: "))
ladoB = int(input("Digite o comprimento: "))
ladoC = int(input("Digite o comprimento: "))

if ladoA == ladoB and ladoA == ladoC :
    print("Triângulo equilátero.")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("Triângulo isóceles.")
else:
    print("Triângulo escaleno.")
    