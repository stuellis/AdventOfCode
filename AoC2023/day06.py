import re

f = open("input_06.txt", 'r')
lines = f.read().splitlines()

rec_time = []
rec_dist = []

part2_time = 0
part2_dist = 0

l = 0
for line in lines:
    print(line)
    
    res = re.findall("\d+", line)

    part2_string = ""

    for r in res:
        num = int(r)
        if l == 0:
            rec_time.append(num)
        else:
            rec_dist.append(num)
        part2_string += r
    if l == 0:
        part2_time = int(part2_string)
    else:
        part2_dist = int(part2_string)
    l += 1


print(rec_time)
print(rec_dist)
print(part2_time)
print(part2_dist)

## PART 1
product = 1
for time in rec_time:
    print(time)
    beat_record = 0
    for h in range(time):
        speed = h
        distance = speed * (time - h)
        print("Hold for {t} ({r}) ==> {d}".format(t=h, r=time-h, d=distance))
        if distance > rec_dist[rec_time.index(time)]:
            print(" >> further")
            beat_record += 1
    
    print("\nWays to beat record: {b}\n".format(b=beat_record))
    product *= beat_record

## PART 2
print("\n\nPART 2\n\n")
min_win = 0
max_win = 0

carry_on = False

for h in range(part2_time):
# for h in range(7300000, 7400000):
# for h in range(37500000, 37600000):
    speed = h
    distance = speed * (part2_time - h)
    print("Hold for {t} ({r}) ==> {d}".format(t=h, r=part2_time-h, d=distance))
    if distance > part2_dist:
        carry_on = True
        if min_win > 0:
            max_win = h
        else:
            min_win = h
        print(" >> further >> {min} :: {max}".format(min=min_win, max=max_win))
    elif carry_on:
        break

# ^^ takes too long / brute force
# can be solved with quadratic ax^2+bx+c
# with a = -1, b = time, c = distance_to_beat

## RESULTS ##
result_line = '-' * 33
print()
print(result_line)
print(' '*12 + "Results")
print(result_line)
print(" Beat Record Product: {prod:10,}".format(prod=product))
print(" Part 2 num of wins:  xxxx")
print(result_line)
