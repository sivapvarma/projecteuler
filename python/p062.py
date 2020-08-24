from itertools import count
from euler import timeit


@timeit
def main():
    cubes = dict()
    found = False

    for n in map(lambda n: n**3, count()):
        k = ''.join(sorted(str(n)))
        if found:
            if len(k) > len(key):
                break
        if k not in cubes:
            cubes[k] = [n]
        else:
            cubes[k].append(n)

        if len(cubes[k]) == 5:
            key = k
            found = True

    print(min([min(c) for c in cubes.values() if len(c)==5]))

if __name__ == '__main__':
    main()
