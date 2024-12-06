import sys
import re

xmas = re.compile("XMAS")

if __name__ == "__main__":
    total = 0
    grid = []

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            grid.append(line.rstrip())

    # horizontal
    for row in grid:
        total += len(xmas.findall(row))
        total += len(xmas.findall(row[::-1]))
    
    # vertical
    for i in range(len(grid[0])):
        col = "".join(row[i] for row in grid)
        total += len(xmas.findall(col))
        total += len(xmas.findall(col[::-1]))
    
    # diagonals
    lines: dict[str, list[str]] = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            k = i + j
            if k not in lines:
                lines[k] = [grid[i][j]]
            else:
                lines[k].append(grid[i][j])
    for line in lines.values():
        if len(line) < 4:
            continue
        line = "".join(line)
        total += len(xmas.findall(line))
        total += len(xmas.findall(line[::-1]))
    
    lines.clear()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            k = i - j
            if k not in lines:
                lines[k] = [grid[i][j]]
            else:
                lines[k].append(grid[i][j])
    for line in lines.values():
        if len(line) < 4:
            continue
        line = "".join(line)
        total += len(xmas.findall(line))
        total += len(xmas.findall(line[::-1]))

    print(total)