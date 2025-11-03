import sys

egyuttes = {}

for line in sys.stdin:
    adat = line.split(":")
    nevek = adat[1].strip().split(",")
    for i in range(0, len(nevek)):
        if nevek[i] in egyuttes:
            egyuttes[nevek[i]] += 1
        else:
            egyuttes[nevek[i]] = 1

for i in sorted(egyuttes):
    print("{0}: {1}".format(i, egyuttes[i]))