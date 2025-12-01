import sys
from typing import NamedTuple

RollerCoaster = NamedTuple("RollerCoaster", [("name", str), ("world", str), ("height", int), ("time", int)])

def line_to_coaster(line:str) -> RollerCoaster:
    adat = line.strip().split(";")
    return RollerCoaster(adat[0], adat[1], int(adat[2]), int(adat[3]))

def coaster_to_line(coasters):
    return f"{coasters.name} ({coasters.world}): {coasters.time}"

def sort_coasters(coasters):
    return sorted(coasters, key = lambda c: (c.time, -c.height, c.name))

def main():
    coasters = []
    for line in sys.stdin:
        coasters.append(line_to_coaster(line))

    for coaster in sort_coasters(coasters):
        print(coaster_to_line(coaster))

if __name__ == "__main__":
    main()