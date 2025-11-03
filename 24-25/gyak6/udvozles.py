def udvozol(nev: str, orszagkod: str = "HU"):
    match orszagkod:
        case "HU":
            print("Szia {}". format(nev))
        case "EN":
            print("Hi {}".format(nev))
        case "FI":
            print("Moi {}".format(nev))
        case _:
            print("Országkód nem ismert!")

udvozol("Evelin", "EN")