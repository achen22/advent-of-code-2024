import sys
from itertools import pairwise

if __name__ == "__main__":
    safe = 0

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            levels = [int(n) for n in line.split()]
            diffs = [b - a for a, b in pairwise(levels)]
            if all(n >= -3 and n <= -1 for n in diffs) or all(n >= 1 and n <= 3 for n in diffs):
                safe += 1
            #    print(line[:-1], ": Safe")
            #else:
            #    print(line[:-1], ": Unsafe")
        print(safe)
