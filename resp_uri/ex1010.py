peca1 = input().split(" ")
peca2 = input().split(" ")

peca1 = [float(i) for i in peca1]
peca2 = [float(i) for i in peca2]

total = (peca1[1] * peca1 [2] + peca2[1] * peca2[2])
print("VALOR A PAGAR: R$ %.2f" % total)
