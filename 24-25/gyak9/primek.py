import math
import sys


def is_prime(n : int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def count_of_primes() -> int:
    count = 0
    for number in sys.argv[1:]:
        if is_prime(int(number)):
            count += 1
    return count


def main():
    print(count_of_primes())


if __name__ == '__main__':
    main()