while True:
    szavak = input()

    if szavak.lower() == "EXIT":
        break

    nagy = szavak.upper()

    for i in "AÁEÉIÍOÓÖŐUÚÜŰ":
        nagy = nagy.replace(i, "*")

    print(nagy)