import random

n = int(input())
szamok = []

for i in range(n):
    szam = random.randint(2, 21)
    szamok.append(szam)
    print(szam)

if szam % 2 == 0:
    atlag = sum(szamok) / n
    print(szamok)
else:
    print(0.00)
