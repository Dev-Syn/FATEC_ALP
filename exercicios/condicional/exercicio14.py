n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

mediaf = (2 * n1 + 2 * n2 + 3 * n3 + 3 * n4) / 10

situacao = ""

if mediaf >= 7:
    situacao= "Aprovado"
elif mediaf < 7 and mediaf >=5:
    situacao = "Recuperação\n"
    e = float(input("Digite a nota do exame: "))
    mediae = (mediaf + e ) / 2
    if mediae >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
else:
    situacao = "Reprovado"

print("O aluno foi" , situacao)

