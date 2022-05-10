import re

def create_array():
    with open("input.txt","r") as f:
        raw_array = [x for x in f]
    array = [re.findall("\d+",x) for x in raw_array]
    return array

def main():
    return


if __name__ == "__main__":
    print(create_array())