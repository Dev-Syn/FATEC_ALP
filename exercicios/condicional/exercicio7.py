n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
n4 = float(input("Digite um número: "))

if n1 == n2 and n2 == n3 and n3 == n4 :
    print("Todos os números são: %.2f" %(n1))
elif n1 == n2 :
    print("Existem números repetidos. %.2f e %.2f" %(n1, n2))
elif n1 == n3:
    print("Existem números repetidos. %.2f e %.2f" %(n1, n3))
elif n1 == n4:
    print("Existem números repetidos. %.2f e %.2f" %(n1, n4))
elif n2 == n3:
    print("Existem números repetidos. %.2f e %.2f" %(n2, n3))
elif n2 == n4:
    print("Existem números repetidos. %.2f e %.2f" %(n2, n4))
elif n3 == n4:
    print("Existem números repetidos. %.2f e %.2f" %(n3, n4))
else:
    print("Não existe números repetidos.")


'''
entrada = input("Digite 4 digitos na mesma linha usando espaço ")

x = entrada.split(" ") #Serve pra quebrar um argumento em vetores.
a = x[0]
b = x[1]
c = x[2]
d = x[3]

if a == b or  a == c  or a == d  or b == c or b == d  or c == d:
    print('Há números repetidos.')
else:
    print("Não há números repetidos")
'''