def create_array():
    with open("day3.txt", "r") as f:
        array = [v.strip() for v in f.readlines()]
    return array


def part1(array):
    gamma = ""
    epsilon = ""
    counts = {i: 0 for i in range(12)}
    half = len(array)/2

    for e in array:
        for i, c in enumerate(e):
            if c == "1":
                counts[i] += 1

    for e in counts:
        if counts[e] >= half:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part2(array):
    oxy_array = array

    for pos in range(12):
        count_0 = 0
        count_1 = 0

        for _ in range(2):
            for i, e in enumerate(oxy_array):

                if _ == 0:
                    if e[pos] == 1:
                        count_1 += 1
                    else:
                        count_0 += 1

                if _ == 1:
                    x = 1 if count_1 >= count_0 else 0






if __name__ == '__main__':
    print(part1(create_array()))
