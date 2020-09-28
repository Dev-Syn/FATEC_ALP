soma = 5 + 2

subtrai = 5 - 2

multiplica = 5 * 2

divide = 5 / 2

x,y = divmod( 5 , 2 ) #retorna dois valores (túpla) - Divisão inteira vai para a variável x, e o resto para a variável y.

w = pow( 5, 2 )

''' %i formata números para exibição no formato inteiro.
    %f formata números para exibição no formato float.
'''

print("Soma 5 e 2 = %i" % soma)

print("Subtrai 5 e 2 = %i" % subtrai)

print("Multiplica 5 e 2 = %i" % multiplica)

print("Divide 5 e 2 = %.1f" % divide)

print("Divide 5 por 2 = %i e o resto da divisão de 5 por 2 = %i" % (x,y))

print("5 elevado à 2 = %i" % w)
