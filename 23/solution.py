import heapq

letters = ('A', 'B', 'C', 'D')
costs = (1, 10, 100, 1000)
doors = (2, 4, 6, 8)

hallway_spots = (0, 1, 3, 5, 7, 9, 10)

start_state_1 = (
    "BD",
    "CC",
    "DA",
    "AB",
    "..........."
)

terminal_state_1 = (
    "AA",
    "BB",
    "CC",
    "DD",
    "..........."
)

start_state_2 = (
    "BDDD",
    "CBCC",
    "DABA",
    "ACAB",
    "..........."
)

terminal_state_2 = (
    "AAAA",
    "BBBB",
    "CCCC",
    "DDDD",
    "..........."
)


def get_next_states(state, cost, room_size):
    next_states = []
    hallway = state[4]

    for i in hallway_spots:
        letter = hallway[i]
        if letter == '.':
            continue
        
        dest_index = letters.index(letter)

        letter_cost = costs[dest_index]
        door_index = doors[dest_index]
        dest_room = state[dest_index]

        if len(dest_room) == 0 or dest_room == len(dest_room) * letters[dest_index]:
            if i > door_index:
                if hallway[door_index:i] == "." * len(hallway[door_index:i]):
                    added_cost = (i - door_index) * letter_cost + (room_size - len(dest_room)) * letter_cost
                else:
                    continue

            if i < door_index:
                if hallway[i + 1:door_index] == "." * len(hallway[i + 1:door_index]):
                    added_cost = (door_index - i) * letter_cost + (room_size - len(dest_room)) * letter_cost
                else:
                    continue

            new_cost = cost + added_cost
            new_hallway = hallway[:i] + '.' + hallway[i + 1:]
            new_room = dest_room + letter

            new_state = (
                *state[:dest_index],
                new_room,
                *state[dest_index + 1:-1],
                new_hallway
            )
            next_states.append((new_cost, new_state))
    
    for i in range(4):
        room = state[i]
        if len(room) == 0 or room == len(room) * letters[i]:
            continue
        
        letter = room[-1]
        letter_cost = costs[letters.index(letter)]
        new_room = room[:-1]
        door_index = doors[i]

        for spot in hallway_spots:
            if spot < door_index:
                if hallway[spot:door_index] == len(hallway[spot:door_index]) * '.':
                    added_cost = (room_size + 1 - len(room)) * letter_cost + (door_index - spot) * letter_cost
                else:
                    continue

            if spot > door_index:
                if hallway[door_index:spot+1] == len(hallway[door_index:spot+1]) * '.':
                    added_cost = (room_size + 1 - len(room)) * letter_cost + (spot - door_index) * letter_cost
                else:
                    continue

            new_cost = cost + added_cost
            new_hallway = hallway[:spot] + letter + hallway[spot+1:]
            new_state = (
                *state[:i],
                new_room,
                *state[i+1:-1],
                new_hallway
            )
            next_states.append((new_cost, new_state))

    return next_states


def get_expected_cost(state):
    cost = 0
    for i in range(4):
        pos = doors[i]
        room = state[i]
        for c in room:
            dest_index = letters.index(c)
            dest = doors[dest_index]
            if pos == dest:
                continue
            cost += costs[dest_index] * (abs(pos - dest) + 2)
    hallway = state[4]
    for pos in hallway_spots:
        letter = hallway[pos]
        if letter == '.':
            continue
        dest_index = letters.index(letter)
        dest = doors[dest_index]
        cost += costs[dest_index] * (abs(pos - dest) + 1)
    return cost


def run(start_state, terminal_state, room_size):
    visited = set()
    horizon = [(get_expected_cost(start_state), 0, start_state)]

    while horizon:
        _, cost, state = heapq.heappop(horizon)
        if state == terminal_state:
            break

        if state in visited:
            continue

        visited.add(state)

        for next_cost, next_state in get_next_states(state, cost, room_size):
            if next_state not in visited:
                next_expected_cost = next_cost + get_expected_cost(next_state)
                heapq.heappush(horizon, (next_expected_cost, next_cost, next_state))
    
    return cost


print("Part 1:", run(start_state_1, terminal_state_1, 2)) # 15160
print("Part 2:", run(start_state_2, terminal_state_2, 4)) # 46772
