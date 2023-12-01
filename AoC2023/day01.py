import re

numConvert = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def get_number(str1: str, str2: str):
    numA = numConvert[str1]
    numB = numConvert[str2]
    return numA*10 + numB

f = open("input_01.txt", 'r')
lines = f.read().splitlines()

sum = 0

for line in lines:
    # print(line)

    # Part 1 regex (just digits)
    # reSinglePart = "(\d)"

    # Part 2 regex (digits, and digits as words)
    reSinglePart = "(\d|one|two|three|four|five|six|seven|eight|nine)"

    res = re.search(reSinglePart + ".*" +reSinglePart, line)

    if res:
        num = get_number(res.group(1), res.group(2))
    else:
        res = re.search(reSinglePart, line)
        num = get_number(res.group(1), res.group(1))

    sum += num

print("Sum: " + str(sum))
