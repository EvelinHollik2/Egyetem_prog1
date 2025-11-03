n = int(input())
db = 0

for _ in range(n):
    szam = int(input())
    if szam > 0 and szam % 2 == 0:
        db += 1

print(db)
