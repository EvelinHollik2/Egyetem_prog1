sor = input()
s = sor.split(" ")
a = int(s[0])
b = int(s[1])

while a % b != 0:
    r = a % b
    a = b
    b = r

print(b)

if b == 1:
    print("IGEN")
else:
    print("NEM")