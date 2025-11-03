import sys

argc = len(sys.argv)
print("a parancssori argumentumok száma: ", argc)

print("fájl helye: ", sys.argv[0])

print("átadott paraméterek:")
for i in range(1, argc):
    print(sys.argv[i])