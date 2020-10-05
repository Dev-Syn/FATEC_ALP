qtdp = int(input("Digite a quantidade de pessoas: "))
tipo = int(input("Digite o tipo de diária: "))

tipo1 = [20,28,35,42,48,53]
tipo2 = [25,34,42,50,57,63]

if qtdp <= 6:
    if tipo == 1:
        total = qtdp * (tipo1[qtdp-1])
    elif tipo ==2:
        total =qtdp *(tipo2[qtdp-1])
    else:
        print("Utilize apenas 1 ou 2 para tipo.")
    print("Total para sua familia: R$",total)
else:
    print("Somente é permitido um quarto por funcionário. (Limite 6 pessoas por quarto)")
    