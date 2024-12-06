import sys

if __name__ == "__main__":
    left = []
    right = []

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            a, b = line.split()
            left.append(int(a))
            right.append(int(b))
    
    left.sort()
    right.sort()
    diffs = [abs(a - b) for a, b in zip(left, right)]
    print(sum(diffs))