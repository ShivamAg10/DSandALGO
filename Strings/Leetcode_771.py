from collections import Counter

def numJewelsInStones(jewels, stones):
    num_dict = Counter(stones)
    total_nums = 0
    for i in range(len(jewels)):
        total_nums += num_dict[jewels[i]]
    return total_nums

stones = "aAAbbbb"
jewels = "aA"

print(numJewelsInStones(jewels, stones))