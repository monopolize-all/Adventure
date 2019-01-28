################################################################################
#                                                                              #
# By:                                                                          #
#   Name: Mohit Mohandas                                                       #
#   Class: XI                                                                  #
#   Roll no.: 20                                                               #
#   Version: 2.0                                                               #
#                                                                              #
################################################################################

# Note: The user interface has been modified to suit the python console.
# Double click on the file to run game.
# Certain features are disabled when running from the IDLE interpreter.

# Edits:
# 1) Added more information via comments.
# 2) Made game more user friendly.

import os
import random
import time

print("""By:
    Name: Mohit Mohandas
    Class: XI
    Roll no.: 20
    Version: 2.0""")
time.sleep(3)

# Clears screen
# Can cause errors in certain computers
os.system('cls' if os.name == 'nt' else 'clear')
# Welcome note
if input("Read instructions?(y for yes or any other key to skip): ") == "y":
    # Clears screen
    # Can cause errors in certain computers
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to The Adventure.")
    time.sleep(1)
    print("Use w, a, s, or d followed by enter to navigate the player P " +
        "up, left, down or right respectively.")
    time.sleep(3)
    print("# represents walls. Players cannot go over walls.")
    time.sleep(2)
    print("C represents coins. They can be collected to increase your money.")
    time.sleep(2)
    print("X represents zombies. Being in the same tile as a zombie causes " +
          "death. So avoid them!")
    time.sleep(3)
    print("e followed by enter ends the game.")
    time.sleep(2)
    print("Use m followed by enter three times consecutively to break all " +
        "walls surrounding you. \nNote: Boundary wall cannot be destroyed.")
    time.sleep(3)
    print("Press enter to start.")
    input()
    # Clears screen
    # Can cause errors in certain computers
    os.system('cls' if os.name == 'nt' else 'clear')

cmd = ""

# Initialises grid size and grid
grid_size = (25, 15)
grid = []
for y in range(grid_size[1]):
    grid.append([])
    for x in range(grid_size[0]):
        grid[y].append(" ")

# Represents the grid which is later converted to a list
grid_str = """
#########################
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                      E#
#########################"""
# Converts grid_str of string type to a grid of list type
x, y = 0, -1
for tile in grid_str:
    if tile != "\n":
        grid[y][x] = tile
        x += 1
    else:
        y += 1
        x = 0

# Old method to create list. Above method allows editing of map beforehand.
# for i in range(grid_size[0]):
#     grid[0][i] = "#"
#     grid[-1][i] = "#"
# for i in range(grid_size[1]):
#     grid[i][0] = "#"
#     grid[i][-1] = "#"

# Adds extra walls
for i in range(100):
    pos = [random.randint(1, grid_size[0] - 1), random.randint(1, grid_size[1] - 1)]
    grid[pos[1]][pos[0]] = "#"

# Initialises player and money
player_pos = [20, 13]
player_pos_old = list(player_pos)
grid[player_pos[1]][player_pos[0]] = "P"
money = 175
coin_value = 25

# Represents different game modes of the game
game_modes = {
    "easy": (2, 2),
    "medium": (5, 5),
    "hard": (10, 10)
}

# Get a game mode from the user
while True:
    difficulty = input("Difficulty (easy, medium or hard): ")
    try:
        no_of_enemies, no_of_coins = game_modes[difficulty]
        break
    except:
        print("Invalid entry, try again.")

# Initialises enemies marked by a X
# no_of_enemies = int(input("Enter number of enemies: "))
random_enemy = []
for i in range(no_of_enemies):
    pos = [random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)]
    while grid[pos[1]][pos[0]] != " ":
        pos = [random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)]
    random_enemy.append({"pos": pos})
    random_enemy[-1]["pos_old"] = pos
    grid[pos[1]][pos[0]] = "X"

# Initialises coins marked by C
# no_of_coins = int(input("Enter number of coins: "))
for i in range(no_of_coins):
    pos = [random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)]
    while grid[pos[1]][pos[0]] != " ":
        pos = [random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)]
    grid[pos[1]][pos[0]] = "C"

# Mining
mine_state = 0

# Main game loop
while True:

    # Clears screen
    # Can cause errors in certain computers
    os.system('cls' if os.name == 'nt' else 'clear')

    # Used for identifying commands
    # wasd to move
    if cmd == "w":
        player_pos[1] -= 1
    if cmd == "a":
        player_pos[0] -= 1
    if cmd == "s":
        player_pos[1] += 1
    if cmd == "d":
        player_pos[0] += 1

    # e to exit
    if cmd == "e":
        input("Exiting, press any key to quit.")
        quit()

    # m on three consequtive turns to destroy adjacent walls
    if cmd == "m":
        mine_state += 1
        if mine_state == 3:
            if grid[player_pos[1] - 1][player_pos[0]] == "#":
                if player_pos[1] - 1 != 0:
                 grid[player_pos[1] - 1][player_pos[0]] = " "
            if grid[player_pos[1] + 1][player_pos[0]] == "#":
                if player_pos[1] + 1 != grid_size[1] - 1:
                    grid[player_pos[1] + 1][player_pos[0]] = " "
            if grid[player_pos[1]][player_pos[0] - 1] == "#":
                if player_pos[0] - 1 != 0:
                    grid[player_pos[1]][player_pos[0] - 1] = " "
            if grid[player_pos[1]][player_pos[0] + 1] == "#":
                if player_pos[0] + 1 != grid_size[0]:
                    grid[player_pos[1]][player_pos[0] + 1] = " "
    else:
        mine_state = 0

    # Checks if player collides with a wall
    if grid[player_pos[1]][player_pos[0]] == "#":
        player_pos = list(player_pos_old)

    # Checks if player gains a coin
    if grid[player_pos[1]][player_pos[0]] == "C":
        money += coin_value

    # Checks if the player reached the end
    if grid[player_pos[1]][player_pos[0]] == "E":
        print("You won!!!")
        print("Your final score: ", money)
        input("Press any key to exit.")
        break

    # Checks if player was killed by an enemy
    if grid[player_pos[1]][player_pos[0]] == "X":
        print("You lost.")
        print("Your final score: ", money)
        input("Press any key to exit.")
        break

    # Updates player location in grid
    if player_pos != player_pos_old:
        grid[player_pos_old[1]][player_pos_old[0]] = " "
        grid[player_pos[1]][player_pos[0]] = "P"
    player_pos_old = list(player_pos)

    # Enemy's AI - currently random
    for i_ in range(len(random_enemy)):
        i = random_enemy[i_]
        r = random.randint(1, 5)
        if r == 1:
            i["pos"][0] += 1
        if r == 2:
            i["pos"][0] -= 1
        if r == 3:
            i["pos"][1] += 1
        if r == 4:
            i["pos"][1] -= 1
        if grid[i["pos"][1]][i["pos"][0]] in ("P", "#"):
            i["pos"] = list(i["pos_old"])
        else:
            grid[i["pos"][1]][i["pos"][0]] = "X"
            grid[i["pos_old"][1]][i["pos_old"][0]] = " "
            i["pos_old"] = list(i["pos"])

    # Displays grid
    for y in grid:
        for x in y:
            print(x, end="")
        print()
        
    # Displays money
    print("\n\tMoney:", money)

    # Gets next command from user
    cmd = input("\nYour move: ")
