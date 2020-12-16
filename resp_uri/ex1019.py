n = int(input())

conth = 0
contm = 0
conts = 0

if n >= 3600:
    while n >= 3600:
        n -= 3600
        conth += 1
if n >= 60:
    while n >= 60:
        n -= 60
        contm += 1
if n > 0 :
    while n != 0:
        n -= 1
        conts += 1
print("%d:%d:%d" % (conth, contm, conts))
