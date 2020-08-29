def fuel(mass):
    return int(mass / 3) - 2


def add_fuel(mass):
    s = fuel(mass)
    if s < 9:
        return s
    return s + add_fuel(s)


assert add_fuel(14) == 2
assert add_fuel(1969) == 966


def sol():
    with open('inp.txt') as f:
        ans = [add_fuel(int(line.strip())) for line in f]
    return sum(ans)


print(sol())
