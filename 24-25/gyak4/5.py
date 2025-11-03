o = 0
paratlan = 0
paros = 0
while True:
    n = int(input("n = "))
    o += n
    if o > 100:
        break
    if n % 2 != 0:
        paratlan = paratlan + 1
    else:
        paros = paros + 1
print("paros számok száma:", paros, "paratlan számok száma:", paratlan)