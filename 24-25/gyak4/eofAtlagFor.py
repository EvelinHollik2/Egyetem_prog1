import sys

szum = 0
db = 0

for n in sys.stdin:
    szum += int(n)
    db += 1

print("{0:.2f}".format(szum / db)) #átlag számítás