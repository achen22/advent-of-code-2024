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
        fixed: list[int] = []
        reverse_rules: dict[int, list[int]] = {}
        for page in update:
            if page in reverse_rules:
                banned = reverse_rules[page]
                i = min(fixed.index(b) for b in banned)
                fixed.insert(i, page)
            else:
                fixed.append(page)
            if page in rules:
                required = rules[page]
                for r in required:
                    if r not in fixed:
                        if r in reverse_rules:
                            reverse_rules[r].append(page)
                        else:
                            reverse_rules[r] = [page]
        #print(update, "Valid" if valid else "Invalid")
        if fixed != update:
            #print(fixed)
            total += fixed[(len(fixed) - 1) // 2]
    print(total)