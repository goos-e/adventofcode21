def create_array():
    with open("day3.txt", "r") as f:
        array = [v.strip() for v in f.readlines()]
    return array


def part1(array):
    gamma = ""
    epsilon = ""
    counts = {i: 0 for i in range(12)}  # counts of 1
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
    half = len(array)/2

    oxy_array = array

    for e in oxy_array:
        count = 0  # counts of 1
        for i in range(12):
            if e[i] == "1":
                count += 1




    print(oxy_array)



if __name__ == '__main__':
    print(part2(create_array()))
