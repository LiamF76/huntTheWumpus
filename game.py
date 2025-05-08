import random

# graph cave map, rooms, then room numbers that room is connected to
cave = {
    1: [2, 5, 8],
    2: [1, 3, 10],
    3: [2, 4, 12],
    4: [3, 5, 14],
    5: [1, 4, 6],
    6: [5, 7, 15],
    7: [6, 8, 17],
    8: [1, 7, 9],
    9: [8, 10, 18],
    10: [2, 9, 11],
    11: [10, 12, 19],
    12: [3, 11, 13],
    13: [12, 14, 20],
    14: [4, 13, 15],
    15: [6, 14, 16],
    16: [15, 17, 20],
    17: [7, 16, 18],
    18: [9, 17, 19],
    19: [11, 18, 20],
    20: [13, 16, 19]
}

def check_hazard(player_location, wumpus_location, pit_locations):
    if player_location == wumpus_location:
        return "wumpus"
    if player_location in pit_locations:
        return "pit"
    return "safe"

def is_valid_move(current_location, next_room):
    return next_room in cave[current_location]

def generate_locations():
    player = random.randint(1, 20)

    # Generate unique locations for wumpus, pits, bats
    all_locations = list(range(1, 21))
    all_locations.remove(player)

    wumpus = random.choice(all_locations)
    all_locations.remove(wumpus)

    pits = random.sample(all_locations, 2)
    for pit in pits:
        all_locations.remove(pit)

    bats = random.sample(all_locations, 2)

    return player, wumpus, pits, bats

def run_game():
    player, wumpus, pits, bats = generate_locations()

    print("Game Start!")
    print(f"You are starting in room: {player}")
    print(f"Pits are in rooms: {pits}")
    print(f"Wumpus is in room: {wumpus}")
    print(f"Bats are in rooms: {bats}")
    print("")

    while True:
        print(f"You are in room {player}. Connected rooms: {cave[player]}")

        # Wumpus warning if it's in an adjacent room
        if wumpus in cave[player]:
            print("It's wumpin time!")

        move = input("Which room do you want to move to? ")

        if not move.isdigit():
            print("Please enter a valid room number.")
            continue

        next_room = int(move)

        if not is_valid_move(player, next_room):
            print("You can't move there! Try a connected room.")
            continue

        player = next_room
        hazard = check_hazard(player, wumpus, pits)

        if hazard == "pit":
            print("You fell into a pit! Game over.")
            break
        elif hazard == "wumpus":
            print("The Wumpus ate you! Game over.")
            break
        elif player in bats:
            new_room = random.randint(1, 20)
            print(f"A bat grabs you and drops you into room {new_room}!")
            player = new_room
            # Re-check for immediate hazard
            hazard = check_hazard(player, wumpus, pits)
            if hazard == "pit":
                print("You fell into a pit after the bat dropped you! Game over.")
                break
            elif hazard == "wumpus":
                print("The Wumpus was waiting in the room the bat dropped you in! Game over.")
                break
        else:
            print("You're safe... for now.")
        print("")


# Run the game
run_game()
