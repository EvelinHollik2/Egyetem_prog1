while True:
    n = int(input())
    if n == 0:
        break
    if n > 10:
        osszeg = 0

        for jegy in str(abs(n)):
            osszeg += int(jegy)

    dupla = osszeg * 2
    print(dupla)