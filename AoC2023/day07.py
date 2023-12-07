import re

#A K Q J T 9 8 7 6 5 4 3 2
def card_value(card: str):
    match card:
        case "9":
            return 9
        case "8":
            return 8
        case "7":
            return 7
        case "6":
            return 6
        case "5":
            return 5
        case "4":
            return 4
        case "3":
            return 3
        case "2":
            return 2
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            # PART 1 would return 11
            return 0
        case "T":
            return 10


# 1: 5kind, 2: 4kind, 3: house, 4: 3kind, 5: 2pair, 6:  pair, 7:  high
# Unique cards:
# AAAAA: 1, AAAAB: 2, AAABB: 2, AAABC: 3, AABBC: 3, AABCD: 4, ABCDE: 5
# PART 2: added # Jokers turns ... returns
#   possible J options:
# JJJJJ     AAAAJ     AAAJJ     AAABJ     AABBJ     AABCJ     ABCDJ
#           JJJJA     JJJAA     JJJAB     JJAAB     JJABC
#           -> (1)    -> (1)    -> (4)    -> (H/4)  -> (3)    -> (P)
def hand_type(hand: str):
    unique_card = list(set(hand))
    match len(unique_card):
        case 1: # 5 of kind
            return 1
        case 2: # 4 of kind or full house
            if hand.find("J") > -1:
                # Jokers turns either into 5 of a kind
                return 1
            count = 0
            for card in hand:
                if card == unique_card[0]:
                    count += 1
            if count == 1 or count == 4:
                # 4 of a kind
                return 2
            else:
                # Full house
                return 3
        case 3: # 3 of kind or 2 pair
            max_count = 0
            for ucard in unique_card:
                count = 0
                for card in hand:
                    if card == ucard:
                        count += 1
                max_count = max(max_count, count)
            if max_count == 2:
                # 2 pair
                j_cards = 0
                for card in hand:
                    if card == "J":
                        j_cards += 1
                if j_cards == 1:
                    # Jokers turns it into full house
                    return 3
                elif j_cards == 2:
                    # Jokers turns it into 4 of a kind
                    return 2
                return 5
            else:
                # 3 of a kind
                if hand.find("J") > -1:
                    # Jokers turns it into 4 of a kind
                    return 2
                return 4
        case 4: # Pair
            if hand.find("J") > -1:
                # Jokers turns it into 3 of a kind
                return 4
            return 6
        case 5: # High Card
            if hand.find("J") > -1:
                # Joker turns it into a pair
                return 6
            return 7
    return 7


class CardHand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = hand_type(hand)
    
    def __lt__(self, other):
        if self.type == other.type:
            for c in range(5):
                s = card_value(self.hand[c])
                o = card_value(other.hand[c])
                if s != o:
                    return s > o
        else:
            return self.type < other.type
    
    def __str__(self) -> str:
        return "{hand} ({type}) - {bid:3}".format(hand=self.hand, type=self.type, bid=self.bid)


f = open("input_07.txt", 'r')
lines = f.read().splitlines()

hands = []
rank = 0
for line in lines:
    # print(line)
    res = re.search("(.*) (\d+)", line)
    if res:
        hand = res.group(1)
        bid = res.group(2)
        hands.append(CardHand(hand, bid))
    rank += 1

winnings_sum = 0
sorted_hands = sorted(hands)
for hand in sorted_hands:
    print(hand)
    winnings = rank * hand.bid
    print(" >{r:4} * {b:3} = {w:7,}".format(r=rank, b=hand.bid, w=winnings))
    winnings_sum += winnings
    rank -= 1


result_line = '-' * 33
print()
print(result_line)
print(' '*12 + "Results")
print(result_line)
print(" Sum of Winnings: {w:10,}".format(w=winnings_sum))
print(result_line)
