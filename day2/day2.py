def create_array():
    with open("input.txt", "r") as f:
        x = f.readlines()
        array = [v.strip() for v in x]
    return array


def part1(array):
    horizontal = 0
    depth = 0

    for e in array:
        if e[0] == "f":
            horizontal += int(e[8])
        elif e[0] == "d":
            depth += int(e[5])
        else:
            depth -= int(e[3])

    return depth * horizontal


def part2(array):
    horizontal = 0
    depth = 0
    aim = 0

    for e in array:
        if e[0] == "f":
            horizontal += int(e[8])
            depth += aim * int(e[8])
        elif e[0] == "d":
            aim += int(e[5])
        else:
            aim -= int(e[3])

    return horizontal * depth


if __name__ == "__main__":
    print(part2(create_array()))