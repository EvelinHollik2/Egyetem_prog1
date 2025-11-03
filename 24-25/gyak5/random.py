import random

szamol = 0
while True:
    n = random.randint(1, 10)
    if n == 5:
        break
    print(n, end=' ')
    szamol += 1

print("{} lépés után állt le!".format(szamol))