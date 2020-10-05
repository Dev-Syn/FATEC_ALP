idade = int(input("Informe a sua idade: "))

if idade > 0:
    if idade <= 12:
        print("Classificação: Criança.")
    elif idade >= 12 and idade <=17:
        print("Classificação: Adolescente.")
    elif idade >= 18 and idade <=59:
        print("Classificação: Adulto.")
    else:
        print("Classificação: Idoso.")
else:
    print("A idade não pode ser menor que ZERO.")