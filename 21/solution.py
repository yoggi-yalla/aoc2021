import functools
import itertools

die = itertools.cycle(list(range(1,101)))

p1_pos = 2
p2_pos = 5

p1_score = 0
p2_score = 0

iteration = 0
while p1_score < 1000 and p2_score < 1000:
    steps = next(die) + next(die) + next(die)

    if iteration % 2 == 0:
        p1_pos = (p1_pos + steps - 1) % 10 + 1
        p1_score += p1_pos
    
    else:
        p2_pos = (p2_pos + steps - 1) % 10 + 1
        p2_score += p2_pos

    iteration += 1
print("Part 1:", iteration * 3 * min(p1_score, p2_score)) # 576600


@functools.cache
def most_wins(p1_score, p2_score, p1_pos, p2_pos, p1_turn):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    
    universes = itertools.product([1,2,3], repeat=3)
    wins = []
    for (d1, d2, d3) in universes:
        steps = d1 + d2 + d3
        if p1_turn:
            p1_sub_pos = (p1_pos + steps - 1) % 10 + 1
            p1_sub_score = p1_score + p1_sub_pos
            wins.append(most_wins(p1_sub_score, p2_score, p1_sub_pos, p2_pos, not p1_turn))
        
        else:
            p2_sub_pos = (p2_pos + steps - 1) % 10 + 1
            p2_sub_score = p2_score + p2_sub_pos
            wins.append(most_wins(p1_score, p2_sub_score, p1_pos, p2_sub_pos, not p1_turn))
    
    wins_1 = sum(w[0] for w in wins)
    wins_2 = sum(w[1] for w in wins)
    
    return wins_1, wins_2

print("Part 2:", max(most_wins(0, 0, 2, 5, True))) # 131888061854776
