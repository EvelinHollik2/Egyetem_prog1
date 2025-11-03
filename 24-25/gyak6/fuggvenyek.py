def table7() -> None: #->None: Nincs visszatérési értéke
    n = 1
    while n < 11:
        print(n * 7, end = " ")
        n += 1

table7()

def tabla(alap : int) -> None:
    n = 1
    while n < 11:
        print(n * alap, end=' ')
        n += 1

print('\n')
tabla(5)

def szorzotabla(alap:int, kezdet:int, veg:int) -> None:
    print("A(z) {}-as szorzótábla részlete".format(alap))
    n = kezdet
    while n <= veg:
        print("{0} x {1} = {2}".format(n, alap, n*alap))
        n += 1

print("\n")
szorzotabla(2, 5, 15)
szorzotabla(4, 1, 3)