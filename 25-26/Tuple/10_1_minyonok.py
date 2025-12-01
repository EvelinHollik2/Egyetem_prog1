import sys
from typing import NamedTuple

Minion = NamedTuple("Minion", [
    ("name", str),
    ("hunger", int),
    ("motivation", int),
    ("size", int)
])
def line_to_minions(line:str) -> Minion:
    adat = line.strip().split(";")
    name = adat[0]
    hunger = int(adat[1])
    motivation = int(adat[2])
    size = adat[3]
    return Minion(name, hunger, motivation, size)

    #adat=line.strip().split(";")
    # return Minion(adat[0], int(adat[1]), int(adat[2]), adat[3])

def minions_to_line(minion: Minion) -> str:
    return f"{minion.name} {minion.hunger} ({minion.size})"

def sort_minions(minions):
    return sorted(minions, key = lambda m: (-m.motivation, m.name))

def main():
    minions = []
    for line in sys.stdin:
        minions.append(line_to_minions(line))
    for minion in sort_minions(minions):
        print(minions_to_line(minion))


if __name__ == "__main__":
    main()