n = int(input("n= "))
szamlalo = 0

while n != 0:
    szamlalo += 1
    n = n // 10
print("Számjegyek száma: ", szamlalo)