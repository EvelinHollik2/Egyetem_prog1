import math

gyumolcs = "Alma"
ar = 2000

print(gyumolcs + "ára: " + str(ar) + " Ft.")
print("{} ára: {} Ft." .format(gyumolcs, ar))
print("{1} ára: {0} Ft." .format(ar, gyumolcs))
print("{gyum} ára: {a} Ft." .format(gyum=gyumolcs, a=ar))

print("Pi értéke: " + str(math.pi))
print("Pi értéke: {:.2f}" .format(math.pi))
print('{0:0d}={0:0b}={0:0o}={0:0X}'.format(15))

#szám beolvasás és elkell döntettni hogy páros e
#szam = int(input("Szám="))
#if szam % 2 == 0:
#    print("A szám páros")
#else:
#    print("A szám páratlan")

#szám beolvasás és eldöntés hogy 4-re végződik e
szam = int(input("Szám="))
if szam % 10 == 4:
    print("4-re végzódik")
else:
    print("Nem 4-re végződik")

#másik megoldás --> string-ként kezeli a számot
n = input("n = ")
if n[-1] == '4':
    print("igen")
else:
    print("nem")