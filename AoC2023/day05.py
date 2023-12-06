import re

f = open("input_05.txt", 'r')
lines = f.read().splitlines()

map_section = 0

mappings = [[], [], [], [], [], [], []]
seeds = []
seed_pairs = []

for line in lines:
    # print(line)

    res = re.search("seeds: (.*)", line)
    if res:
        # print(line)

        seed_pairs = re.findall("(\d+) (\d+)", res.group(1))

        # SEED NUMBERS
        seeds = re.split("\s+", res.group(1))
        # print(seeds)
        continue

    if line == "seed-to-soil map:":
        map_section = 1
        continue

    if line == "soil-to-fertilizer map:":
        map_section = 2
        continue

    if line == "fertilizer-to-water map:":
        map_section = 3
        continue

    if line == "water-to-light map:":
        map_section = 4
        continue

    if line == "light-to-temperature map:":
        map_section = 5
        continue

    if line == "temperature-to-humidity map:":
        map_section = 6
        continue

    if line == "humidity-to-location map:":
        map_section = 7
        continue

    range_map = re.search("(\d+) (\d+) (\d+)", line)
    if range_map:
        mappings[map_section-1].append(range_map.groups())

# print(seed_pairs)

print()

min_loc = 0

for seed in seeds:
    num = int(seed)
    print("Seed [{seed:,}]".format(seed=num))

    for m in range(7):
        ranges = mappings[m]
        print("[{num:,}]".format(num=num))
        # print("> " + str(ranges))
        for r in ranges:
            dest_range = int(r[0])
            source_range = int(r[1])
            range_len = int(r[2])
            print("    " + str(r) + "\t\t:: " + "source range: {s1:15,} - {s2:15,}".format(s1=source_range, s2=source_range+range_len-1))

            if num >= source_range and num < source_range + range_len:
                num = dest_range + (num - source_range)
                print("     >> in range ==> {num:,}".format(num=num))
                break

    print(("\n[{seed:,}] => location {loc:,}").format(seed=int(seed), loc=num))

    if min_loc > 0:
        min_loc = min(min_loc, num)
    else:
        min_loc = num

all_min = 0


## RESULTS ##
result_line = '-' * 39
print()
print(result_line)
print(' '*16 + "Results")
print(result_line)
print(" Minimum Location: {loc:19,}".format(loc=min_loc))
print(" Part 2 incomplete: {loc:18,}".format(loc=all_min))
print(result_line)

