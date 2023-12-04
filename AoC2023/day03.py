import re

GRIDY = 139

def contains_symbol(line: str):
    symbol = "[^\d.]"
    res = re.search(symbol, line)
    return res


def part_1_check_number(num: str, line: int, start: int, end: int):
    # search left
    pre = grid[line][start-1:start]
    # print("< " + pre)
    if contains_symbol(pre):
        print("  FOUND <")
        return int(num)
    
    # search right
    post = grid[line][end:end+1]
    # print("> " + post)
    if contains_symbol(post):
        print("  FOUND >")
        return int(num)
    
    # search above
    if line > 0:
        above = grid[line-1][start-1:end+1]
        # print("^ " + above)
        if contains_symbol(above):
            print("  FOUND ^")
            return int(num)
    
    # search below
    if line < GRIDY:
        below = grid[line+1][start-1:end+1]
        # print("v " + below)
        if contains_symbol(below):
            print("  FOUND v")
            return int(num)
    
    return 0


def adjust_gears(line: int, col: int, num: str):
    gearRatio = 0
    currentGear = gears[line][col]
    if currentGear > 0:
        gearRatio = currentGear * int(num)
        gears[line][col] = 0
    else:
        gears[line][col] = int(num)
    
    return gearRatio


def part_2_check_for_gears(num: str, line: int, start: int, end: int):
    # search left
    pre = grid[line][start-1:start]
    x = pre.find("*")
    if x > -1:
        print("  GEAR <")
        return adjust_gears(line, start-1, num)

    # search right
    post = grid[line][end:end+1]
    x = post.find("*")
    if x > -1:
        print("  GEAR > ")
        return adjust_gears(line, end, num)

    # search above
    if line > 0:
        above = grid[line-1][start-1:end+1]
        x = above.find("*")
        if x > -1:
            print("  GEAR ^")
            return adjust_gears(line-1, start-1+x, num)

    # search below
    if line < GRIDY:
        below = grid[line+1][start-1:end+1]
        x = below.find("*")
        if x > -1:
            print("  GEAR v")
            return adjust_gears(line+1, start-1+x, num)
    
    return 0


f = open("input_03.txt", 'r')
lines = f.read().splitlines()

grid = []
for line in lines:
    # print(line)
    # pad each from with '.' at start and end to avoid edge detection
    line = "." + line + "."
    grid.append(line)

sum = 0
sumGearRatios = 0

gears = [[0 for col in range(GRIDY+1+2)] for row in range(GRIDY+1)]

currentNum = ""
checkNumber = False

lineNum = -1

for line in grid:
    lineNum += 1
    charPos = -1

    print(str(lineNum) + "> " + line)

    for char in line:
        charPos += 1

        # print(" " + str(charPos) + "> " + char)
        if char >= '0' and char <= '9':
            checkNumber = True
            currentNum += char
        else:
            # end of number

            if checkNumber:
                p1 = part_1_check_number(currentNum, lineNum, charPos-len(currentNum), charPos)
                sum += p1
                print("[check_number] " + currentNum + " >> " + str(p1))
                
                if p1 > 0:
                    p2 = part_2_check_for_gears(currentNum, lineNum, charPos-len(currentNum), charPos)
                    print("[check_for_gears] " + str(p2))
                    sumGearRatios += p2

            checkNumber = False
            currentNum = ""

print("\n\n-------------\n   Results\n-------------")
print(("Sum: {a}").format(a=sum))
print(("Sum ratio: {a}").format(a=sumGearRatios))

