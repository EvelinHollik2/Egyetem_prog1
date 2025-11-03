n=int(input())
tantargyak ={}

for i in range(n):
    adat=input().split(":")
    tantargyak[adat[0]] = adat[1]

for kulcs, ertek in sorted(tantargyak.items()):
    print(ertek)