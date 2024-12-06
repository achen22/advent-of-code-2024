import sys
from itertools import pairwise

def is_safe(levels: list[int]):
    diffs = [b - a for a, b in pairwise(levels)]
    return all(n >= -3 and n <= -1 for n in diffs) or all(n >= 1 and n <= 3 for n in diffs)

if __name__ == "__main__":
    total = 0

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            levels = [int(n) for n in line.split()]
            if is_safe(levels):
                total += 1
                #print(line[:-1], ": Safe")
            else:
                safe = False
                for i in range(len(levels)):
                    if is_safe(levels[:i] + levels[i + 1:]):
                        safe = True
                        #print(" ".join(str(n) for n in levels[:i] + levels[i + 1:]), ": Safe")
                        break
                total += safe
                #if not safe:
                #    print(line[:-1], ": Unsafe")
        print(total)
