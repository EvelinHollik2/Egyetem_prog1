negativ = 0
paros = 0

try:
    while True:
        sor = input()
        szamok = sor.split()

        for i in szamok:
            szam = int(i)
            if szam < 0:
                negativ += 1
            if szam % 2 == 0:
                paros += 1

except EOFError:
    pass

print(negativ)
print(paros)