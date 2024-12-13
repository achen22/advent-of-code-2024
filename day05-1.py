import sys

if __name__ == "__main__":
    rules: dict[int, list[int]] = {}
    updates: list[list[int]] | None = None

    filename = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip()
            if not line:
                updates = []
                continue
            if updates is None:
                a, b = [int(n) for n in line.split("|")]
                if b in rules:
                    rules[b].append(a)
                else:
                    rules[b] = [a]
            else:
                updates.append([int(n) for n in line.split(",")])

    total = 0
    for update in updates:
        valid = True
        before: list[int] = []
        banned: list[int] = []
        for page in update:
            if page in banned:
                valid = False
                break
            if page in rules:
                required = rules[page]
                for r in required:
                    if r not in before:
                        banned.append(r)
            before.append(page)
        #print(update, "Valid" if valid else "Invalid")
        if valid:
            total += update[(len(update) - 1) // 2]
    print(total)