import sys

majmok = {}
for line in sys.stdin:
    adat = line.split(";")
    if adat[0] in majmok:
        majmok[adat[0]] += int(adat[1])
    else:
        majmok[adat[0]] = int(adat[1])

for i in sorted(majmok): # -> sorted: rendezett sorrend
    print ("{0}: {1}".format(i, majmok[i]))