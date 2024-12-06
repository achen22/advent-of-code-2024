import sys

if __name__ == "__main__":
    total = 0
    grid = []

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            grid.append(line.rstrip())

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "A":
                sides = (
                    grid[i-1][j-1], grid[i+1][j+1],
                    grid[i+1][j-1], grid[i-1][j+1]
                )
                if all(c in "MS" for c in sides):
                    if sides[0] != sides[1] and sides[2] != sides[3]:
                        total += 1

    print(total)