##írjatok rekurzív hatvány függvényt, amely meghatározza X^n-t.

#def hatv(x: int, n: int) -> int:
#    if n == 0:
#        return 1
#    else:
#        return x * hatv(x, n - 1)


#def main():
#    x = int(input("x = "))
#    n = int(input("n = "))
#    print(hatv(x, n))


#if __name__ == "__main__":
#    main()

##írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok összegét
#def ossz(n: int) -> int:
#    if n == 1:
#        return 1
#    else:
#        return n + ossz(n - 1)

#def main():
#    n = int(input("n = "))
#    print(ossz(n))


#if __name__ == "__main__":
#    main()


##írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok négyzet összegét
#def negyzetossz(n: int) -> int:
#    if n == 1:
#        return 1
#    else:
#        return n * n + negyzetossz(n - 1)
#        #return n**2 + negyzetossz(n-1)


#def main():
#    n = int(input("n = "))
#    print(negyzetossz(n))


#if __name__ == "__main__":
#    main()

#írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok összegét (i^2-2 (i=1))
#def vlm(n: int) -> int:
#    if n == 1:
#        return 1**2 - 2
#        #return -1
#    else:
#        return (n ** 2 - 2) + vlm(n - 1)
#        #return n * n -2 + vlm(n-1)

#def main():
#    n = int(input("n = "))
#    print(vlm(n))


#if __name__ == "__main__":
#    main()


#írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok összegét (i^2-2 (i=3))
#def vlm(n: int) -> int:
#    if n == 3:
#        return 7
#    else:
#        return n * n -2 + vlm(n-1)
#
#def main():
#    n = int(input("n = "))
#    print(vlm(n))
#
##return 7 if n == 3 else n * n - 2 + vlm(n-1)
#
#if __name__ == "__main__":
#    main()

# írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok összegét (i(i^2-1) (i=4))
#def vlm(n: int) -> int:
#    if n < 4:
#        return 0
#    else:
#        return n * (n * n - 1) + vlm(n - 1)
#
#
#def main():
#    n = int(input("n = "))
#    print(vlm(n))
#
#
#if __name__ == "__main__":
#    main()

# írjatok rekurzív függvényt, mely meghatározza 1-től N-ig a számok összegét ((i^3-5) (i=2))
#def vlm(n: int) -> int:
#    if n < 2:
#        return 0
#    else:
#        return (n * n * n - 5) + vlm(n - 1)


#def main():
#    n = int(input("n = "))
#    print(vlm(n))


#if __name__ == "__main__":
#    main()

#írjatok rekurzív függvényt az n-ik Fibbonacci szám meghatározására
#def fibbonacci(n: int) -> int:
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibbonacci(n - 1) + fibbonacci(n - 2)
#    #return 0 if n == 0 elif 1 if n == 1 else fibbonacci(n-1) + fibbonacci(n-2)

#def main():
#    n = int(input("n = "))
#    print(fibbonacci(n))

#if __name__ == "__main__":
#    main()

#írjatok iteratív függvényt az n-ik Fibbonacci szám meghatározására
import time
def fibonacci_ite(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#írjunk még egy for ciklust, hogy mennyire gyorsan írja így ki az eredményt

#for n in range(1, 1000):
#        start_time = time.time()
#        result = fibonacci_ite(n)
#        end_time = time.time()
#        print(f"F({n}) = {result}, számítás ideje: {end_time - start_time:.6f} másodperc")

def main():
    n = int(input("n = "))
    print(fibonacci_ite(n))


if __name__ == "__main__":
    main()
