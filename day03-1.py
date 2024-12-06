import sys
import re

if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        pairs = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", f.read())
        print(sum(int(a) * int(b) for a, b in pairs))