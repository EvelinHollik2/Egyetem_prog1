import sys

gyerekek = {}
for line in sys.stdin:
    adat = line.split(":")
    nevek = adat[1].strip().split(",")
    for i in range(len(nevek)):
        if nevek[i] in gyerekek:
            gyerekek[nevek[i]] += 1
        else:
            gyerekek[nevek[i]] = 1
for kulcs, ertek in sorted(gyerekek.items()):
    print(ertek)
