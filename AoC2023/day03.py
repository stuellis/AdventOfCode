import re

NUM_OF_ROWS = 139

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
    if line < NUM_OF_ROWS:
        below = grid[line+1][start-1:end+1]
        # print("v " + below)
        if contains_symbol(below):
            print("  FOUND v")
            return int(num)
    
    return 0


def adjust_gears(line: int, col: int, num: str):
    gear_ratio = 0
    current_gear_val = gears[line][col]
    if current_gear_val > 0:
        gear_ratio = current_gear_val * int(num)
        gears[line][col] = 0
    else:
        gears[line][col] = int(num)
    
    return gear_ratio


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
    if line < NUM_OF_ROWS:
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

sum_of_part_nums = 0
sum_of_gear_ratios = 0

gears = [[0 for col in range(NUM_OF_ROWS+1+2)] for row in range(NUM_OF_ROWS+1)]

current_num = ""
check_number = False

line_num = -1

for line in grid:
    line_num += 1
    char_pos = -1

    print(str(line_num) + "> " + line)

    for char in line:
        char_pos += 1

        # print(" " + str(char_pos) + "> " + char)
        if char >= '0' and char <= '9':
            check_number = True
            current_num += char
        else:
            # end of number

            if check_number:
                p1 = part_1_check_number(current_num, line_num, char_pos-len(current_num), char_pos)
                sum_of_part_nums += p1
                print("[check_number] " + current_num + " >> " + str(p1))
                
                if p1 > 0:
                    p2 = part_2_check_for_gears(current_num, line_num, char_pos-len(current_num), char_pos)
                    print("[check_for_gears] " + str(p2))
                    sum_of_gear_ratios += p2

            check_number = False
            current_num = ""

print()


## RESULTS ##
result_line = '-' * 33
print(result_line)
print(' '*13 + "Results")
print(result_line)
print((" Sum of Part Numbers: {sum:10,}").format(sum=sum_of_part_nums))
print((" Sum of  Gear Ratios: {sum:10,}").format(sum=sum_of_gear_ratios))
print(result_line)
