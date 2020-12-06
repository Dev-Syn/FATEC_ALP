cont = 0
pos = 0

while cont <= 5:
    num = float(input())
    if num > 0:
        pos += 1
    cont += 1
print("%d valores positivos" % pos)
