# a halmaz típus: class set

s = set(["magyar", "angol", "német"])
ures = set() # -> üres halmaz létrehozása
s = {"magyar", "angol", "német"}

print("angol" in s) # -> az angol benne van e az s-ben?
print("japán" in s) # -> japán nincs e benne?

s.add("olasz") # -> olasz hozzáadása a listába
print(s)

s.remove("német") # -> német elem eltávolítása
print(s)


# halmaz művelete:
# s1 & s2 -> metszet
# s1 | s2 -> unió
# s1 - s2 -> különbség
# s1 ^ s2 -> szimetrikus különbség

# s1 <= s2 -> igazat ad, ha s1 részhalmaza az s2-nek
# s1 => s2 -> igazat ad, ha s2 részhalmaza az s1-nek

s2 = set()
s2.add("olasz")
s2.add("német")
print(s)
print(s2)
print(s & s2) # -> metszet
print(s | s2) # -> unió --> print(s.union(s2))
print(s - s2) # -> különbség
print(s ^ s2) # -> szimetrikus különbség

