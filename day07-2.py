import sys

def find_operators(target, current, remaining):
    if len(remaining) == 0:
        return [] if current == target else None
    n = remaining[0]
    operators = find_operators(target, current * n, remaining[1:])
    if operators is not None:
        return ["*"] + operators
    operators = find_operators(target, current + n, remaining[1:])
    if operators is not None:
        return ["+"] + operators
    operators = find_operators(target, int(str(current) + str(n)), remaining[1:])
    if operators is not None:
        return ["||"] + operators
    return None

if __name__ == "__main__":
    total = 0

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip().split()
            target = int(line[0][:-1])
            values = [int(n) for n in line[1:]]
            operators = find_operators(target, values[0], values[1:])

            if operators is not None:
                # check that operators are correct
                value = values[0]
                for op, n in zip(operators, values[1:]):
                    if op == "*":
                        value *= n
                    elif op == "+":
                        value += n
                    else:
                        assert op == "||"
                        value = int(str(value) + str(n))
                assert value == target
            #print(target, operators)
            if operators is not None:
                total += target
    print(total)
