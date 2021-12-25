def create_array():
    with open("day3.txt", "r") as f:
        array = [v.strip() for v in f.readlines()]
    return array


def part1(array):
    gamma = ""
    epsilon = ""
    counts = {i: 0 for i in range(12)}  # counts of 1
    half = len(array)/2

    # counter
    for e in array:
        for i, c in enumerate(e):
            if c == "1":
                counts[i] += 1

    # creating binary values
    for e in counts:
        if counts[e] >= half:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part2(array):

    # Bit criteria for oxygen
    oxy_array = array.copy()
    i = 0
    while len(oxy_array) > 1:

        # Counting
        counts = [0, 0]  # zeros, ones
        for e in oxy_array:
            if e[i] == '0':
                counts[0] += 1
            else:
                counts[1] += 1

        # Modifying list
        if counts[1] >= counts[0]:  # ones more common
            oxy_array = [e for e in oxy_array if e[i] == '1']
        else:
            oxy_array = [e for e in oxy_array if e[i] == '0']

        i += 1

    # Bit criteria for co2
    co2_array = array.copy()
    i = 0
    while len(co2_array) > 1:

        # Counting
        counts = [0, 0]  # zeros, ones
        for e in co2_array:
            if e[i] == '0':
                counts[0] += 1
            else:
                counts[1] += 1

        # Modifying list
        if counts[1] >= counts[0]:  # zeros more common
            co2_array = [e for e in co2_array if e[i] == '0']
        else:
            co2_array = [e for e in co2_array if e[i] == '1']

        i += 1

    oxy_rating = int(oxy_array[0], 2)
    co2_rating = int(co2_array[0], 2)

    return oxy_rating * co2_rating


if __name__ == '__main__':
    print(part2(create_array()))
