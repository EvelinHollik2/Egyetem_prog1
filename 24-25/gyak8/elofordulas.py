elofordulas = {}

szo = input()
while szo != "":
    if szo in elofordulas:
        elofordulas[szo] += 1
    else:
        elofordulas[szo] = 1
    szo = input()

for szo, db in elofordulas.items():
    print(f"{szo}: {db}")