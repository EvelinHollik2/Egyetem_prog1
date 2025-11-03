import sys


def fact(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fact1(n: int) -> int:
    return 1 if n == 1 else n * fact(n - 1)


def read() -> None:
    while True:
        try:
            n = int(input("n = "))
            print(fact(n))
        except EOFError:
            break


def read1() -> None:
    for line in sys.stdin:
        n = int(line)
        print(fact(n))


def read2() -> None:
    n = int(input())
    for i in range(n):
        num = int(input())
        if num < 0 or num > 50:
            break
        print(fact(num))


def main():
    print(fact(5))
    print(fact1(5))
    read()
    read1()
    read2()


if __name__ == '__main__':
    main()
