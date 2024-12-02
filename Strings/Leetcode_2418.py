names = ["Mary","John","Emma"]
heights = [180,165,170]

mapp = {}
for i in range(len(names)):
    mapp[heights[i]] = names[i]
heights.sort(reverse=True)
answer = []
for h in heights:
    answer.append(mapp[h])
print(answer)