import sys
from collections import Counter

if __name__ == "__main__":
    left = []
    right = []

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            a, b = line.split()
            left.append(int(a))
            right.append(int(b))

    right = Counter(right)
    scores = [a * right[a] for a in left]
    print(sum(scores))