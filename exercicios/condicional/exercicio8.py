n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2 or n1 > n3:
    maior = n1
elif n1 > n2 and n1 < n3:
    maior = n3
    medio = n1
    menor = n2
elif n1 < n2 and n1 < n3:
    menor = n1
