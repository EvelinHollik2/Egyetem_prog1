bevasarlolista = {
    "alma" : 1,
    "korte" : 2,
    "barack" : 5
}

print(bevasarlolista)
bevasarlolista["meggy"] = 3
print(bevasarlolista)
print("Almából", bevasarlolista["alma"], "db kell")

bevasarlolista = {}
bevasarlolista["alma"] = 1
bevasarlolista["korte"] = 2
bevasarlolista["barack"] = 3
print(bevasarlolista)

print("alma" in bevasarlolista)
bevasarlolista["szilva"] = 7
print(bevasarlolista)

try:
    print(bevasarlolista["papaja"])
except KeyError as e:
    print("Nincs benne a szotarban")

# kulcsokon át literálás
for kulcs in bevasarlolista:
    ertek = bevasarlolista[kulcs]
    print(kulcs, ertek)

# értékeken át literálás
for ertek in bevasarlolista.values():
    print(ertek)

# kulcsokon és értékeken át literálás
for kulcs, ertek in bevasarlolista.items():
    print(f"{kulcs}: {ertek}")

# értékek összeadása (hány db termék szerepel a bevásárlólistán)
print("összeg = ", sum(bevasarlolista.values()))