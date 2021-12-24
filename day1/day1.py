def create_array():
    with open("day1.txt", "r") as f:
        x = f.readlines()
        array = [int(v.strip()) for v in x]
    return array


def part1(array):
    count = 0
    for i, e in enumerate(array):
        if e > array[i-1]:
            count += 1
    return count


def part2(array):
    count = 0
    old_sum = 0
    for i, e in enumerate(array):
        try:
            new_sum = e + array[i+1] + array[i+2]
            if i == 0:
                old_sum = new_sum
                continue
            if new_sum > old_sum:
                count += 1
            old_sum = new_sum
        except IndexError:
            continue
    return count


if __name__ == '__main__':
    print(part2(create_array()))
