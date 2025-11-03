import random

paros = set()
paratlan = set()

n = int(input("n = "))
m = int(input("m = "))

while len(paros) < n:
    szam = random.randint(1,20)
    if szam % 2 == 0:
        paros.add(szam)

while len(paratlan) < m:
    szam = random.randint(1, 20)
    if szam % 2 != 0:
        paratlan.add(szam)

print(paros)
print(paratlan)

print("Unio = ", paros.union(paratlan))

