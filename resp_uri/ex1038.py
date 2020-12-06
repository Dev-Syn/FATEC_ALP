c,q = input().split(" ")

c = int(c)
q = int(q)

if c == 1:
    t = 4.00
elif c == 2:
    t = 4.50
elif c == 3:
    t = 5.00
elif c == 4:
    t = 2.00
elif c == 5:
    t = 1.50
print("Total: R$ %.2f" %(t*q))
