pont = int(input("Adjon meg egy ponszamot "))

match pont:
    case 1:
        print("Elégtelen")
    case 2:
        print("Elégséges")
    case 3:
        print("Közepes")
    case 4:
        print("Jó")
    case 5:
        print("Kitünő")
    case _:
        print("Hibás adat")
