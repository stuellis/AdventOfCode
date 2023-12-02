import re

FINALRED = 12
FINALGREEN = 13
FINALBLUE = 14

# SUM for PART 1
idSum = 0

# SUM for PART 2
powerSum = 0

f = open("input_02.txt", 'r')
lines = f.read().splitlines()

for line in lines:
    # print(line)

    x = line.split(":")
    game = x[0]
    results = x[1]
    
    pulls = results.split(";")

    maxRed = 0
    maxGreen = 0
    maxBlue = 0

    for pull in pulls:
        # print(pull)

        res = re.search("(\d+) red", pull)
        if res:
            maxRed = max(maxRed, int(res.group(1)))
        
        res = re.search("(\d+) green", pull)
        if res:
            maxGreen = max(maxGreen, int(res.group(1)))
        
        res = re.search("(\d+) blue", pull)
        if res:
            maxBlue = max(maxBlue, int(res.group(1)))

    # PART 1
    if maxRed <= FINALRED and maxGreen <= FINALGREEN and maxBlue <= FINALBLUE:
        res = re.search("Game (\d+)", game)
        if res:
            idSum += int(res.group(1))

    # PART 2
    powerSum += maxRed * maxGreen * maxBlue

print(("ID Sum: {s}").format(s=idSum))
print(("Power Sum: {s}").format(s=powerSum))
