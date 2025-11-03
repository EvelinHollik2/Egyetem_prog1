import math
import random

#feltöltünk egy listát 10 darab random számmal 1-100-ig
def feltolt(lista:list) -> None:
    for i in range(10):
        lista.append(random.randint(1, 100))

#kiirajtuk a listából a legkisebb számot
def legkisebb(lista:list) -> int:
    min = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

#kiirajtuk a listából a legnagyobb számot
def legnagyobb_index(lista:list)->int:
    maxi = 0
    for i in range(len(lista)):
        if lista[i] > lista[maxi]:
            maxi = 1
    return maxi

#kiirajtuk a listából a páros elemek számát
def paros_elem(lista:list)->int:
    db = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            db += 1
    return db

#megnézzük hogy prím e
def prim_e(szam: int) -> bool:
    if szam == 0 or szam == 1:
        return False
    o = 2
    while o <= math.sqrt(szam):
        if szam % o == 0:
            return False
        o += 1
    return True

#prím számok elemeinek száma
def primek_szama(lista:list) -> int:
    prim_db = 0
    for i in range(len(lista)):
        if prim_e(lista[i]):
            prim_db += 1
    return prim_db

#függvény ellenőrzés
def main():
    lista=[]
    feltolt(lista)
    print(lista)
    print("Legkisebb = ", legkisebb(lista))
    print("Legnagyobb indexe = ", legnagyobb_index(lista))
    print("Párosok száma = ", paros_elem(lista))
    print("Primek száma = ", primek_szama(lista))

if __name__ == '__main__':
    main()