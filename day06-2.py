import sys

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
turn: dict[tuple[int, int], tuple[int, int]] = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}

def path_loops(obstructions, width, height, x, y, direction):
    states = set()

    while x not in [-1, width] and y not in [-1, height]:
        i, j = direction
        position = (x + i, y + j)
        if position in obstructions:
            state = (x, y, *direction)
            if state in states:
                #display({tuple(state[:2]) for state in states}, obstructions)
                return True
            states.add(state)
            direction = turn[direction]
        else:
            x, y = position
    return False

def display(visited, obstructions):
    for j in range(height):
        for i in range(width):
            if (i, j) in obstructions:
                print("# ", end="")
            elif (i, j) in visited:
                print("X ", end="")
            else:
                print(". ", end="")
        print()
    print()

if __name__ == "__main__":
    obstructions: set[tuple[int, int]] = set()
    x = 0
    y = 0
    direction = UP

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        j = 0
        for line in f.readlines():
            j += 1
            for i, c in enumerate(line.rstrip()):
                if c == "#":
                    obstructions.add((i, j))
                elif c != ".":
                    assert c == "^"
                    x = i
                    y = j
    width = i + 1
    height = j + 1
    start = (x, y)

    new_obstructions = set()
    visited = set()

    while x not in [-1, width] and y not in [-1, height]:
        i, j = direction
        position = (x + i, y + j)
        if position in obstructions:
            direction = turn[direction]
        else:
            if position[0] not in [-1, width] and position[1] not in [-1, height]:
                if position not in visited:
                    if path_loops(obstructions | {position}, width, height, x, y, direction):
                        new_obstructions.add(position)
            visited.add((x, y))
            x, y = position

    #display(new_obstructions, obstructions)
    print(len(new_obstructions))