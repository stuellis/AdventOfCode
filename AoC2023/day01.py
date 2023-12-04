import re

num_convert = {
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
    num_a = num_convert[str1]
    num_b = num_convert[str2]
    return num_a*10 + num_b

f = open("input_01.txt", 'r')
lines = f.read().splitlines()

sum = 0

for line in lines:
    print(line)

    # PART 1 :: regex (just digits)
    # reSinglePart = "(\d)"

    # PART 2 :: regex (digits, and digits as words)
    reSinglePart = "(\d|one|two|three|four|five|six|seven|eight|nine)"

    res = re.search(reSinglePart + ".*" +reSinglePart, line)

    if res:
        print(" > " + res.group(1) + " :: " + res.group(2))
        num = get_number(res.group(1), res.group(2))
    else:
        res = re.search(reSinglePart, line)
        print(" > " + res.group(1) + " :: " + res.group(1))
        num = get_number(res.group(1), res.group(1))

    print("=> " + str(num))
    sum += num
    
    print()


## RESULTS ##
result_line = '-' * 23
print(result_line)
print(' '*8 + "Results")
print(result_line)
print((" Sum of Values: {sum:6,}").format(sum=sum))
print(result_line)
