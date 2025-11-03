import sys

n = int(input())
sportolok = {}
for line in sys.stdin:
    adat = line.split(":")
    nevek = adat[1].split(",")
    for i in range(0, len(nevek)):
        if nevek[i] in sportolok:
            sportolok[nevek[i]] += 1
        else:
            sportolok[nevek[i]] = 1

for kulcs, ertek in sorted(sportolok.items(), key=lambda rend: (-rend[1], rend[0])): # -> lambdával rendezzük
    if ertek > n:
        print("{0}: {1}".format(kulcs, ertek))