import random

# Cave graph
cave = {
    1: [2, 5, 8],  2: [1, 3, 10],  3: [2, 4, 12],  4: [3, 5, 14],
    5: [1, 4, 6],  6: [5, 7, 15],  7: [6, 8, 17],  8: [1, 7, 9],
    9: [8, 10, 18], 10: [2, 9, 11], 11: [10, 12, 19], 12: [3, 11, 13],
    13: [12, 14, 20], 14: [4, 13, 15], 15: [6, 14, 16], 16: [15, 17, 20],
    17: [7, 16, 18], 18: [9, 17, 19], 19: [11, 18, 20], 20: [13, 16, 19]
}

def check_hazard(player_location, wumpus_location, pit_locations):
    if player_location == wumpus_location:
        return "wumpus"
    if player_location in pit_locations:
        return "pit"
    return "safe"

def is_valid_move(current_location, next_room):
    return next_room in cave[current_location]

def generate_locations(seed=None):
    if seed is not None:
        random.seed(seed)

    player = random.randint(1, 20)
    all_locations = list(range(1, 21))
    all_locations.remove(player)

    wumpus = random.choice(all_locations)
    all_locations.remove(wumpus)

    pits = random.sample(all_locations, 2)
    for pit in pits:
        all_locations.remove(pit)

    bats = random.sample(all_locations, 2)

    return player, wumpus, pits, bats

def move_player(current_location, next_room):
    if is_valid_move(current_location, next_room):
        return next_room
    return current_location

def bat_transport(player_location, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.randint(1, 20)
