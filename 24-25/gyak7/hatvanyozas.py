def power(x: int, n: int) -> int:
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)


def power2(x: int, n: int) -> int:
    return x if n == 1 else x * power(x, n - 1)


def power3(x: int, n: int) -> int:
    p = 1
    for i in range(n):
        p = p * x
    return p


def main():
    x = int(input("x = "))
    n = int(input("n = "))
    print(power(x, n))


if __name__ == '__main__':
    main()
