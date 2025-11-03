#Relatív prímek
#Írjon programot, amely a standard bemenetről két pozitív egész számot olvas be, majd eldönti, hogy relatív prímek-e vagy sem!
#A bemenet specifikációja
#A bemenet két darab pozitív egész számot tartalmaz, melyek egy darab szóközzel vannak elválasztva.
#A kimenet specifikációja
#A programnak egy sort kell a standard kimenetre írnia, amely az „IGEN” vagy a „NEM” sztringet tartalmazza annak megfelelően, hogy a két beolvasott szám relatív prím-e vagy sem.

import math

a, b = map(int, input().split())
if math.gcd(a, b) == 1:
    print("IGEN")
else:
    print("NEM")


#a, b = map(int, input().split())

#while b != 0:
#    a, b = b, a % b
#if a == 1:
#    print("IGEN")
#else:
#    print("NEM")
