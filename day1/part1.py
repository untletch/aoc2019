def fuel(mass):
    return int(mass / 3) - 2


assert fuel(1969) == 654
assert fuel(100756) == 33583


def sol():
    with open('inp.txt') as f:
        ans = [fuel(int(line.strip())) for line in f]
    return sum(ans)


print(sol())
