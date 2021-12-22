from collections import deque

with open('day6.txt', 'r') as f:
    state = [int(i) for i in f.read().split(',')]

def AOC_day6_pt1_and_pt2(days):
    totals = deque(state.count(i) for i in range(9))
    for _ in range(days):
        totals.rotate(-1)
        totals[6] += totals[8]
    return sum(totals)

print(AOC_day6_pt1_and_pt2(80))
print(AOC_day6_pt1_and_pt2(256))