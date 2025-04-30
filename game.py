## Liam Fogarty
## DevOps
## Final Project: Hunt the Wumpus

import random

# graph cave map, rooms, then room numbers that room is connected to
cave_map = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: []
}

def game():
    print("Game time!")

def main():
    print("Hello, Wumpus!")

    ## Define starting locations
    player_location = random.randint(1, 20)
    wumpus_location = random.randint(1, 20)

    ## Prevent Wumpus and player from having same starting spot
    while wumpus_location == player_location:
        wumpus_location = random.randint(1, 20)

    pit_locations = random.sample(range(1, 21), 2)  # generates randoms no duplicates, from chatGPT
    while player_location in pit_locations or wumpus_location in pit_locations:
        pit_locations = random.sample(range(1, 21), 2)




if __name__ == "__main__":
    main()