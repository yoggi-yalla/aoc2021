import heapq

from collections import namedtuple

room_size = 4

State = namedtuple(
    'State', [
        'room1',
        'room2',
        'room3',
        'room4',
        'hallway',
    ]
)

letter_to_cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000 
}

letter_to_index = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

hallway_spots = (0, 1, 3, 5, 7, 9, 10)
doors = (2, 4, 6, 8)


start_state_1 = State(
    ('B', 'D'),
    ('C', 'C'),
    ('D', 'A'),
    ('A', 'B'),
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'),
)

terminal_state_1 = State(
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'),
)

start_state_2 = State(
    ('B', 'D', 'D', 'D'),
    ('C', 'B', 'C', 'C'),
    ('D', 'A', 'B', 'A'),
    ('A', 'C', 'A', 'B'),
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'),
)

terminal_state_2 = State(
    ('A', 'A', 'A', 'A'),
    ('B', 'B', 'B', 'B'),
    ('C', 'C', 'C', 'C'),
    ('D', 'D', 'D', 'D'),
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'),
)


def get_next_states(state, cost, path, room_size):
    next_states = []
    for i in range(11):
        letter = state.hallway[i]
        if letter == '.':
            continue
        
        room_index = letter_to_index[letter]
        door_index = doors[room_index]
        letter_cost = letter_to_cost[letter]
        room = state[room_index]

        if len(room) == 0 or all(c == letter for c in room):
            if i > door_index:    
                if all(c == '.' for c in state.hallway[door_index:i]):
                    new_cost = (i - door_index) * letter_cost + (room_size - len(room)) * letter_cost
                else:
                    continue

            if i < door_index:
                if all(c == '.' for c in state.hallway[i + 1:door_index]):
                    new_cost = (door_index - i) * letter_cost + (room_size - len(room)) * letter_cost
                else:
                    continue
        
            new_hallway = tuple([*state.hallway[:i], '.', *state.hallway[i + 1:]])
            new_room = tuple([*room, letter])
            new_state = State(
                *state[:room_index],
                new_room,
                *state[room_index+1:-1],
                new_hallway
            )
            sub_path = path + str(new_state) + "\n\n"
            next_states.append((cost + new_cost, new_state, str(sub_path)))
    
    for i in range(4):
        room = state[i]
        if len(room) == 0:
            continue
        letter = room[-1]
        letter_cost = letter_to_cost[letter]

        new_room = room[:-1]
        
        door_index = doors[i]

        for spot in hallway_spots:
            if spot < door_index:
                if all(c == '.' for c in state.hallway[spot:door_index]):
                    new_cost = (room_size + 1 - len(room)) * letter_cost + (door_index - spot) * letter_cost
                    new_hallway = tuple([
                        *state.hallway[:spot],
                        letter,
                        *state.hallway[spot+1:]
                    ])
                    new_state = State(
                        *state[:i],
                        new_room,
                        *state[i+1:-1],
                        new_hallway
                    )
                    sub_path = path + str(new_state) + "\n\n"
                    next_states.append((cost + new_cost, new_state, str(sub_path)))

            if spot > door_index:
                if all(c == '.' for c in state.hallway[door_index:spot+1]):
                    new_cost = (room_size + 1 - len(room)) * letter_cost + (spot - door_index) * letter_cost
                    new_hallway = tuple([
                        *state.hallway[:spot],
                        letter,
                        *state.hallway[spot+1:]
                    ])
                    new_state = State(
                        *state[:i],
                        new_room,
                        *state[i+1:-1],
                        new_hallway
                    )
                    sub_path = path + str(new_state) + "\n\n"
                    next_states.append((cost + new_cost, new_state, str(sub_path)))

    return next_states


def run(start_state, terminal_state, room_size):
    visited = set()
    horizon = [(0, start_state, "")]
    while horizon:
        cost, state, path = heapq.heappop(horizon)
        if state == terminal_state:
            break

        if state in visited:
            continue

        visited.add(state)

        next_states = get_next_states(state, cost, path, room_size)
        for state in next_states:
            heapq.heappush(horizon, state)
    
    return cost, path


print("Part 1:", run(start_state_1, terminal_state_1, 2)[0]) # 15160
print("Part 2:", run(start_state_2, terminal_state_2, 4)[0]) # 46772
