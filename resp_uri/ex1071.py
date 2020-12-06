x = int(input())
y = int(input())

impar = 0

if x > y:
    ma = x
    me = y
else:
    ma = y
    me = x

me += 1

while me < ma:
    if me % 2 != 0:
        impar += me
    me += 1
print(impar)
