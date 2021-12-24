def create_array():
    with open("day3.txt", "r") as f:
        array = [v.strip() for v in f.readlines()]
    return array


def part1(array):
    gamma = ""
    epsilon = ""

    for pos in range(12):
        count_1 = 0
        count_0 = 0
        for e in array:
            if e[pos] == "1":
                count_1 += 1
            else:
                count_0 += 1
        if count_1 > count_0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)

def part2(array):


if __name__ == '__main__':
    print(part1(create_array()))
