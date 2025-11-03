n = int(input("n = "))
oszto = 1

for i in range(1,n):
    if n % i == 0:
        oszto = i

if oszto == 1:
    print("a szam primszam")
else:
    print("a szám legnagyobb valódi osztója: ", oszto)