import sys
import re

def subtotal(s: str):
    pairs = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", s)
    return sum(int(a) * int(b) for a, b in pairs)

if __name__ == "__main__":
    total = 0

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        line = re.split(r"(do(?:n't)?\(\))", f.read())
        do = True
        for s in line:
            if s == "do()":
                do = True
            elif s == "don't()":
                do = False
            elif do:
                total += subtotal(s)
        print(total)