import random

n = int(input("n = "))
p = 1

for i in range(n):
    x = random.randint(1, 10)
    p *= x
    print("\nSzorzat", p)