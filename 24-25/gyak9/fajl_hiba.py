try:
    with open("ki3.txt", encoding="utf-8") as file:
        for line in file:
            print(line.strip("\n"))
except FileNotFoundError:
    print("Nem létezik a fájl")