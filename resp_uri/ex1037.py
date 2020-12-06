v = float(input())

if v < 0 or v > 100:
    print("Fora de intervalo")
elif v >= 0 and v <= 25:
    print("Intervalo [0,25]")
elif v >= 25.1 and v <= 50:
    print("Intervalo (25,50]")
elif v >= 50.1 and v <= 75:
    print("Intervalo (50,75]")
elif v >= 75.1 and v <= 100:
    print("Intervalo (75,100]")
