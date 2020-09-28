n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))

if n1 > 0 and n2 > 0 :
  if n1 > n2 :
    res = n1 - n2
  else :
    res = n2 - n1
else :
  if n1 > n2 :
    res = - n2 - n1
  else :
    res = - n1 - n2
print("Resultado: ", res)