#írjunk függgvényt, ameky megadott nyelven köszönti a felhasználót, alapértelmezetten legyen magyar, de negadott országkód esetén változtatja a nyelvet.
#amennyiben nem ismert az országkód, tudassa a felhasználóval

def koszon(nev: str, orszagkod: str = "HU"):
    match orszagkod:
        case "HU":
            print("Szia {}". format(nev))
        case "EN":
            print("Hi {}".format(nev))
        case "FR":
            print("Bonjour {}".format(nev))
        case _:
            print("Országkód nem ismert!")

koszon("Evelin")
koszon("Evelin", "EN")
koszon("Evelin", "FR")