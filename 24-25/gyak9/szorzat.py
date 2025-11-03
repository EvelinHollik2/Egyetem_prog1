import sys

argc = len(sys.argv)

print("a parancssori argumentumok száma: ", argc)

p = 1
for i in range(1, argc):
    p = p * int(sys.argv[i])
print("Szorzat: ", p)