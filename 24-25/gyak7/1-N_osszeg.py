def szum(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + szum(n - 1)


def main():
    print(szum(10))


if __name__ == '__main__':
    main()
