import re

FINAL_RED = 12
FINAL_GREEN = 13
FINAL_BLUE = 14

# SUM for PART 1
id_sum = 0

# SUM for PART 2
power_sum = 0

f = open("input_02.txt", 'r')
lines = f.read().splitlines()

for line in lines:
    print(line)

    parts = line.split(":")
    game_num = parts[0]
    results = parts[1]
    
    pulls = results.split(";")

    max_red = 0
    max_green = 0
    max_blue = 0

    for pull in pulls:
        # print(pull)

        res = re.search("(\d+) red", pull)
        if res:
            max_red = max(max_red, int(res.group(1)))
        
        res = re.search("(\d+) green", pull)
        if res:
            max_green = max(max_green, int(res.group(1)))
        
        res = re.search("(\d+) blue", pull)
        if res:
            max_blue = max(max_blue, int(res.group(1)))

    print(("  Max :: Red {r}, Green {g}, Blue {b}").format(r=max_red, g=max_green, b=max_blue))

    # PART 1
    if max_red <= FINAL_RED and max_green <= FINAL_GREEN and max_blue <= FINAL_BLUE:
        res = re.search("Game (\d+)", game_num)
        if res:
            id_sum += int(res.group(1))

    # PART 2
    power_sum += max_red * max_green * max_blue

    print()


## RESULTS ##
result_line = '-' * 23
print(result_line)
print(' '*8 + "Results")
print(result_line)
print(("   Game ID Sum: {id:6,}").format(id=id_sum))
print((" Set Power Sum: {power:6,}").format(power=power_sum))
print(result_line)
