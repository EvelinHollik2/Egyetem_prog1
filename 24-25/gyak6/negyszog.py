#negyszog terület számítás
def negyszog(a: int, b: int = 0) -> int:
    if b == 0:
        b = a
    return a * b

print("Négyzet területe: ", negyszog(10))
print("Téglalap területe: ", negyszog(10,12))
