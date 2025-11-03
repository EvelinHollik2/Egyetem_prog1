import random

#n = int(input())
#szorzat = 1
#for i in range(n):
 #   szam =random.randint(1, 10)
 #   print(szam)
 #   szorzat = szorzat*szam

#print(szorzat)

# feladat: írjunk egy programot, amely 1 és 10 közötti számokat generál, 5-ös esetén pedig kilép. A program végén írassátok ki a lépésszámot.
lepes = 0
while True:
    szam = random.randint(1, 10)
    lepes += 1
    print(szam)
    if szam == 5:
        break

print("Lépésszám:", lepes)
