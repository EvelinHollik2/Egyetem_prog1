import sys

utcak = {}

with open(sys.argv[1]) as file:
    for line in file:
        adat = line.strip("\n").split(";")
        print(adat)
        if adat[0] in utcak:
            utcak[adat[0]] += float(adat[2])
        else:
            utcak[adat[0]] = float(adat[2])

for kulcs, ertek in sorted(utcak.items(), key=lambda rend: (-rend[1], rend[0])):
    print(kulcs)
    #print("{}: {}".format(kulcs, ertek))