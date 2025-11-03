neg = 0
poz = 0
while True:
    n = int(input("n = "))
    if n == 0:
        break
    if n < 0:
        neg = neg + 1
        continue
    if n > 0:
        poz = poz + 1
        continue

print("Pozitív számok száma: ", poz)
print("Negatív számok száma: ", neg)