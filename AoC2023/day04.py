import re

f = open("input_04.txt", 'r')
lines = f.read().splitlines()

point_sum = 0
num_of_copies = [1] * 197

for line in lines:
    print(line)

    matches = 0
    points = 0

    res = re.search("Card\s+(\d+):\s+(.*) \|\s+(.*)", line)
    if res:
        card = int(res.group(1))
        wins = res.group(2)
        have = res.group(3)

        ws = re.split("\s+", wins)
        hs = re.split("\s+", have)

        for h in hs:
            if h in ws:
                matches += 1
                p = pow(2, matches-1)
                print(("  {num:2} is in!! > {points:4}").format(num=h, points=p))
        
        if matches > 0:
            # PART 1 points
            points = pow(2, matches-1)
            point_sum += points
            print("Total: " + str(point_sum))

            # PART 2 card copies
            print("To add: [" + str(num_of_copies[card-1]) + "] to next [" + str(matches) + "] cards")
            for i in range(matches):
                num_of_copies[card+i] += num_of_copies[card-1]
    
    print(num_of_copies)

    print()

scratchcards = 0
for c in num_of_copies:
    scratchcards += c

result_line = '-' * 25
print(result_line)
print(' '*9 + "Results")
print(result_line)
print((" Total Points: {points:9,}").format(points=point_sum))
print((" Total  Cards: {cards:9,}").format(cards=scratchcards))
print(result_line)