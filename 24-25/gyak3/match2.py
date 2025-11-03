ev = int(input("Adj meg egy évszámot= "))
honap = int(input("Adj meg egy hónapot= "))

match honap:
    case 1 | 3| 5| 7| 8| 10| 12:
        nap = 31
    case 4| 6| 9| 11:
        nap = 30
    case 2:
        if (ev % 4 ==0 and ev % 100 !=0) or ev % 400 == 0:
            nap = 29
        else:
            nap = 28
    case _:
        print("Hibás adat")
        nap = 0
print("Napok száma = ", nap)